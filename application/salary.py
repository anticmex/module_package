# Here the Salary counting is been making
from Accounting_department.application.db.people import get_employers, people_db

salary_amount = 1000000
calculates = get_employers(people_db) * salary_amount
result = '{0:,}'.format(calculates).replace(',', ' ')

def calculate_salary():
    print(f'ЗП предприятия за текущий месяц составляет {result}')
