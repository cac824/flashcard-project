import tkinter as tk
from tkinter import ttk
import random

window = tk.Tk()

count = 0
is_flipped = False
first_card_replaced = False

flashcard_front = []  # holds all elements for the front of flashcard
flashcard_back = []  # holds all elements for the back of flashcard


def enable_button(button_name):
    if len(flashcard_front) >= 0:
        button_name.config(state=tk.NORMAL)


def disable_button(button_name):
    if len(flashcard_front) <= 1:
        button_name.config(state=tk.DISABLED)


def update_label():
    global count
    if len(flashcard_front) > 0:
        label2.config(text=flashcard_front[count])
    else:
        label2.config(text="No Cards Available")


def menu():
    menu_window = tk.Tk()
    menu_window.geometry("300x300")
    menu_window.title("Menu")

    def color_change():
        colors_list = [
            "White", "Black", "Red", "Green", "Blue", "Cyan",
            "Yellow", "Magenta", "Gray", "LightGray", "DarkGray",
            "Brown", "Orange", "Pink", "Purple", "Violet",
            "Gold", "Silver", "LightBlue", "Maroon"
        ]
        color_name = random.choice(colors_list)
        window.config(bg=color_name)

    def settings():
        menu_window.destroy()
        settings_window = tk.Tk()
        settings_window.geometry("300x300")
        settings_window.title("Settings")
        color_button = tk.Button(settings_window, text="Background Color", font='Arial', command=color_change)
        color_button.pack()

    settings_button = tk.Button(menu_window, text="Settings", font='Arial', command=settings)
    settings_button.pack()


def message(title, text):  # function that makes message messages
    message_window = tk.Tk()
    message_window.geometry("300x300")
    message_window.title(title)
    message_label = tk.Label(message_window, text=text, font='Arial')
    message_label.pack()


def new_flashcard():  # function that makes a new card
    new_window = tk.Tk()
    new_window.geometry("500x400")
    new_window.title("New Flashcard")

    term_label = tk.Label(new_window, text="Term", font='Arial')
    term_label.pack()

    term_entry = ttk.Entry(new_window)
    term_entry.pack()

    definition_label = ttk.Label(new_window, text="Definition", font='Arial')
    definition_label.pack()

    definition_entry = ttk.Entry(new_window)
    definition_entry.pack()

    def add_flashcard():  # nested function that adds a new card
        global first_card_replaced
        term = term_entry.get()
        definition = definition_entry.get()
        if term and definition:  # checks if term and definiton are filled out
            if not flashcard_front:  # checks if there is flashcard_front is empty
                flashcard_front.append(term)
                flashcard_back.append(definition)
            else:
                flashcard_front.append(term)
                flashcard_back.append(definition)
            update_label()
        else:
            message("Error", "Both entries need to be filled out")
        term_entry.delete(0, tk.END)  # clears the entries after all are filled out and submitted
        definition_entry.delete(0, tk.END)
        num_label.config(text="{}/{}".format(count + 1, len(flashcard_front)))

    add_card_button = tk.Button(new_window, text="Add Flashcard", font='Arial', command=add_flashcard)
    add_card_button.pack()


def flip_card():
    global count, is_flipped
    if count >= len(flashcard_front):
        return
    if is_flipped:
        label2.config(text=flashcard_front[count])
    else:
        label2.config(text=flashcard_back[count])
    is_flipped = not is_flipped


def next_card():
    global count, is_flipped
    if count < len(flashcard_front) - 1:
        count += 1
    if len(flashcard_front) == 0:
        label2.config(text="No Cards Available")
        num_label.config(text="0/0")
    else:
        label2.config(text=flashcard_front[count])
        num_label.config(text="{}/{}".format(count + 1, len(flashcard_front)))
    is_flipped = False
    enable_button(prevcard_button)
    disable_button(nextcard_button)


def prev_card():
    global count, is_flipped
    if count > 0:
        count -= 1
    if len(flashcard_front) == 0:
        label2.config(text="No Cards Available")
        num_label.config(text="0/0")
    else:
        label2.config(text=flashcard_front[count])
        num_label.config(text="{}/{}".format(count + 1, len(flashcard_front)))
    is_flipped = False
    enable_button(nextcard_button)
    disable_button(prevcard_button)


def delete_card():
    global count
    if len(flashcard_front) == 1:  # checks if flashcard_front only has one card
        flashcard_front.pop(count)
        flashcard_back.pop(count)
        num_label.config(text="0/0")
        label2.config(text="")
    elif len(flashcard_front) > 1:  # checks if flashcard_front has more than one card
        flashcard_front.pop(count)
        flashcard_back.pop(count)
        if count >= len(flashcard_front):
            count = len(flashcard_front) - 1
        label2.config(text=flashcard_front[count])
        num_label.config(text="{}/{}".format(count + 1, len(flashcard_front)))
    else:
        message("Error", "There are no cards to delete")


# sets up the window
window.geometry("800x500")
window.title("Flashcard")
# sets up the label at the top of the screen
label1 = ttk.Label(window, text="Flashcards", font='Arial')
label1.pack()
# creates label showing what card you're on
num_label = tk.Label(window, text="{}/{}".format(count, len(flashcard_front)))
num_label.pack()
# creates the flashcard
card_frame = tk.Frame(window, bg="white", width=500, height=300)
card_frame.pack(pady=20, padx=20)
# words that go on the flashcard
label2 = tk.Label(card_frame, text="No Cards Available", bg="white", font=('Arial', "25"))
label2.pack(pady=50, padx=50)
# new flashcard button
button = tk.Button(window, text="New Flashcard", font='Arial', command=new_flashcard)
button.pack()
# previous card button
prevcard_button = tk.Button(window, text="Previous Card", font='Arial', command=prev_card)
prevcard_button.pack()
prevcard_button.place(x=100, y=249)
# next card button
nextcard_button = tk.Button(window, text="Next Card", font='Arial', command=next_card)
nextcard_button.pack()
nextcard_button.place(x=575, y=249)
# flip card button
flipcard_button = tk.Button(window, text="Flip Card", font='Arial', command=flip_card)
flipcard_button.pack()
flipcard_button.place(x=275, y=300)
# delete card button
deletecard_button = tk.Button(window, text="Delete Card", font='Arial', command=delete_card)
deletecard_button.pack()
deletecard_button.place(x=425, y=300)
# menu button
menu_button = tk.Button(window, text="Menu", font='Arial', command=menu)
menu_button.pack()
menu_button.place(x=10, y=10)

window.mainloop()
