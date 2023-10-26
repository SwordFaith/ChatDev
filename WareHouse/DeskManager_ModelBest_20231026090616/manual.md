# Work Desks Management System User Manual

## Introduction

The Work Desks Management System is a web application designed to help organizations manage their work desks efficiently. It provides a visual editor to place desks, supports group selection, copying and pasting desks, labeling desks' names, and dragging desks to other positions. Additionally, it includes an editor for managing users and groups, with support for importing and exporting data from/to Excel or CSV files. The system also allows for assigning desks to individual users or groups of users, either visually or through a spreadsheet-like interface.

## Installation

To use the Work Desks Management System, you need to install the required dependencies. Follow the steps below:

1. Make sure you have Python installed on your system. If not, download and install Python from the official website: [Python.org](https://www.python.org/).

2. Open a command prompt or terminal.

3. Navigate to the directory where you have the project files.

4. Run the following command to install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

   This will install the necessary packages, including `numpy`, `pandas`, `tkinter`, and `openpyxl`.

## Getting Started

To start using the Work Desks Management System, follow the steps below:

1. Open a command prompt or terminal.

2. Navigate to the directory where you have the project files.

3. Run the following command to start the application:

   ```
   python main.py
   ```

   This will launch the application in a new window.

## Main Functions

### Visual Editor

The visual editor allows you to place desks on the canvas, select desks, copy desks, paste desks, label desks' names, and drag desks to other positions.

- To place a desk on the canvas, click on an empty area of the canvas.

- To select a desk, click on it. The selected desk will be outlined in red.

- To copy a selected desk, use the copy function (not implemented yet).

- To paste a copied desk, use the paste function (not implemented yet).

- To label a desk's name, right-click on the desk and enter the desired name.

- To drag a selected desk to another position, click and hold the mouse button on the desk, then move the mouse to the desired position.

### User and Group Editor

The user and group editor allows you to manage users and groups, import data from Excel or CSV files, and export data to Excel or CSV files.

- To open the user and group editor, click on the "Users and Groups" button in the application.

- To import data from an Excel or CSV file, click on the "Import" button and select the file. The data will be imported into the system.

- To export data to an Excel or CSV file, click on the "Export" button and select the file. The data will be saved in the selected file format.

### Assigning Desks

The system allows you to assign desks to individual users or groups of users, either visually or through a spreadsheet-like interface.

- To assign a desk to a user or group visually, select the desk and then click on the user or group on the canvas.

- To assign desks to users or groups through a spreadsheet-like interface, click on the "Assign Desks" button in the application. You can then select the desks and users/groups from the table and click on the "Assign" button.

## Conclusion

The Work Desks Management System provides a comprehensive solution for managing work desks in organizations. With its visual editor, user and group editor, and desk assignment capabilities, it simplifies the process of organizing and allocating workspaces. Follow the installation instructions and explore the main functions to effectively utilize the system for your organization's needs.