from external import Synthesizer, Human

class Computer:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'the {} computer'.format(self.name)

    def execute(self):
        return 'executes a program'

class ComputerAdapter:
    def __init__(self, obj, adapted_methods):
        self.obj = obj
        self.__dict__.update(adapted_methods)

    def __str__(self):
        return str(self.obj)

class Factory:
    def getObject(self, type):
        obj = None
        if type == "Computer":
            obj = Computer("Apple")
        elif type == "Synthesizer":
            synth = Synthesizer("Homepod")
            obj = ComputerAdapter(synth, dict(execute=synth.play))
        elif type == "Human":
            human = Human('Peter')
            obj = ComputerAdapter(human, dict(execute=human.speak))
      
        return obj
        
def main():
    type = input("Enter the type of object: ")
    obj = Factory().getObject(type)
    print(obj.execute())

if __name__ == "__main__":
    main()