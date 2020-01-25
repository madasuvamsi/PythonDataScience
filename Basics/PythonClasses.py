class Employee:
    def __init__(self, empname, emptitle,empsalary):
        self.EmpName=empname
        self.EmpTitle=emptitle
        self.EmpSalary=empsalary

    def calsalary(self):
        if self.EmpTitle=="Developer":
            print("Salary of the Developer is ",self.EmpSalary)
        elif self.EmpTitle=="Manager":
            print("Salary of the Manager is ",self.EmpSalary)
        else:
            print("Salary Not Defined,Please contact HR")

    def responsibilites(self):
        if self.EmpTitle=="Developer":
            print("The responsibiliy of the Developer is to Write Code")
        elif self.EmpTitle=="Manager":
            print("The responsibiliy of the Manager is to Manages the team")
        else:
            print("Responsibilities Not Defined,Please contact HR")

Sam=Employee("Sam","Developer",6000)
Sam.calsalary()
Sam.responsibilites()

Nag=Employee("Nag","Manager",7000)
Nag.calsalary()
Nag.responsibilites()

John=Employee("John","HR",5500)
John.calsalary()
John.responsibilites()