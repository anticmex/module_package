# This is a accounting department program.
from datetime import date
from Accounting_department.application.salary import calculate_salary


def main():
    if __name__ == '__main__':
        print('Добрый день, Главный бухгалтер!')
        print(f'Сегодня {date.today()}')

        if input("Подсчитать затраты на ЗП в этом месяце? (y|n): ").lower() == 'y':
            calculate_salary()
        else:
            print("Скорее всего мы никогда не узнаем затраты текущего месяца!")
    else:
        print('Зафиксирован запуск программы не из главного модуля!')

main()
