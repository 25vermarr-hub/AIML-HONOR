
import pandas as pd
import os

file = "employees.csv"

# Create file if it does not exist
if not os.path.exists(file):
    df = pd.DataFrame(columns=["ID", "Name", "Salary"])
    df.to_csv(file, index=False)


while True:
    print("\n----- Employee Management System -----")
    print("1. Add Employee")
    print("2. Display Employees")
    print("3. Update Employee")
    print("4. Delete Employee")
    print("5. Exit")

    choice = input("Enter your choice: ")

    df = pd.read_csv(file)

    if choice == "1":
        emp_id = int(input("Enter Employee ID: "))
        
        if emp_id in df["ID"].values:
            print("Employee ID already exists")
        else:
            name = input("Enter Employee Name: ")
            salary = int(input("Enter Salary: "))

            new_employee = pd.DataFrame({
                "ID": [emp_id],
                "Name": [name],
                "Salary": [salary]
            })

            df = pd.concat([df, new_employee], ignore_index=True)
            df.to_csv(file, index=False)

            print("Employee added successfully")

    elif choice == "2":
        if df.empty:
            print("No employee records found")
        else:
            print("\nEmployee Details:")
            print(df)

    elif choice == "3":
        emp_id = int(input("Enter Employee ID to update: "))

        if emp_id in df["ID"].values:
            name = input("Enter new name: ")
            salary = int(input("Enter new salary: "))

            df.loc[df["ID"] == emp_id, "Name"] = name
            df.loc[df["ID"] == emp_id, "Salary"] = salary

            df.to_csv(file, index=False)
            print("Employee updated successfully")
        else:
            print("Employee not found")

    elif choice == "4":
        emp_id = int(input("Enter Employee ID to delete: "))

        if emp_id in df["ID"].values:
            df = df[df["ID"] != emp_id]
            df.to_csv(file, index=False)

            print("Employee deleted successfully")
        else:
            print("Employee not found")

    elif choice == "5":
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please try again.")
