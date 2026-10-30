from datetime import datetime
GREEN = "\033[92m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
PURPLE = "\033[95m"
RED = "\033[91m"
RESET = "\033[0m"


def calculate_bmi():

    print(CYAN + "\n========== BMI CALCULATOR ==========" + RESET)

    name = input("Enter your name: ")

    try:
        weight = float(input("Enter weight (kg): "))
        height = float(input("Enter height (cm): "))

        if weight <= 0 or height <= 0:
            print(RED + "Please enter positive values!" + RESET)
            return

        height_m = height / 100
        bmi = weight / (height_m ** 2)

        if bmi < 18.5:
            category = "Underweight"
            advice = "Focus on balanced nutrition."
            color = YELLOW

        elif bmi < 25:
            category = "Normal Weight"
            advice = "Maintain your healthy habits!"
            color = GREEN

        elif bmi < 30:
            category = "Overweight"
            advice = "Regular physical activity may help."
            color = YELLOW

        else:
            category = "Obesity"
            advice = "Consider consulting a healthcare professional."
            color = RED

        print(PURPLE + "\n========== YOUR BMI REPORT ==========" + RESET)

        print(CYAN + f"Name     : {name}" + RESET)
        print(f"Weight   : {weight} kg")
        print(f"Height   : {height} cm")
        print(f"BMI      : {bmi:.2f}")

        print(color + f"Category : {category}" + RESET)

        progress = min(int(bmi / 40 * 30), 30)

        print("\nBMI Progress:")
        print(GREEN + "[" + "#" * progress +
              "-" * (30 - progress) + "]" + RESET)

        print(CYAN + f"\nHealth Tip: {advice}" + RESET)

        with open("bmi_history.txt", "a") as file:
            file.write(
                f"Name: {name} | BMI: {bmi:.2f} | "
                f"Category: {category}\n"
            )
            current_time = datetime.now().strftime("%d-%m-%Y %I:%M %p")

        with open("BMI_Report.txt", "a") as report:
            report.write("\n========== BMI REPORT ==========\n")
            report.write(f"Name: {name}\n")
            report.write(f"Weight: {weight} kg\n")
            report.write(f"Height: {height} cm\n")
            report.write(f"BMI: {bmi:.2f}\n")
            report.write(f"Category: {category}\n")
            report.write(f"Health Tip: {advice}\n")
            report.write(f"Date & Time: {current_time}\n")
            report.write("===============================\n")

        print(GREEN + "Your detailed report is saved!" + RESET)

        print(GREEN + "\nReport saved successfully!" + RESET)

    except ValueError:
        print(RED + "Invalid input! Enter numbers only." + RESET)


if __name__ == "__main__":
    calculate_bmi()