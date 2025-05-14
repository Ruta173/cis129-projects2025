#Ruth Andrews
#CIS129
#Module 12 Lab

class Pet:
      def set_name(self, name):
          self.__name = name
  
      def set_type(self, type):
          self.__type = type
  
      def set_age(self, age):
          self.__age = age
 
      def get_name(self):
          return self.__name
 
      def get_type(self):
          return self.__type
 
      def get_age(self):
          return self.__age
 
def main():
     myPet = Pet()
 
     # Store values in the object's fields.
     inputName = input('Enter a pet name:\n')
     myPet.set_name(inputName)

     inputType = input('Enter a pet type:\n')
     myPet.set_type(inputType)

     inputAge = input('Enter a pet age:\n')
     myPet.set_age(inputAge)
 
     # Display the values stored in the fields.
     print(f'The pet name is', myPet.get_name())
     print(f'The pet type is', myPet.get_type())
     print(f'The pet age is', myPet.get_age())

# Call the main function.
main()