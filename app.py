import tkinter as tk
from tkinter import messagebox
from requests import get
import sys
import os



config_language = "EN"
attempts = 6
guess_number = 0
selected_letter = 0
dark_mode = True
win = False
game_over = False
c = "#818384" if dark_mode == True else "FFFFFF"

def request_word():
    response = get("https://random-word-api.herokuapp.com/word?length=5&lang=en")
    if response.status_code == 200:
        secretWord = response.json()[0].upper()
    else:
        secretWord = 'APPLE'
    print(secretWord)
    return secretWord

def restart_app():
    root.destroy()
    os.execl(sys.executable, sys.executable, *sys.argv)   

def virtual_keyboard_press(e):
    if win or game_over:
        return
    input = e.widget["text"]
    validade_key(input)

def keyboard_press(e):
    if win or game_over:
        return
    input = e.keysym
    if input == 'BackSpace': validade_key("⌫")
    elif input == 'Return' : validade_key("ENTER")
    else:
        input = e.char
        if input.isalpha():
            validade_key(input.upper())

def validade_key(input):
    global selected_letter
    match input:
        case "ENTER":
            if guesses_labels[guess_number][len(secretWord) - 1].cget("text").isalpha():
                validade_input()
            else:
                messagebox.showwarning("", "Not enough letters")

        case "⌫":
            if selected_letter == 4 and not guesses_labels[guess_number][selected_letter].cget("text") == ' ' :
                guesses_labels[guess_number][selected_letter].configure(text=' ')
            elif 0 < selected_letter < len(secretWord):
                selected_letter -= 1
                guesses_labels[guess_number][selected_letter].configure(text=' ')
        case _:
            if selected_letter < len(secretWord) and guesses_labels[guess_number][selected_letter].cget("text") == ' ':
                guesses_labels[guess_number][selected_letter].configure(text=input)
                if selected_letter < len(secretWord) - 1:
                    selected_letter += 1    
def end_game():
    lbl = tk.Label(root, fg="black", bg="white")
    width = 100
    if game_over:
        lbl.config(text=secretWord, font=("Segoe UI", 14, "bold"))
    if win:
        match guess_number:
            case 1:
                end_message = "Genius"
            case 2:
                end_message = "Magnificent"
                width = 120
            case 3:
                end_message = "Impressive"
                width = 120
            case 4:
                end_message = "Splendid"
                width = 110
            case 5:
                end_message = "Great"
            case 6:
                end_message = "Phew"

        lbl.config(
            text=end_message,
            font=("Segoe UI", 12, "bold"),
            fg="black",
            bg="white"
        )

    lbl.place(relx=0.5, rely=0.06, anchor="center", width=width, height=45)
    root.after(4000, lbl.destroy)

def validade_input():
    global guess_number, selected_letter, win, game_over
    aux_Word = list(secretWord)
    guesses_letters = []

    for letter in guesses_labels[guess_number]:
        guesses_letters.append(letter.cget("text"))
    
    for i in range(len(guesses_letters)): 
        if guesses_letters[i] == aux_Word[i]: 
            guesses_labels[guess_number][i].master.configure(bg = "#538d4e") 
            guesses_labels[guess_number][i].configure(bg = "#538d4e")
            for key in keyboard_keys: 
                if key.cget("text") == guesses_letters[i]: 
                    key.configure(bg = "#538d4e") 
                    keyboard_keys.remove(key) 
            guesses_letters[i] = None 
            aux_Word[i] = None 
    
    if all(letter is None for letter in guesses_letters):
        win = True
    
    for i in range(len(guesses_letters)): 
        if guesses_letters[i] is not None and guesses_letters[i] in aux_Word: 
            guesses_labels[guess_number][i].master.configure(bg = "#b59f3b") 
            guesses_labels[guess_number][i].configure(bg = "#b59f3b")
            idx = aux_Word.index(guesses_letters[i])
            for key in keyboard_keys: 
                if key.cget("text") == guesses_letters[i]: 
                    key.configure(bg = "#b59f3b") 
            aux_Word[idx] = None 
            guesses_letters[i] = None 

    for i in range(len(guesses_letters)): 
        if guesses_letters[i] is not None: 
            guesses_labels[guess_number][i].master.configure(bg = "#3a3a3c")
            guesses_labels[guess_number][i].configure(bg = "#3a3a3c") 
            for key in keyboard_keys: 
                if key.cget("text") == guesses_letters[i]: 
                    key.configure(bg = "#3a3a3c") 
                    keyboard_keys.remove(key)          
    guess_number += 1
    selected_letter = 0

    if guess_number == attempts:
        game_over = True
    if game_over or win:
        end_game()
def create_menu_bar(parent, language):
    menu_bar = tk.Menu(parent)
    parent.config(menu=menu_bar)

    menu_options = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="Options", menu=menu_options)
    menu_options.add_command(label="Restart", command=restart_app)
    menu_languages = tk.Menu(menu_options, tearoff=0)
    menu_options.add_cascade(label="Language", menu=menu_languages)
    menu_languages.add_radiobutton(label="EN", value="EN", variable=language)
    menu_languages.add_radiobutton(label="PT-BR", value="PT-BR", variable=language)
    menu_options.add_command(label="Toggle Mode")
    menu_options.add_separator()
    menu_options.add_command(label="Exit", command=parent.quit)

    menu_help = tk.Menu(menu_bar, tearoff=0)
    menu_help.add_command(label="About")
    menu_help.add_command(label="Github")
    menu_bar.add_cascade(label="Help", menu=menu_help)

def create_guess_section(parent, attempts, secretWord, bg_color):
    guesses = tk.Frame(parent, background=bg_color, width=300, height=350)
    guesses.pack()
    guesses.pack_propagate(False)
    guesses.grid_propagate(False)

    guesses_labels = [[] for _ in range(attempts)]

    for i in range(attempts):
        for j in range(len(secretWord)):
            frame = tk.Frame(master=guesses,
                            background=bg_color,
                            highlightbackground="grey",
                            highlightthickness=1)
            frame.grid(row=i, column=j, sticky="nsew", padx=2, pady=2)
            frame.grid_propagate(False)
            frame.pack_propagate(False)
            guesses.grid_rowconfigure(i, weight=1)
            guesses.grid_columnconfigure(j, weight=1)
            lbl = tk.Label(frame,text=" ", 
                        background=bg_color, 
                        font=("Segoe UI", 20, "bold"),
                        fg="white")
            lbl.pack(expand=True)
            guesses_labels[i].append(lbl)
    return guesses, guesses_labels


def create_keyboard_section(parent, root_width , bg_color, bg_key_color):
    keyboard = tk.Frame(parent, background=bg_color, width=root_width, height=201)
    keyboard.pack(pady=(29,0))
    keyboard.pack_propagate(False)

    keys_value = [
        ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
        ["A", "S", "D", "F", "G", "H", "J", "K", "L"],
        ["ENTER", "Z", "X", "C", "V", "B", "N", "M", "⌫"]
    ]
    keys_default_width = 3

    keyboard_rows = []
    for i in keys_value:
        frame = tk.Frame(keyboard, background=bg_color)
        frame.pack(fill="y", expand=True, anchor="center", pady=3)
        keyboard_rows.append(frame)

    keyboard_keys = []
    for i, row in enumerate(keys_value):
        for key in row:
            lbl = tk.Label(master=keyboard_rows[i],
                            text=key,
                            background=bg_key_color,
                            fg="white",
                            font=("Segoe UI", 16, "bold"),
                            width=keys_default_width,
                        )
            if len(key) > 1:
                lbl.configure(width=9, font=("Segoe UI", 9, "bold"))
            if key == "⌫":
                lbl.configure(width=6, font=("Segoe UI", 14, "bold"))
            lbl.pack(side="left", fill="y", anchor="center", padx=2)
            lbl.bind("<Button-1>", virtual_keyboard_press)
            if lbl.cget("text") != "ENTER" and lbl.cget("text") != "⌫":
                keyboard_keys.append(lbl)
    return keyboard, keyboard_rows, keyboard_keys

#
secretWord = request_word()

root = tk.Tk()
language = tk.StringVar(value=config_language)
root.title("Word Guessing Game")
root.geometry("500x650+100+80")
root.config(bg="grey", background="#1D1D1D")
root.minsize(500, 650)

root.update_idletasks()
root_width = root.winfo_width()

main= tk.Frame(root, background=root["bg"])
main.pack(expand=True)

create_menu_bar(root, language)
guesses, guesses_labels = create_guess_section(main, attempts, secretWord, root["bg"]) 
keyboard, keyboard_rows, keyboard_keys = create_keyboard_section(main, root_width, root["bg"], c)

root.bind("<Key>", keyboard_press)
root.mainloop()
#