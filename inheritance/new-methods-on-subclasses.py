class Employee():
    def do_work(self):
        print("I'm working")


class Manager(Employee):
    def waste_time(self):
        print("Wow, this YouTube video is fun!")


class Director(Manager):
    def fire_employee(self):
        print("You're fired")

e = Employee()
m = Manager()

e.do_work()
print()
m.do_work()
m.waste_time()

d = Director()
print()
d.do_work()
d.waste_time()
d.fire_employee()