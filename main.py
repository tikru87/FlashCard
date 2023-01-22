from tkinter import *
from gtts import gTTS
import os
import pandas
import random
from playsound import playsound

BACKGROUND_COLOR = "#B1DDC6"

data = pandas.read_csv("data/french_words.csv")
to_learn = data.to_dict(orient="records")
current_card = {}


def play_sound():
    language = "fr"
    tts = gTTS(text=current_card["French"], lang=language, slow=False)
    tts.save("french.mp3")
    playsound("french.mp3")
    os.remove("french.mp3")


def next_card():
    global current_card
    window.after(1000, func=play_sound)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_img, image=c_front_img)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    window.after(5000, func=flip_card)



def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_img, image=c_back_img)


#  Window
window = Tk()
window.title("FlashCard App")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

window.after(3000, func=flip_card)

# Canvas
canvas = Canvas(width=800, height=526)
c_front_img = PhotoImage(file="images/card_front.png")
c_back_img = PhotoImage(file="images/card_back.png")

card_img = canvas.create_image(400, 263, image=c_front_img)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
v_img = PhotoImage(file="images/right.png")
v_button = Button(image=v_img, highlightthickness=0, command=next_card)
v_button.grid(row=1, column=0)

x_img = PhotoImage(file="images/wrong.png")
x_button = Button(image=x_img, highlightthickness=0, command=next_card)
x_button.grid(row=1, column=1)

next_card()

window.mainloop()
