from tkinter import Tk, Canvas, PhotoImage, Button

BACKGROUND_COLOR = "#B1DDC6"


# ---------------------------- UI SETUP ------------------------------- #
def main():
    window = Tk()
    window.title("Flashy")
    window.config(bg=BACKGROUND_COLOR, highlightthickness=0, width=1000, height=800)

    canvas = Canvas(width=900, height=600, bg=BACKGROUND_COLOR, highlightthickness=0)
    front_img = PhotoImage(file="./images/card_front.png")
    canvas.create_image(460, 300, image=front_img)
    title_txt = canvas.create_text(460, 180, text="Title", font=("Ariel", 30, "italic"), fill="Black")
    word_txt = canvas.create_text(460, 280, text="Word", font=("Ariel", 30, "bold"), fill="Black")
    canvas.grid(row=0, column=0, columnspan=2)
    wrong_btn_img = PhotoImage(file="./images/wrong.png")
    wrong_btn = Button(image=wrong_btn_img, highlightthickness=0)
    wrong_btn.grid(row=1, column=0)

    right_btn_img = PhotoImage(file="./images/right.png")
    wrong_btn = Button(image=right_btn_img, highlightthickness=0)
    wrong_btn.grid(row=1, column=1)

    window.mainloop()


if __name__ == '__main__':
    main()
