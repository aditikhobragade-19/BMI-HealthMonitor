BMI & Health Monitor

A Python-based BMI (Body Mass Index) Calculator designed to help users calculate their BMI, understand their weight category, view basic health guidance, and maintain a record of previous calculations through a user-friendly desktop application.

About the Project

BMI & Health Monitor is a desktop application developed using Python and Tkinter. It provides a simple and interactive interface where users can enter their name, weight, and height to calculate their Body Mass Index.

The application displays the calculated BMI, identifies the corresponding BMI category, provides general health advice, and stores calculation records for future reference.

Features

- BMI Calculation: Calculates Body Mass Index using weight and height.
- User-Friendly GUI: Interactive desktop interface built with Tkinter.
- BMI Categories: Displays Underweight, Normal Weight, Overweight, and Obesity categories.
- Health Advice: Provides general guidance based on the calculated BMI.
- BMI History: Stores previous BMI calculations.
- Total Records: Displays the total number of saved BMI records.
- Detailed Reports: Automatically generates a BMI report with date and time.
- Reset Option: Clears input fields for a new calculation.
- Input Validation: Handles invalid and incorrect input values.

Technologies Used

- Python 3.11
- Tkinter
- File Handling
- DateTime Module

Project Structure

BMI-Health-Monitor/
│
├── bmi_calculator.py
├── view_history.py
├── main.py
├── bmi_gui.py
├── bmi_history.txt
├── BMI_Report.txt
└── README.md

Installation and Setup

1. Install Python

Download and install Python from:

https://www.python.org/

2. Clone the Repository

git clone https://github.com/aditikhobragade-19/BMI-HealthMonitor.git

3. Open the Project Folder

cd BMI-HealthMonitor

4. Run the GUI Application

py -3.11 bmi_gui.py

How to Use

1. Launch the BMI Health Monitor application.
2. Enter your full name.
3. Enter your weight in kilograms.
4. Enter your height in centimeters.
5. Click the Calculate BMI button.
6. View your BMI value, category, and general health advice.
7. Click View BMI History to see previous records.
8. Click Open BMI Report to access the detailed report.
9. Use Reset to clear the input fields.

BMI Categories

BMI Range| Category
Below 18.5| Underweight
18.5 – 24.9| Normal Weight
25 – 29.9| Overweight
30 and above| Obesity

Note: BMI is a general screening measure and is not a medical diagnosis. These adult BMI categories may not apply to everyone.

Future Enhancements

- Interactive BMI charts and visual analytics.
- Improved dashboard design.
- User profile management.
- Export reports to PDF.
- Additional health and wellness insights.

Developer

Aditi Khobragade

Project Purpose

This project was developed to strengthen practical Python programming skills, GUI development, file handling, and application development.

---

If you find this project useful, feel free to explore the repository!
