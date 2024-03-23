import re
from typing import Callable

def generator_numbers(text: str):
    yield from re.findall(r"\d+\.\d{0,9}", text)

def sum_profit(text: str, generator_numbers: Callable[[str], str]):
    numbers = generator_numbers(text)
    total = sum(float(i) for i in numbers)
    return total
    
def main():
    text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."
    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income}")

if __name__ == "__main__":
    main()
