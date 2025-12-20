import tkinter as tk

secretWord = 'APPLE'
blank = ' ' * len(secretWord)
print(blank)

attempts = 6

def click(e):
    input = e.widget["text"]
    if input == "⌫":
        print("Backspace")
    elif input == "ENTER":
        print("Enter")
    else:
        print(input)


root = tk.Tk()
root.title("Word Guessing Game")
root.geometry("500x650+100+80")
root.config(bg="grey")
root.minsize(500, 600)

root.update_idletasks()
root_width = root.winfo_width()

#root.resizable(False, False)
#root.iconbitmap('local-icon')

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
main= tk.Frame(root, background="blue")
main.pack(expand=True)

guesses = tk.Frame(main, background="darkgray", width=350, height=400)
guesses.pack()
guesses.pack_propagate(False)

keyboard = tk.Frame(main, background="red", width=root_width, height=201)
keyboard.pack(pady=(29,0))
keyboard.pack_propagate(False)

dark_mode = True
c = "#A1A1A1" if dark_mode == True else "FFFFFF"

keys_value = [
    {"Q": c, "W": c, "E": c, "R": c, "T": c, "Y": c, "U": c, "I": c, "O": c, "P": c},
    {"A": c, "S": c, "D": c, "F": c, "G": c, "H": c, "J": c, "K": c, "L": c},
    {"ENTER": c, "Z": c, "X": c, "C": c, "V": c, "B": c, "N": c, "M": c, "⌫": c}
]
keys_default_width = 3

keyboard_rows = []
for i in keys_value:
    frame = tk.Frame(keyboard, background="yellow")
    frame.pack(fill="y", expand=True, anchor="center", pady=3)
    keyboard_rows.append(frame)
#keyboard_rows[1].pack_configure(padx=6)

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
            lbl.configure(width=7, font=("Segoe UI", 11, "bold"))
        if list(keys_value[i].keys())[j] == "⌫":
            lbl.configure(width=5)
        lbl.pack(side="left", fill="y", anchor="center", padx=2)
        lbl.bind("<Button-1>", click)
##

root.mainloop()