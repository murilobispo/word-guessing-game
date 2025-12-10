import tkinter as tk
from tkinter import ttk

secretWord = 'APPLE'
blank = ' ' * len(secretWord)
print(blank)

attempts = 6
root = tk.Tk()

root.title("Word Guessing Game")
root.geometry("500x700")
root.config(bg="grey")
root.resizable(False,False)
#root.maxsize("600x700")
#root.mminsize("400x500")
#root.state('zoomed')
#root.iconbitmap('local-icon')

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

letters_grid = tk.Label(master=main, background="grey")
letters_grid.grid(row=0, column=1, sticky="nsew")


keyboard_grid = tk.Label(master=main, background="yellow")
keyboard_grid.grid(row=1, column=0, sticky="nsew", columnspan=3)

main.grid_rowconfigure(0, weight=70)
main.grid_rowconfigure(1, weight=30)

main.grid_columnconfigure(0, weight=1)   
main.grid_columnconfigure(1, weight=3)   
main.grid_columnconfigure(2, weight=1)   
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