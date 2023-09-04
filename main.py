import random
from tkinter import Tk, Canvas, PhotoImage, Button
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"


# ---------------------------- GENERATE WORDS -----------------------  #
def generate_words(data, canvas, word_label):
    french_word = random.choice(list(data.keys()))
    english_word = random.choice(list(data.values()))
    print(len("word"))
    canvas.itemconfig(word_label, text=french_word)


# ---------------------------- READ FILE ----------------------------- #
def read_file():
    data = pd.read_csv("./data/french_words.csv")
    dict_data = dict(data.values)
    return dict_data


# ---------------------------- UI SETUP ------------------------------- #
def main():
    vocabulary = read_file()
    window = Tk()
    window.title("Flashy")
    window.config(bg=BACKGROUND_COLOR, highlightthickness=0, width=1000, height=800)

    canvas = Canvas(width=900, height=600)
    front_img = PhotoImage(file="./images/card_front.png")
    canvas.create_image(460, 300, image=front_img)
    canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
    title_label = canvas.create_text(460, 180, text="French", font=("Ariel", 30, "italic"), fill="Black")
    word_label = canvas.create_text(460, 280, text="Word", font=("Ariel", 30, "bold"), fill="Black")
    canvas.grid(row=0, column=0, columnspan=2)
    wrong_btn_img = PhotoImage(file="./images/wrong.png")
    wrong_btn = Button(image=wrong_btn_img, highlightthickness=0,
                       command=lambda: generate_words(vocabulary, canvas, word_label))
    wrong_btn.grid(row=1, column=0)

    right_btn_img = PhotoImage(file="./images/right.png")
    right_btn = Button(image=right_btn_img, highlightthickness=0,
                       command=lambda: generate_words(vocabulary, canvas, word_label))
    right_btn.grid(row=1, column=1)

    window.mainloop()


if __name__ == '__main__':
    main()
