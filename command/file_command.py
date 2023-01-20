from abc import ABC, abstractmethod
import os  
verbose = True

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class CreateFileCommand(Command):
     def __init__(self, path, txt='hello world\n'):  
         self.path = path
         self.txt = txt
 
     def execute(self):  
         if verbose:  
             print(f"[creating file '{self.path}']")  
         with open(self.path, mode='w', encoding='utf-8') as out_file:  
             out_file.write(self.txt)
             
     def undo(self):  
         if verbose:
             print(f"deleting file {self.path}")
             os.remove(self.path)
         
         
class ReadFileCommand(Command):
     def __init__(self, path):  
         self.path = path
 
     def execute(self):  
         if verbose:  
             print(f"[reading file '{self.path}']")  
         with open(self.path, mode='r', encoding='utf-8') as in_file:  
             print(in_file.read(), end='')
             
             
class RenameFileCommand(Command):
    def __init__(self, src, dest):  
        self.src = src 
        self.dest = dest
        
    def execute(self):  
        if verbose:  
            print(f"[renaming '{self.src}' to '{self.dest}']")  
        os.rename(self.src, self.dest)  

    def undo(self):  
        if verbose:  
            print(f"[renaming '{self.dest}' back to '{self.src}']")  
            os.rename(self.dest, self.src) 
            
class Invoker:
    def __init__(self):
        self.commands = []
        
    def setCommand(self, command):
        self.commands.append(command)
        
    def commit(self):
        [c.execute() for c in self.commands]
        
    def rollback(self):
        for c in reversed(self.commands):  
            try:  
                c.undo()  
            except AttributeError as e:  
                print("Error", str(e))
        
                     
def main(): 
    orig_name, new_name = 'file1', 'file2'
    invoker = Invoker()
    invoker.setCommand(CreateFileCommand(orig_name))
    invoker.setCommand(ReadFileCommand(orig_name))
    invoker.setCommand(RenameFileCommand(orig_name, new_name))
    
    invoker.commit()
     
    answer = input('reverse the executed commands? [y/n] ')  
    
    if answer not in 'yY':
        print(f"the result is {new_name}")  
        exit()  
  
    invoker.rollback()
  
if __name__ == "__main__":  
    main()