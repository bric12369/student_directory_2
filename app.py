from lib.database_connection import *
from lib.cohort_repository import *

class Application:
    def __init__(self):
        self._connection = DatabaseConnection()
        self._connection.connect()
        self._connection.seed('seeds/students.sql')

    def run(self):
        repo = CohortRepository(self._connection)

        choice = input('\nWhich cohort do you require information on, 1 or 2?\n')

        print(f'\nYou have chosen {choice}\n')

        if choice == '1' or choice == '2':
            res = repo.find_with_students(choice)
            print(f'Cohort {choice}, {res.name}, started on {res.start_date}.\nThe following students are enrolled:')
            [print('    ',res.student.name) for res.student in res.students]
        else:
            print('Invalid choice. Please choose 1 or 2.')

if __name__ == '__main__':
    app = Application()
    app.run()