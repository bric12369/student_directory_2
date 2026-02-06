from lib.cohort_repository import *
from lib.cohort import *

def test_lists_all_cohorts(db_connection):
    db_connection.seed('seeds/students.sql')
    repo = CohortRepository(db_connection)
    assert repo.all() == [
        Cohort(1, 'Orange', '12/12/2025'),
        Cohort(2, 'Blue', '12/06/2025')
    ]