from lib.student import *

def test_init_with_attributes():
    student = Student(1, 'John Smith', 1)
    assert student.id == 1
    assert student.name == 'John Smith'
    assert student.cohort_id == 1

def test_instances_with_same_attributes_equal():
    student1 = Student(1, 'John Smith', 1)
    student2 = Student(1, 'John Smith', 1)
    assert student1 == student2

def test_format():
    student = Student(1, 'John Smith', 1)
    assert str(student) == 'Student(1, John Smith, 1)'