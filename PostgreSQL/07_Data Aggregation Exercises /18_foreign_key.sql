CREATE TABLE employees_projects(
	id SERIAL PRIMARY KEY,
	employee_id INT REFERENCES employees(id),
	project_id INT REFERENCES projects(id)
);


-- OR
CREATE TABLE employees_projects (
	id INT PRIMARY KEY,
	employee_id INT,
	project_id INT,

	FOREIGN KEY (employee_id) REFERENCES employees(id),
	FOREIGN KEY (project_id) REFERENCES projects(id)
);