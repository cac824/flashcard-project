import tkinter as tk
from tkinter import ttk
import random

window = tk.Tk()

count = 0
correct_answer = 0
question_count = 0
is_flipped = False
window_destroyed = False

flashcard_front = []  # holds all elements for the front of flashcard
flashcard_back = []  # holds all elements for the back of flashcard

quiz_dict = {}
question_number = 0

# default settings for GUI
button_color = "systembuttonface"
font = "Arial"


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


def message(title, text):  # function that makes messages
    message_window = tk.Tk()
    message_window.geometry("300x300")
    message_window.title(title)
    message_label = tk.Label(message_window, text=text, font='Arial')
    message_label.pack()


def open_quiz():
    global question_count

    def update_question():
        if question_count < len(quiz_dict):
            current_key = list(quiz_dict.keys())[question_count]
            question_label.config(text=quiz_dict[current_key]["Question"])
            choice1_button.config(text=quiz_dict[current_key]["Choices"][0])
            choice2_button.config(text=quiz_dict[current_key]["Choices"][1])
            choice3_button.config(text=quiz_dict[current_key]["Choices"][2])
            choice4_button.config(text=quiz_dict[current_key]["Choices"][3])
        else:
            question_label.config(text="Score {}/{}".format(correct_answer, len(quiz_dict)))

    def check_answer(choice):
        global question_count, correct_answer

        if question_count < len(quiz_dict):
            first_key = list(quiz_dict.keys())[question_count]
            if choice == quiz_dict[first_key]["Answer"]:
                correct_answer += 1
            question_label.config(text=quiz_dict[first_key]["Question"])
            question_count += 1
            update_question()

        else:
            question_label.config(text="Score {}/{}".format(correct_answer, len(quiz_dict)))

    def answer_choice1():
        check_answer(quiz_dict[list(quiz_dict.keys())[question_count]]["Choices"][0])

    def answer_choice2():
        check_answer(quiz_dict[list(quiz_dict.keys())[question_count]]["Choices"][1])

    def answer_choice3():
        check_answer(quiz_dict[list(quiz_dict.keys())[question_count]]["Choices"][2])

    def answer_choice4():
        check_answer(quiz_dict[list(quiz_dict.keys())[question_count]]["Choices"][3])

    # creates the window
    quiz_window = tk.Tk()
    quiz_window.geometry("300x300")
    quiz_window.title("Quiz")
    # creates the label for the questions
    question_frame = tk.Frame(quiz_window, bg="white", width=250, height=250)
    question_frame.pack()
    question_label = tk.Label(question_frame, text="", bg="white", font=(font, "15"))
    question_label.pack(pady=50, padx=50)
    # creates all the multiple choice buttons
    choice1_button = tk.Button(quiz_window, text="", width=10, command=answer_choice1)
    choice1_button.pack()
    choice2_button = tk.Button(quiz_window, text="", width=10, command=answer_choice2)
    choice2_button.pack()
    choice3_button = tk.Button(quiz_window, text="", width=10, command=answer_choice3)
    choice3_button.pack()
    choice4_button = tk.Button(quiz_window, text="", width=10, command=answer_choice4)
    choice4_button.pack()

    update_question()

def menu():
    menu_window = tk.Tk()
    menu_window.geometry("300x300")
    menu_window.title("Menu")

    def back():
        menu_window.destroy()

    def color_change():
        global button_color
        colors_list = [
            "White", "Black", "Red", "Green", "Blue", "Cyan",
            "Yellow", "Magenta", "Gray", "LightGray", "DarkGray",
            "Brown", "Orange", "Pink", "Purple", "Violet",
            "Gold", "Silver", "LightBlue", "Maroon"
        ]
        button_color = "systembuttonface"
        generated_color = random.choice(colors_list)
        window.config(bg=generated_color)
        button.config(bg=button_color)
        flipcard_button.config(bg=button_color)
        nextcard_button.config(bg=button_color)
        prevcard_button.config(bg=button_color)
        deletecard_button.config(bg=button_color)
        menu_button.config(bg=button_color)
        label1.config(background=button_color)
        num_label.config(background=button_color)
        card_frame.config(background=button_color)
        label2.config(background=button_color)

    def dark_mode():
        global button_color
        window.config(bg="gray16")
        button_color = "gray54"
        button.config(bg=button_color)
        flipcard_button.config(bg=button_color)
        nextcard_button.config(bg=button_color)
        prevcard_button.config(bg=button_color)
        deletecard_button.config(bg=button_color)
        menu_button.config(bg=button_color)
        label1.config(background=button_color)
        num_label.config(background=button_color)
        card_frame.config(background=button_color)
        label2.config(background=button_color)

    def change_fonts():
        global font
        fonts_list = [
            "times", "timesbold", "timesitalic",
            "courier", "arial", "symbol",
            "lucidaconsole", "monaco", "fixedsys"
        ]
        font = random.choice(fonts_list)
        button.config(font=font)
        flipcard_button.config(font=font)
        nextcard_button.config(font=font)
        prevcard_button.config(font=font)
        deletecard_button.config(font=font)
        menu_button.config(font=font)
        label1.config(font=font)
        num_label.config(font=font)
        label2.config(font=font)

    def settings():
        menu_window.destroy()
        settings_window = tk.Tk()
        settings_window.geometry("300x300")
        settings_window.title("Settings")
        color_button = tk.Button(settings_window, text="Background Color", font='Arial', command=color_change)
        color_button.pack()
        darkmode_button = tk.Button(settings_window, text="Dark Mode", font=font, command=dark_mode)
        darkmode_button.pack()
        font_button = tk.Button(settings_window, text="Change Font", font=font, command=change_fonts)
        font_button.pack()

    def quiz():
        menu_window.destroy()
        makequiz_window = tk.Tk()
        makequiz_window.geometry("300x300")
        makequiz_window.title("Quiz")
        # tells the user where to enter the question
        question_label = tk.Label(makequiz_window, text="Enter Question")
        question_label.pack()
        question_entry = tk.Entry(makequiz_window)
        question_entry.pack()
        # tells the user where to enter the first choice
        choice1_label = tk.Label(makequiz_window, text="Enter Choice 1\n(Correct Answer)")
        choice1_label.pack()
        choice1_entry = tk.Entry(makequiz_window)
        choice1_entry.pack()
        # tells the user where to enter the second choice
        choice2_label = tk.Label(makequiz_window, text="Enter Choice 2")
        choice2_label.pack()
        choice2_entry = tk.Entry(makequiz_window)
        choice2_entry.pack()
        # tells the user where to enter the third choice
        choice3_label = tk.Label(makequiz_window, text="Enter Choice 3")
        choice3_label.pack()
        choice3_entry = tk.Entry(makequiz_window)
        choice3_entry.pack()
        # tells the user where to enter the fourth choice
        choice4_label = tk.Label(makequiz_window, text="Enter Choice 4")
        choice4_label.pack()
        choice4_entry = tk.Entry(makequiz_window)
        choice4_entry.pack()

        def add_question():  # nested function to add a question
            global window_destroyed, question_number
            question = question_entry.get()
            choice1 = choice1_entry.get()
            choice2 = choice2_entry.get()
            choice3 = choice3_entry.get()
            choice4 = choice4_entry.get()

            if question and choice1 and choice2 and choice3 and choice4:  # checks if all entries are filled out
                question_number += 1
                quiz_dict[question_number] = {  # updates the quiz_dict each time
                    "Question": question,
                    "Choices": [choice1, choice2, choice3, choice4],
                    "Answer": choice1
                }
            else:
                message("Error", "All entries must be filled")

            question_entry.delete(0, tk.END)
            choice1_entry.delete(0, tk.END)
            choice2_entry.delete(0, tk.END)
            choice3_entry.delete(0, tk.END)
            choice4_entry.delete(0, tk.END)
            print(quiz_dict)
            print(len(list(quiz_dict)))
            if not window_destroyed:
                window.destroy()
                window_destroyed = True
                open_quiz()

        # this button makes the quiz
        addquestion_button = tk.Button(makequiz_window, text="Add Question", command=add_question)
        addquestion_button.pack()

    settings_button = tk.Button(menu_window, text="Settings", font='Arial', command=settings)
    settings_button.pack()
    quiz_button = tk.Button(menu_window, text="Make A Quiz", font='Arial', command=quiz)
    quiz_button.pack()
    back_button = tk.Button(menu_window, text="Back", font='Arial', command=back)
    back_button.pack()
    back_button.place(x=120, y=250)


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
label2 = tk.Label(card_frame, text="No Cards Available", bg="white", font=(font, "25"))
label2.pack(pady=50, padx=50)
# new flashcard button
button = tk.Button(window, text="New Flashcard", font=font, bg=button_color, command=new_flashcard)
button.pack()
# previous card button
prevcard_button = tk.Button(window, text="Previous Card", font=font, bg=button_color, command=prev_card)
prevcard_button.pack()
prevcard_button.place(x=100, y=249)
# next card button
nextcard_button = tk.Button(window, text="Next Card", font=font, bg=button_color, command=next_card)
nextcard_button.pack()
nextcard_button.place(x=575, y=249)
# flip card button
flipcard_button = tk.Button(window, text="Flip Card", font=font, bg=button_color, command=flip_card)
flipcard_button.pack()
flipcard_button.place(x=275, y=300)
# delete card button
deletecard_button = tk.Button(window, text="Delete Card", font=font, bg=button_color, command=delete_card)
deletecard_button.pack()
deletecard_button.place(x=425, y=300)
# menu button
menu_button = tk.Button(window, text="Menu", font='Arial', bg=button_color, command=menu)
menu_button.pack()
menu_button.place(x=10, y=10)

window.mainloop()
