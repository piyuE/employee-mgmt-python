def get_valid_salary():
    while True:
        try:
            salary = int(input("Enter salary: "))
            if salary <= 0:
                print("Salary must be positive")
            else:
                return salary
        except ValueError:
            print("Please enter a valid number")


def get_non_empty_input(message):
    while True:
        value = input(message).strip()
        if value:
            return value
        else:
            print("Input cannot be empty")

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
        print(" 3. Search employee")
        print(" 4. Exit")

    def add_employee(self):
        name = get_non_empty_input("Enter name: ")
        role = get_non_empty_input("Enter role: ")
        experience = get_non_empty_input("Enter Experience: ")
        salary = get_valid_salary()

        emp = Employee(name,experience, role, salary)

        with open("employees.txt", "a") as f:
            f.write(emp.to_file())

        print("Employee added")

    def search_employee(self):
        name_to_search = get_non_empty_input("Enter name to search: ")

        try:
            with open("employees.txt", "r") as f:
                for em in f:
                    name, experience, role, salary = em.strip().split(",")
                    if name.lower() == name_to_search.lower():
                        print("Name:", name, "| Experience:", experience,"| Role:", role, "| Salary:", salary)
                        return
            print("Employee not found")
        except FileNotFoundError:
            print("No records found")

    def display_employees(self):
        try:
            with open("employees.txt","r") as emp:
                for em in emp:
                    name, experience, role, salary = em.strip().split(",")
                    print("Name:", name, "| Experience:", experience,"| Role:", role, "| Salary:", salary)
        except FileNotFoundError:
            print("No employee records found")
    def select_option(self,option):
        match option:
            case 1:
                self.add_employee()
                return "Employee added successfully"
            case 2:
                self.display_employees()
                return "Employees displayed"
            case 3:
                self.search_employee()
                return "Employee Searched"
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
