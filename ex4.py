def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact not found."
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "IndexError."

    return inner

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    if len(args)!= 2:
        raise ValueError("Give me name and phone please.")
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact phone is updated."
    else:
        return "Contact not found."
   
@input_error  
def delete_contact(args, contacts):
    name = args[0]
    if name in contacts:
        del contacts[name]
        return "Contact deleted."
    else: 
        return "Contact not found."
    
def show_contacts(args, contacts):
    name, _ = args
    return contacts[name]

def all_contacts(args, contacts):
    return contacts


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit", "quit", "stop"]:
            print("Good bye, see you soon!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "show":
            print(show_contacts(args, contacts))
        elif command == "all":
            print(all_contacts(args, contacts))
        elif command == "delete":
            print(delete_contact(args, contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
