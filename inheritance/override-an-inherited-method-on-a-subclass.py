# To overide a method means to define a different implementation of it in a subclass
class Teacher():
    def teach_class(self):
        print("Teaching stuff ")

    def grab_lunch(self):
        print("Yum yum tum!")

    def grade_tests(self):
        print("F! F! F!")

class CollegeProfessor(Teacher):
    def publish_book(self):
        print("Hooray, I'm an author")

    def grade_tests(self):
        print(" A1 A1 A1")
        # return super().grade_tests()


cp = CollegeProfessor()
cp.grade_tests()