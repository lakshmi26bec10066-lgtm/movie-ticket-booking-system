# Statement of the Project

## 1. Problem Statement

Managing cinema theater and ticket-booking activities manually can be difficult and time-consuming. Theater details, seat information, ticket bookings, cancellations, and booking searches need to be handled in an organized way.

The **Book My Show - Cinema Ticket Booking System** is developed to provide a simple Python-based system for managing these activities through a menu-driven console application.

The system allows the user to manage theater information, book and cancel tickets, search booking details, and generate reports without using SQL or a MySQL database.

---

## 2. Scope of the Project

The scope of the project covers the basic management of cinema theaters and ticket bookings.

The project includes:

- Administrator login.
- Adding theater details.
- Updating theater details.
- Removing theater details.
- Searching theater details.
- Displaying available theater information.
- Booking cinema tickets.
- Cancelling booked tickets.
- Searching ticket booking details.
- Generating reports based on ticket/seat type.
- Generating reports based on ticket price.
- Displaying reports using bar graphs.

The current version uses **Python lists for temporary data storage**. Data is available only while the program is running and is not permanently stored.

The project is designed as a console-based application and focuses on demonstrating Python programming concepts through a practical cinema ticket-booking system.

---

## 3. Target Users

The primary target users of the project are:

### Administrator

The administrator manages the cinema-related information and operations through the system.

The administrator can:

- Log in to the system.
- Add theater details.
- Update theater details.
- Remove theater details.
- Search theater information.
- Manage ticket bookings.
- Cancel bookings.
- Search booking details.
- View reports.

### Students / Learners

The project can also be used by students and learners as an example of a Python-based modular application demonstrating:

- Functions
- Modules
- Lists
- Conditional statements
- Loops
- User input
- Data manipulation
- Matplotlib-based reporting

---

## 4. High-Level Features

### 1. User Login
Provides administrator authentication using a User ID and Password.

### 2. Theater Management
Allows the administrator to add, update, remove, and search theater details.

### 3. Ticket Booking
Allows tickets to be booked by specifying the Booking ID, Theater ID, and ticket type.

### 4. Ticket Cancellation
Allows an existing ticket booking to be cancelled using its Booking ID.

### 5. Booking Search
Allows the user to search and display booking information using the Booking ID.

### 6. Theater Search
Allows theater information to be searched using the Theater ID.

### 7. Seat-Type Reporting
Generates a graphical report showing the number of bookings for each ticket type.

### 8. Ticket-Price Reporting
Generates a graphical report showing the total ticket amount for each ticket type.

### 9. Modular Python Structure
The project is divided into separate Python files such as `main.py`, `login.py`, `homepage.py`, `registration.py`, `booking.py`, `reports.py`, and `data.py` for better organization and maintenance.

### 10. Python-Only Data Handling
The project does not use SQL or MySQL. Theater and booking information is maintained using Python lists during program execution.
