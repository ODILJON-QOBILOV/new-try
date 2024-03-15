# class Person:
#     def __init__(self, name, surname, userId):
#         self.name = name
#         self.surname = surname
#         self.userId = userId
#     def get_info(self):
#         return f'Name: {self.name} \nSurname: {self.surname} \nUser ID: {self.userId}'

# class Student(Person):
#     def __init__(self, name, surname, userId, passport):
#         super().__init__(name, surname, userId)
#         self.passport = passport
    
#     def get_passport(self):
#         return self.passport

# persoon1 = Student('John', 'Doe', '123456', '123456789')
# print(persoon1.get_info())




# class Human:
#     def __init__(self, name, surname, age) -> None:
#         self.name = name
#         self.surname = surname
#         self.age = age
#     def get_info(self):
#         return f'Name: {self.doUpper(self.name)} \nSurname: {self.doUpper(self.surname)} \nAge: {self.doUpper(self.age)}'
#     def __str__(self):
#         return self.get_info()
    
#     @staticmethod
#     def doUpper(param):
#         try:
#             return param.title()
#         except:
#             return param


# human1 = Human('john', 'doe', 25)
# print(human1)


# with open('try.txt', 'a+') as f:
#     f.write('hello\n')

# def save_user_msg(answer):
#     with open('try.txt', 'a+') as f:
#         f.write(f'{answer}\n')


# while True:
#     answer = input('>>> ')
#     if answer == 'exit':
#         break
#     save_user_msg(answer)