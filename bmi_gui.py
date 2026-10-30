import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import os

# ---------------- CONFIGURATION ----------------

BG = "#F3F6FC"
CARD = "#FFFFFF"
PRIMARY = "#3157D5"
DARK = "#172B4D"
MUTED = "#718096"
GREEN = "#15966A"
ORANGE = "#E99A32"
RED = "#D94B55"

HISTORY_FILE = "bmi_history.txt"
REPORT_FILE = "BMI_Report.txt"

# ---------------- BMI CALCULATION ----------------

def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight", "Consider a balanced and nutritious diet.", ORANGE
    elif bmi < 25:
        return "Normal Weight", "Great! Keep maintaining healthy habits.", GREEN
    elif bmi < 30:
        return "Overweight", "Regular activity and balanced meals may help.", ORANGE
    else:
        return "Obesity", "Consider discussing your health goals with a doctor.", RED


def calculate_bmi():
    name = name_entry.get().strip()

    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())
    except ValueError:
        messagebox.showerror(
            "Invalid Input",
            "Please enter valid numbers for weight and height."
        )
        return

    if not name:
        messagebox.showwarning("Missing Name", "Please enter your name.")
        return

    if weight <= 0 or height <= 0:
        messagebox.showwarning(
            "Invalid Input",
            "Weight and height must be greater than zero."
        )
        return

    if weight > 500 or height > 300:
        messagebox.showwarning(
            "Invalid Input",
            "Please check your weight and height values."
        )
        return

    height_m = height / 100
    bmi = weight / (height_m ** 2)

    category, advice, result_color = get_bmi_category(bmi)
    now = datetime.now()
    date_time = now.strftime("%d-%m-%Y %I:%M %p")

    # Display result
    result_value.config(text=f"{bmi:.2f}", fg=result_color)
    category_value.config(text=category, fg=result_color)
    advice_value.config(text=advice)

    result_card.pack(fill="x", padx=25, pady=15)

    # Save history
    record = (
        f"{date_time} | {name} | {weight} kg | "
        f"{height} cm | BMI: {bmi:.2f} | {category}\n"
    )

    try:
        with open(HISTORY_FILE, "a", encoding="utf-8") as file:
            file.write(record)

        with open(REPORT_FILE, "a", encoding="utf-8") as file:
            file.write(
                "\n========== BMI HEALTH REPORT ==========\n"
                f"Date & Time : {date_time}\n"
                f"Name        : {name}\n"
                f"Weight      : {weight} kg\n"
                f"Height      : {height} cm\n"
                f"BMI         : {bmi:.2f}\n"
                f"Category    : {category}\n"
                f"Advice      : {advice}\n"
                "=======================================\n"
            )

        update_total_records()

    except OSError as error:
        messagebox.showerror("File Error", str(error))


# ---------------- RESET ----------------

def reset_fields():
    name_entry.delete(0, tk.END)
    weight_entry.delete(0, tk.END)
    height_entry.delete(0, tk.END)

    result_value.config(text="--", fg=PRIMARY)
    category_value.config(text="Waiting for calculation", fg=MUTED)
    advice_value.config(text="Enter your details to see your health advice.")

    result_card.pack_forget()
    name_entry.focus()


# ---------------- HISTORY ----------------

def view_history():
    history_window = tk.Toplevel(root)
    history_window.title("BMI History")
    history_window.geometry("780x480")
    history_window.configure(bg=BG)
    history_window.minsize(600, 350)

    tk.Label(
        history_window,
        text="Your BMI History",
        font=("Segoe UI", 20, "bold"),
        bg=BG,
        fg=DARK
    ).pack(anchor="w", padx=25, pady=(20, 5))

    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as file:
            records = [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        records = []

    tk.Label(
        history_window,
        text=f"Total Records: {len(records)}",
        font=("Segoe UI", 11, "bold"),
        bg=BG,
        fg=PRIMARY
    ).pack(anchor="w", padx=25, pady=5)

    table_frame = tk.Frame(history_window, bg=CARD)
    table_frame.pack(fill="both", expand=True, padx=25, pady=15)

    scrollbar = ttk.Scrollbar(table_frame, orient="vertical")
    scrollbar.pack(side="right", fill="y")

    history_list = tk.Listbox(
        table_frame,
        font=("Consolas", 10),
        bg=CARD,
        fg=DARK,
        yscrollcommand=scrollbar.set,
        activestyle="none",
        selectbackground=PRIMARY
    )
    history_list.pack(side="left", fill="both", expand=True)
    scrollbar.config(command=history_list.yview)

    if records:
        for index, record in enumerate(records, start=1):
            history_list.insert(tk.END, f"{index}. {record}")
    else:
        history_list.insert(tk.END, "No BMI records found yet.")

    tk.Button(
        history_window,
        text="Close",
        command=history_window.destroy,
        bg=PRIMARY,
        fg="white",
        font=("Segoe UI", 10, "bold"),
        relief="flat",
        padx=25,
        pady=8,
        cursor="hand2"
    ).pack(pady=(0, 20))


# ---------------- TOTAL RECORDS ----------------

def update_total_records():
    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as file:
            total = sum(1 for line in file if line.strip())
    except FileNotFoundError:
        total = 0

    total_value.config(text=str(total))


# ---------------- OPEN REPORT ----------------

def open_report():
    if not os.path.exists(REPORT_FILE):
        messagebox.showinfo("Report", "No report available yet.")
        return

    try:
        os.startfile(os.path.abspath(REPORT_FILE))
    except OSError:
        messagebox.showinfo(
            "Report",
            f"Your report is saved as {REPORT_FILE} in the project folder."
        )


# ---------------- MAIN WINDOW ----------------

root = tk.Tk()
root.title("BMI Health Tracker | Dashboard")
root.geometry("850x760")
root.minsize(650, 650)
root.configure(bg=BG)

# ---------------- HEADER ----------------

header = tk.Frame(root, bg=DARK, height=125)
header.pack(fill="x")
header.pack_propagate(False)

tk.Label(
    header,
    text="BMI HEALTH TRACKER",
    font=("Segoe UI", 25, "bold"),
    bg=DARK,
    fg="white"
).pack(anchor="w", padx=30, pady=(22, 2))

tk.Label(
    header,
    text="Your personal health and wellness dashboard",
    font=("Segoe UI", 11),
    bg=DARK,
    fg="#C9D5EA"
).pack(anchor="w", padx=32)


# ---------------- DASHBOARD SUMMARY ----------------

summary = tk.Frame(root, bg=BG)
summary.pack(fill="x", padx=25, pady=20)

tk.Label(
    summary,
    text="TOTAL BMI RECORDS",
    font=("Segoe UI", 10, "bold"),
    bg=BG,
    fg=MUTED
).pack(side="left")

total_value = tk.Label(
    summary,
    text="0",
    font=("Segoe UI", 20, "bold"),
    bg=BG,
    fg=PRIMARY
)
total_value.pack(side="left", padx=12)


# ---------------- INPUT CARD ----------------

input_card = tk.Frame(root, bg=CARD, highlightthickness=1,
                      highlightbackground="#E1E7F0")
input_card.pack(fill="x", padx=25, pady=5)

tk.Label(
    input_card,
    text="Calculate Your BMI",
    font=("Segoe UI", 17, "bold"),
    bg=CARD,
    fg=DARK
).pack(anchor="w", padx=22, pady=(18, 12))


def create_input(label_text, placeholder):
    tk.Label(
        input_card,
        text=label_text,
        font=("Segoe UI", 10, "bold"),
        bg=CARD,
        fg=DARK
    ).pack(anchor="w", padx=22, pady=(7, 3))

    entry = tk.Entry(
        input_card,
        font=("Segoe UI", 12),
        bg="#F7F9FD",
        fg=DARK,
        relief="flat",
        highlightthickness=1,
        highlightbackground="#DCE3EF",
        highlightcolor=PRIMARY
    )
    entry.pack(fill="x", padx=22, ipady=9)

    return entry


name_entry = create_input("Full Name", "Enter your name")
weight_entry = create_input("Weight (kg)", "Enter weight in kg")
height_entry = create_input("Height (cm)", "Enter height in cm")


# ---------------- ACTION BUTTONS ----------------

button_frame = tk.Frame(input_card, bg=CARD)
button_frame.pack(fill="x", padx=22, pady=20)

tk.Button(
    button_frame,
    text="Calculate BMI",
    command=calculate_bmi,
    bg=PRIMARY,
    fg="white",
    activebackground="#2446B5",
    activeforeground="white",
    font=("Segoe UI", 11, "bold"),
    relief="flat",
    padx=22,
    pady=11,
    cursor="hand2"
).pack(side="left", padx=(0, 10))

tk.Button(
    button_frame,
    text="Reset",
    command=reset_fields,
    bg="#E9EEF8",
    fg=DARK,
    font=("Segoe UI", 11, "bold"),
    relief="flat",
    padx=22,
    pady=11,
    cursor="hand2"
).pack(side="left")


# ---------------- RESULT CARD ----------------

result_card = tk.Frame(
    root,
    bg=CARD,
    highlightthickness=1,
    highlightbackground="#E1E7F0"
)

tk.Label(
    result_card,
    text="YOUR BMI RESULT",
    font=("Segoe UI", 11, "bold"),
    bg=CARD,
    fg=MUTED
).pack(pady=(15, 2))

result_value = tk.Label(
    result_card,
    text="--",
    font=("Segoe UI", 35, "bold"),
    bg=CARD,
    fg=PRIMARY
)
result_value.pack()

category_value = tk.Label(
    result_card,
    text="Waiting for calculation",
    font=("Segoe UI", 14, "bold"),
    bg=CARD,
    fg=MUTED
)
category_value.pack(pady=4)

advice_value = tk.Label(
    result_card,
    text="Enter your details to see your health advice.",
    font=("Segoe UI", 10),
    bg=CARD,
    fg=DARK,
    wraplength=650
)
advice_value.pack(pady=(4, 18))


# ---------------- HISTORY AND REPORT BUTTONS ----------------

bottom_frame = tk.Frame(root, bg=BG)
bottom_frame.pack(fill="x", padx=25, pady=15)

tk.Button(
    bottom_frame,
    text="View BMI History",
    command=view_history,
    bg=GREEN,
    fg="white",
    font=("Segoe UI", 10, "bold"),
    relief="flat",
    padx=18,
    pady=10,
    cursor="hand2"
).pack(side="left", padx=(0, 10))

tk.Button(
    bottom_frame,
    text="Open BMI Report",
    command=open_report,
    bg=DARK,
    fg="white",
    font=("Segoe UI", 10, "bold"),
    relief="flat",
    padx=18,
    pady=10,
    cursor="hand2"
).pack(side="left")


# ---------------- FOOTER ----------------

tk.Label(
    root,
    text="BMI is a screening tool, not a medical diagnosis.",
    font=("Segoe UI", 9),
    bg=BG,
    fg=MUTED
).pack(side="bottom", pady=12)


# ---------------- START APPLICATION ----------------

update_total_records()
name_entry.focus()

root.mainloop()