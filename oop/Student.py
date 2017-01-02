class Student(object):

    def __init__(self, name="zing", score=100):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

    def set(self, name, score):
        self.__name = name
        self.__score = score

    def p(self):
        print("p"*50)

if __name__ == '__main__':
    stu = Student("zhangrxiang", 200)
    stu2 = Student()
    stu.print_score()
    stu2.print_score()

    stu.set("hly",300)
    stu.print_score()
    stu.p()
