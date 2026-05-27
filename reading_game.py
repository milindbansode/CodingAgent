import random
import tkinter as tk
from tkinter import messagebox


SENTENCES = [
    "I see a cat.",
    "The dog is big.",
    "I can jump.",
    "The sun is hot.",
    "I like red.",
    "We can run.",
    "The bird can fly.",
    "I have a hat.",
    "The ball is blue.",
    "I can clap.",
    "My mom is kind.",
    "My dad is funny.",
    "I eat an apple.",
    "The frog is green.",
    "I can hop.",
    "The fish can swim.",
    "I see the moon.",
    "The star is bright.",
    "I like to read.",
    "We play at home.",
    "The cup is full.",
    "I have two shoes.",
    "The tree is tall.",
    "I can sing.",
    "The car is fast.",
    "I see a bee.",
    "The bee is small.",
    "I like my bed.",
    "The book is new.",
    "I can draw.",
    "The sky is blue.",
    "I eat warm soup.",
    "The kite is high.",
    "I can smile.",
    "The duck is yellow.",
    "I hear the bell.",
    "The bell is loud.",
    "I like soft rain.",
    "The sock is clean.",
    "I can count to ten.",
    "The cow says moo.",
    "I have a toy.",
    "The toy is fun.",
    "I can dance.",
    "The goat can jump.",
    "I see a boat.",
    "The boat is white.",
    "I like warm milk.",
    "The bread is soft.",
    "I can wave.",
    "The fox is quick.",
    "I see a clock.",
    "The clock can tick.",
    "I like to help.",
    "The dish is round.",
    "I can zip my coat.",
    "The coat is red.",
    "I see a flower.",
    "The flower smells nice.",
    "I like my class.",
    "The map is big.",
    "I can write my name.",
    "The pen is black.",
    "I see a train.",
    "The train is long.",
    "I like cool water.",
    "The chair is brown.",
    "I can open the door.",
    "The door is wide.",
    "I see a snail.",
    "The snail is slow.",
    "I like my school.",
    "The rug is soft.",
    "I can close my eyes.",
    "The leaf is green.",
    "I see a cloud.",
    "The cloud is gray.",
    "I like to share.",
    "The spoon is small.",
    "I can tie my shoe.",
    "The shoe is black.",
    "I see a plane.",
    "The plane is loud.",
    "I like my friend.",
    "The friend is kind.",
    "I can sit still.",
    "The bell rings now.",
    "I see a rabbit.",
    "The rabbit is soft.",
    "I like sunny days.",
    "The day is bright.",
    "I can wash my hands.",
    "The soap is clean.",
    "I see a pencil.",
    "The pencil is sharp.",
    "I like to paint.",
    "The paint is wet.",
    "I can read this line.",
    "The line is easy.",
    "I am a good reader.",
]


class ReadingGame:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Balloon Reading Game")
        self.root.geometry("640x520")
        self.root.configure(bg="#f0f8ff")

        self.kid_name = tk.StringVar()
        self.score = 0
        self.available_sentences = []
        self.current_sentence = ""

        self._build_name_screen()

    def _build_name_screen(self) -> None:
        frame = tk.Frame(self.root, bg="#f0f8ff")
        frame.pack(expand=True)

        tk.Label(
            frame,
            text="Welcome to the Reading Balloon Game!",
            font=("Arial", 20, "bold"),
            bg="#f0f8ff",
            fg="#2a4d69",
        ).pack(pady=20)

        tk.Label(
            frame,
            text="What is your name?",
            font=("Arial", 14),
            bg="#f0f8ff",
        ).pack(pady=10)

        tk.Entry(frame, textvariable=self.kid_name, font=("Arial", 14), justify="center").pack(
            pady=10
        )

        tk.Button(
            frame,
            text="Start Game",
            font=("Arial", 13, "bold"),
            bg="#ff8fab",
            fg="white",
            activebackground="#ff5d8f",
            command=self._start_game,
            padx=12,
            pady=8,
        ).pack(pady=20)

    def _start_game(self) -> None:
        name = self.kid_name.get().strip()
        if not name:
            messagebox.showinfo("Name needed", "Please type your name first.")
            return

        for widget in self.root.winfo_children():
            widget.destroy()

        self.available_sentences = SENTENCES.copy()
        random.shuffle(self.available_sentences)

        top_bar = tk.Frame(self.root, bg="#f0f8ff")
        top_bar.pack(fill="x", pady=(12, 2), padx=16)

        self.welcome_label = tk.Label(
            top_bar,
            text=f"Great job, {name}! Click the balloon to read.",
            font=("Arial", 14, "bold"),
            bg="#f0f8ff",
            fg="#2a4d69",
        )
        self.welcome_label.pack(side="left")

        self.score_label = tk.Label(
            top_bar,
            text="Stickers: 0",
            font=("Arial", 14, "bold"),
            bg="#f0f8ff",
            fg="#ec407a",
        )
        self.score_label.pack(side="right")

        self.canvas = tk.Canvas(self.root, width=640, height=420, bg="#cdeffd", highlightthickness=0)
        self.canvas.pack(fill="both", expand=True)

        self.balloon = self.canvas.create_oval(225, 70, 415, 290, fill="#ff6fae", outline="#e91e63", width=4)
        self.canvas.create_line(320, 290, 320, 390, fill="#7a5c61", width=3)
        self.canvas.create_text(
            320,
            180,
            text="Click\nMe!",
            fill="white",
            font=("Arial", 28, "bold"),
        )

        self.canvas.tag_bind(self.balloon, "<Button-1>", self._show_sentence_popup)

    def _next_sentence(self) -> str:
        if not self.available_sentences:
            self.available_sentences = SENTENCES.copy()
            random.shuffle(self.available_sentences)
        return self.available_sentences.pop()

    def _show_sentence_popup(self, _event=None) -> None:
        self.current_sentence = self._next_sentence()

        popup = tk.Toplevel(self.root)
        popup.title("Read this sentence")
        popup.geometry("500x320")
        popup.configure(bg="#fff9e6")
        popup.transient(self.root)
        popup.grab_set()

        tk.Label(
            popup,
            text=f"{self.kid_name.get()}, read this:",
            font=("Arial", 14, "bold"),
            bg="#fff9e6",
            fg="#5d4037",
        ).pack(pady=(20, 10))

        tk.Label(
            popup,
            text=self.current_sentence,
            font=("Arial", 26, "bold"),
            bg="#fff9e6",
            fg="#1e3a5f",
            wraplength=460,
            justify="center",
        ).pack(pady=(0, 25))

        tk.Label(
            popup,
            text="Pick a sticker:",
            font=("Arial", 12, "bold"),
            bg="#fff9e6",
        ).pack()

        buttons = tk.Frame(popup, bg="#fff9e6")
        buttons.pack(pady=10)

        tk.Button(
            buttons,
            text="⭐ Star",
            font=("Arial", 12, "bold"),
            bg="#ffd166",
            command=lambda: self._give_sticker(popup),
            padx=8,
            pady=6,
        ).pack(side="left", padx=8)

        tk.Button(
            buttons,
            text="🌈 Rainbow",
            font=("Arial", 12, "bold"),
            bg="#a2d2ff",
            command=lambda: self._give_sticker(popup),
            padx=8,
            pady=6,
        ).pack(side="left", padx=8)

        tk.Button(
            buttons,
            text="🎉 Wow",
            font=("Arial", 12, "bold"),
            bg="#cdb4db",
            command=lambda: self._give_sticker(popup),
            padx=8,
            pady=6,
        ).pack(side="left", padx=8)

    def _give_sticker(self, popup: tk.Toplevel) -> None:
        self.score += 1
        self.score_label.config(text=f"Stickers: {self.score}")
        popup.destroy()


def main() -> None:
    root = tk.Tk()
    ReadingGame(root)
    root.mainloop()


if __name__ == "__main__":
    main()
