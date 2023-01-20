from abc import ABC, abstractmethod

class ImageInterface(ABC):
    @abstractmethod
    def displayImage(self):
        pass

class ImageReal(ImageInterface):
    def __init__(self, filename):
        self._filename = filename
    
    def loadImageFromDisk(self):
        print("loading " + self._filename)
    
    def displayImage(self):
        print("display " + self._filename)

class ImageProxy(ImageInterface):
    def __init__( self, subject ):
        self._subject = subject
        self._proxystate = None

    def displayImage(self):
        if self._proxystate == None:
            self._subject.loadImageFromDisk()
            self._proxystate = 1
        print("display " + self._subject._filename)
            
def main():
    imag1 = ImageProxy(ImageReal('ABC.jpg'));
    imag2 = ImageProxy(ImageReal('DEF.jpg'));
    
    imag1.displayImage();
    imag2.displayImage();
    imag1.displayImage();
    imag2.displayImage();
    imag1.displayImage();
    imag2.displayImage();
    

main()