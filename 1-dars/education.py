class Education:
    students_dict = {}
    
    def __init__(self, name, surname, ball, passport):
        self.name = name
        self.surname = surname
        self.ball = ball
        self.passport = passport
    
    @staticmethod
    def get_info(self):
        return f'Name: {self.name} \nSurname: {self.surname} \nBall: {self.ball} \nPassport: {self.passport}'
    
    @classmethod
    def append_student(cls, name, surname, ball, passport):
        # Проверяем, что балл студента выше 80
        if ball >= 80:
            # Добавляем студента в словарь
            cls.students_dict[passport] = {'name': name, 'surname': surname, 'ball': ball}
        else:
            print("Невозможно добавить студента с баллом ниже 80.")
    
    @classmethod
    def delete_student(cls, passport):
        if passport in cls.students_dict:
            del cls.students_dict[passport]

# Education.append_student("John", "Doe", 90, "AB1234567")
# Education.append_student("Jane", "Smith", 70, "CD9876543")

while True:
    print('1) add student\n2) delete student\n3) get info')
    answer = input('what do you want to do?\n>>> ')
    if answer == '1':
        name = input('enter name: ')
        surname = input('enter surname: ')
        ball = int(input('enter ball: '))
        passport = input('enter passport: ')
        Education.append_student(name, surname, ball, passport)
        answer = input('do you want to continue? (1/0)')
        if answer == 'no':
            break
        else:
            continue
    elif answer == '2':
        passport = input('enter passport: ')
        Education.delete_student(passport)
        answer = input('do you want to continue? (1/0)')
        if answer == 'no':
            break
        else:
            continue
    elif answer == '3':
        passport = input('enter passport: ')
        print(Education.get_info(passport))
        answer = input('do you want to continue? (1/0)')
        if answer == 'no':
            break
        else:
            continue
    else:
        print('your answer is not correct')