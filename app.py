import tkinter as tk
from tkinter import ttk

secretWord = 'APPLE'
blank = ' ' * len(secretWord)
print(blank)

attempts = 6
root = tk.Tk()

root.title("Word Guessing Game")
root.geometry("500x650")
root.config(bg="grey")
root.minsize(500, 700)

root.update_idletasks()
root_width = root.winfo_width()
#root.resizable(False, False)

#root.maxsize("600x700")
#root.state('zoomed')
#root.iconbitmap('local-icon')

#def f(event):
#    print("pressed:", event.keysym)

#root.bind("<Key>", f)

header = tk.Frame(root, background="green", height=50)
header.pack(fill="x", side="top")
header.pack_propagate(False)

h1 = tk.Label(
    master=header, 
    text="1 Word",
    font=("Arial", 20),
    background="red",
    foreground="white",
    anchor="center"
)
h1.pack(expand=True)

##
main= tk.Frame(root, background="blue")
main.pack(expand=True)

guesses = tk.Frame(main, background="darkgray", width=350, height=400)
guesses.pack()
guesses.pack_propagate(False)

keyboard = tk.Frame(main, background="red", width=root_width, height=201)
keyboard.pack(pady=(29,0))
keyboard.pack_propagate(False)



keys_value =[   ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
                ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L'],
                ['ENTER', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', 'BS']
            ]

keyboard_rows = []
for i in keys_value:
    frame = tk.Frame(keyboard)
    frame.pack(fill="both", expand=True, pady=4)
    keyboard_rows.append(frame)
keyboard_rows[1].pack_configure(padx=6)

for i in range(len(keyboard_rows)):
    for j in range(len(keys_value[i])):
        lbl = tk.Label(master=keyboard_rows[i],
                       text=keys_value[i][j],
                        relief="solid"
                        
                       )
        lbl.pack(side="left", expand=True, fill="both", padx=2)

#for i, row in enumerate(keys_value):
    #row_frame = tk.Frame(keyboard, bg="white")
    #row_frame.pack()
    #for j, value in enumerate(row):
        #lbl = tk.Label(row_frame, text=value, background="green", width=4, height=4)
       # lbl.grid(row=i, column=j)

##
footer= tk.Frame(root, background="orange", height=20)
footer.pack(fill="x", side="bottom")
footer.pack_propagate(False)

a = tk.Label(
    master=footer,
    text="murilobispo",
    background="purple",
    anchor="center"
)
a.pack(expand=True)
##

root.mainloop()