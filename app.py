from lib.database_connection import *

connection = DatabaseConnection()
connection.connect()
connection.seed('seeds/students.sql')