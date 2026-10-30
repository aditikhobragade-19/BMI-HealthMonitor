def view_history():

    print("\n" + "=" * 45)
    print("             BMI HISTORY")
    print("=" * 45)

    try:
        with open("bmi_history.txt", "r") as file:
            history = file.readlines()

        records = [line for line in history if line.strip()]

        print(f"\nTotal BMI Records: {len(records)}")

        if records:
            print("\nYour Previous BMI Reports:\n")

            for number, record in enumerate(records, start=1):
                print(f"{number}. {record.strip()}")

        else:
            print("\nNo BMI records available.")

    except FileNotFoundError:
        print("\nNo history file found.")

    print("=" * 45)


if __name__ == "__main__":
    view_history()