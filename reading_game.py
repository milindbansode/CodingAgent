import random
import tkinter as tk
from tkinter import messagebox

SENTENCES = [
    "I see a cat.",
    "The sun is hot.",
    "I like my dog.",
    "We can run fast.",
    "The ball is red.",
    "I can hop high.",
    "My mom is kind.",
    "The sky is blue.",
    "I have two eyes.",
    "The fish can swim.",
    "I like to read.",
    "The bird can sing.",
    "I see a big tree.",
    "My hat is green.",
    "We play at school.",
    "The cake is sweet.",
    "I have a toy car.",
    "The moon is bright.",
    "My shoes are clean.",
    "I can clap my hands.",
    "The duck says quack.",
    "I drink warm milk.",
    "The frog can jump.",
    "I love my family.",
    "The bus is yellow.",
    "I can tie my shoe.",
    "The bee is small.",
    "I see a little bug.",
    "My book is fun.",
    "I can draw a star.",
    "The rain is wet.",
    "I like red apples.",
    "The cow eats grass.",
    "I can count to ten.",
    "My bed is soft.",
    "The fox is quick.",
    "I can jump rope.",
    "The bear is big.",
    "My hands are warm.",
    "I can zip my coat.",
    "The kite can fly.",
    "I like to smile.",
    "The cup is full.",
    "My dad can cook.",
    "I see a green leaf.",
    "The ant is tiny.",
    "I can wash my hands.",
    "The star can shine.",
    "I like to paint.",
    "My friend is nice.",
    "The chair is brown.",
    "I can read this.",
    "The snail is slow.",
    "I hear a loud bell.",
    "My socks are blue.",
    "The pig likes mud.",
    "I can open the door.",
    "The lamb is soft.",
    "I can tap my feet.",
    "My lunch is yummy.",
    "The owl is awake.",
    "I can close my eyes.",
    "The crab walks sideways.",
    "I like my class.",
    "The fan is on.",
    "I can throw a ball.",
    "My pencil is sharp.",
    "The boat can float.",
    "I can bounce a ball.",
    "The goat can climb.",
    "I like soft music.",
    "My coat is warm.",
    "The hen has eggs.",
    "I can fold paper.",
    "The seed will grow.",
    "I like to help.",
    "My room is neat.",
    "The wind can blow.",
    "I can feed my pet.",
    "The jam is sweet.",
    "I like clean water.",
    "My cup is pink.",
    "The baby can laugh.",
    "I can stack blocks.",
    "The road is long.",
    "I like sunny days.",
    "My bag is light.",
    "The peach is soft.",
    "I can skip and hop.",
    "The bell rings loud.",
    "I like small books.",
    "My star is bright.",
    "The hill is steep.",
    "I can pet the cat.",
    "The soup is warm.",
    "I like my teacher.",
    "My smile is big.",
    "The clock can tick.",
    "I can read more.",
    "The stars are far.",
]


class ReadingGameApp:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Balloon Reading Game")
        self.root.geometry("520x420")
        self.root.configure(bg="#dff7ff")

        self.child_name = ""
        self.score = 0
        self.sentence_pool = []

        self.name_label = tk.Label(
            root,
            text="Enter your name:",
            font=("Arial", 14, "bold"),
            bg="#dff7ff",
        )
        self.name_label.pack(pady=(20, 8))

        self.name_entry = tk.Entry(root, font=("Arial", 14), justify="center")
        self.name_entry.pack()

        self.start_button = tk.Button(
            root,
            text="Start Game",
            font=("Arial", 12, "bold"),
            command=self.start_game,
            bg="#71c7ff",
        )
        self.start_button.pack(pady=10)

        self.greeting_label = tk.Label(
            root,
            text="Type your name and press Start!",
            font=("Arial", 14),
            bg="#dff7ff",
        )
        self.greeting_label.pack(pady=10)

        self.balloon_button = tk.Button(
            root,
            text="🎈 Click Balloon 🎈",
            font=("Arial", 22, "bold"),
            command=self.show_sentence_popup,
            bg="#ff7db8",
            fg="white",
            state=tk.DISABLED,
            width=18,
            height=2,
        )
        self.balloon_button.pack(pady=20)

        self.score_label = tk.Label(
            root,
            text="Sticker Score: 0 ⭐",
            font=("Arial", 16, "bold"),
            bg="#dff7ff",
        )
        self.score_label.pack(pady=10)

    def start_game(self) -> None:
        name = self.name_entry.get().strip()
        if not name:
            messagebox.showwarning("Name needed", "Please type your name first.")
            return

        self.child_name = name
        self.score = 0
        self.sentence_pool = []
        self.score_label.config(text="Sticker Score: 0 ⭐")
        self.greeting_label.config(text=f"Hi {self.child_name}! Click the balloon to read.")
        self.balloon_button.config(state=tk.NORMAL)

    def _next_sentence(self) -> str:
        if not self.sentence_pool:
            self.sentence_pool = SENTENCES.copy()
            random.shuffle(self.sentence_pool)
        return self.sentence_pool.pop()

    def show_sentence_popup(self) -> None:
        sentence = self._next_sentence()
        self.balloon_button.config(state=tk.DISABLED)

        popup = tk.Toplevel(self.root)
        popup.title("Read this sentence")
        popup.geometry("440x260")
        popup.configure(bg="#fff9d8")

        def close_popup() -> None:
            self.balloon_button.config(state=tk.NORMAL)
            popup.destroy()

        popup.protocol("WM_DELETE_WINDOW", close_popup)

        text = tk.Label(
            popup,
            text=f"{self.child_name}, read this:\n\n{sentence}",
            font=("Arial", 16, "bold"),
            bg="#fff9d8",
            wraplength=380,
            justify="center",
        )
        text.pack(pady=(20, 12))

        popup_score = tk.Label(
            popup,
            text=f"Sticker Score: {self.score} ⭐",
            font=("Arial", 14),
            bg="#fff9d8",
        )
        popup_score.pack(pady=6)

        cheer_label = tk.Label(popup, text="", font=("Arial", 12, "bold"), bg="#fff9d8")
        cheer_label.pack(pady=4)

        def earn_sticker() -> None:
            self.score += 1
            self.score_label.config(text=f"Sticker Score: {self.score} ⭐")
            popup_score.config(text=f"Sticker Score: {self.score} ⭐")
            cheer_label.config(text="Great reading! You earned a sticker! 🎉")
            sticker_button.config(state=tk.DISABLED)

        sticker_button = tk.Button(
            popup,
            text="I read it! Get sticker ⭐",
            font=("Arial", 12, "bold"),
            command=earn_sticker,
            bg="#8be28b",
        )
        sticker_button.pack(pady=10)

        close_button = tk.Button(
            popup,
            text="Close",
            font=("Arial", 11),
            command=close_popup,
        )
        close_button.pack(pady=(4, 12))


def main() -> None:
    root = tk.Tk()
    ReadingGameApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
