import sys 
from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass
 
class Window: 
    def exit(self): 
        sys.exit(0) 
 
class Document: 
    def __init__(self, filename): 
        self.filename = filename 
        self.contents = "This file cannot be modified" 
 
    def save(self): 
        with open(self.filename, 'w') as file: 
            file.write(self.contents) 
            
class ToolbarButton:
    def __init__(self, name, iconname):
        self.name = name
        self.iconname = iconname
        
    def set_command(self, command):
        self.command = command

    def click(self):
        print("The button was clicked")
        self.command.execute()


class MenuItem:
    def __init__(self, menu_name, menuitem_name):
        self.menu = menu_name
        self.item = menuitem_name

    def set_command(self, command):
        self.command = command
        
    def click(self):
        print("The menu item was clicked")
        self.command.execute()


class KeyboardShortcut:
    def __init__(self, key, modifier):
        self.key = key
        self.modifier = modifier

    def set_command(self, command):
        self.command = command
        
    def keypress(self):
        print("The key was pressed")
        self.command.execute()
        
class SaveCommand(Command):
    def __init__(self, document):
        self.document = document

    def execute(self):
        self.document.save()


class ExitCommand(Command):
    def __init__(self, window):
        self.window = window

    def execute(self):
        self.window.exit()
        
def main():
    window = Window() 
    document = Document("a_document.txt") 
    save = SaveCommand(document) 
    exit = ExitCommand(window) 
     
    save_button = ToolbarButton('save', 'save.png') 
    save_button.set_command(save) 
    save_keystroke = KeyboardShortcut("s", "ctrl") 
    save_keystroke.set_command(save) 
    exit_menu = MenuItem("File", "Exit") 
    exit_menu.set_command(exit) 
    
    # Sometime later the user clicks button to invoke the command
    save_button.click()
    save_keystroke.keypress()
    exit_menu.click()
    
if __name__ == "__main__":
    main()