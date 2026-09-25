import csv


class EmployeeManager:

    def add_employee(self):
        emp_id = input("Enter ID: ")
        name = input("Enter name: ")
        salary = input("Enter salary: ")

        with open("employees.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([emp_id, name, salary])

        print("Employee added successfully.")

    def display_employees(self):
        try:
            with open("employees.csv", "r") as file:
                reader = csv.reader(file)

                for row in reader:
                    print(row)

        except FileNotFoundError:
            print("No employees found.")

    def update_employee(self):
        emp_id = input("Enter employee ID to update: ")

        rows = []
        found = False

        try:
            with open("employees.csv", "r") as file:
                reader = csv.reader(file)

                for row in reader:
                    if row[0] == emp_id:
                        row[1] = input("Enter new name: ")
                        row[2] = input("Enter new salary: ")
                        found = True

                    rows.append(row)

            with open("employees.csv", "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerows(rows)

            if found:
                print("Employee updated successfully.")
            else:
                print("Employee not found.")

        except FileNotFoundError:
            print("No employees found.")

    def delete_employee(self):
        emp_id = input("Enter employee ID to delete: ")

        rows = []
        found = False

        try:
            with open("employees.csv", "r") as file:
                reader = csv.reader(file)

                for row in reader:
                    if row[0] == emp_id:
                        found = True
                    else:
                        rows.append(row)

            with open("employees.csv", "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerows(rows)

            if found:
                print("Employee deleted successfully.")
            else:
                print("Employee not found.")

        except FileNotFoundError:
            print("No employees found.")


manager = EmployeeManager()


while True:

    print(" Employee Management")
    print("1. Add Employee")
    print("2. Display Employees")
    print("3. Update Employee")
    print("4. Delete Employee")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        manager.add_employee()

    elif choice == "2":
        manager.display_employees()

    elif choice == "3":
        manager.update_employee()

    elif choice == "4":
        manager.delete_employee()

    elif choice == "5":
        print("Exiting...")
        break

    else:
        print("Invalid choice.")
