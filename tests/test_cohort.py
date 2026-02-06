from lib.cohort import *

def test_init_with_attributes():
    cohort = Cohort(1, 'Blue', '12/12/2025')
    assert cohort.id == 1
    assert cohort.name == 'Blue'
    assert cohort.start_date == '12/12/2025'

def test_instances_with_same_attributes_equal():
    cohort1 = Cohort(1, 'Blue', '12/12/2025')
    cohort2 = Cohort(1, 'Blue', '12/12/2025')
    assert cohort1 == cohort2

def test_format():
    cohort = Cohort(1, 'Blue', '12/12/2025')
    assert str(cohort) == 'Cohort(1, Blue, 12/12/2025)'