import sqlite3

class Employee:

    def __init__(self):
        self.db = "employee.db"

        con = sqlite3.connect(self.db)
        cur = con.cursor()

        cur.execute("""
        CREATE TABLE IF NOT EXISTS employee(
            id INTEGER PRIMARY KEY,
            name TEXT,
            department TEXT,
            salary REAL,
            email TEXT
        )
        """)

        con.commit()
        con.close()

    def create(self):
        try:
            con = sqlite3.connect(self.db)
            cur = con.cursor()

            id = input("Enter ID: ")
            name = input("Enter Name: ")
            dept = input("Enter Department: ")
            salary = input("Enter Salary: ")
            email = input("Enter Email: ")

            cur.execute(
                "INSERT INTO employee VALUES(?,?,?,?,?)",
                (id, name, dept, salary, email)
            )

            con.commit()
            con.close()

            print("Employee added!")

        except Exception as e:
            print("Error:", e)

    def read(self):
        try:
            con = sqlite3.connect(self.db)
            cur = con.cursor()

            cur.execute("SELECT * FROM employee")
            rows = cur.fetchall()

            for row in rows:
                print(row)

            con.close()

        except Exception as e:
            print("Error:", e)

    def update(self):
        try:
            con = sqlite3.connect(self.db)
            cur = con.cursor()

            id = input("Enter ID: ")
            name = input("Enter New Name: ")

            cur.execute(
                "UPDATE employee SET name=? WHERE id=?",
                (name, id)
            )

            con.commit()
            con.close()

            print("Employee updated!")

        except Exception as e:
            print("Error:", e)

    def delete(self):
        try:
            con = sqlite3.connect(self.db)
            cur = con.cursor()

            id = input("Enter ID: ")

            cur.execute(
                "DELETE FROM employee WHERE id=?",
                (id,)
            )

            con.commit()
            con.close()

            print("Employee deleted!")

        except Exception as e:
            print("Error:", e)


emp = Employee()

while True:

    print("""
1. Create Employee
2. Read Employees
3. Update Employee
4. Delete Employee
5. Exit
""")

    choice = input("Enter choice: ")

    if choice == "1":
        emp.create()

    elif choice == "2":
        emp.read()

    elif choice == "3":
        emp.update()

    elif choice == "4":
        emp.delete()

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice")