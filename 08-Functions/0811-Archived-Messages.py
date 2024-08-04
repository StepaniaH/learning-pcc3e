hello = [
    "Hello",
    "Hi",
    "Hey",
    "Yo",
]

sent_messages = []


def show_message(messages):
    for message in messages:
        print(message)

    print("\n")


def send_message(messages):
    while messages:
        sent_messages.append(messages.pop(0))


show_message(hello)
send_message(hello[:])
show_message(hello)
show_message(sent_messages)
