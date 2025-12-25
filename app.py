import tkinter as tk
import json
from tkinter import messagebox
from requests import get
import sys
import os

attempts = 6
guess_number = 0
selected_letter = 0
win = False
game_over = False
config_file = "config.json"
lang_file  = "lang.json"
correct_color = "#538d4e"
close_color   = "#b59f3b"
wrong_color   = "#3a3a3c"

def load_config(file_path):
    with open(file_path, "r") as f:
        config = json.load(f)
    return config

def load_lang(config, file_path):
    LANG = config.get("language", "en")
    with open(file_path, "r", encoding="utf-8") as f:
        LANG_DATA = json.load(f)
    TEXTS = LANG_DATA[LANG]
    return LANG, TEXTS, LANG_DATA

def change_lang(*args ,file_path="config.json"):
    global lang, texts
    new_lang = lang_menu.get()
    if new_lang == lang:
        return
    with open(file_path, "r", encoding="utf-8") as f:
        config = json.load(f)
    config["language"] = new_lang
    restart_req =  messagebox.askyesno( texts["restart"]["title"], texts["restart"]["dialog"])
    with open(file_path, "w") as f:
        json.dump(config, f, indent=4)
    if restart_req: restart_game()

def restart_game():
    root.quit()
    root.destroy()
    os.execl(sys.executable, sys.executable, *sys.argv) 
    
def toggle_theme():
    config["dark_theme"] = not config.get("dark_theme", True)
    with open("config.json", "w") as f:
        json.dump(config, f, indent=4)
    apply_theme(config)
        
def apply_theme(config):
    theme = config.get("dark_theme", True)

    bg_color  = "#1D1D1D" if theme else "#FFFFFF"
    fg_color  = "#FFFFFF" if theme else "#000000"
    key_color = "#AAAAAA" if theme else "#d3d6da"

    root.config(bg=bg_color)
    main.config(bg=bg_color)
    guesses.config(bg=bg_color)
    keyboard.config(bg=bg_color)
    for row in keyboard_rows:
        row.config(bg=bg_color)
    for key in keyboard_keys:
        if key.cget("bg") != close_color:
            key.config(bg=key_color, fg=fg_color)
    for i in range(guess_number, len(guesses_labels)):
        for j in range(len(secretWord)):
            guesses_labels[i][j].master.configure(bg=bg_color) 
            guesses_labels[i][j].configure(bg=bg_color, fg=fg_color)

    return theme

def request_word(lang = "en"):
    url = "https://random-word-api.herokuapp.com/word?length=5&lang=" + lang
    response = get(url)
    if response.status_code == 200:
        secretWord = response.json()[0].upper()
    else:
        secretWord = 'APPLE'
    print(secretWord)
    return secretWord

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
    if game_over:
        end_message = secretWord
    if win:
        end_message = texts["end_msg"][f"guess{guess_number}"]

    lbl.config(
        text=end_message,
        font=("Segoe UI", 14, "bold"),
        fg="black",
        bg="white",
        padx=10,
        pady=5
    )

    lbl.place(relx=0.5, rely=0.06, anchor="center")
    root.after(4000, lbl.destroy)

def validade_input():
    global guess_number, selected_letter, win, game_over
    aux_Word = list(secretWord)
    guesses_letters = []

    for letter in guesses_labels[guess_number]:
        guesses_letters.append(letter.cget("text"))
    
    for i in range(len(guesses_letters)): 
        if guesses_letters[i] == aux_Word[i]: 
            guesses_labels[guess_number][i].master.configure(bg=correct_color) 
            guesses_labels[guess_number][i].configure(bg=correct_color, fg="white")
            for key in keyboard_keys: 
                if key.cget("text") == guesses_letters[i]: 
                    key.configure(bg=correct_color, fg="white") 
                    keyboard_keys.remove(key) 
            guesses_letters[i] = None 
            aux_Word[i] = None 
    
    if all(letter is None for letter in guesses_letters):
        win = True
    
    for i in range(len(guesses_letters)): 
        if guesses_letters[i] is not None and guesses_letters[i] in aux_Word: 
            guesses_labels[guess_number][i].master.configure(bg=close_color) 
            guesses_labels[guess_number][i].configure(bg=close_color, fg="white")
            idx = aux_Word.index(guesses_letters[i])
            for key in keyboard_keys: 
                if key.cget("text") == guesses_letters[i]: 
                    key.configure(bg=close_color, fg="white") 
            aux_Word[idx] = None 
            guesses_letters[i] = None 

    for i in range(len(guesses_letters)): 
        if guesses_letters[i] is not None: 
            guesses_labels[guess_number][i].master.configure(bg = wrong_color)
            guesses_labels[guess_number][i].configure(bg=wrong_color, fg="white") 
            for key in keyboard_keys: 
                if key.cget("text") == guesses_letters[i]: 
                    key.configure(bg=wrong_color, fg="white") 
                    keyboard_keys.remove(key)          
    guess_number += 1
    selected_letter = 0

    if guess_number == attempts:
        game_over = True
    if game_over or win:
        end_game()

def create_menu_bar(parent, lang_menu):
    menu_bar = tk.Menu(parent)
    parent.config(menu=menu_bar)

    menu_options = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label=texts["menu_title"]["options"], menu=menu_options)
    menu_options.add_command(label=texts["menu_1"]["restart"], command=restart_game)
    menu_languages = tk.Menu(menu_options, tearoff=0)
    menu_options.add_cascade(label=texts["menu_1"]["language"], menu=menu_languages)
    for lang_code in lang_data.keys():
        menu_languages.add_radiobutton(label=lang_code.upper(), value=lang_code, variable=lang_menu)
    lang_menu.trace_add("write", change_lang)
    menu_options.add_command(label=texts["menu_1"]["theme"], command=toggle_theme)
    menu_options.add_separator()
    menu_options.add_command(label=texts["menu_1"]["exit"], command=parent.quit)

    menu_help = tk.Menu(menu_bar, tearoff=0)
    menu_help.add_command(label=texts["menu_2"]["about"])
    menu_help.add_command(label=texts["menu_2"]["github"])
    menu_bar.add_cascade(label=texts["menu_title"]["help"], menu=menu_help)

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

def create_keyboard_section(parent, root_width , bg_color):
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
                            fg="white",
                            font=("Segoe UI", 16, "bold"),
                            width=keys_default_width,
                        )
            if len(key) > 1:
                lbl.configure(width=8, font=("Segoe UI", 10, "bold"))
            if key == "⌫":
                lbl.configure(width=6, font=("Segoe UI", 14, "bold"))
            lbl.pack(side="left", fill="y", anchor="center", padx=2)
            lbl.bind("<Button-1>", virtual_keyboard_press)
            keyboard_keys.append(lbl)
    return keyboard, keyboard_rows, keyboard_keys
#
config = load_config(config_file)
lang, texts, lang_data = load_lang(config, lang_file)
secretWord = request_word(lang,)

root = tk.Tk()
root.title("Word Guessing Game")
root.geometry("500x650+100+80")
root.config()
root.minsize(500, 650)
root.update_idletasks()
root_width = root.winfo_width()

main = tk.Frame(root, background=root["bg"])
main.pack(expand=True)

lang_menu = tk.StringVar(value=lang)
create_menu_bar(root, lang_menu)
guesses, guesses_labels = create_guess_section(main, attempts, secretWord, root["bg"]) 
keyboard, keyboard_rows, keyboard_keys = create_keyboard_section(main, root_width, root["bg"])

apply_theme(config)
root.bind("<Key>", keyboard_press)

root.mainloop()
#