class Dog:
    def bark(self):
        print("instance bark")
    @staticmethod
    def bark():
        print("staticmethod bark")
    @classmethod
    def bark(cls):
        print("class singleton bark")


fido = Dog()

'''
if all same name, the class singleton method will win at the end of the day. 
'''
fido.bark()