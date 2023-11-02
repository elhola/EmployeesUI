from employee import Employee


class EmployeeManager:
    def __init__(self, db):
        self.db = db

    def search(self, department=None, position=None, full_name=None):
        query = "SELECT * FROM employees WHERE TRUE"
        values = []

        if department:
            query += " AND department = %s"
            values.append(department)

        if position:
            query += " AND position = %s"
            values.append(position)

        if full_name:
            query += " AND full_name = %s"
            values.append(full_name)

        return [Employee(*result) for result in self.db.fetch(query, values)]

    def export_to_txt(self, file_path, department=None, position=None, full_name=None):
        employees = self.search(department, position, full_name)
        with open(file_path, "w") as file:
            for employee in employees:
                file.write(f"{employee.full_name}: {employee.salary}\n")

    def calculate_salary_report(self, department):
        query = "SELECT full_name, salary FROM employees WHERE department = %s"
        values = (department,)
        employees = self.db.fetch(query, values)

        total_salary = sum(employee[1] for employee in employees)

        report = f"Зарплатна звітність для відділу '{department}':\n"
        for employee in employees:
            report += f"{employee[0]}: {employee[1]}\n"

        report += f"Загальна виплата відділу: {total_salary}"

        return report

    def from_db(self, employee_id):
        query = "SELECT * FROM employees WHERE id = %(employee_id)s LIMIT 1"
        values = {"employee_id": employee_id}
        result = self.db.fetch(query, values)
        if result:
            return Employee(*result[0])
        return None

    def get_all_employees(self):
        query = "SELECT * FROM employees"
        result = self.db.fetch(query)
        employees = [Employee(*row) for row in result]
        return employees

    def update_in_db(self, employee):
        query = "UPDATE employees SET department = %s, position = %s, full_name = %s, address = %s, phone = %s, " \
                "date_of_birth = %s, hire_date = %s, salary = %s, company_info = %s WHERE id = %s"
        values = (
            employee.department,
            employee.position,
            employee.full_name,
            employee.address,
            employee.phone,
            employee.date_of_birth,
            employee.hire_date,
            employee.salary,
            employee.company_info,
            employee.id
        )
        self.db.execute(query, values)
