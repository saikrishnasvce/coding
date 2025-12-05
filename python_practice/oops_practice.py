class Employee:
    raise_amount = 1.2
    num_of_emps = 0
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    # Class variables
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

emp_1 = Employee(first='James', last='Smith', pay=100)
emp_2 = Employee(first='sachin', last='Tendulkar', pay=200)

print(Employee.raise_amount)
#print(emp_1.raise_amount)
#print(emp_2.raise_amount)
print(emp_1.apply_raise())
print(emp_1.pay)
