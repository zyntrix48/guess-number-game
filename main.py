from modules.generate_number import *
from modules.guess_controller import *

def main() -> None: 
    min_number = int(input("Enter min number: "))
    max_number = int(input("Enter max number: "))
    target_number  = generate_random_number(min_number, max_number)

    while True:
        number = int(input("Enter guessed number: "))
        guess_number(number, target_number)

if __name__ == "__main__":
    main()