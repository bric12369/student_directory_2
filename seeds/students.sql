DROP TABLE IF EXISTS students;
DROP TABLE IF EXISTS cohorts;

CREATE TABLE cohorts(
    id SERIAL PRIMARY KEY,
    name TEXT,
    start_date TEXT
);

CREATE TABLE students(
    id SERIAL PRIMARY KEY,
    name TEXT,
    cohort_id INT REFERENCES cohorts(id)
    on delete cascade
);

INSERT INTO cohorts
    (name, start_date)
    VALUES('Orange', '12/12/2025');

INSERT INTO cohorts
    (name, start_date)
    VALUES('Blue', '12/06/2025');

INSERT INTO students
    (name, cohort_id)
    VALUES('John Robinson', 1);

INSERT INTO students
    (name, cohort_id)
    VALUES('Jane Smith', 2);