import mysql.connector
from tabulate import tabulate

# Establishing Database Connection
def connect_to_db():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",  # Replace with your MySQL username
        password="asdf1234",  # Replace with your MySQL password
        database="food"
    )
    if connection.is_connected():
        print("Connected to the database!")
        return connection

# Ensure necessary tables exist
def initialize_tables(cursor):
    table_creation_queries = {
        "employee": """
        CREATE TABLE IF NOT EXISTS employee (
            Emp_id INT PRIMARY KEY,
            E_name VARCHAR(100),
            Emp_gender VARCHAR(10),
            e_age INT,
            emp_phone VARCHAR(15)
        );
        """,
        "customer": """
        CREATE TABLE IF NOT EXISTS customer (
            c_id INT PRIMARY KEY,
            c_name VARCHAR(100),
            cphone VARCHAR(15),
            payment VARCHAR(50),
            email VARCHAR(100),
            empid INT,
            date DATE,
            FOREIGN KEY (empid) REFERENCES employee(Emp_id)
        );
        """,
        "Food": """
        CREATE TABLE IF NOT EXISTS Food (
            Food_id INT PRIMARY KEY,
            Foodname VARCHAR(100) UNIQUE,  
            quantity INT,
            price DECIMAL(10, 2)
        );
        """,
        "OrderFood": """
        CREATE TABLE IF NOT EXISTS OrderFood (
            OrderF_id INT PRIMARY KEY,
            C_id INT,
            Employee_id INT,
            Foodname VARCHAR(100),
            Food_qty INT,
            Total_price DECIMAL(10, 2),
            FOREIGN KEY (C_id) REFERENCES customer(c_id),
            FOREIGN KEY (Employee_id) REFERENCES employee(Emp_id),
            FOREIGN KEY (Foodname) REFERENCES Food(Foodname)
        );
        """
    }

    for table, query in table_creation_queries.items():
        cursor.execute(query)
        print("Checked and ensured table '" + table + "' exists.")

# Add a new employee
def add_employee(cursor, db):
    emp_id = int(input("Enter Employee ID: "))
    e_name = input("Enter Employee Name: ")
    emp_gender = input("Enter Employee Gender: ")
    e_age = int(input("Enter Employee Age: "))
    emp_phone = input("Enter Employee Phone Number: ")

    query = """
    INSERT INTO employee (Emp_id, E_name, Emp_gender, e_age, emp_phone)
    VALUES (%s, %s, %s, %s, %s)
    """
    cursor.execute(query, (emp_id, e_name, emp_gender, e_age, emp_phone))
    db.commit()
    print("Employee added successfully!")

# Add a new customer
def add_customer(cursor, db):
    c_id = int(input("Enter Customer ID: "))
    c_name = input("Enter Customer Name: ")
    c_phone = input("Enter Customer Phone Number: ")
    payment = input("Enter Payment Method (Card/Cash): ")
    email = input("Enter Customer Email: ")
    emp_id = int(input("Enter Employee ID (Assigned): "))
    date = input("Enter Date (YYYY-MM-DD): ")

    query = """
    INSERT INTO customer (c_id, c_name, cphone, payment, email, empid, date)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    cursor.execute(query, (c_id, c_name, c_phone, payment, email, emp_id, date))
    db.commit()
    print("Customer added successfully!")

# Add a new food item
def add_food(cursor, db):
    food_id = int(input("Enter Food ID: "))
    food_name = input("Enter Food Name: ")
    quantity = int(input("Enter Food Quantity: "))
    price = float(input("Enter Food Price: "))

    query = """
    INSERT INTO Food (Food_id, Foodname, quantity, price)
    VALUES (%s, %s, %s, %s)
    """
    cursor.execute(query, (food_id, food_name, quantity, price))
    db.commit()
    print("Food item added successfully!")

# Place an order
def place_order(cursor, db):
    order_id = int(input("Enter Order ID: "))
    c_id = int(input("Enter Customer ID: "))
    emp_id = int(input("Enter Employee ID: "))
    food_name = input("Enter Food Name: ")
    food_qty = int(input("Enter Food Quantity: "))

    # Check stock availability
    cursor.execute("SELECT quantity, price FROM Food WHERE Foodname = %s", (food_name,))
    result = cursor.fetchone()

    if not result:
        print("Food item '" + food_name + "' does not exist.")
        return

    available_qty, food_price = result
    if food_qty > available_qty:
        print("The food '" + food_name + "' is out of stock.")
        return

    # Calculate total price
    total_price = food_qty * food_price
    print("Total Price for " + str(food_qty) + " units of " + food_name + ": $" + str(round(total_price, 2)))

    # Update stock
    cursor.execute("UPDATE Food SET quantity = quantity - %s WHERE Foodname = %s", (food_qty, food_name))

    # Insert order details
    query = """
    INSERT INTO OrderFood (OrderF_id, C_id, Employee_id, Foodname, Food_qty, Total_price)
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    cursor.execute(query, (order_id, c_id, emp_id, food_name, food_qty, total_price))
    db.commit()
    print("Order placed successfully!")

# View data from tables
def view_data(cursor):
    print("\nView Options:")
    print("1. View Employees")
    print("2. View Customers")
    print("3. View Food Items")
    print("4. View Orders")
    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        query = "SELECT * FROM employee"
        cursor.execute(query)
        rows = cursor.fetchall()
        print("\nEmployees:")
        print(tabulate(rows, headers=["ID", "Name", "Gender", "Age", "Phone"], tablefmt="grid"))
    elif choice == "2":
        query = "SELECT * FROM customer"
        cursor.execute(query)
        rows = cursor.fetchall()
        print("\nCustomers:")
        print(tabulate(rows, headers=["ID", "Name", "Phone", "Payment", "Email", "Emp ID", "Date"], tablefmt="grid"))
    elif choice == "3":
        query = "SELECT * FROM Food"
        cursor.execute(query)
        rows = cursor.fetchall()
        print("\nFood Items:")
        print(tabulate(rows, headers=["ID", "Name", "Quantity", "Price"], tablefmt="grid"))
    elif choice == "4":
        query = "SELECT * FROM OrderFood"
        cursor.execute(query)
        rows = cursor.fetchall()
        print("\nOrders:")
        print(tabulate(rows, headers=["Order ID", "Customer ID", "Employee ID", "Food Name", "Quantity", "Total Price"], tablefmt="grid"))
    else:
        print("Invalid choice!")

# Menu for the application
def menu():
    connection = connect_to_db()
    cursor = connection.cursor()

    # Ensure tables exist
    initialize_tables(cursor)

    while True:
        print("\nFood Booking System Menu")
        print("1. Add Employee")
        print("2. Add Customer")
        print("3. Add Food Item")
        print("4. Place Order")
        print("5. View Data")
        print("6. Exit")

        choice = int(input("Enter your choice: "))
        if choice == 1:
            add_employee(cursor, connection)
        elif choice == 2:
            add_customer(cursor, connection)
        elif choice == 3:
            add_food(cursor, connection)
        elif choice == 4:
            place_order(cursor, connection)
        elif choice == 5:
            view_data(cursor)
        elif choice == 6:
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

    cursor.close()
    connection.close()

if __name__ == "__main__":
    menu()
