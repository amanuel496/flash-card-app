import random
from tkinter import Tk, Canvas, PhotoImage, Button
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"
data_size = 0
current_word = ""
french_word = ""
english_word = ""
vocabulary = None


# ---------------------------- FLIP CARD --------------------------- #
def flip_card(canvas, card_img, new_img, word_label, english, title_label):
    canvas.itemconfig(card_img, image=new_img)
    canvas.itemconfig(title_label, text="English", fill="white")
    canvas.itemconfig(word_label, text=english, fill="white")


# ---------------------------- GENERATE WORDS -----------------------  #
def generate_words(window, data, canvas, word_label, card_img, back, title_label, front, remove):
    global current_word
    global french_word
    global english_word

    if data:
        current_word = french_word
        french_word = random.choice(list(data.keys()))
        english_word = data[french_word]
        canvas.itemconfig(card_img, image=front)
        canvas.itemconfig(title_label, text="French", fill="black")
        canvas.itemconfig(word_label, text=french_word, fill="black")

        if remove and data[current_word]:
            data.__delitem__(current_word)
            current_word = french_word
            pd.DataFrame.from_dict(data, orient="index").to_csv("./data/words_to_learn.csv")
        window.after(3000, flip_card, canvas, card_img, back, word_label, english_word, title_label)
    else:
        # os.remove("./data/words_to_learn.csv")
        canvas.itemconfig(title_label, text="Congratulations! 🥳🎉\nYou've learned every word.")
        canvas.itemconfig(word_label, text="")
        # window.after


# ---------------------------- READ FILE ----------------------------- #
def read_file():
    try:
        data = pd.read_csv("./data/words_to_learn.csv")
        if data.empty:
            data = pd.read_csv("./data/french_words.csv")
    except FileNotFoundError:
        data = pd.read_csv("./data/french_words.csv")
    dict_data = dict(data.values)
    return dict_data


# ---------------------------- UI SETUP ------------------------------- #
def main():
    global vocabulary
    global data_size
    vocabulary = read_file()
    data_size = len(vocabulary)
    # remove = False
    window = Tk()
    window.title("Flashy")
    window.config(bg=BACKGROUND_COLOR, highlightthickness=0, width=1000, height=800)

    canvas = Canvas(width=900, height=600)
    front_img = PhotoImage(file="./images/card_front.png")
    back_img = PhotoImage(file="./images/card_back.png")
    card_img = canvas.create_image(460, 300, image=front_img)

    canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
    title_label = canvas.create_text(460, 180, text="French", font=("Ariel", 30, "italic"), fill="Black")
    word_label = canvas.create_text(460, 280, text="Word", font=("Ariel", 30, "bold"), fill="Black")
    canvas.grid(row=0, column=0, columnspan=2)
    wrong_btn_img = PhotoImage(file="./images/wrong.png")
    wrong_btn = Button(image=wrong_btn_img, highlightthickness=0,
                       command=lambda: generate_words(window, vocabulary, canvas, word_label, card_img, back_img,
                                                      title_label, front_img, False))
    wrong_btn.grid(row=1, column=0)

    right_btn_img = PhotoImage(file="./images/right.png")
    right_btn = Button(image=right_btn_img, highlightthickness=0,
                       command=lambda: generate_words(window, vocabulary, canvas, word_label, card_img, back_img,
                                                      title_label, front_img, True))
    right_btn.grid(row=1, column=1)

    generate_words(window, vocabulary, canvas, word_label, card_img, back_img, title_label, front_img,
                   False)

    window.mainloop()


if __name__ == '__main__':
    main()
