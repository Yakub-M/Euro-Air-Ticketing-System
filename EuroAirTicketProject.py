#  Made by Yakub Mehmedali <3

import tkinter as tk
import tkinter.messagebox
from tkcalendar import Calendar
import datetime
import random
import ast
from geopy.distance import great_circle as grc


class UserInterface:
    def __init__(self):
        self.window = tk.Tk()  # Creating the window
        self.window.geometry('610x800+0+0')  # Declaring size and position
        self.window.title("Euro Air Ticketing System")
        self.window.resizable(False, False)

        self.ticket_information = {
            "ticket_id": "",
            "airplane_id": "",
            "ticket_class": "",
            "ticket_price": "",
            "ticket_way": "",
            "departure_date": "",
            "return_date": "",
            "travel_distance": "",
            "travel_time": "",
            "customer_first_name": "",
            "customer_last_name": "",
            "departure_country": "",
            "departure_city": "",
            "departure_airport": "",
            "departure_airport_gate": "",
            "departure_airport_icao": "",
            "departure_airport_iata": "",
            "departure_airport_latitude": "",
            "departure_airport_longitude": "",
            "arrival_country": "",
            "arrival_city": "",
            "arrival_airport": "",
            "arrival_airport_gate": "",
            "arrival_airport_icao": "",
            "arrival_airport_iata": "",
            "arrival_airport_latitude": "",
            "arrival_airport_longitude": "",
        }

        def verify_departure_airport_code_and_fill():
            # Checking the validity of the entered airport code and filling the dictionary if it is
            with (open('airports_europe.csv', 'r', encoding='utf-8') as file_1):
                self.airports_europe = file_1.readlines()
                self.entered_departure_airport_code_get = self.entered_departure_airport_code.get().upper()
                for _ in self.airports_europe:
                    self.temp_icao = _.split(",")[3]
                    self.temp_iata = _.split(",")[4]
                    if (self.entered_departure_airport_code_get == self.temp_icao or
                            self.entered_departure_airport_code_get == self.temp_iata):
                        self.chosen_departure_country_name = _.split(",")[0]
                        self.chosen_departure_city_name = _.split(",")[1]
                        self.chosen_departure_airport_name = _.split(",")[2]
                        self.chosen_departure_airport_icao = _.split(",")[3]
                        self.chosen_departure_airport_iata = _.split(",")[4]
                        self.chosen_departure_airport_latitude = _.split(",")[5]
                        self.chosen_departure_airport_longitude = (_.split(",")[6]).rstrip()

                        self.ticket_information["departure_country"] = self.chosen_departure_country_name
                        self.ticket_information["departure_city"] = self.chosen_departure_city_name
                        self.ticket_information["departure_airport"] = self.chosen_departure_airport_name
                        self.ticket_information["departure_airport_gate"] = hex(
                            random.randrange(0, 2 ** 4))[2:] + hex(random.randrange(0, 2 ** 4))[2:]
                        self.ticket_information["departure_airport_icao"] = self.chosen_departure_airport_icao
                        self.ticket_information["departure_airport_iata"] = self.chosen_departure_airport_iata
                        self.ticket_information["departure_airport_latitude"] = self.chosen_departure_airport_latitude
                        self.ticket_information["departure_airport_longitude"] = self.chosen_departure_airport_longitude

                        self.confirm_message = tk.messagebox.showinfo(
                            title="Airport found", message=f"You have chosen {self.chosen_departure_airport_name} "
                                                           f"in {self.chosen_departure_country_name}, "
                                                           f"{self.chosen_departure_city_name} for departure")
                        return True
                self.confirm_message = tk.messagebox.showinfo(
                    title="Airport not found", message="Please enter a valid ICAO or IATA code of the "
                                                       "departure airport.")
                return False

        def verify_arrival_airport_code_and_fill():
            # Checking the validity of the entered airport code and filling the dictionary if it is
            with (open('airports_europe.csv', 'r', encoding='utf-8') as file_2):
                self.airports_europe = file_2.readlines()
                self.entered_arrival_airport_code_get = self.entered_arrival_airport_code.get().upper()
                for _ in self.airports_europe:
                    self.temp_icao = _.split(",")[3]
                    self.temp_iata = _.split(",")[4]
                    if (self.entered_arrival_airport_code_get == self.temp_icao or
                            self.entered_arrival_airport_code_get == self.temp_iata):
                        self.chosen_arrival_country_name = _.split(",")[0]
                        self.chosen_arrival_city_name = _.split(",")[1]
                        self.chosen_arrival_airport_name = _.split(",")[2]
                        self.chosen_arrival_airport_icao = _.split(",")[3]
                        self.chosen_arrival_airport_iata = _.split(",")[4]
                        self.chosen_arrival_airport_latitude = _.split(",")[5]
                        self.chosen_arrival_airport_longitude = (_.split(",")[6]).rstrip()

                        self.ticket_information["arrival_country"] = self.chosen_arrival_country_name
                        self.ticket_information["arrival_city"] = self.chosen_arrival_city_name
                        self.ticket_information["arrival_airport"] = self.chosen_arrival_airport_name
                        self.ticket_information["arrival_airport_gate"] = hex(
                            random.randrange(0, 2 ** 4))[2:] + hex(random.randrange(0, 2 ** 4))[2:]
                        self.ticket_information["arrival_airport_icao"] = self.chosen_arrival_airport_icao
                        self.ticket_information["arrival_airport_iata"] = self.chosen_arrival_airport_iata
                        self.ticket_information["arrival_airport_latitude"] = self.chosen_arrival_airport_latitude
                        self.ticket_information["arrival_airport_longitude"] = self.chosen_arrival_airport_longitude

                        self.confirm_message = tk.messagebox.showinfo(
                            title="Airport found", message=f"You have chosen {self.chosen_arrival_airport_name} "
                                                           f"in {self.chosen_arrival_country_name}, "
                                                           f"{self.chosen_arrival_city_name} for arrival")
                        return True
                self.confirm_message = tk.messagebox.showinfo(
                    title="Airport not found", message="Please enter a valid ICAO or IATA code of the "
                                                       "airport of arrival.")
                return False

        def verify_arrival_airport_exists_and_fill():
            with open('airports_europe.csv', 'r', encoding='utf-8') as file_3:
                self.airports_europe = file_3.readlines()
                self.name_arrival_country = self.chosen_arrival_country.get()
                self.name_arrival_city = self.chosen_arrival_city.get()
                self.name_arrival_airport = self.chosen_arrival_airport.get()
                for _ in self.airports_europe:
                    self.temp_country = _.split(",")[0]
                    self.temp_city = _.split(",")[1]
                    self.temp_airport = _.split(",")[2]
                    if self.name_arrival_airport == self.temp_airport:
                        if self.name_arrival_country != self.temp_country or self.name_arrival_city != self.temp_city:
                            self.confirm_message = tk.messagebox.showinfo(
                                title="Airport not found", message="Please select valid arrival airport details.")
                            return False

            with open('airports_europe.csv', 'r', encoding='utf-8') as file_4:
                self.airports_europe = file_4.readlines()
                for _ in self.airports_europe:
                    self.temp_country = _.split(",")[0]
                    self.temp_city = _.split(",")[1]
                    self.temp_airport = _.split(",")[2]
                    if self.name_arrival_airport == self.temp_airport:
                        if self.name_arrival_country == self.temp_country and self.name_arrival_city == self.temp_city:
                            self.chosen_arrival_country_name = _.split(",")[0]
                            self.chosen_arrival_city_name = _.split(",")[1]
                            self.chosen_arrival_airport_name = _.split(",")[2]
                            self.chosen_arrival_airport_icao = _.split(",")[3]
                            self.chosen_arrival_airport_iata = _.split(",")[4]
                            self.chosen_arrival_airport_latitude = _.split(",")[5]
                            self.chosen_arrival_airport_longitude = (_.split(",")[6]).rstrip()

                            self.ticket_information["arrival_country"] = self.chosen_arrival_country_name
                            self.ticket_information["arrival_city"] = self.chosen_arrival_city_name
                            self.ticket_information["arrival_airport"] = self.chosen_arrival_airport_name
                            self.ticket_information["arrival_airport_gate"] = hex(
                                random.randrange(0, 2 ** 4))[2:] + hex(random.randrange(0, 2 ** 4))[2:]
                            self.ticket_information["arrival_airport_icao"] = self.chosen_arrival_airport_icao
                            self.ticket_information["arrival_airport_iata"] = self.chosen_arrival_airport_iata
                            self.ticket_information["arrival_airport_latitude"] = self.chosen_arrival_airport_latitude
                            self.ticket_information["arrival_airport_longitude"] = self.chosen_arrival_airport_longitude

                            self.confirm_message = tk.messagebox.showinfo(
                                title="Airport found", message=f"You have chosen {self.chosen_arrival_airport_name} "
                                                               f"in {self.chosen_arrival_country_name}, "
                                                               f"{self.chosen_arrival_city_name} for arrival")
                            return True

        def verify_departure_airport_exists_and_fill():
            with (open('airports_europe.csv', 'r', encoding='utf-8') as file_5):
                self.airports_europe = file_5.readlines()
                self.name_departure_country = self.chosen_departure_country.get()
                self.name_departure_city = self.chosen_departure_city.get()
                self.name_departure_airport = self.chosen_departure_airport.get()
                for _ in self.airports_europe:
                    self.temp_country = _.split(",")[0]
                    self.temp_city = _.split(",")[1]
                    self.temp_airport = _.split(",")[2]
                    if self.name_departure_airport == self.temp_airport:
                        if (self.name_departure_country != self.temp_country or
                                self.name_departure_city != self.temp_city):
                            self.confirm_message = tk.messagebox.showinfo(
                                title="Airport not found", message="Please select valid departure airport details.")
                            return False

            with open('airports_europe.csv', 'r', encoding='utf-8') as file_6:
                self.airports_europe = file_6.readlines()
                for _ in self.airports_europe:
                    self.temp_country = _.split(",")[0]
                    self.temp_city = _.split(",")[1]
                    self.temp_airport = _.split(",")[2]
                    if self.name_departure_airport == self.temp_airport:
                        if (self.name_departure_country == self.temp_country and
                                self.name_departure_city == self.temp_city):
                            self.chosen_departure_country_name = _.split(",")[0]
                            self.chosen_departure_city_name = _.split(",")[1]
                            self.chosen_departure_airport_name = _.split(",")[2]
                            self.chosen_departure_airport_icao = _.split(",")[3]
                            self.chosen_departure_airport_iata = _.split(",")[4]
                            self.chosen_departure_airport_latitude = _.split(",")[5]
                            self.chosen_departure_airport_longitude = (_.split(",")[6]).rstrip()

                            self.ticket_information["departure_country"] = self.chosen_departure_country_name
                            self.ticket_information["departure_city"] = self.chosen_departure_city_name
                            self.ticket_information["departure_airport"] = self.chosen_departure_airport_name
                            self.ticket_information["departure_airport_gate"] = hex(
                                random.randrange(0, 2 ** 4))[2:] + hex(random.randrange(0, 2 ** 4))[2:]
                            self.ticket_information["departure_airport_icao"] = self.chosen_departure_airport_icao
                            self.ticket_information["departure_airport_iata"] = self.chosen_departure_airport_iata
                            self.ticket_information[
                                "departure_airport_latitude"] = self.chosen_departure_airport_latitude
                            self.ticket_information[
                                "departure_airport_longitude"] = self.chosen_departure_airport_longitude

                            self.confirm_message = tk.messagebox.showinfo(
                                title="Airport found", message=f"You have chosen {self.name_departure_airport} "
                                                               f"in {self.name_departure_country}, "
                                                               f"{self.name_departure_city} for departure")
                            return True

        def finalize_ticket():
            self.ticket_information["ticket_id"] = random.randrange(10000, 100000)
            self.ticket_information["airplane_id"] = (f"{hex(random.randrange(0, 2 ** 5))[2:]}" +
                                                      f"{random.randrange(100, 1000)}")
            self.ticket_information["ticket_class"] = self.ticket_class_var.get()
            self.ticket_information["ticket_price"] = str(calculate_ticket_price()) + " lev"
            self.ticket_information["ticket_way"] = "one_way" if self.radio_button_var.get() == 0 else "round_trip"
            self.ticket_information["customer_first_name"] = self.entered_customer_first_name.get()
            self.ticket_information["customer_last_name"] = self.entered_customer_last_name.get()
            self.ticket_information["travel_distance"] = str(int(calculate_travel_distance())) + " km"
            self.ticket_information["travel_time"] = calculate_travel_time()
            self.ticket_information["departure_date"] = str(self.departure_date_calendar.selection_get())

            self.is_round_trip = False if self.radio_button_var.get() == 0 else True
            if self.is_round_trip:
                self.ticket_information["return_date"] = str(self.return_date_calendar.selection_get())

            with open('customer_ticket.csv', 'w', encoding='utf-8') as file_7:
                print(self.ticket_information, file=file_7)

            print(self.ticket_information)
            self.confirm_message = tk.messagebox.showinfo(
                title="Successful processing", message="Press OK to print your ticket.")
            if self.confirm_message == "ok":
                self.window.destroy()
                DisplayTicket()

        def calculate_travel_distance():
            self.departure_airport_location = (
                self.ticket_information["departure_airport_latitude"],
                self.ticket_information["departure_airport_longitude"])
            self.arrival_airport_location = (
                self.ticket_information["arrival_airport_latitude"],
                self.ticket_information["arrival_airport_longitude"])
            return grc(self.departure_airport_location, self.arrival_airport_location).km

        def calculate_travel_time():
            self.travel_time_minutes = calculate_travel_distance() / 10  # Arbitrary
            self.hours, self.minutes = divmod(self.travel_time_minutes / 60, 1)
            self.minutes = 60 * self.minutes
            if self.minutes == 60:
                self.minutes = 0
            self.minutes = int(self.minutes)
            if len(str(self.minutes)) == 1:
                self.minutes = str(self.minutes)
                self.minutes = "0" + self.minutes
            return f"{int(self.hours)}" + ":" + f"{self.minutes}"

        def calculate_ticket_price():
            # Arbitrary
            # 4km = 1lev
            # Economy class = 1x
            # Premium economy class = 2x
            # Business class = 5x
            # First class = 10x
            # Round-Trip = +50%

            self.travel_distance = calculate_travel_distance()
            self.base_price = int(self.travel_distance / 4)
            self.final_price = self.base_price
            self.ticket_classes = self.ticket_class_var.get()
            self.is_round_trip = False if self.radio_button_var.get() == 0 else True
            match self.ticket_classes:
                case 'Economy':
                    if self.is_round_trip:
                        self.final_price = self.base_price * 1.5
                        return int(self.final_price)
                    else:
                        return int(self.final_price)
                case 'Premium Economy':
                    if self.is_round_trip:
                        self.final_price = self.base_price * 2 * 1.5
                    else:
                        self.final_price = self.base_price * 2
                    return int(self.final_price)
                case 'Business':
                    if self.is_round_trip:
                        self.final_price = self.base_price * 5 * 1.5
                    else:
                        self.final_price = self.base_price * 5
                    return int(self.final_price)
                case 'First':
                    if self.is_round_trip:
                        self.final_price = self.base_price * 10 * 1.5
                    else:
                        self.final_price = self.base_price * 10
                    return int(self.final_price)

        def return_calendar_toggler():
            if self.radio_button_var.get() == 1:
                self.return_date_calendar.grid()  # Show the calendar
                self.return_date_calendar_label.grid()  # Show the calendar label
            else:
                self.return_date_calendar.grid_remove()  # Hide the calendar
                self.return_date_calendar_label.grid_remove()  # Hide the calendar label

        def verify_ticket_button_click():
            # Checking the validity of the ticket information entered and if so,
            # saving the ticket and calling DisplayTicket() which reads the finished ticket
            if (self.entered_customer_first_name.get().isalpha() is False or
                    self.entered_customer_last_name.get().isalpha() is False):
                # Checks the validity of the entered names
                self.confirm_message = tk.messagebox.showinfo(
                    title="Invalid ticket", message="Please correct the names entered.")
                return

            if len(self.entered_customer_first_name.get()) < 3 or len(self.entered_customer_last_name.get()) < 3:
                # Checks the validity of the entered names
                self.confirm_message = tk.messagebox.showinfo(
                    title="Invalid ticket", message="Please correct the names entered.")
                return

            if self.ticket_class_var.get() == "":
                self.confirm_message = tk.messagebox.showinfo(
                    title="Invalid ticket", message="Please correct the ticket class.")
                return

            if self.entered_departure_airport_code.get() == "" or self.entered_arrival_airport_code.get() == "":
                if (self.chosen_departure_country.get() == "" or self.chosen_departure_city.get() == "" or
                        self.chosen_departure_airport.get() == "" or self.chosen_arrival_country.get() == "" or
                        self.chosen_arrival_city.get() == "" or self.chosen_arrival_airport.get() == ""):
                    self.confirm_message = tk.messagebox.showinfo(
                        title="Invalid ticket", message="Please correct the selected countries or cities or airports.")
                    return

            if self.entered_departure_airport_code.get() != "" or self.entered_arrival_airport_code.get() != "":
                if self.chosen_departure_airport.get() != "" or self.chosen_arrival_airport.get() != "":
                    self.confirm_message = tk.messagebox.showinfo(
                        title="Invalid ticket", message="Please use only one method to select a destination.")
                    return

            if self.entered_departure_airport_code.get() != "" or self.entered_arrival_airport_code.get() != "":
                self.verify_departure_airport_exists = verify_departure_airport_exists_and_fill()
                if self.verify_departure_airport_exists is False:
                    self.confirm_message = tk.messagebox.showinfo(
                        title="Invalid ticket", message="The selected departure airport does not exist "
                                                        "in the country or city.")
                    return

                self.verify_arrival_airport_exists = verify_arrival_airport_exists_and_fill()
                if self.verify_arrival_airport_exists is False:
                    self.confirm_message = tk.messagebox.showinfo(
                        title="Invalid ticket", message="The selected arrival airport does not exist "
                                                        "in the country or city.")
                    return

            if self.entered_departure_airport_code.get() == "" or self.entered_arrival_airport_code.get() == "":
                if self.chosen_departure_airport.get() == self.chosen_arrival_airport.get():
                    self.confirm_message = tk.messagebox.showinfo(
                        title="Invalid ticket", message="You cannot depart and arrive at the same airport.1")
                    return

            if self.chosen_departure_airport.get() == "" or self.chosen_arrival_airport.get() == "":
                if self.entered_departure_airport_code.get() == self.entered_arrival_airport_code.get():
                    self.confirm_message = tk.messagebox.showinfo(
                        title="Invalid ticket", message="You cannot depart and arrive at the same airport.2")
                    return

            if self.entered_departure_airport_code.get() == "" and self.entered_arrival_airport_code.get() == "":
                if (verify_departure_airport_exists_and_fill() is True and
                        verify_arrival_airport_exists_and_fill() is True):
                    finalize_ticket()

            if self.entered_departure_airport_code.get() != "" and self.entered_arrival_airport_code.get() != "":
                if verify_departure_airport_code_and_fill() is True and verify_arrival_airport_code_and_fill() is True:
                    finalize_ticket()

        # This list will be used in tk.OptionMenu to select a country
        self.airports_europe_country_list = []
        with open('airports_europe.csv', 'r', encoding='utf-8') as file_12:
            self.airports_europe = file_12.readlines()
            for _ in self.airports_europe:
                # Create a temporary variable to store first column values for each row in self.airports_europe
                self.country_temp = _.split(",")[0]
                # Adding temporary rows to the list
                self.airports_europe_country_list.append(self.country_temp)

        # Based on the selected country, cities from that country are filtered
        self.chosen_departure_country = tk.StringVar()
        self.filtered_departure_cities = []
        # Based on the selected city, the airports from that city are filtered
        self.chosen_departure_city = tk.StringVar()
        self.filtered_departure_airports = []

        self.chosen_departure_airport = tk.StringVar()

        self.filtered_departure_city_list = []

        def update_option_menu_departure_city(*_):
            with open('airports_europe.csv', 'r', encoding='utf-8') as file_8:
                self.airports_europe = file_8.readlines()
                self.name_departure_country = self.chosen_departure_country.get()
                self.filtered_departure_city_list.clear()
                # self.chosen_departure_city.set("") doesn't work???
                for _ in self.airports_europe:
                    # self.country_temp contains the current country and self.city_temp contains the current city.
                    # If the current country is the one selected by tk.OptionMenu,
                    # it is put in self.filtered_departure_city_list
                    self.country_temp = _.split(",")[0]
                    if self.country_temp == self.name_departure_country:
                        self.city_temp = _.split(",")[1]
                        self.filtered_departure_city_list.append(self.city_temp)
                self.departure_city_var_placeholder.grid_remove()
                tk.OptionMenu(
                    self.window, self.chosen_departure_city,
                    *list(set(self.filtered_departure_city_list))).grid(
                    column=0, row=10, padx=(35, 0), sticky='w')
                # Removes duplicates

        self.filtered_departure_airport_list = []

        def update_option_menu_departure_airport(*_):
            with open('airports_europe.csv', 'r', encoding='utf-8') as file_9:
                self.airports_europe = file_9.readlines()
                self.name_departure_city = self.chosen_departure_city.get()
                self.filtered_departure_airport_list.clear()
                self.chosen_departure_airport.set("")
                for _ in self.airports_europe:
                    # self.city_temp contains the current city and self.airport_temp contains the current airport
                    # If the current city is the one selected by tk.OptionMenu,
                    # it is put in self.filtered_departure_airport_list
                    self.city_temp = _.split(",")[1]
                    if self.city_temp == self.name_departure_city:
                        self.airport_temp = _.split(",")[2]
                        self.filtered_departure_airport_list.append(self.airport_temp)
                self.departure_airport_var_placeholder.grid_remove()
                tk.OptionMenu(
                    self.window, self.chosen_departure_airport,
                    *list(set(self.filtered_departure_airport_list))).grid(
                    column=0, row=12, padx=(35, 0), sticky='w')
                # Removes duplicates

        # Based on the selected country, cities from that country are filtered
        self.chosen_arrival_country = tk.StringVar()
        self.filtered_arrival_cities = []
        # Based on the selected city, the airports from that city are filtered
        self.chosen_arrival_city = tk.StringVar()
        self.filtered_arrival_airports = []

        self.chosen_arrival_airport = tk.StringVar()

        self.filtered_arrival_city_list = []

        def update_option_menu_arrival_city(*_):
            with open('airports_europe.csv', 'r', encoding='utf-8') as file_10:
                self.airports_europe = file_10.readlines()
                self.name_arrival_country = self.chosen_arrival_country.get()
                self.filtered_arrival_city_list.clear()
                for _ in self.airports_europe:
                    # self.country_temp contains the current country and self.city_temp contains the current city
                    # If the current country is the one selected by tk.OptionMenu,
                    # it is put in self.filtered_arrival_city_list
                    self.country_temp = _.split(",")[0]
                    if self.country_temp == self.name_arrival_country:
                        self.city_temp = _.split(",")[1]
                        self.filtered_arrival_city_list.append(self.city_temp)
                self.arrival_city_var_placeholder.grid_remove()
                tk.OptionMenu(
                    self.window, self.chosen_arrival_city, *list(set(self.filtered_arrival_city_list))).grid(
                    column=1, row=10, padx=(35, 0), sticky='w')
                # Removes duplicates

        self.filtered_arrival_airport_list = []

        def update_option_menu_arrival_airport(*_):
            with open('airports_europe.csv', 'r', encoding='utf-8') as file_11:
                self.airports_europe = file_11.readlines()
                self.name_arrival_city = self.chosen_arrival_city.get()
                self.filtered_arrival_airport_list.clear()
                self.chosen_arrival_airport.set("")
                for _ in self.airports_europe:
                    # self.city_temp contains the current city and self.airport_temp contains the current airport
                    # If the current city is the one selected by tk.OptionMenu,
                    # it is put in self.filtered_arrival_airport_list
                    self.city_temp = _.split(",")[1]
                    if self.city_temp == self.name_arrival_city:
                        self.airport_temp = _.split(",")[2]
                        self.filtered_arrival_airport_list.append(self.airport_temp)
                self.arrival_airport_var_placeholder.grid_remove()
                tk.OptionMenu(
                    self.window, self.chosen_arrival_airport,
                    *list(set(self.filtered_arrival_airport_list))).grid(
                    column=1, row=12, padx=(35, 0), sticky='w')
                # Removes duplicates

        tk.Label(
            self.window, text="Welcome to Euro Air Ticketing System", font=('Helvetica', 20)).grid(
            column=0, row=0, columnspan=2, padx=(35, 0), sticky='w')

        tk.Label(
            self.window, text="Enter first and last name:", font='Helvetica 12').grid(
            column=0, row=1, padx=(35, 0), pady=(10, 0), sticky='w')

        self.entered_customer_first_name = tk.StringVar()

        tk.Entry(
            self.window, font='Helvetica 11', textvariable=self.entered_customer_first_name).grid(
            column=0, row=2, padx=(35, 0), sticky='w')

        self.entered_customer_last_name = tk.StringVar()

        tk.Entry(
            self.window, font='Helvetica 11', textvariable=self.entered_customer_last_name).grid(
            column=0, row=3, padx=(35, 0), sticky='w')

        tk.Label(
            self.window, text="Select the direction of the ticket:", font='Helvetica 12').grid(
            column=1, row=1, padx=(35, 0), pady=(10, 0), sticky='w')

        self.radio_button_var = tk.IntVar()  # Control variable

        tk.Radiobutton(
            self.window, text="One-Way", font='Helvetica 12', variable=self.radio_button_var, value=0,
            command=return_calendar_toggler).grid(column=1, row=2, padx=(35, 0), sticky='w')

        tk.Radiobutton(
            self.window, text="Round-Trip", font='Helvetica 12', variable=self.radio_button_var, value=1,
            command=return_calendar_toggler).grid(column=1, row=3, padx=(35, 0), sticky='w')

        tk.Label(
            self.window, text="Select the ticket class:", font='Helvetica 12').grid(
            column=0, row=4, padx=(35, 0), pady=(10, 0), sticky='w')

        self.ticket_class_var = tk.StringVar(self.window)

        self.ticket_classes = ['Economy', 'Premium Economy', 'Business', 'First']

        tk.OptionMenu(
            self.window, self.ticket_class_var, *self.ticket_classes).grid(
            column=0, row=5, padx=(35, 0), sticky='w')

        tk.Label(
            self.window, text="Departing from", font='Helvetica 12 bold').grid(
            column=0, row=6, padx=(35, 0), pady=(10, 0), sticky='w')

        self.departure_country_var = tk.StringVar(self.window)

        tk.Label(
            self.window, text="Country:", font='Helvetica 12').grid(
            column=0, row=7, padx=(35, 0), pady=(5, 0), sticky='w')
        self.chosen_departure_country.trace('w', update_option_menu_departure_city)

        # self.departure_country OptionMenu is here
        tk.OptionMenu(
            self.window, self.chosen_departure_country, *self.airports_europe_country_list).grid(
            column=0, row=8, padx=(35, 0), sticky='w')

        self.departure_city_var = tk.StringVar(self.window)

        tk.Label(
            self.window, text="City:", font='Helvetica 12').grid(
            column=0, row=9, padx=(35, 0), pady=(5, 0), sticky='w')

        self.departure_city_var_placeholder = tk.StringVar(self.window)

        self.departure_city_var_placeholder = tk.OptionMenu(self.window, self.departure_city_var_placeholder, "")
        self.departure_city_var_placeholder.grid(column=0, row=10, padx=(35, 0), sticky='w')

        self.departure_airport_var = tk.StringVar(self.window)

        tk.Label(
            self.window, text="Airport:", font='Helvetica 12').grid(
            column=0, row=11, padx=(35, 0), pady=(5, 0), sticky='w')

        self.departure_airport_var_placeholder = tk.StringVar(self.window)

        self.departure_airport_var_placeholder = tk.OptionMenu(
            self.window, self.departure_airport_var_placeholder, "")
        self.departure_airport_var_placeholder.grid(column=0, row=12, padx=(35, 0), sticky='w')

        self.chosen_departure_city.trace('w', update_option_menu_departure_airport)

        # self.departure_airport OptionMenu is here
        tk.Label(
            self.window, text="Or search by airport code:", font='Helvetica 12').grid(
            column=0, row=13, padx=(35, 0), pady=(5, 0), sticky='w')

        self.entered_departure_airport_code = tk.StringVar()

        tk.Entry(
            self.window, font='Helvetica 12', textvariable=self.entered_departure_airport_code).grid(
            column=0, row=14, padx=(35, 0), sticky='w')

        tk.Button(
            self.window, text="Check code", font='Helvetica 12', command=verify_departure_airport_code_and_fill).grid(
            column=0, row=15, padx=(35, 0), pady=(5, 0), sticky='w')

        tk.Label(
            self.window, text="Choose departure date:", font='Helvetica 12').grid(
            column=0, row=16, padx=(35, 0), pady=(10, 0), sticky='w')

        self.departure_date_calendar = Calendar(self.window, mindate=datetime.date.today(), font='Helvetica 10')

        self.departure_date_calendar.grid(column=0, row=17, padx=(35, 0), pady=(5, 0), sticky='w')

        tk.Label(self.window, text="Arriving to", font='Helvetica 12 bold').grid(
            column=1, row=6, padx=(35, 0), pady=(10, 0), sticky='w')

        self.arrival_country_var = tk.StringVar(self.window)

        tk.Label(self.window, text="Country:", font='Helvetica 12').grid(
            column=1, row=7, padx=(35, 0), pady=(5, 0), sticky='w')

        self.chosen_arrival_country.trace('w', update_option_menu_arrival_city)

        tk.OptionMenu(
            self.window, self.chosen_arrival_country, *self.airports_europe_country_list).grid(
            column=1, row=8, padx=(35, 0), sticky='w')

        self.arrival_city_var = tk.StringVar(self.window)

        tk.Label(self.window, text="City:", font='Helvetica 12').grid(
            column=1, row=9, padx=(35, 0), pady=(5, 0), sticky='w')

        self.arrival_city_var_placeholder = tk.StringVar(self.window)

        self.arrival_city_var_placeholder = tk.OptionMenu(self.window, self.arrival_city_var_placeholder, "")
        self.arrival_city_var_placeholder.grid(column=1, row=10, padx=(35, 0), sticky='w')

        # self.arrival_city OptionMenu is here
        self.arrival_airport_var = tk.StringVar(self.window)

        tk.Label(self.window, text="Airport:", font='Helvetica 12').grid(
            column=1, row=11, padx=(35, 0), pady=(5, 0), sticky='w')

        self.arrival_airport_var_placeholder = tk.StringVar(self.window)

        self.arrival_airport_var_placeholder = tk.OptionMenu(
            self.window, self.arrival_airport_var_placeholder, "")
        self.arrival_airport_var_placeholder.grid(column=1, row=12, padx=(35, 0), sticky='w')

        self.chosen_arrival_city.trace('w', update_option_menu_arrival_airport)

        # self.arrival_airport OptionMenu is here
        tk.Label(self.window, text="Or search by airport code:", font='Helvetica 12').grid(
            column=1, row=13, padx=(35, 0), pady=(5, 0), sticky='w')

        self.entered_arrival_airport_code = tk.StringVar()

        tk.Entry(
            self.window, font='Helvetica 12', textvariable=self.entered_arrival_airport_code).grid(
            column=1, row=14, padx=(35, 0), sticky='w')

        tk.Button(
            self.window, text="Check code", font='Helvetica 12', command=verify_arrival_airport_code_and_fill).grid(
            column=1, row=15, padx=(35, 0), pady=(5, 0), sticky='w')

        self.return_date_calendar_label = (tk.Label(self.window, text="Choose date for return:", font='Helvetica 12'))
        self.return_date_calendar_label.grid(column=1, row=16, padx=(35, 0), pady=(10, 0), sticky='w')
        self.return_date_calendar_label.grid_remove()

        self.return_date_calendar = Calendar(self.window, mindate=datetime.date.today(), font='Helvetica 10')
        self.return_date_calendar.grid(column=1, row=17, padx=(35, 0), pady=(5, 0), sticky='w')
        self.return_date_calendar.grid_remove()

        tk.Button(
            self.window, text="Process ticket", font='Helvetica 12', command=verify_ticket_button_click).grid(
            column=0, row=25, columnspan=2, padx=(35, 0), pady=(20, 0))

        self.window.mainloop()


class DisplayTicket:
    def __init__(self):
        self.window = tk.Tk()  # Creating the window
        self.window.geometry('630x760+0+0')  # Declaring size and position
        self.window.title("Euro Air Ticketing System")
        self.window.resizable(False, False)

        self.print_ticket_information = {
            "ticket_id": "",
            "airplane_id": "",
            "ticket_class": "",
            "ticket_price": "",
            "ticket_way": "",
            "departure_date": "",
            "return_date": "",
            "travel_distance": "",
            "travel_time": "",
            "customer_first_name": "",
            "customer_last_name": "",
            "departure_country": "",
            "departure_city": "",
            "departure_airport": "",
            "departure_airport_gate": "",
            "departure_airport_icao": "",
            "departure_airport_iata": "",
            "arrival_country": "",
            "arrival_city": "",
            "arrival_airport": "",
            "arrival_airport_gate": "",
            "arrival_airport_icao": "",
            "arrival_airport_iata": ""
        }

        with open('customer_ticket.csv', 'r', encoding='utf-8') as file:
            self.print_ticket_information = ast.literal_eval(file.read())

        tk.Label(self.window, text="Ticket ID:", font='Helvetica 12').grid(
            column=0, row=0, pady=(5, 0), sticky='w')

        tk.Label(self.window, text=self.print_ticket_information["ticket_id"], font='Helvetica 12').grid(
            column=1, row=0, pady=(5, 0), sticky='w')

        tk.Label(self.window, text="Ticket class:", font='Helvetica 12').grid(
            column=0, row=1, pady=(5, 0), sticky='w')

        tk.Label(self.window, text=self.print_ticket_information["ticket_class"], font='Helvetica 12').grid(
            column=1, row=1, pady=(5, 0), sticky='w')

        tk.Label(self.window, text="Ticket way:", font='Helvetica 12').grid(
            column=0, row=2, pady=(5, 0), sticky='w')

        if self.print_ticket_information["ticket_way"] == "one_way":
            tk.Label(self.window, text="One-Way", font='Helvetica 12').grid(
                column=1, row=2, pady=(5, 0), sticky='w')
        else:
            tk.Label(self.window, text="Round-Trip", font='Helvetica 12').grid(
                column=1, row=2, pady=(5, 0), sticky='w')

        tk.Label(self.window, text="Ticket price:", font='Helvetica 12').grid(
            column=0, row=3, pady=(5, 0), sticky='w')

        tk.Label(self.window, text=self.print_ticket_information["ticket_price"], font='Helvetica 12').grid(
            column=1, row=3, pady=(5, 0), sticky='w')

        tk.Label(self.window, text="Client name:", font='Helvetica 12').grid(
            column=0, row=4, pady=(5, 0), sticky='w')

        tk.Label(self.window, text=self.print_ticket_information["customer_first_name"], font='Helvetica 12').grid(
            column=1, row=4, pady=(5, 0), sticky='w')

        tk.Label(self.window, text="Client surname:", font='Helvetica 12').grid(
            column=0, row=5, pady=(5, 0), sticky='w')

        tk.Label(self.window, text=self.print_ticket_information["customer_last_name"], font='Helvetica 12').grid(
            column=1, row=5, pady=(5, 0), sticky='w')

        tk.Label(self.window, text="Airplane ID:", font='Helvetica 12').grid(
            column=0, row=6, pady=(5, 0), sticky='w')

        tk.Label(self.window, text=self.print_ticket_information["airplane_id"], font='Helvetica 12').grid(
            column=1, row=6, pady=(5, 0), sticky='w')

        tk.Label(self.window, text="Departing from", font='Helvetica 12 bold').grid(
            column=0, row=7, pady=(5, 0), sticky='w')

        tk.Label(self.window, text="Country:", font='Helvetica 12').grid(
            column=0, row=8, pady=(5, 0), sticky='w')

        tk.Label(self.window, text=self.print_ticket_information["departure_country"], font='Helvetica 12').grid(
            column=1, row=8, pady=(5, 0), sticky='w')

        tk.Label(self.window, text="City:", font='Helvetica 12').grid(
            column=0, row=9, pady=(5, 0), sticky='w')

        tk.Label(self.window, text=self.print_ticket_information["departure_city"], font='Helvetica 12').grid(
            column=1, row=9, pady=(5, 0), sticky='w')

        tk.Label(self.window, text="Airport:", font='Helvetica 12').grid(
            column=0, row=10, pady=(5, 0), sticky='w')

        tk.Label(self.window, text=self.print_ticket_information["departure_airport"], font='Helvetica 12').grid(
            column=1, row=10, pady=(5, 0), sticky='w')

        tk.Label(self.window, text="Airport ICAO code:", font='Helvetica 12').grid(
            column=0, row=11, pady=(5, 0), sticky='w')

        tk.Label(self.window, text=self.print_ticket_information["departure_airport_icao"], font='Helvetica 12').grid(
            column=1, row=11, pady=(5, 0), sticky='w')

        tk.Label(self.window, text="Airport IATA code:", font='Helvetica 12').grid(
            column=0, row=12, pady=(5, 0), sticky='w')

        tk.Label(self.window, text=self.print_ticket_information["departure_airport_iata"], font='Helvetica 12').grid(
            column=1, row=12, pady=(5, 0), sticky='w')

        tk.Label(self.window, text="Airport gate:", font='Helvetica 12').grid(
            column=0, row=13, pady=(5, 0), sticky='w')

        tk.Label(self.window, text=self.print_ticket_information["departure_airport_gate"], font='Helvetica 12').grid(
            column=1, row=13, pady=(5, 0), sticky='w')

        tk.Label(self.window, text="Date departure:", font='Helvetica 12').grid(
            column=0, row=14, pady=(5, 0), sticky='w')

        tk.Label(self.window, text=self.print_ticket_information["departure_date"], font='Helvetica 12').grid(
            column=1, row=14, pady=(5, 0), sticky='w')

        tk.Label(self.window, text="Arriving to", font='Helvetica 12 bold').grid(
            column=0, row=15, pady=(5, 0), sticky='w')

        tk.Label(self.window, text="Country:", font='Helvetica 12').grid(
            column=0, row=16, pady=(5, 0), sticky='w')

        tk.Label(self.window, text=self.print_ticket_information["arrival_country"], font='Helvetica 12').grid(
            column=1, row=16, pady=(5, 0), sticky='w')

        tk.Label(self.window, text="City:", font='Helvetica 12').grid(
            column=0, row=17, pady=(5, 0), sticky='w')

        tk.Label(self.window, text=self.print_ticket_information["arrival_city"], font='Helvetica 12').grid(
            column=1, row=17, pady=(5, 0), sticky='w')

        tk.Label(self.window, text="Airport:", font='Helvetica 12').grid(
            column=0, row=18, pady=(5, 0), sticky='w')

        tk.Label(self.window, text=self.print_ticket_information["arrival_airport"], font='Helvetica 12').grid(
            column=1, row=18, pady=(5, 0), sticky='w')

        tk.Label(self.window, text="Airport ICAO code:", font='Helvetica 12').grid(
            column=0, row=19, pady=(5, 0), sticky='w')

        tk.Label(self.window, text=self.print_ticket_information["arrival_airport_icao"], font='Helvetica 12').grid(
            column=1, row=19, pady=(5, 0), sticky='w')

        tk.Label(self.window, text="Airport IATA code:", font='Helvetica 12').grid(
            column=0, row=20, pady=(5, 0), sticky='w')

        tk.Label(self.window, text=self.print_ticket_information["arrival_airport_iata"], font='Helvetica 12').grid(
            column=1, row=20, pady=(5, 0), sticky='w')

        tk.Label(self.window, text="Airport gate:", font='Helvetica 12').grid(
            column=0, row=21, pady=(5, 0), sticky='w')

        tk.Label(self.window, text=self.print_ticket_information["arrival_airport_gate"], font='Helvetica 12').grid(
            column=1, row=21, pady=(5, 0), sticky='w')

        if self.print_ticket_information["ticket_way"] == "round_trip":
            tk.Label(self.window, text="Return date:", font='Helvetica 12').grid(
                column=0, row=22, pady=(5, 0), sticky='w')

            tk.Label(self.window, text=self.print_ticket_information["return_date"], font='Helvetica 12').grid(
                column=1, row=22, pady=(5, 0), sticky='w')

        tk.Label(self.window, text="-------------------------", font='Helvetica 12 bold').grid(
            column=0, row=23, sticky='w', )

        tk.Label(self.window, text="Travel distance:", font='Helvetica 12').grid(
            column=0, row=24, pady=(5, 0), sticky='w')

        tk.Label(self.window, text=self.print_ticket_information["travel_distance"], font='Helvetica 12').grid(
            column=1, row=24, pady=(5, 0), sticky='w')

        tk.Label(self.window, text="Travel time:", font='Helvetica 12').grid(
            column=0, row=25, pady=(5, 0), sticky='w')

        tk.Label(self.window, text=self.print_ticket_information["travel_time"], font='Helvetica 12').grid(
            column=1, row=25, pady=(5, 0), sticky='w')

        self.window.mainloop()


UserInterface()
