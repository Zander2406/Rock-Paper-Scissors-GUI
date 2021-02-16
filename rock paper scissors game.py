from tkinter import *
from PIL import Image, ImageTk
import os
import random
root = Tk()
root.title("Rock Paper Scissors Game")
root.geometry("700x500")

os.chdir(r"Moves")
wins = {'Rock': 'Scissors', 'Paper': 'Rock', 'Scissors': 'Paper'}
loses = {'Rock': 'Paper', 'Paper': 'Scissors', 'Scissors': 'Rock'}
draws = {'Rock': 'Rock', 'Paper': 'Paper', 'Scissors': 'Scissors'}
Player_Score = 0
Computer_Score = 0


# Updating pictures of the moves, scores and who won
def play_game(Player_Move):
    global Player_Score, Computer_Score
    game_moves = ['Rock', 'Paper', 'Scissors']
    # Computer_Move = random.choice(game_moves)
    # Prefer to use the randint method because somehow choice gives me same choice too often
    Computer_Move = game_moves[random.randint(0, 2)]
    if Computer_Move == wins.get(Player_Move):
        Player_Score += 1
        PScore_Label.config(text=str(Player_Score))
        Winner_Label.config(text="You Win!")
        Computer_Photo_Raw = Image.open(Computer_Move + ".png")
        Player_Photo_Raw = Image.open(Player_Move + ".png")
        Computer_Photo_Raw = Computer_Photo_Raw.resize((150, 150), Image.ANTIALIAS)
        Player_Photo_Raw = Player_Photo_Raw.resize((150, 150), Image.ANTIALIAS)
        Computer_Photo = ImageTk.PhotoImage(Computer_Photo_Raw)
        Player_Photo = ImageTk.PhotoImage(Player_Photo_Raw)
        CLabel = Label(root, image=Computer_Photo)
        CLabel.image = Computer_Photo
        CLabel.place(relx=0.71, rely=0.3)
        PLabel = Label(root, image=Player_Photo)
        PLabel.image = Player_Photo
        PLabel.place(relx=0.07, rely=0.3)
    elif Computer_Move == loses.get(Player_Move):
        Computer_Score += 1
        CScore_Label.config(text=str(Computer_Score))
        Winner_Label.config(text="You Lose!")
        Computer_Photo_Raw = Image.open(Computer_Move + ".png")
        Player_Photo_Raw = Image.open(Player_Move + ".png")
        Computer_Photo_Raw = Computer_Photo_Raw.resize((150, 150), Image.ANTIALIAS)
        Player_Photo_Raw = Player_Photo_Raw.resize((150, 150), Image.ANTIALIAS)
        Computer_Photo = ImageTk.PhotoImage(Computer_Photo_Raw)
        Player_Photo = ImageTk.PhotoImage(Player_Photo_Raw)
        CLabel = Label(root, image=Computer_Photo)
        CLabel.image = Computer_Photo
        CLabel.place(relx=0.71, rely=0.3)
        PLabel = Label(root, image=Player_Photo)
        PLabel.image = Player_Photo
        PLabel.place(relx=0.07, rely=0.3)
    else:
        Player_Score += 1
        Computer_Score += 1
        PScore_Label.config(text=str(Player_Score))
        CScore_Label.config(text=str(Computer_Score))
        Winner_Label.config(text="Draw!")
        Computer_Photo_Raw = Image.open(Computer_Move + ".png")
        Player_Photo_Raw = Image.open(Player_Move + ".png")
        Computer_Photo_Raw = Computer_Photo_Raw.resize((150, 150), Image.ANTIALIAS)
        Player_Photo_Raw = Player_Photo_Raw.resize((150, 150), Image.ANTIALIAS)
        Computer_Photo = ImageTk.PhotoImage(Computer_Photo_Raw)
        Player_Photo = ImageTk.PhotoImage(Player_Photo_Raw)
        CLabel = Label(root, image=Computer_Photo)
        CLabel.image = Computer_Photo
        CLabel.place(relx=0.71, rely=0.3)
        PLabel = Label(root, image=Player_Photo)
        PLabel.image = Player_Photo
        PLabel.place(relx=0.07, rely=0.3)


# Frames with scores and winner
PScore_Frame = Frame(root, height=50, width=50)
CScore_Frame = Frame(root, height=50, width=50)
PScore_Frame.place(relx=0.15, rely=0.05)
CScore_Frame.place(relx=0.79, rely=0.05)
PScore_Frame.pack_propagate(False)
CScore_Frame.pack_propagate(False)
Winner_Frame = Frame(root, height=50, width=100)
Winner_Frame.place(relx=0.43, rely=0.05)
Winner_Frame.pack_propagate(False)
# Labels with which side is which
Label(root, text="Player: ").place(relx=0.15, rely=0.2)
Label(root, text="Computer: ").place(relx=0.78, rely=0.2)
# Image of Computer Move
Computer_Move_Image_Raw = Image.open('All.png')
Computer_Move_Image_Raw = Computer_Move_Image_Raw.resize((150, 150), Image.ANTIALIAS)
Computer_Move_Image = ImageTk.PhotoImage(Computer_Move_Image_Raw)
Computer_Image = Label(root, image=Computer_Move_Image)
Computer_Image.place(relx=0.71, rely=0.3)
# Image of Player Move
Player_Move_Image_Raw = Image.open('All.png')
Player_Move_Image_Raw = Player_Move_Image_Raw.resize((150, 150), Image.ANTIALIAS)
Player_Move_Image = ImageTk.PhotoImage(Player_Move_Image_Raw)
Player_Image = Label(root, image=Player_Move_Image)
Player_Image.place(relx=0.07, rely=0.3)
# Buttons for choice
Rock_Button = Button(root, text="Rock", height=2, width=10, command=lambda: play_game("Rock"))
Paper_Button = Button(root, text="Paper", height=2, width=10, command=lambda: play_game("Paper"))
Scissors_Button = Button(root, text="Scissors", height=2, width=10, command=lambda: play_game("Scissors"))
Rock_Button.place(relx=0.2, rely=0.8)
Paper_Button.place(relx=0.47, rely=0.8)
Scissors_Button.place(relx=0.7, rely=0.8)
# Labels with scores and winner
PScore_Label = Label(PScore_Frame, text=str(Player_Score), font=40)
PScore_Label.place(x=25, y=25, anchor="center")
CScore_Label = Label(CScore_Frame, text=str(Computer_Score), font=40)
CScore_Label.place(x=25, y=25, anchor="center")
Winner_Label = Label(Winner_Frame, text="Start!", font=70)
Winner_Label.place(x=50, y=25, anchor="center")





root.mainloop()