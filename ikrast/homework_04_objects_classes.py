# This app shows the creation of classes for a customer, city and package so that final shipping calculation is made
# Classes for Customer, City & Package
class Customer:
    def __init__(self, first_name, last_name, phone_number, zip_code, city):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.zip_code = zip_code
        self.city = city



class City:
    # Shipping prices per city
    def __init__(self, city_price):
        self.city_price = city_price


class Package:

    def __init__(self, small, medium, large):
        self.small = small
        self.medium = medium
        self.large = large


def sender_info():
    sender_first_name = input("Welcome. Please enter your first name:  \n")
    sender_last_name = input("Please enter your last name:  \n")
    sender_phone_number = input("Please enter your phone number:  \n")
    sender_zip_code = input("Please enter your zip code:  \n")
    sender_city = input("Please enter your city:  \n")

    sender = Customer(sender_first_name, sender_last_name, sender_phone_number, sender_zip_code, sender_city)
    return sender


def recipient_entry(user_data):
    size = 1
    print("Thank you.")
    existing_user = user_data
    # get dictionary size
    user_count = len(existing_user.keys())
    # print all dict
    while user_count >= size:
        print(f"{size} - {existing_user[str(size)]}")
        size = size + 1
    recipient_selection = input("Please select recipient number: ")
    customer_string = existing_user[recipient_selection]

    return customer_string


# Separate function will work on splitting existing values by commas
def separate(recipient):
    input_string = recipient
    recipient_info = input_string.split(",")
    recipient_obj = Customer(recipient_info[0], recipient_info[1], recipient_info[2], recipient_info[3],
                             recipient_info[4])
    return recipient_obj


# Calculating prices based on selected city + package sizes
def price_calculation(sender, recipient):
    package_from = sender.city
    package_to = recipient.city
    package = Package(locations[package_to] + 5, locations[package_to] + 10, locations[package_to] + 15)
    package_selection = input("Please select the package option: \n"
                              "1 - small\n"
                              "2 - medium\n"
                              "3 - large\n")
    if package_selection == "1":
        final_price = package.small
    elif package_selection == "2":
        final_price = package.medium
    elif package_selection == "3":
        final_price = package.large
    return final_price


def decision(price):
    response = input("Please confirm this is the correct recipient information (yes/no):  \n")

    if response == "yes":
        print(f"Thank you. Your total is {price}. Shipment will arrive to recipient in 2 days.")
    elif response == "no":
        return response


def receipt(recipient_parsed_first_name,
            recipient_parsed_last_name,
            recipient_parsed_city,
            sender_first_name,
            sender_last_name,
            sender_city,
            price):
    print("------Confirmation------\n"
          "\n"
          "Recipient: \n"
          f"{recipient_parsed_first_name} {recipient_parsed_last_name}\n"
          f"City: {recipient_parsed_city}\n"
          "\n"
          "------------------------\n"
          "\n"
          f"Sender: \n"
          f"{sender_first_name} {sender_last_name}\n"
          f"City: {sender_city}"
          "\n")


if __name__ == '__main__':

    # initialize existing users
    existing_user = {"1": "Antonio,Stewart,0878777888,1818,Barcelona",
                     "2": "Jeremy,Benson,0999616161,2090,Berlin",
                     "3": "Ivan,Stoyanov,0897090807,1000,Sofia"}
    # initialize locations
    locations = {"Barcelona": 15, "Berlin": 20, "Sofia": 10}

    # initialize value for loop continuation
    response = "no"

    # main loop
    while response == "no":
        sender = sender_info()
        recipient = recipient_entry(existing_user)
        recipient_parsed = separate(recipient)
        price = price_calculation(sender, recipient_parsed)
        response = receipt(recipient_parsed.first_name,
                           recipient_parsed.last_name,
                           recipient_parsed.city,
                           sender.first_name,
                           sender.last_name,
                           sender.city,
                           price)
        response = decision(price)