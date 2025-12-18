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
h1.pack(expand=True)
##

##
main= tk.Frame(root, background="blue")
main.pack(expand=True)

guesses = tk.Frame(main, background="darkgray", width=350, height=400)
guesses.pack()
guesses.pack_propagate(False)

keyboard = tk.Frame(main, background="red", width=root_width, height=200)
keyboard.pack(pady=(30,0))
keyboard.pack_propagate(False)

keys_value = [['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
              ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L'],
              ['ENTER', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', 'BS']
                ]

#for i, row in enumerate(keys_value):
    #row_frame = tk.Frame(keyboard, bg="white")
    #row_frame.pack(pady=2)
    #for value in row:
       # lbl = tk.Label(row_frame, text=value, background="green", width=5, height=2)
        #lbl.pack(side="left", padx=2)



        
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