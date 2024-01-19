'''
This is a short exercise to practice creating classes that follow the 4 OOP principles.
'''

class Student:

    def __init__(self, name, age, course):
        self.name=name
        self.age=age
        self.course=course

    def calculate_tests_average(self,score_test1,score_test2,score_test3):

        self.score_average=(score_test1+score_test2+score_test3)/3

        return self.score_average




if __name__ == '__main__':

    student1=Student('Julio', 31, 'DevOps')
    print(f'{student1.name} is {student1.age} years old and enrolled in {student1.course}')

    student1.calculate_tests_average(70,61,65)
    print(f'{student1.name} average score is {student1.score_average:.2f}')
    
    student2=Student('Maria', 28, 'Data Science')
    print(f'{student2.name} is {student2.age} years old and enrolled in {student2.course}')

    student2.calculate_tests_average(75,55,67)
    print(f'{student2.name} average score is {student2.score_average:.2f}')
