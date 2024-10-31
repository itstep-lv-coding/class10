from idlelib.iomenu import encoding
from typing import List,Dict

# Читання файлу
# List
def read_file(file_name:str) -> List[str]:
    file_lines=[]
    try:
        with open(file_name, 'r', encoding="UTF16") as file:
            file_lines = file.readlines()
    except FileNotFoundError:
        print(f"File {file_name} not found")
    except PermissionError:
        print()
    except Exception as e:
        print(f"Error {e}")
    return file_lines

def parse_report_lines(file_lines) -> List[Dict[str, str]]:
# [ {"kiosk": "Стрийська", "expenses"="400"}, {"kiosk": "Стрийська", "expenses"="400"} ]
    res=[]
    for line in file_lines[1:]:
        parts = line.strip().split('\t')
        kiosk = parts[5]
        expenses = parts[4]
        res.append({"kiosk": kiosk, "expenses": expenses})
    return res


def calculate_expenses_by_kiosk(expenses) -> dict[str, int]:
    res = {}
    for expense in expenses:
        kiosk = expense["kiosk"]
        expenses = float(expense["expenses"])
        res[kiosk]=res.get(kiosk, 0) + expenses
    return res


def main():
    file_lines = read_file('kiosk2.txt')
    expenses = parse_report_lines(file_lines)
    expenses_by_kiosk = calculate_expenses_by_kiosk(expenses)
    print(expenses_by_kiosk)
    # Закупівля інгредієнтів	М'ясо	Постачальник м'яса	05.10.2024	3000	Стрийська


if __name__ == '__main__':
    main()