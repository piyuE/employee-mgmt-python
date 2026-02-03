class Employee:
    def __init__(self, name,experience, role, salary):
        self.name = name
        self.experience = experience
        self.role = role
        self.salary = salary

    def give_bonus(self):
        if(self.salary < 40000):
           self.salary += 3000
        else:
            self.salary += 5000
        return self.salary

    def to_file(self):
        self.salary = self.give_bonus()
        return f"{self.name},{self.experience},{self.role},{self.salary}\n"

class EmployeeManager:

    def portal_info(self):
        print(" 1. Add employee")
        print(" 2. Display all the employees")
        print(" 3. Exit")

    def add_employee(self):
        name = input("Enter the employee name : ")
        experience = input("Enter years of experience: ")
        role = input("Enter preferred role: ")
        salary = int(input("Enter the expected salary :"))

        emp = Employee(name,experience, role, salary)

        with open("employees.txt", "a") as f:
            f.write(emp.to_file())

        print("Employee added")

    def display_employees(self):
        with open("employees.txt","r") as emp:
            for em in emp:
                name, experience, role, salary = em.strip().split(",")
                print("Name:", name, "| Experience:", experience,"| Role:", role, "| Salary:", salary)

    def select_option(self,option):
        match option:
            case 1:
                self.add_employee()
                return "Employee added successfully"
            case 2:
                self.display_employees()
                return "Employees displayed"
            case _:
                print("Exiting system")
                return False
        
print("Welcome to Employees Portal")
running = True
manager = EmployeeManager()
while running:
    manager.portal_info()
    option = int(input("Select the option from the above menu : "))
    running = manager.select_option(option)
