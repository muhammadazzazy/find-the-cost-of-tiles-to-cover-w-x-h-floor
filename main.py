def main() -> None:
    while True:
        user_input = input('Enter the cost of a square unit: ')
        if user_input == 'exit':
            break
        try:
            cost_per_square = float(user_input)
            while cost_per_square <= 0:
                cost_per_square = float(
                    input('Enter the cost of a square unit: '))

            width = float(input('Enter the width of a tile: '))
            while width <= 0:
                width = float(input('Enter the width of a tile: '))

            height = float(input('Enter the height of a tile: '))
            while height <= 0:
                height = float(input('Enter the height of a tile'))
            total_cost = cost_per_square * width * height
            print(f'The cost of tiles to cover a {
                width} x {height} floor is {total_cost}.')
        except ValueError:
            print('The input should be a floating-point number!')


if __name__ == '__main__':
    main()
