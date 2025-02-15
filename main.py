from sys import exit
from unicodedata import category


def main() -> None:
    exit_message: str = 'Exiting program...'
    while True:
        try:
            user_input: str = input('Enter the cost of a square unit: ')
            if user_input == 'exit':
                print(exit_message)
                exit()

            currency_symbols: list[str] = [
                ch for ch in user_input if category(ch) == 'Sc']

            if currency_symbols != [] and len(currency_symbols) == 1:
                currency_symbol: str = currency_symbols[0]
                cost_per_square: float = float(user_input[1:])
            else:
                print('Please enter a valid cost...')
                continue

            if cost_per_square <= 0:
                print('Please enter a valid cost...')
                continue

            user_input = input('Enter the width of a tile: ')

            if user_input[-2:] == 'cm' or user_input[-2:] == 'mm' or user_input[-2:] == '\'\'' or user_input[-2:] == 'in':
                width: float = float(user_input[:-2])
                length_unit: str = user_input[-2:]
            elif user_input[-1] == 'm':
                width: float = float(user_input[:-1])
                length_unit: str = user_input[-1]
            else:
                print('Please enter a valid width....')

            if width <= 0:
                print('Please enter a valid width...')
                continue

            user_input = input('Enter the height of a tile: ')

            if user_input[-2:] == length_unit:
                height: float = float(user_input[:-2])
            elif user_input[-1] == length_unit:
                height: float = float(user_input[:-1])
            else:
                print('Please enter a valid height...')
                continue

            if height <= 0:
                print('Please enter a valid height...')
                continue

            total_cost: float = cost_per_square * width * height

            print(f'Total cost = {currency_symbol}{total_cost:.2f}')

        except ValueError:
            print('Please enter valid input...')
            continue

        except KeyboardInterrupt:
            print(exit_message)
            exit()


if __name__ == '__main__':
    main()
