import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel, QTextEdit, \
    QStackedWidget, QComboBox, QLineEdit

from database import Database
from employee import Employee
from employeeeditdialog import EmployeeEditDialog
from manager import EmployeeManager


def create_home_page(layout):
    company_info_label = QLabel("Інформація про компанію:")
    company_info_text = QTextEdit()
    company_info_text.setPlainText("Наша компанія пропонує рішення для вашого бізнесу")
    company_info_text.setReadOnly(True)
    company_info_text.setStyleSheet("background-color: #f0f0f0; border: 1px solid #d3d3d3; padding: 10px;")

    layout.addWidget(company_info_label)
    layout.addWidget(company_info_text)


def create_button(text, function):
    button = QPushButton(text)
    button.clicked.connect(function)
    return button


class EmployeeApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.salary_report_page = None
        self.view_employees_page = None
        self.home_page = None
        self.salary_report_textedit = None
        self.add_employee_button = None
        self.result_textedit = None
        self.salary_report_button = None
        self.view_employees_button = None
        self.home_button = None
        self.filename_lineedit = None
        self.edit_employee_button = None
        self.department_combobox_report = None
        self.employee_combobox = None
        self.position_combobox = None
        self.full_name_lineedit = None
        self.department_combobox = None
        self.setWindowTitle("Система обліку працівників")
        self.setGeometry(100, 100, 800, 400)

        self.stacked_widget = QStackedWidget()
        self.toolbar = self.addToolBar("Toolbar")

        db = Database(host="localhost", database="lajob_db", user="postgres", password="")

        self.employee_manager = EmployeeManager(db)

        main_widget = QWidget()
        main_layout = QVBoxLayout()

        self.create_buttons()
        self.create_pages()

        main_layout.addWidget(self.toolbar)
        main_layout.addWidget(self.stacked_widget)

        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

    def create_buttons(self):
        self.home_button = create_button("Головна сторінка", self.show_home_page)
        self.view_employees_button = create_button("Перегляд персоналу", self.show_view_employees_page)
        self.salary_report_button = create_button("Зарплатна звітність", self.show_salary_report_page)

        self.toolbar.addWidget(self.home_button)
        self.toolbar.addWidget(self.view_employees_button)
        self.toolbar.addWidget(self.salary_report_button)

    def create_pages(self):
        self.home_page = QWidget()
        home_layout = QVBoxLayout()
        create_home_page(home_layout)
        self.home_page.setLayout(home_layout)
        self.stacked_widget.addWidget(self.home_page)

        self.view_employees_page = QWidget()
        view_employees_layout = QVBoxLayout()
        self.create_view_employees_page(view_employees_layout)
        self.view_employees_page.setLayout(view_employees_layout)
        self.stacked_widget.addWidget(self.view_employees_page)

        self.salary_report_page = QWidget()
        salary_report_layout = QVBoxLayout()
        self.create_salary_report_page(salary_report_layout)
        self.salary_report_page.setLayout(salary_report_layout)
        self.stacked_widget.addWidget(self.salary_report_page)

    def create_view_employees_page(self, layout):
        department_label = QLabel("Відділ:")
        self.department_combobox = QComboBox()
        self.department_combobox.addItem("IT")
        self.department_combobox.addItem("HR")
        layout.addWidget(department_label)
        layout.addWidget(self.department_combobox)

        position_label = QLabel("Посада:")
        self.position_combobox = QComboBox()
        self.position_combobox.addItem("Програміст")
        self.position_combobox.addItem("Менеджер")
        layout.addWidget(position_label)
        layout.addWidget(self.position_combobox)

        full_name_label = QLabel("ПІБ:")
        self.full_name_lineedit = QLineEdit()
        search_button = QPushButton("Пошук")
        search_button.clicked.connect(self.search_employees_view)
        layout.addWidget(full_name_label)
        layout.addWidget(self.full_name_lineedit)
        layout.addWidget(search_button)

        self.result_textedit = QTextEdit()
        layout.addWidget(self.result_textedit)

        employee_label = QLabel("Оберіть працівника:")
        self.employee_combobox = QComboBox()
        self.populate_employee_combobox()
        layout.addWidget(employee_label)
        layout.addWidget(self.employee_combobox)

        self.edit_employee_button = QPushButton("Редагувати працівника")
        self.edit_employee_button.clicked.connect(self.edit_employee)
        layout.addWidget(self.edit_employee_button)

        self.add_employee_button = QPushButton("Додати працівника")
        self.add_employee_button.clicked.connect(self.add_employee)
        layout.addWidget(self.add_employee_button)

    def populate_employee_combobox(self):
        employees = self.employee_manager.get_all_employees()
        self.employee_combobox.clear()
        for employee in employees:
            self.employee_combobox.addItem(employee.full_name, userData=employee.id)

    def create_salary_report_page(self, layout):
        department_label = QLabel("Відділ:")
        self.department_combobox_report = QComboBox()
        self.department_combobox_report.addItem("IT")
        self.department_combobox_report.addItem("HR")

        calculate_button = QPushButton("Розрахувати зарплатну звітність")
        calculate_button.clicked.connect(self.calculate_salary_report)

        layout.addWidget(department_label)
        layout.addWidget(self.department_combobox_report)
        layout.addWidget(calculate_button)

        self.salary_report_textedit = QTextEdit()
        layout.addWidget(self.salary_report_textedit)

        filename_label = QLabel("Ім'я файлу:")
        self.filename_lineedit = QLineEdit()
        self.filename_lineedit.setText("new_report")

        export_button = QPushButton("Експортувати в файл")
        export_button.clicked.connect(self.export_to_txt)

        layout.addWidget(filename_label)
        layout.addWidget(self.filename_lineedit)
        layout.addWidget(export_button)

    def show_home_page(self):
        self.stacked_widget.setCurrentIndex(0)

    def show_view_employees_page(self):
        self.stacked_widget.setCurrentIndex(1)

    def show_salary_report_page(self):
        self.stacked_widget.setCurrentIndex(2)

    def search_employees_view(self):
        department = self.department_combobox.currentText()
        position = self.position_combobox.currentText()
        full_name = self.full_name_lineedit.text()
        employees = self.employee_manager.search(department, position, full_name)

        result = ""
        for employee in employees:
            result += f"ПІБ: {employee.full_name}, Посада: {employee.position}, Відділ: {employee.department}\n"

        self.result_textedit.setPlainText(result)

    def calculate_salary_report(self):
        department = self.department_combobox_report.currentText()
        report = self.employee_manager.calculate_salary_report(department)

        self.salary_report_textedit.setPlainText(report)

    def edit_employee(self):
        selected_employee_id = self.employee_combobox.currentData()
        if selected_employee_id is not None:
            selected_employee = self.employee_manager.from_db(selected_employee_id)
            if selected_employee:
                dialog = EmployeeEditDialog(selected_employee, self.employee_manager)
                if dialog.exec_():
                    updated_employee = dialog.get_updated_employee()
                    self.employee_manager.update_in_db(updated_employee)
                    self.populate_employee_combobox()

    def export_to_txt(self):
        department = self.department_combobox_report.currentText()
        filename = self.filename_lineedit.text() + ".txt"
        self.employee_manager.export_to_txt(filename, department)

    def add_employee(self):
        new_employee = Employee(None, "", "", "", "", "", "", "", 0, "")
        dialog = EmployeeEditDialog(new_employee, self.employee_manager)
        if dialog.exec_():
            pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = EmployeeApp()
    window.show()
    sys.exit(app.exec_())
