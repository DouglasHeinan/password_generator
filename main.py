from tkinter import *
from tkinter import messagebox
import pyperclip
import random


def main():



# ---------------------------- PASSWORD GENERATOR ------------------------------- #
    def gen_password():

        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                   'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
                   'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

        nr_letters = random.randint(8, 14)
        nr_symbols = random.randint(1, 4)
        nr_numbers = random.randint(1, 4)

        password_letters = [random.choice(letters) for n in range(nr_letters)]
        password_symbols = [random.choice(symbols) for n in range(nr_symbols)]
        password_numbers = [random.choice(numbers) for n in range(nr_numbers)]

        password_list = password_letters + password_symbols + password_numbers
        random.shuffle(password_list)

        password = "".join(password_list)
        password_entry.delete(0, END)
        password_entry.insert(END, password)
        pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
    def save_password():
        password_entry_submission = password_entry.get()
        website_entry_submission = website_entry.get()
        email_entry_submission = email_entry.get()

        if len(password_entry_submission) < 1 or len(website_entry_submission) < 1 or len(email_entry_submission) < 1:
            messagebox.showerror(title="Empty Field", message="You can't leave any fields empty!")
        else:
            save_ok = messagebox.askokcancel(title=website_entry_submission,
                                             message=f"These are the details entered: \n"
                                                     f"Email: {email_entry_submission}\n"
                                                     f"Password: {password_entry_submission} \n"
                                                     f"Is it ok to save?")

            if save_ok:
                with open("my_data.txt", "a") as f:
                    f.write(f"{website_entry_submission} | {email_entry_submission} | {password_entry_submission}\n")
                password_entry.delete(0, END)
                website_entry.delete(0, END)
                website_entry.focus()
# ---------------------------- UI SETUP ------------------------------- #
    window = Tk()
    window.title("Password Manager")
    window.config(padx=50, pady=50)

    canvas = Canvas(width=200 , height=200 ,)
    logo = PhotoImage(file="logo.png")
    canvas.create_image(100, 100, image=logo)
    canvas.grid(column=1, row=0)

    # Labels
    website_prompt = Label(text="Website:")
    website_prompt.grid(column=0, row=1)

    email_prompt = Label(text="Email/Username:")
    email_prompt.grid(column=0, row=2)

    password_prompt = Label(text="Password:")
    password_prompt.grid(column=0, row=3)

    # Entries
    website_entry = Entry(width=52)
    website_entry.grid(column=1, row=1, columnspan=2)
    website_entry.focus()

    email_entry = Entry(width=52)
    email_entry.grid(column=1, row=2, columnspan=2)
    email_entry.insert(END, "myname@email.com")

    password_entry = Entry(width=33)
    password_entry.grid(column=1, row=3)

    # Buttons
    password_button = Button(text="Generate Password", command=gen_password)
    password_button.grid(column=2, row=3)

    add_button = Button(text="Add", command=save_password, width=44)
    add_button.grid(column=1, row=4, columnspan=2)

    window.mainloop()


if __name__ == '__main__':
    main()
