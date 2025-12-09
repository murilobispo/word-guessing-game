import tkinter as tk
from tkinter import ttk

secretWord = 'APPLE'
blank = ' ' * len(secretWord)
print(blank)

attempts = 6
root = tk.Tk()

root.title("Word Guessing Game")
root.geometry("500x600")
root.config(bg="grey")
#root.maxsize("600x700")
#root.mminsize("400x500")
#root.resizable(False,False)
#root.state('zoomed')
#root.iconbitmap('local-icon')

##
header = tk.Frame(root, background="green", height=60)
header.pack(fill="x", side="top")
header.pack_propagate(False)

h1 = tk.Label(
    master=header, 
    text="1 Word",
    font=("Arial", 30),
    background="red",
    foreground="white",
    anchor="center"
)
h1.pack(expand=True )
##

##
main= tk.Frame(root, background="blue")
main.pack(fill="both", expand=True)
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