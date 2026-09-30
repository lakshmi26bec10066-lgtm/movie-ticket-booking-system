# 5.1 README.md

# Book My Show - Cinema Ticket Booking System

## 1. Project Title

**Book My Show - Cinema Ticket Booking System**

A Python-based cinema ticket booking project developed as a Computer Science practical project.

---

## 2. Overview of the Project

The **Book My Show - Cinema Ticket Booking System** is a console-based Python application for managing cinema theaters and ticket bookings.

The project allows an administrator to log in, add and manage theater details, book tickets, cancel tickets, search theater and booking information, and generate reports.

This version of the project uses **Python only** for data handling. SQL and MySQL database commands have been removed. Theater and ticket-booking information is stored temporarily using Python lists.

The project is divided into different Python modules so that each part of the application has a separate purpose.

---

## 3. Features

### Login
- Administrator login using User ID and Password.
- Invalid credentials are rejected.

### Theater Registration
- Add theater details.
- Update theater details.
- Remove theater details.
- Search theater details.

### Ticket Booking
- Display available theater information.
- Book a ticket using Booking ID and Theater ID.
- Select ticket type:
  - Front
  - Middle
  - Back
  - Balcony
- Calculate the ticket fare according to the selected theater and ticket type.

### Ticket Cancellation
- Cancel a ticket using the Booking ID.
- Remove the booking from the booking data.
- Update the corresponding theater seat count.

### Booking Search
- Search booking details using the Booking ID.
- Display Booking ID, Theater ID, ticket type, and price.

### Reports
- Generate a report based on ticket/seat type.
- Generate a report based on total ticket price.
- Display reports as bar graphs using Matplotlib.

---

## 4. Technologies / Tools Used

| Technology / Tool | Purpose |
|---|---|
| **Python 3** | Main programming language |
| **Python Lists** | Temporary storage of theater and booking data |
| **Python Functions** | Organizing different operations |
| **Python Modules** | Separating the project into multiple files |
| **Matplotlib** | Creating graphical reports |
| **VS Code / IDLE / PyCharm** | Any Python-compatible code editor can be used |
| **Command Prompt / Terminal** | Running the application |

### Project Modules

```text
Book_My_Show/
│
├── main.py
├── login.py
├── homepage.py
├── registration.py
├── booking.py
├── reports.py
├── data.py
└── README.md
```

### Module Responsibilities

- **main.py** - Starts the application.
- **login.py** - Handles administrator login.
- **homepage.py** - Displays the main application menu.
- **registration.py** - Handles theater registration and theater search operations.
- **booking.py** - Handles ticket booking, cancellation, and booking search.
- **reports.py** - Generates graphical reports.
- **data.py** - Contains the Python lists used for temporary data storage.

---

## 5. Steps to Install & Run the Project

### Step 1: Install Python

Install **Python 3** on the computer.

Check the installation using:

```bash
python --version
```

If required, use:

```bash
python3 --version
```

### Step 2: Install Matplotlib

The report section uses Matplotlib.

Install it with:

```bash
pip install matplotlib
```

Or:

```bash
python -m pip install matplotlib
```

### Step 3: Download / Copy the Project

Place all project files in the same folder:

```text
main.py
login.py
homepage.py
registration.py
booking.py
reports.py
data.py
README.md
```

### Step 4: Open the Project Folder

Open the project folder in Command Prompt, PowerShell, VS Code, or another Python-compatible environment.

### Step 5: Run the Project

Run:

```bash
python main.py
```

The program will display the login screen.

### Default Login

```text
USER ID: Admin
PASSWORD: mgm
```

After successful login, the main homepage will be displayed.

---

## 6. Instructions for Testing

The project can be tested by checking each feature separately.

### Test 1: Login

**Input:**

```text
USER ID: Admin
PASSWORD: mgm
```

**Expected Result:**

```text
SUCCESSFULLY LOGGED !!!!
```

The homepage should be displayed.

Also test an incorrect User ID or Password.

**Expected Result:**

```text
INCORRECT CREDENTIALS
```

---

### Test 2: Add Theater

Go to:

```text
Homepage
→ Registration Session
→ ADD THEATER DETAILS
```

Enter valid theater information.

**Expected Result:**

```text
SUCCESSFULLY ADD THEATER DEATILS
```

The theater details should be available when the theater list is displayed.

---

### Test 3: Update Theater

Go to:

```text
Registration Session
→ UPDATE THEATER DETAILS
```

Enter an existing Theater ID and new theater information.

**Expected Result:**

```text
SUCCESSFULLY UPDATE THEATER DEATILS
```

The stored theater information should be updated.

---

### Test 4: Remove Theater

Go to:

```text
Registration Session
→ REMOVE DETAILS OF THEATER
```

Enter an existing Theater ID.

**Expected Result:**

```text
SUCCESSFULLY REMOVE   THEATER DEATILS
```

The theater should no longer appear in the theater data.

---

### Test 5: Search Theater

Go to:

```text
Registration Session
→ SEARCH
```

Enter a Theater ID.

**Expected Result:**

The matching theater details should be displayed.

---

### Test 6: Ticket Booking

Go to:

```text
Homepage
→ Ticket Booking
→ Ticket Booking
```

Enter:

- Booking ID
- Theater ID
- Ticket type

Use one of:

```text
Front
Middle
Back
Balcony
```

**Expected Result:**

```text
Successfully Booking done
```

The booking should be stored in the booking data.

---

### Test 7: Search Booking

Go to:

```text
Ticket Booking
→ Search Booking details
```

Enter the Booking ID used during booking.

**Expected Result:**

The program should display:

```text
Bookingid
TheaterId
Typeofseat
price
```

with the corresponding booking details.

---

### Test 8: Ticket Cancellation

Go to:

```text
Ticket Booking
→ Ticket Cancellation
```

Enter an existing Booking ID.

**Expected Result:**

```text
SUCCESSFULLY DONE THE CANCELLATION OF TICKET
```

The booking should be removed from the booking data.

---

### Test 9: Seat-Type Report

Go to:

```text
Homepage
→ REPORT
→ Report Based on Types of seats
```

**Expected Result:**

A bar graph showing the number of bookings for each ticket type should be displayed.

---

### Test 10: Ticket-Price Report

Go to:

```text
Homepage
→ REPORT
→ Report Based on Ticket price
```

**Expected Result:**

A bar graph showing the total ticket amount for each ticket type should be displayed.

---

## 7. Screenshots

Screenshots are recommended for the final project submission.

Suggested screenshots to include:

### Screenshot 1 - Login Screen

Capture the initial login screen showing:

```text
WELCOME TO BOOK MY SHOW
Enter USER ID:
Enter PASSWORD:
```

### Screenshot 2 - Homepage

Capture the main menu showing:

```text
1. Registration Session
2. Ticket Booking
3. SEARCH
4. REPORT
```

### Screenshot 3 - Theater Registration

Capture the screen used to enter theater details.

### Screenshot 4 - Ticket Booking

Capture the ticket booking screen and successful booking message.

### Screenshot 5 - Booking Search

Capture the displayed booking details.

### Screenshot 6 - Reports

Capture one or both Matplotlib graphs generated by the application.

> **Note:** Actual screenshots are not included in this README because no screenshots were provided with the project files. Screenshots can be added to this section after running the application.

---

## Data Storage

This project does not use SQL or MySQL.

The file `data.py` contains Python lists for temporary storage:

```python
Theater = []
ticketbooking = []
```

Theater information is stored in `Theater`.

Ticket booking information is stored in `ticketbooking`.

### Important

The data is stored only while the program is running. When the program is closed, the data in these lists is lost.

---

## Project Flow

```text
main.py
   |
   v
Login
   |
   v
Homepage
   |
   +---- Registration Session
   |       |
   |       +---- Add Theater
   |       +---- Update Theater
   |       +---- Remove Theater
   |       +---- Search Theater
   |
   +---- Ticket Booking
   |       |
   |       +---- Ticket Booking
   |       +---- Ticket Cancellation
   |       +---- Search Booking
   |
   +---- Search
   |
   +---- Report
           |
           +---- Seat Type Report
           +---- Ticket Price Report
```

---

## Conclusion

The Book My Show project demonstrates the use of Python programming concepts including:

- Functions
- Modules
- Lists
- Loops
- Conditional statements
- User input
- Data manipulation
- Matplotlib graphs

The project is organized into separate modules and can be run directly through `main.py`.

