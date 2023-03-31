from application.salary import *
from application.db.people import *
from datetime import *
from pyjokes import *


if __name__ == '__main__':
    calculate_salary()
    get_employees()
    print("Дата расчета: ", datetime.now().strftime("%d-%m-%y"))
    print("Рубрика 'Шуточки за 300': \t", get_joke())




