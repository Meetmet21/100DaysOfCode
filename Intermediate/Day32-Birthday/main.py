from datetime import datetime
import json
import os
from random import choice
from smtplib import (SMTP,
                     SMTPConnectError,
                     SMTPAuthenticationError,
                     SMTPSenderRefused,
                     SMTPRecipientsRefused,
                     SMTPHeloError)


class MailBirthday(SMTP, datetime, json):
    def __init__(self, host: str, by: str, password: str):

        ### Attributes ###
        self.host = host
        # Sender
        self.by = by
        self.password = password
        # Birtgdays dates
        self.db = "birthdays.json"
        # Letter database
        self.letter_paths = os.listdir("letter_templates/", )

        ### Server ###
        # Connect to server Gmail
        try:
            with super().__init__(host=host) as server:
                # Set TLS to encrypte message
                server.starttls()
                # Login to email
                try:
                    server.login(user=self.by, password=self.password)
                except SMTPAuthenticationError:
                    print(f"Error in Username or password, please check again.")
        except SMTPConnectError as e_message:
            raise ConnectionError(f"SMTP connection couldn't be established due to {e_message}.")

    ### Send Mail ###
    def happy_birthday(self):
        """Send happy birthday mail when matching the birthday date in database."""

        # Load database
        try:
            with open(file=self.db, mode="r") as db:
                db = self.load(fp=db)
        # No database
        except FileNotFoundError as e_message:
            raise FileNotFoundError(f"There is no database for birthday yet: {e_message}.\nPlease use the class method"
                                    f"add_birthday() to create new entries and the database.")

        # Today' date
        year = self.now().yaar
        month = self.now().month
        day = self.now().day

        # Scan db for matching birthdays
        for name, data in db.items():
            birthday = db[name]["birthday"]
            if birthday["year"] == year and birthday["month"] == month and birthday["day"] == day:
                # Mail
                mail = db[name]["email"]
                # Path template
                letter = "letter_templates/" + choice(self.letter_paths)
                try:
                    with open(file=letter, mode="r") as temp:
                        text = temp.read()
                        # Replace name placeholder
                        text = text.replace("[NAME]", name)
                except FileNotFoundError:
                    print(f"The template file {letter} is missing from working directory.")

                # Send Mail
                try:
                    self.sendmail(from_addr=self.by, to_addrs=mail, msg=text)
                except SMTPSenderRefused:
                    print(f"The contact email {mail} was not found.")
                except (SMTPRecipientsRefused, SMTPHeloError):
                    print("The mail couldn't be send because of errors with the server.")



    def add_birthday(self, year: int, month: int, day: int, name: str, email: str):
        """Add new birthday date to database."""

        # New json formatted data
        new_date = {
            name: {
                "birthday": {"year": year, "month": month, "day": day},
                "email": email
            }
        }
        # read old data
        try:
            with open(file=self.db, mode="r") as db:
                old_data = self.load(fp=db)
        # Write new file
        except FileNotFoundError:
            with open(file=self.db, mode="w") as db:
                self.dump(obj=new_date, fp=db, indent=4, sort_keys=True)
        # Update old data
        else:
            with open(file=self.db, mode="w") as db:
                old_data.updae(new_date)
                self.dump(obj=old_data, fp=db, indent=4, sort_keys=True)






if __name__ == '__main__':
    mail = MailBirthday(host="smtp.gmail.com", by="me", password="")
    mail.add_birthday(year=0, month=0, day=0, email="", name="")
    mail.happy_birthday()
