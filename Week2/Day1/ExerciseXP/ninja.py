class Phone():
    def __init__(self, phone_number):
        self.call_history = []
        self.messages = []
        self.phone_number = phone_number
    
    def call(self, other_phone):
        # print a string showing who called who
        print(f"{self.phone_number} called {other_phone.phone_number}")
        self.call_history.append(other_phone)
        other_phone.call_history.append(self.phone_number)
        

    def show_call_history(self):
        print(self.call_history)
        

    def send_message(self, other_phone):
        content = input("Enter a message: ")
        new_message = {
            "to": other_phone.phone_number,
            "from": self.phone_number,
            "content": content
        }
        self.messages.append(new_message)
        print(self.messages)

    def show_outgoing_messages(self):
        for message in self.messages:
            print(f"Sent {message["content"]} to {message["to"]}")
    
    def show_incoming_messages(self):
        for message in self.messages:
            print(f"Recieved {message["content"]} from {message["from"]}")

    def show_messages_from(self, other_phone):
        if other_phone.phone_number == "0987-654-321":
            for message in self.messages:
                print(f"recieved {message["content"]} from {other_phone.phone_number}")
        

my_phone = Phone("123-456-7890")
brother_phone = Phone("0987-654-321")
alternative_phone = Phone("0967-653-301")
my_phone.call(brother_phone)
brother_phone.call(my_phone)

my_phone.show_call_history()
brother_phone.show_call_history()
my_phone.send_message(brother_phone)
brother_phone.send_message(my_phone)
my_phone.show_outgoing_messages()
my_phone.show_incoming_messages()
my_phone.show_messages_from(brother_phone)
my_phone.show_messages_from(alternative_phone)