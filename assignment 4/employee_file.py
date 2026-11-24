
import csv
import os

file = "employees.csv"

# Create file if it does not exist
if not os.path.exists(file):
    with open(file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Name", "Salary"])


while True:
    print("\n----- Employee Management System -----")
    print("1. Add Employee")
    print("2. Display Employees")
    print("3. Update Employee")
    print("4. Delete Employee")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        emp_id = input("Enter Employee ID: ")

        employees = []
        with open(file, "r") as f:
            reader = csv.DictReader(f)
            employees = list(reader)

        found = False
        for emp in employees:
            if emp["ID"] == emp_id:
                found = True

        if found:
            print("Employee ID already exists")
        else:
            name = input("Enter Employee Name: ")
            salary = input("Enter Salary: ")

            with open(file, "a", newline="") as f:
                writer = csv.writer(f)
                writer.writerow([emp_id, name, salary])

            print("Employee added successfully")

    elif choice == "2":
        with open(file, "r") as f:
            reader = csv.reader(f)

            print("\nEmployee Details:")
            for row in reader:
                print(row)

    elif choice == "3":
        emp_id = input("Enter Employee ID to update: ")

        employees = []
        found = False

        with open(file, "r") as f:
            reader = csv.DictReader(f)
            employees = list(reader)

        for emp in employees:
            if emp["ID"] == emp_id:
                emp["Name"] = input("Enter new name: ")
                emp["Salary"] = input("Enter new salary: ")
                found = True

        if found:
            with open(file, "w", newline="") as f:
                writer = csv.DictWriter(
                    f, fieldnames=["ID", "Name", "Salary"]
                )
                writer.writeheader()
                writer.writerows(employees)

            print("Employee updated successfully")
        else:
            print("Employee not found")

    elif choice == "4":
        emp_id = input("Enter Employee ID to delete: ")

        employees = []
        found = False

        with open(file, "r") as f:
            reader = csv.DictReader(f)
            employees = list(reader)

        new_employees = []

        for emp in employees:
            if emp["ID"] == emp_id:
                found = True
            else:
                new_employees.append(emp)

        if found:
            with open(file, "w", newline="") as f:
                writer = csv.DictWriter(
                    f, fieldnames=["ID", "Name", "Salary"]
                )
                writer.writeheader()
                writer.writerows(new_employees)

            print("Employee deleted successfully")
        else:
            print("Employee not found")

    elif choice == "5":
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please try again.")
