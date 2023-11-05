from datetime import datetime
from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLineEdit, QComboBox, QPushButton, QTextEdit, QDateEdit
from employee import Employee

class EmployeeEditDialog(QDialog):
    def __init__(self, employee, employee_manager):
        super().__init__()
        self.employee = employee
        self.id = employee.id if employee else None
        self.selected_department = None
        self.employee_manager = employee_manager

        layout = QVBoxLayout()

        self.full_name_lineedit = QLineEdit()
        self.full_name_lineedit.setText(self.employee.full_name)
        self.full_name_lineedit.setPlaceholderText("ПІБ")
        layout.addWidget(self.full_name_lineedit)

        self.department_combobox = QComboBox()
        self.department_combobox.addItem("IT")
        self.department_combobox.addItem("HR")
        self.department_combobox.setCurrentText(self.employee.department)
        layout.addWidget(self.department_combobox)

        self.position_lineedit = QLineEdit()
        self.position_lineedit.setText(self.employee.position)
        self.position_lineedit.setPlaceholderText("Посада")
        layout.addWidget(self.position_lineedit)

        self.salary_lineedit = QLineEdit()
        self.salary_lineedit.setText(str(self.employee.salary))
        layout.addWidget(self.salary_lineedit)

        self.address_lineedit = QLineEdit()
        self.address_lineedit.setText(self.employee.address)
        self.address_lineedit.setPlaceholderText("Адреса")
        layout.addWidget(self.address_lineedit)

        self.phone_lineedit = QLineEdit()
        self.phone_lineedit.setText(self.employee.phone)
        self.phone_lineedit.setPlaceholderText("Номер телефону")
        layout.addWidget(self.phone_lineedit)

        self.date_of_birth_dateedit = QDateEdit()
        if self.employee.date_of_birth:
            self.date_of_birth_dateedit.setDate(
                datetime.strptime(str(self.employee.date_of_birth), '%Y-%m-%d').date()
            )
        self.date_of_birth_dateedit.setCalendarPopup(True)
        layout.addWidget(self.date_of_birth_dateedit)

        self.hire_date_dateedit = QDateEdit()
        if self.employee.hire_date:
            self.hire_date_dateedit.setDate(
                datetime.strptime(str(self.employee.hire_date), '%Y-%m-%d').date()
            )
        self.hire_date_dateedit.setCalendarPopup(True)
        layout.addWidget(self.hire_date_dateedit)

        save_button = QPushButton("Зберегти")
        save_button.clicked.connect(self.accept)
        layout.addWidget(save_button)

        delete_button = QPushButton("Видалити співробітника")
        delete_button.clicked.connect(self.delete_employee)
        layout.addWidget(delete_button)

        if self.employee is None:
            # Если сотрудник не существует, добавляем кнопку "Додати співробітника"
            add_employee_button = QPushButton("Додати співробітника")
            add_employee_button.clicked.connect(self.add_employee)
            layout.addWidget(add_employee_button)

        self.setLayout(layout)

    def add_employee(self):
        new_employee = Employee(
            id=None,
            department=self.department_combobox.currentText(),
            position=self.position_lineedit.text(),
            full_name=self.full_name_lineedit.text(),
            address=self.address_lineedit.text(),
            phone=self.phone_lineedit.text(),
            date_of_birth=self.date_of_birth_dateedit.date().toString("yyyy-MM-dd"),
            hire_date=self.hire_date_dateedit.date().toString("yyyy-MM-dd"),
            salary=float(self.salary_lineedit.text())
        )
        if self.employee_manager:
            new_employee.save_to_db(self.employee_manager.db)
        self.accept()

    def get_updated_employee(self):
        updated_employee = Employee(
            id=self.id,
            department=self.department_combobox.currentText(),
            position=self.position_lineedit.text(),
            full_name=self.full_name_lineedit.text(),
            address=self.address_lineedit.text(),
            phone=self.phone_lineedit.text(),
            date_of_birth=self.date_of_birth_dateedit.date().toString("yyyy-MM-dd"),
            hire_date=self.hire_date_dateedit.date().toString("yyyy-MM-dd"),
            salary=float(self.salary_lineedit.text())
        )
        return updated_employee

    def delete_employee(self):
        if self.employee:
            self.employee.delete_from_db(self.employee_manager.db)
            self.accept()
