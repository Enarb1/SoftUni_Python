class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_send = False

    def send(self):
        self.is_send = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_send}"


emails = []

while True:
    command = input().split()
    if command[0] == "Stop":
        break
    sender = command[0]
    receiver = command[1]
    content = command[2]
    email = Email(sender, receiver, content)
    emails.append(email)


sent_mails = list (map(int, input().split(", ")))

for index_mail in sent_mails:
    emails[index_mail].send()

for email in emails:
    print(email.get_info())
