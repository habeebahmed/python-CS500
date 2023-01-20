from state_machine import (State, Event, acts_as_state_machine,
after, before, InvalidStateTransition)

@acts_as_state_machine
class Process:
    # define 4 states
    created = State(initial=True)
    waiting = State()
    running = State()
    terminated = State()
  
    # define transitions
    wait = Event(from_states=(created, running), to_state=waiting)
    run = Event(from_states=waiting,to_state=running)
    terminate = Event(from_states=running,to_state=terminated)
    
    def __init__(self, name):
        self.name = name
             
    @after('wait')
    def wait_info(self):
        print(f'{self.name} entered waiting mode')
    
    @after('run')
    def run_info(self):
        print(f'{self.name} is running')
    
    @before('terminate')
    def terminate_info(self):
        print(f'{self.name} terminated')
         
def makeTransition(process, event, event_name):
    try:
        event()
    except  InvalidStateTransition as err:
        print(f'Error: transition of {process.name} from {process.current_state} to {event_name} failed')
        
def state_info(process):
    print(f'state of {process.name}: {process.current_state}')
    
def main():
    RUNNING = 'running'
    WAITING = 'waiting'
    TERMINATED = 'terminated'
    
    p1 = Process('process1')
    p2 = Process('process2')
    [state_info(p) for p in (p1, p2)]
    
    print()
    makeTransition(p1, p1.wait, WAITING)
    makeTransition(p2, p2.terminate, TERMINATED)
    [state_info(p) for p in (p1, p2)]
    
    print()
    makeTransition(p1, p1.run, RUNNING)
    makeTransition(p2, p2.wait, WAITING)
    [state_info(p) for p in (p1, p2)]
    
    print()
    makeTransition(p2, p2.run, RUNNING)
    [state_info(p) for p in (p1, p2)]
    
    print()
    makeTransition(p1, p1.terminate, TERMINATED)
    makeTransition(p2, p2.terminate, TERMINATED)
    [state_info(p) for p in (p1, p2)]
  
if __name__ == '__main__':
    main()