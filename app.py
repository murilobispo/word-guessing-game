import tkinter as tk
from tkinter import messagebox

secretWord = 'APPLE'
blank = ' ' * len(secretWord)
print(blank)

attempts = 6
guess_number = 0
selected_letter = 0
dark_mode = True
c = "#818384" if dark_mode == True else "FFFFFF"

def keyboard_press(e):
    input = e.keysym
    if input == 'BackSpace': validade_key("⌫")
    elif input == 'Return' : validade_key("ENTER")
    else:
        input = e.char
        if input.isalpha():
            validade_key(input.upper())

def virtual_keyboard_press(e):
    input = e.widget["text"]
    validade_key(input)

def validade_input():
    global guess_number, selected_letter
    aux_Word = list(secretWord)
    guesses_letters = []
    green = "#538d4e"
    orange = "#b59f3b"

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

#
#
root = tk.Tk()
root.title("Word Guessing Game")
root.geometry("500x650+100+80")
root.config(bg="grey", background="#1D1D1D")
root.minsize(500, 650)

root.update_idletasks()
root_width = root.winfo_width()

#root.resizable(False, False)
#root.iconbitmap('local-icon')
#
#

menu_bar = tk.Menu(root)

menu_options = tk.Menu(menu_bar, tearoff=0)
menu_options.add_command(label="Restart")
menu_options.add_command(label="Toggle Mode")
menu_options.add_separator()
menu_options.add_command(label="Exit", command= root.quit)

menu_help = tk.Menu(menu_bar, tearoff=0)
menu_help.add_command(label="About")
menu_help.add_command(label="Github")

menu_bar.add_cascade(label="Options", menu=menu_options)
menu_bar.add_cascade(label="Options", menu=menu_help)

root.config(menu=menu_bar)

#
#

main= tk.Frame(root, background=root["bg"])
main.pack(expand=True)

guesses = tk.Frame(main, background=root["bg"], width=300, height=350)
guesses.pack()
guesses.pack_propagate(False)
guesses.grid_propagate(False)

guesses_labels = [[] for _ in range(attempts)]

for i in range(attempts):
    for j in range(len(secretWord)):
        frame = tk.Frame(master=guesses,
                         background=root["bg"],
                         highlightbackground="grey",
                        highlightthickness=1)
        frame.grid(row=i, column=j, sticky="nsew", padx=2, pady=2)
        frame.grid_propagate(False) # Se o frame fosse grid
        frame.pack_propagate(False) # Como o Label dentro dele usa pack, usamo
        guesses.grid_rowconfigure(i, weight=1)
        guesses.grid_columnconfigure(j, weight=1)
        lbl = tk.Label(frame,text=" ", 
                       background=root["bg"], 
                       font=("Segoe UI", 20, "bold"),
                       fg="white")
        lbl.pack(expand=True)
        guesses_labels[i].append(lbl)

#
#

keyboard = tk.Frame(main, background=root["bg"], width=root_width, height=201)
keyboard.pack(pady=(29,0))
keyboard.pack_propagate(False)

keys_value = [
    {"Q": c, "W": c, "E": c, "R": c, "T": c, "Y": c, "U": c, "I": c, "O": c, "P": c},
    {"A": c, "S": c, "D": c, "F": c, "G": c, "H": c, "J": c, "K": c, "L": c},
    {"ENTER": c, "Z": c, "X": c, "C": c, "V": c, "B": c, "N": c, "M": c, "⌫": c}
]
keys_default_width = 3

keyboard_rows = []
for i in keys_value:
    frame = tk.Frame(keyboard, background=root["bg"])
    frame.pack(fill="y", expand=True, anchor="center", pady=3)
    keyboard_rows.append(frame)
#keyboard_rows[1].pack_configure(padx=6)

keyboard_keys = []
for i in range(len(keyboard_rows)):
    for j in range(len(keys_value[i])):
        lbl = tk.Label(master=keyboard_rows[i],
                        text=list(keys_value[i].keys())[j],
                        background=list(keys_value[i].values())[j],
                        fg="white",
                        font=("Segoe UI", 16, "bold"),
                        width=keys_default_width,
                       )
        if len(list(keys_value[i].keys())[j]) > 1:
            lbl.configure(width=9, font=("Segoe UI", 9, "bold"))
        if list(keys_value[i].keys())[j] == "⌫":
            lbl.configure(width=6, font=("Segoe UI", 14, "bold"))
        lbl.pack(side="left", fill="y", anchor="center", padx=2)
        lbl.bind("<Button-1>", virtual_keyboard_press)
        if lbl.cget("text") != "ENTER" and lbl.cget("text") != "⌫":
            keyboard_keys.append(lbl)

#
#
root.bind("<Key>", keyboard_press)
root.mainloop()