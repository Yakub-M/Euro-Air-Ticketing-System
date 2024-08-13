# Euro-Air-Ticketing-System

This program is designed to process airline tickets for a fictional airline "Euro Air", operating within the European Union. The code is intended for use in a POS terminal to print tickets for clients.

The program consists of two main components: the UserInterface and DisplayTicket classes. Upon starting the program, the UserInterface class enables the client to input the necessary information to create a ticket. After entering the details, the client must click the "Process ticket" button. This action triggers the verify_ticket_button_click() function, which validates the entered information and displays appropriate warnings and informational messages.

Clients can select their departure and arrival destinations either manually or by using airport codes (ICAO or IATA), but only one method can be used at a time to prevent conflicts. The required airport data is stored in the "airports_europe.csv" file. If the entered information is valid, the finalize_ticket() function is called. This function adds the final details to the ticket, including calculating the price based on the distance between the selected destinations. The distance is computed using the "great_circle" formula from the geopy.distance module.

Once the ticket is finalized, it is saved in the "customer_ticket.csv" file. The UserInterface window is then closed, and the DisplayTicket class is invoked to display the printed ticket details.

Payment for the ticket will be processed through the POS terminal.
