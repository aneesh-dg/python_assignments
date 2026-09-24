from abc import ABC,abstractmethod
class person(ABC):
    @abstractmethod
    def get_gender(self):
        pass

class male(person):
    def get_gender(self):
        print("Male here.")

class female(person):
    def get_gender(self):
        print("female here.")

m=male()
f=female()
m.get_gender()
f.get_gender()
