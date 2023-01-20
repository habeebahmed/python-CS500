class Receiver:
    def doAction1(self):
        print("Action 1 performed")
        
    def doAction2(self):
        print("Action 2 performed")
        
class Command:
    def __init__(self, receiver):
        self.receiver = receiver
        
    def execute(self):
        self.receiver.doAction1()
        self.receiver.doAction2()
        
class Invoker:
    def __init__(self):
        self.slot = None
        
    def setCommand(self, command):
        self.slot = command
        
    def invoke(self):
        self.slot.execute()
        
def main():
    receiver = Receiver()
    command = Command(receiver)
    invoker = Invoker()
    invoker.setCommand(command)
    
    # Sometime later the client calls invoker to invoke the command
    invoker.invoke()
    
if __name__ == "__main__":
    main()