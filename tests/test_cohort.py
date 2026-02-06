from lib.cohort import *

def test_init_with_attributes():
    cohort = Cohort('Blue', '12/12/2025')
    assert cohort.name == 'Blue'
    assert cohort.start_date == '12/12/2025'