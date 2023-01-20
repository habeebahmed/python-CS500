from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass
        
class StackAddCommand(Command):
    def __init__(self, stack, newItem):
        self.stack = stack
        self.newItem = newItem

    def execute(self):
        self.stack.append(self.newItem)
        print('Pushed', self.newItem)
        
class StackDeleteCommand(Command):
    def __init__(self, stack):
        self.stack = stack

    def execute(self):
        deletedItem = self.stack.pop()    # delete the last one
        print('Popped', deletedItem)
        
class QueueAddCommand(Command):
    def __init__(self, queue, newItem):
        self.queue = queue
        self.newItem = newItem

    def execute(self):
        self.queue.append(self.newItem)
        print('Enqeued', self.newItem)
        
class QueueDeleteCommand(Command):
    def __init__(self, queue):
        self.queue = queue

    def execute(self):
        deletedItem = self.queue.pop(0)   # delete the first one
        print('Dequeued', deletedItem)
        
class NoCommand(Command):
    def execute(self):
        pass
        
class ControlPanel:
    def __init__(self):
        self.addCommands = []
        self.deleteCommands = []
        
        noCommand = NoCommand()
        for i in range(5):
            self.addCommands.append(noCommand)
            self.deleteCommands.append(noCommand)
            
    def setCommand(self, slot, addCommand, deleteCommand):
        self.addCommands[slot] = addCommand
        self.deleteCommands[slot] = deleteCommand

    def pressAddButton(self, slot):
        self.addCommands[slot].execute()
        
    def pressDeleteButton(self, slot):
        self.deleteCommands[slot].execute()
        
def main():
    control = ControlPanel()
    
    stack = []
    stackAdd = StackAddCommand(stack, "A")
    stackDelete = StackDeleteCommand(stack)
    
    queue = []
    queueAdd = QueueAddCommand(queue, 10)
    queueDelete = QueueDeleteCommand(queue)
    
    control.setCommand(0, stackAdd, stackDelete)
    control.setCommand(1, queueAdd, queueDelete)
    
    control.pressAddButton(0)       # slot 0
    control.pressDeleteButton(0)    # slot 0
    control.pressAddButton(1)       # slot 1
    control.pressDeleteButton(1)    # slot 1
    
if __name__ == "__main__":
    main()