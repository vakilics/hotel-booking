import pandas

df = pandas.read_csv("hotels.csv", dtype={"id": str})
df_cards = pandas.read_csv("cards.csv", dtype=str).to_dict(orient="records")
print("---------------", df_cards)
#NOTE: as we get input as int, but
class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name =  df.loc[df["id"] == self.hotel_id, "name"].squeeze()
        self.city =  df.loc[df["id"] == self.hotel_id, "city"].squeeze()

    def book(self):
        """Book a hotel by changing its availability to no"""
        df.loc[df["id"] == self.hotel_id, "available"] = "no"
        df.to_csv("hotels.csv", index=False)

    def available(self):
        """Check if hotel is available"""
        availability = df.loc[df["id"] == self.hotel_id, "available"].squeeze()
        if availability == "yes":
            return True
        else:
            return  False
class ReservationTicket:
    def __init__(self,customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object

    def generate(self,):
        content = f"""
        Thanks you for your reservation!
        Here are you booking data:
        Name: {self.customer_name}
        Hotel: {self.hotel.name}
        City: {self.hotel.city}
        """
        return content

class CreditCard:
    def __init__(self, number):
        self.number = number

    def validate(self, expiration, holder, cvc):
        card_data = {"number":self.number, "expiration": expiration,
                     "cvc": cvc, "holder": holder}
        print("===========", card_data)
        if card_data in df_cards:
            return True
        else:
            return False

    #def pay(self):   find the existing balance and subtract ....


print(df)
hotel_ID = input("Enter  the Hotel ID: ")
hotel = Hotel(hotel_ID)
if hotel.available():   #Note: in real, we connect to a DB and get data from it (bank,,,)
    credit_card = CreditCard(number="1234567890123456")
    if credit_card.validate(expiration="12/26",cvc="123", holder="JOHN SMITH"):
        hotel.book()
        name = input("Enter your name: ")
        reservation_ticket = ReservationTicket(name, hotel)
        print("============================")
        print(reservation_ticket.generate())
    else:
        print("There was a problem with your payment!")

else:
    print("Hotel has no space!")