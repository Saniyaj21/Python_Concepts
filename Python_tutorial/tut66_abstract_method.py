# Abstract Base Class & @abstractmethod 

from abc import ABC, abstractmethod


class phone(ABC):  #  abc force to implement some methods in derived classes
    @abstractmethod  # we can not create object of abstruct class
    def wifi():
       return 0

class smartPhone(phone):
    def display():
        print("display something")

    def wifi(self):  # implementing abstract class
        tips = "Wifi is must for derived classes"
        return tips


a = smartPhone()
print(a.wifi())