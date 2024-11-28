import pandas

# Abstract Base Class
from abc import ABC, abstractmethod

df = pandas.read_csv("hotels.csv", dtype={"id": str})


class Hotel:
    watermark = "This Real State Company"  # Class Variable! 
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df["id"] == self.hotel_id, "name"].squeeze()

    def book(self):
        """Book a hotel by changing its availability to no"""
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        df.to_csv("hotels.csv", index=False)

    def available(self):
        """Check if the hotel is available"""
        availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
        if availability == "yes":
            return True
        else:
            return False

    # here we define a class method! ^^^^
    @classmethod
    def get_hotel_count(cls, data):
        return len(data)

# Abstract Class

class Ticket(ABC):  # here means: any class that inherit from abstract class, should then implement the abstract method "generate".

                    # So, if any class that should implement/have specific method, then we define that method in abstract class and let other classes to inherit
                    # from abstract class!
    @abstractmethod
    def generate(self):
        pass


class ReservationTicket(Ticket):
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object

    def generate(self):
        content = f"""
        Thank you for your reservation!
        Here are you booking data:
        Name: {self.the_customer_name}
        Hotel name: {self.hotel.name}
        """
        return content

    @property    #define it and access it anywhere as if it was a normal instance variable
    def the_customer_name(self):
        name = self.customer_name.strip()  #eg: "john smith "  -> "john smith"
        name = name.title()  #eg: "john smith" -> "John Smith"
        return name

    @staticmethod  # eg: convert Euro to Dollar. is used when we use some Utility
    def convert(amount):
        return  amount * 1.2

    # Magic method
    def __eq__(self):
        if self.hotel_id == self.hotel_id:
            return  True
        else:
            return False


hotel1 = Hotel(hotel_id="188")
hotel2 = Hotel(hotel_id="134")

print(hotel1.name)
print(hotel2.name)

print(hotel1.watermark)
print(Hotel.watermark)
#print(Hotel.name)  # Not working! Hotel has no variable neme but its method has!

# use and call class method. call using the Classname.classmethod ^^^^
print(Hotel.get_hotel_count(data=df))
# Or using an instance
print(hotel1.get_hotel_count(data=df))

# @property
ticket = ReservationTicket(customer_name="john smith", hotel_object=hotel1)
print(ticket.the_customer_name) # benefit is that we dont need to call it like a method: ticket.the_customer_name() but like a property. So, behaves like a variable

print(ticket.generate())

# @staticmethod
converted = ReservationTicket.convert(10)
print(converted)