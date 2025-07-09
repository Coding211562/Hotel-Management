# 🏨 Hotel Room Booking System (Python OOP Project)

This project is a simple **Hotel Room Booking System** built using Python and Object-Oriented Programming principles. It allows adding rooms, booking rooms for customers, checking out, and viewing room availability.

---

## ✅ Features

- Add multiple types of rooms (Single, Double, Suite, etc.)
- Book available rooms for customers
- Check out customers from rooms
- View list of currently available rooms
- Tracks room booking status and associated customer

---

## 🧱 Class Overview

### `Room`
Represents a room in the hotel.
- Attributes: `room_no`, `room_type`, `price`, `is_booked`, `customer`
- Methods:
  - `book_room(customer)`: Books the room for a customer
  - `checkout()`: Checks the customer out of the room

### `Customer`
Represents a hotel guest.
- Attributes: `name`, `phone`

### `Hotel`
Handles overall room management.
- Attributes: `rooms` (a list of all rooms)
- Methods:
  - `add_room(room)`: Adds a room to the hotel
  - `room_availability()`: Prints all available rooms
  - `book_room(room_no, customer)`: Books a room by room number
  - `check_out(room_no)`: Checks out a room by room number

---

## 🧪 Sample Usage

```python
room1 = Room(101, "Single", 1500)
room2 = Room(201, "Double", 2500)
room3 = Room(301, "Suite", 4000)

hotel = Hotel()
hotel.add_room(room1)
hotel.add_room(room2)
hotel.add_room(room3)

hotel.room_availability()

customer1 = Customer("Klaus", 9924563783)
customer2 = Customer("Elijah", 8765496754)

hotel.book_room(301, customer1)
hotel.book_room(101, customer2)

hotel.room_availability()

hotel.check_out(101)
hotel.check_out(301)

hotel.room_availability()
