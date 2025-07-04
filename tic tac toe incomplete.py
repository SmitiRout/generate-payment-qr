import tkinter as tk   #tkinter is a standard library used to make GUI in python. Its helps to create the  buttons , window , icone etc.
from tkinter import messagebox #messagebox used to tell the status of the game

# Now we will create a function which will check after clicking button each time whether someone has won or not.
# we will create list of 8 combinations , if one of the combo matches the winner will win. these combinations are 3 vertical , 3 horizontal  , 2 diagonal lines)

##buttons will be created in a pattern 012
                                    345
                            678 
##

# we will check in loop the combo of this button , if in any combo the text is same , we will make the bg of button green and relct the message box as user won.

def check_winner():
    for combo in[(0,1,2,), (3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]:
        if buttons[combo[0]]["text"] == buttons[combo[1]]["text"] == buttons[combo[2]]["text"] !="":
            button[combo[0]].config(bg="green")
            button[combo[1]].config(bg="green")
            button[combo[2]].config(bg="green")
            messagebox.showinfo("Tic-Tac-Toe",f"Player {buttons[combo[0]]['text']} wins!")
            root.quit()
          
def button_click(index):
    if buttons[index]["text"] ==  
