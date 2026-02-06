from lib.cohort import *

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