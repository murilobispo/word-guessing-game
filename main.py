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
root.minsize(500, 650)

#root.maxsize("600x700")
#root.state('zoomed')
#root.iconbitmap('local-icon')

#def f(event):
#    print("pressed:", event.keysym)

#root.bind("<Key>", f)

##
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
h1.pack(expand=True )
##

##
main= tk.Frame(root, background="blue")
main.pack(fill="both", expand=True)
main.grid_columnconfigure(0, weight=1)   
main.grid_columnconfigure(1, weight=3)   
main.grid_columnconfigure(2, weight=1)   
main.grid_rowconfigure(0, weight=60)
main.grid_rowconfigure(1, weight=40)

letters_section= tk.Label(master=main, background="grey")
letters_section.grid(row=0, column=1, sticky="nsew")
#letters_grid = []

for i in range(0, attempts):
    for j in range(0, len(secretWord)):
        box = tk.Label(
            master=letters_section,
            text=secretWord[j], 
            background="purple")
        box.grid(row=i, column=j, sticky="nsew", pady=2, padx=2)
        letters_section.grid_rowconfigure(i, weight=1)
        letters_section.grid_columnconfigure(j, weight=1)

keyboard_section= tk.Label(master=main, background="yellow")
keyboard_section.grid(row=1, column=0, sticky="nsew", columnspan=3)
##

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