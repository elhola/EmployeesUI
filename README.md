# EmployeesUI
with PostgreSQL

Notes: 

CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
    department VARCHAR(255),
    position VARCHAR(255),
    full_name VARCHAR(255),
    address VARCHAR(255),
    phone VARCHAR(15),
    date_of_birth DATE,
    hire_date DATE,
    salary DECIMAL(10, 2),
    company_info TEXT
);

<img width="1179" alt="Снимок экрана 2023-11-02 в 11 37 39" src="https://github.com/elhola/EmployeesUI/assets/25703908/41686fce-c202-46d4-a28e-040d5bbd22ab">


<img width="912" alt="Снимок экрана 2023-11-02 в 11 44 47" src="https://github.com/elhola/EmployeesUI/assets/25703908/7732a0ad-2400-4b62-93e9-29644dd9beb3">
<img width="912" alt="Снимок экрана 2023-11-02 в 11 45 07" src="https://github.com/elhola/EmployeesUI/assets/25703908/176669dc-3ddb-4d9b-99b9-3113f84a4c18">
<img width="408" alt="Снимок экрана 2023-11-02 в 11 45 26" src="https://github.com/elhola/EmployeesUI/assets/25703908/92a5083b-7e7f-47e7-a4a4-d60f76fd8fd8">
<img width="912" alt="Снимок экрана 2023-11-02 в 11 45 35" src="https://github.com/elhola/EmployeesUI/assets/25703908/8f9c25a3-3102-4455-8942-de35803f83bc">
