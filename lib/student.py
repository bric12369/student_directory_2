class Student:
    def __init__(self, name, cohort_id):
        self.name = name
        self.cohort_id = cohort_id
    
    def __eq__(self, value):
        return self.__dict__ == value.__dict__
    
    def __repr__(self):
        return f'Student({self.name}, {self.cohort_id})'