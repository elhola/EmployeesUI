# EmployeesUI
with PostgreSQL

Notes: створення таблиць по НФ

CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
    department TEXT,
    position TEXT,
    full_name TEXT,
    address TEXT,
    phone TEXT,
    date_of_birth DATE,
    hire_date DATE,
    salary NUMERIC
);

CREATE TABLE company (
    id SERIAL PRIMARY KEY,
    name TEXT,
    address TEXT,
    phone TEXT,
    website TEXT
);

<img width="1102" alt="Снимок экрана 2023-11-05 в 10 36 10" src="https://github.com/elhola/EmployeesUI/assets/25703908/bf024681-3a90-4496-b1fa-fcbc3764ed13">


<img width="912" alt="Снимок экрана 2023-11-02 в 11 44 47" src="https://github.com/elhola/EmployeesUI/assets/25703908/7732a0ad-2400-4b62-93e9-29644dd9beb3">
<img width="912" alt="Снимок экрана 2023-11-02 в 11 45 07" src="https://github.com/elhola/EmployeesUI/assets/25703908/176669dc-3ddb-4d9b-99b9-3113f84a4c18">
<img width="335" alt="Снимок экрана 2023-11-05 в 10 24 36" src="https://github.com/elhola/EmployeesUI/assets/25703908/7ebef694-3188-453d-89e3-d2c5cfa18934">
<img width="912" alt="Снимок экрана 2023-11-02 в 11 45 35" src="https://github.com/elhola/EmployeesUI/assets/25703908/8f9c25a3-3102-4455-8942-de35803f83bc">
