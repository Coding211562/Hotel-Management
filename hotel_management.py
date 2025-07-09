class Room:
    def __init__(self , room_no , room_type , price):
        self.room_no = room_no
        self.room_type = room_type
        self.price = price
        self.is_booked = False
        self.customer = None

    def book_room(self , customer):
        if not self.is_booked:
            self.is_booked = True
            self.customer = customer
            print(f"{self.room_no} has successfully booked for {customer.name} ")
        else:
            print("Room is already Booked")

    def checkout(self):
        if self.is_booked:
            print(f"{self.customer.name} has checked out of room {self.room_no}")
            self.is_booked = False
            self.customer = None
        else:
            print(f"Room {self.room_no} is booked")

class Customer:
    def __init__(self , name , phone):
        self.name = name
        self.phone = phone

class Hotel:
    def __init__(self):
        self.rooms=[]    

    def add_room(self , room):
        self.rooms.append(room)

    def room_availability(self):
        print("Availble room:") 
        for room in self.rooms:
            if not room.is_booked:
                print(f"{room.room_no} , {room.room_type} - {room.price}")

    def book_room(self , room_no , customer):
        for room in self.rooms:
            if room.room_no == room_no :
                room.book_room(customer)
                return
        print("Room not found")    

    def check_out(self , room_no):
        for room in self.rooms:
            if room.room_no == room_no :
                room.checkout()
                return
        print("Room not found")  

room1 = Room(101 ,"single" , 1500)
room2 = Room(201 , "Double" , 2500)
room3 = Room(301 , "Suite" , 4000)

hotel = Hotel()

hotel.add_room(room1)
hotel.add_room(room2)
hotel.add_room(room3)

hotel.room_availability()

customer1 = Customer("Klaus" , 9924563783)
customer2 = Customer("Elijah" , 8765496754)

hotel.book_room(301 , customer1)

hotel.room_availability()

hotel.book_room(101 , customer2)
 
hotel.room_availability()

hotel.check_out(101)
hotel.check_out(301)

hotel.room_availability()