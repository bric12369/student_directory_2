from lib.cohort import *
from lib.student import *

class CohortRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * FROM cohorts')
        cohorts = []
        for row in rows:
            cohort = Cohort(row['id'], row['name'], row['start_date'])
            cohorts.append(cohort)
        return cohorts
    
    def find(self, cohort_id):
        rows = self._connection.execute('SELECT * FROM cohorts WHERE id = %s', [cohort_id])
        row = rows[0]
        return Cohort(row['id'], row['name'], row['start_date'])
    
    def find_with_students(self, cohort_id):
        rows = self._connection.execute(
            'SELECT cohort_id, ' \
            'cohorts.name AS cohort_name, ' \
            'start_date, ' \
            'students.id AS student_id, ' \
            'students.name AS student_name ' \
            'FROM cohorts ' \
            'JOIN students ON cohorts.id = students.cohort_id ' \
            'WHERE cohort_id = %s', [cohort_id])
        students = []
        for row in rows:
            student = Student(row['student_id'], row['student_name'], row['cohort_id'])
            students.append(student)
        cohort = Cohort(rows[0]['cohort_id'], rows[0]['cohort_name'], rows[0]['start_date'], students)
        return cohort