import application.salary as salary
import application.db.people as people
from datetime import datetime as dt
import pyjokes


if __name__ == '__main__':
    salary.calculate_salary()
    people.get_employees()
    print("Дата расчета: ", dt.now().strftime("%d-%m-%y"))
    print("Рубрика 'Шуточки за 300': \t", pyjokes.get_joke())




