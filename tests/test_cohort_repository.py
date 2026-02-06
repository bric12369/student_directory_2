from lib.cohort_repository import *
from lib.cohort import *
from lib.student import *

def test_lists_all_cohorts(db_connection):
    db_connection.seed('seeds/students.sql')
    repo = CohortRepository(db_connection)
    assert repo.all() == [
        Cohort(1, 'Orange', '12/12/2025'),
        Cohort(2, 'Blue', '12/06/2025')
    ]

def test_find(db_connection):
    db_connection.seed('seeds/students.sql')
    repo = CohortRepository(db_connection)
    assert repo.find(1) == Cohort(1, 'Orange', '12/12/2025')

def test_find_with_students(db_connection):
    db_connection.seed('seeds/students.sql')
    repo = CohortRepository(db_connection)
    assert repo.find_with_students(1) == Cohort(1, 'Orange', '12/12/2025', [
        Student(1, 'John Robinson', 1),
        Student(2, 'Rachel Brown', 1)
    ])