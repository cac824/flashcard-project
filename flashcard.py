import tkinter as tk
from tkinter import ttk

window = tk.Tk()

count = 0
is_flipped = False
first_card_replaced = False

flashcard_front = ['']  # holds all elements for the front of flashcard
flashcard_back = ['']  # holds all elements for the back of flashcard


def error(text):
    error_window = tk.Tk()
    error_window.geometry("300x300")
    error_window.title("Error")
    error_label = tk.Label(error_window, text=text, font='Arial')
    error_label.pack()


def new_flashcard():  # function that makes a new card
    new_window = tk.Tk()
    new_window.geometry("500x400")
    new_window.title("New Flashcard")

    term_label = tk.Label(new_window, text="Term", font='Arial')
    term_label.pack()

    entry = tk.Entry(new_window)
    entry.pack()

    definition_label = tk.Label(new_window, text="Definition", font='Arial')
    definition_label.pack()

    entry2 = tk.Entry(new_window)
    entry2.pack()

    def add_flashcard():  # nested function that adds a new card
        global first_card_replaced
        term = entry.get()
        definition = entry2.get()
        if term and definition:  # checks if term and definition are filled out
            if not first_card_replaced:  # checks if first_card_replaced is false
                flashcard_front[0] = term  # sets the first index of flashcard_front and back to term and definition
                flashcard_back[0] = definition
                first_card_replaced = True  # sets first_card_replaced as true to stop running this conditional
            if len(flashcard_front) >= 1 and flashcard_front[0] == term:  # gets rid of duplicates of first term
                flashcard_front.pop(0)
                flashcard_back.pop(0)
        else:
            error("Both entries need to be filled out")
        flashcard_front.append(term)
        flashcard_back.append(definition)
        entry.delete(0, tk.END)  # clears the entries after all are filled out and submitted
        entry2.delete(0, tk.END)

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
    is_flipped = False
    label2.config(text=flashcard_front[count])
    num_label.config(text="{}/{}".format(count + 1, len(flashcard_front)))


def prev_card():
    global count, is_flipped
    if count > 0:
        count -= 1
    is_flipped = False
    label2.config(text=flashcard_front[count])
    num_label.config(text="{}/{}".format(count + 1, len(flashcard_front)))


def delete_card():
    global count
    if flashcard_front and flashcard_back:
        flashcard_front.pop(count)
        flashcard_back.pop(count)
    if len(flashcard_front) and len(flashcard_back) == 1:
        flashcard_front[0] = ''
        flashcard_back[0] = ''
        num_label.config(text="{}/{}".format(count + 1, len(flashcard_front)))


# sets up the window
window.geometry("800x500")
window.title("Flashcard")
# sets up the label at the top of the screen
label1 = ttk.Label(window, text="Flashcards", font='Arial')
label1.pack()
# creates label showing what card you're on
num_label = tk.Label(window, text="{}/{}".format(count + 1, len(flashcard_front)))
num_label.pack()
# creates the flashcard
card_frame = tk.Frame(window, bg="white", width=500, height=300)
card_frame.pack(pady=20, padx=20)
# words that go on the flashcard
label2 = tk.Label(card_frame, text="{}".format(flashcard_front[count]), bg="white", font=('Arial', "25"))
label2.pack(pady=50, padx=50)
# new flashcard button
button = tk.Button(window, text="New Flashcard", font='Arial', command=new_flashcard)
button.pack()
# previous card button
button2 = tk.Button(window, text="Previous Card", font='Arial', command=prev_card)
button2.pack()
button2.place(x=100, y=249)
# next card button
button3 = tk.Button(window, text="Next Card", font='Arial', command=next_card)
button3.pack()
button3.place(x=575, y=249)
# flip card button
button4 = tk.Button(window, text="Flip Card", font='Arial', command=flip_card)
button4.pack()
button4.place(x=275, y=300)
# delete card button
button5 = tk.Button(window, text="Delete Card", font='Arial', command=delete_card)
button5.pack()
button5.place(x=425, y=300)

window.mainloop()
