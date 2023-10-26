# Work Desks Management System User Manual

## Introduction

The Work Desks Management System is a web application developed in Python that allows users to manage work desks and assign them to users or groups. This user manual provides detailed instructions on how to install the necessary dependencies and how to use the software effectively.

## Installation

To install the Work Desks Management System, follow these steps:

1. Ensure that you have Python installed on your system. If not, you can download and install Python from the official website: [Python.org](https://www.python.org/).

2. Clone or download the project files from the repository.

3. Open a terminal or command prompt and navigate to the project directory.

4. Create a virtual environment (optional but recommended) by running the following command:

   ```
   python -m venv venv
   ```

5. Activate the virtual environment. The command may vary depending on your operating system:

   - For Windows:

     ```
     venv\Scripts\activate
     ```

   - For macOS/Linux:

     ```
     source venv/bin/activate
     ```

6. Install the required dependencies by running the following command:

   ```
   pip install -r requirements.txt
   ```

## Usage

To use the Work Desks Management System, follow these steps:

1. Ensure that you have completed the installation steps mentioned above.

2. Open a terminal or command prompt and navigate to the project directory.

3. Activate the virtual environment (if you created one) by running the appropriate command mentioned in the installation steps.

4. Run the following command to start the application:

   ```
   python main.py
   ```

5. The application window will open, displaying the Work Desks Management System.

6. Use the buttons provided to perform various actions:

   - **Place Desk**: Click this button to place a desk on the canvas. You can click on the canvas to position the desk.

   - **Copy**: Click this button to copy the selected desk. You can then paste the copied desk using the Paste button.

   - **Paste**: Click this button to paste the copied desk onto the canvas.

   - **Label**: Click this button to label the selected desk. You can enter the label text in the dialog box that appears.

   - **Assign Desk**: Click this button to assign a desk to a user or desks to a group of users. You can select the user or group visually or using a sheet.

   - **Import**: Click this button to import users from an Excel or CSV file. The file should be named "users.csv" and placed in the project directory.

7. Explore the various features of the Work Desks Management System to manage desks and assign them to users or groups effectively.

## Conclusion

Congratulations! You have successfully installed and learned how to use the Work Desks Management System. Enjoy managing work desks and improving productivity in your organization. If you have any further questions or need assistance, please refer to the documentation or contact our support team.