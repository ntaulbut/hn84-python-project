from utils import *
from colorama import Fore, Back, Style
import keyboard

# Constants
MAX_EMAILS = 17
MAX_EMAIL_LINES = 16
EMAIL_WIDTH = 76


class Email:
    def __init__(self, subject, author, body):
        self.subject = subject
        self.author = author
        self.body = body


emails: list[Email] = [
    Email(
        "Hello this is a subject",
        "Jeff",
        """Hi John,
    
There's been a few problems with the mainframe lately.
Someone has encrypted our files...
    
Hope you can fix it.
    
Regards,
Jeff""",
    ),
    Email("This is another subject", "Bob", "Email body!!!"),
    Email("Something about HackNotss84", "Trijit", "Your ticket is here."),
]


def email_subject(email: Email, index: int):
    text = email.subject.ljust(EMAIL_WIDTH)
    return (
        Back.WHITE + Fore.BLACK + text + Style.RESET_ALL
        if index == selection_index
        else text
    )


def print_inbox():
    template = (
        TOP_LINE
        + "│ "
        + "Inbox".ljust(EMAIL_WIDTH)
        + " │\n"
        + DIV_LINE
        + "│ {} │\n" * MAX_EMAILS
        + DIV_LINE
        + "│ "
        + "[Q] Quit [Up/Down] Change Selection [Enter] Open Email".ljust(EMAIL_WIDTH)
        + " │\n"
        + BOTTOM_LINE
    )
    print(
        template.format(
            *[email_subject(email, index) for index, email in enumerate(emails)],
            *[" " * EMAIL_WIDTH for _ in range(MAX_EMAILS - len(emails))],
        )
    )


def print_email_view():
    template = (
        TOP_LINE
        + "│ {} │\n" * 2
        + DIV_LINE
        + "│ {} │\n" * MAX_EMAIL_LINES
        + DIV_LINE
        + "│ "
        + "[Q] Quit [Esc] Inbox".ljust(EMAIL_WIDTH)
        + " │\n"
        + BOTTOM_LINE
    )
    email = emails[selection_index]
    email_lines = email.body.split("\n")
    print(
        template.format(
            f"Subject: {email.subject}".ljust(EMAIL_WIDTH),
            f"Author: {email.author}".ljust(EMAIL_WIDTH),
            *[email_line.ljust(EMAIL_WIDTH) for email_line in email_lines],
            *[" " * EMAIL_WIDTH for _ in range(MAX_EMAIL_LINES - len(email_lines))],
        )
    )


def display():
    global selection_index, menu, run
    clear()

    # Print
    match menu:
        case "inbox":
            print_inbox()
        case "email":
            print_email_view()

    # Input
    event = keyboard.read_event()
    if event.event_type == keyboard.KEY_DOWN:
        match menu:
            # Inbox
            case "inbox":
                match event.name:
                    case "down" | "j":
                        selection_index = inc_b(selection_index, len(emails) - 1)
                    case "up" | "k":
                        selection_index = dec_b(selection_index, 0)
                    case "enter" | "l":
                        menu = "email"
            # Email
            case "email":
                if event.name == "esc" or event.name == "h":
                    menu = "inbox"
        # All menus
        if event.name == "q":
            run = False


run = True
menu = "inbox"
selection_index = 0


def mail_app():
    global run, menu, selection_index
    run = True
    menu = "inbox"
    selection_index = 0
    while run:
        display()
    clear()


if __name__ == "__main__":
    mail_app()
