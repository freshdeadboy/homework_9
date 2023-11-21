def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter a valid user name."
        except ValueError:
            return "Give me name and phone, please."
        except IndexError:
            return "Contact not found."
    return wrapper


class AssistantBot:
    def __init__(self):
        self.contacts = {}

    @input_error
    def handle_hello(self):
        return "How can I help you?"

    @input_error
    def handle_add(self, command):
        _, name, phone = command.split()
        self.contacts[name] = phone
        return f"Contact {name} added with phone {phone}."

    @input_error
    def handle_change(self, command):
        _, name, phone = command.split()
        if name in self.contacts:
            self.contacts[name] = phone
            return f"Phone number for {name} changed to {phone}."
        else:
            raise IndexError

    @input_error
    def handle_phone(self, command):
        _, name = command.split()
        return f"The phone number for {name} is {self.contacts[name]}."

    @input_error
    def handle_show_all(self):
        if not self.contacts:
            return "No contacts available."
        else:
            return "\n".join([f"{name}: {phone}" for name, phone in self.contacts.items()])

    def handle_goodbye(self):
        return "Good bye!"

    def main(self):
        while True:
            user_input = input("Enter command: ").lower()
            
            if user_input == "hello":
                print(self.handle_hello())
            elif user_input.startswith("add"):
                print(self.handle_add(user_input))
            elif user_input.startswith("change"):
                print(self.handle_change(user_input))
            elif user_input.startswith("phone"):
                print(self.handle_phone(user_input))
            elif user_input == "show all":
                print(self.handle_show_all())
            elif user_input in ["good bye", "close", "exit"]:
                print(self.handle_goodbye())
                break
            else:
                print("Invalid command. Try again.")


if __name__ == "__main__":
    bot = AssistantBot()
    bot.main()
