import time
import tkinter as tk

import random
from PIL import Image, ImageTk
from os import listdir, path
from pathlib import Path


class Window:
    number_folder = path.join(Path(__file__).parent, 'resources')
    numbers = listdir(number_folder)
    options = []
    button_list = []
    photo_image = None
    correct = 0

    def __init__(self):
        self.root = tk.Tk()
        self.root.resizable = False
        self.root.title('Learn Riven Numbers!')
        self.root.minsize(640, 480)

        self.question_image_label = tk.Label(image=self.photo_image)
        self.question_image_label.grid(column=1, row=0, pady=100)

        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(2, weight=1)

        self.answer_1 = tk.Button(width=50, command=lambda: self.on_button_1())
        self.answer_1.grid(column=1, row=1, sticky='ew', pady=10)
        self.answer_2 = tk.Button(width=50, command=lambda: self.on_button_2())
        self.answer_2.grid(column=1, row=2, sticky='ew', pady=10)
        self.answer_3 = tk.Button(width=50, command=lambda: self.on_button_3())
        self.answer_3.grid(column=1, row=3, sticky='ew', pady=10)
        self.answer_4 = tk.Button(width=50, command=lambda: self.on_button_4())
        self.answer_4.grid(column=1, row=4, sticky='ew', pady=10)
        self.button_list.append(self.answer_1)
        self.button_list.append(self.answer_2)
        self.button_list.append(self.answer_3)
        self.button_list.append(self.answer_4)

        self.setup_question()

        self.root.mainloop()

    def get_random_answer(self) -> str:
        return random.choice(self.numbers)

    def get_random_wrongs(self, answer) -> list:
        wrongs_pool = []
        wrongs_pool.clear()

        for number in self.numbers:
            wrongs_pool.append(number[:-4])
        wrongs_pool.remove(answer[:-4])

        wrongs_pool = random.sample(wrongs_pool, k=3)

        return wrongs_pool

    def clear_previous_question(self):
        self.options.clear()
        self.answer_1.configure(background='SystemButtonFace')
        self.answer_2.configure(background='SystemButtonFace')
        self.answer_3.configure(background='SystemButtonFace')
        self.answer_4.configure(background='SystemButtonFace')

    def setup_question(self):
        self.clear_previous_question()

        answer = self.get_random_answer()
        wrongs = self.get_random_wrongs(answer)

        self.options.append(answer[:-4])
        for wrong in wrongs:
            self.options.append(wrong)

        random.shuffle(self.options)
        self.correct = self.options.index(answer[:-4])

        self.assign_image(path.join(self.number_folder, answer))
        self.assign_button_labels(self.options)

    def assign_image(self, image):
        opened_image = Image.open(image)
        self.photo_image = ImageTk.PhotoImage(image=opened_image)
        self.question_image_label.configure(image=self.photo_image)
        self.question_image_label.update()

    def assign_button_labels(self, options):
        for count, button in enumerate(self.button_list, 0):
            button.configure(text=options[count])

    def on_button_1(self):
        if self.correct == 0:
            self.given_correct_answer()
        else:
            self.given_wrong_answer(0)

    def on_button_2(self):
        if self.correct == 1:
            self.given_correct_answer()
        else:
            self.given_wrong_answer(1)

    def on_button_3(self):
        if self.correct == 2:
            self.given_correct_answer()
        else:
            self.given_wrong_answer(2)

    def on_button_4(self):
        if self.correct == 3:
            self.given_correct_answer()
        else:
            self.given_wrong_answer(3)

    def given_correct_answer(self):
        self.button_list[self.correct].configure(background='green')
        self.root.update()
        time.sleep(1)
        self.setup_question()

    def given_wrong_answer(self, clicked):
        self.button_list[clicked].configure(background='red')
        self.button_list[self.correct].configure(background='green')
        self.root.update()
        time.sleep(1)
        self.setup_question()


if __name__ == '__main__':
    window = Window()
