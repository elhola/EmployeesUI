class Employee:
    def __init__(self, id, department, position, full_name, address, phone, date_of_birth, hire_date, salary):
        self.id = id
        self.department = department
        self.position = position
        self.full_name = full_name
        self.address = address
        self.phone = phone
        self.date_of_birth = date_of_birth
        self.hire_date = hire_date
        self.salary = salary

    def save_to_db(self, db):
        query = "INSERT INTO employees (department, position, full_name, address, phone, date_of_birth, hire_date, salary) " \
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s) RETURNING id"
        values = (
            self.department, self.position, self.full_name, self.address, self.phone,
            self.date_of_birth, self.hire_date, self.salary
        )
        self.id = db.execute(query, values)
        return self.id
    def delete_from_db(self, db):
        query = "DELETE FROM employees WHERE id = %s"
        values = (self.id,)
        db.execute(query, values)
