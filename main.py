# Premium BMI Health Tracker

RESET = "\033[0m"
GREEN = "\033[92m"
CYAN = "\033[96m"
PURPLE = "\033[95m"
YELLOW = "\033[93m"
RED = "\033[91m"

from bmi_calculator import calculate_bmi
from view_history import view_history


def main():

    while True:

        print("\n")
        print(PURPLE + "=" * 48 + RESET)
        print(GREEN + "          💚 BMI HEALTH TRACKER" + RESET)
        print(CYAN + "             YOUR HEALTH MATTERS" + RESET)
        print(PURPLE + "=" * 48 + RESET)

        print(GREEN + "\n  [1] Calculate BMI" + RESET)
        print(CYAN + "  [2] View BMI History" + RESET)
        print(YELLOW + "  [3] Exit Application" + RESET)

        print(PURPLE + "\n" + "-" * 48 + RESET)

        choice = input(YELLOW + "\n  Enter your choice (1-3): " + RESET)

        if choice == "1":
            calculate_bmi()

        elif choice == "2":
            print("BMI HISTORY OPTION SELECTED!")
            view_history()

        elif choice == "3":
            print(GREEN + "\n  Thank you for using BMI Health Tracker!" + RESET)
            print(CYAN + "  Stay Healthy! 💚" + RESET)
            break

        else:
            print(RED + "\n  Invalid choice! Try again." + RESET)


if __name__ == "__main__":
  main()