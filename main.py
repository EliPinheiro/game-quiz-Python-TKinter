from data import datas
from tkinter import *
from tkinter import messagebox
import random

from defs import Def

# defs= Def()
quest = 1
game_running = False
lista_escolhas = []
lista_radio_buttons = []
n = 0
contador = 1
score = 0

def try_user():
    global entry_name
    if entry_name.get() == '':
        messagebox.showerror(title='error',message='No name was given')
    else:
        start()
def start():
    global user_name, game_running, label_name
    user_name = entry_name.get()
    entry_name.destroy()
    label_name.destroy()
    start_buttom.place_forget()
    questions()

def final_page():
    global next_buttom, question,user_name,score
    number_question.place_forget()
    result_label = Label(window,text=f'{user_name.capitalize()} ser resultado é :',font='Arial 20')
    result_label.place(x=120,y=220)

    score_label = Label(window,text=f'{score}/10',font='Arial 40')
    score_label.place(x=220,y=350)







def next():
    global correct, X , n, contador, question, escolhas,lista_radio_buttons,next_buttom,score
    number_question.place_forget()
    next_buttom.place_forget()
    lista_escolhas.clear()

    if correct == X.get():
        score += 1
    n += 1
    contador +=1
    question.destroy()
    for butons in lista_radio_buttons:
        butons.place_forget()

    lista_radio_buttons.clear()
    if contador < 11:

        questions()

    else:
        final_page()

#
def questions():

    global X, correct, question,escolhas,lista_radio_buttons, next_buttom,number_question
    number_question = Label(window,font=('Arial', 15), text=f'Question {contador}')
    number_question.place(x=195, y=170)
    numberOfScreenUnits = 480
    question = Label(window,font=('Arial 15'),text=datas[n]['question'],wraplength=numberOfScreenUnits)
    question.place(x=20,y=220)
    print(contador)

    next_buttom = Button(window,text='NEXT ->',command=next)
    next_buttom.place(x=400,y=550)


    for perguntas in datas:
        if datas[n] == perguntas:
            for key,value in perguntas.items():
                if key == "incorrect_answers":
                    lista_escolhas.extend(value)
                if key == "correct_answer":
                    correct = value
                    lista_escolhas.append(value)
                random.shuffle(lista_escolhas)

    X = StringVar()
    for index in range(len(lista_escolhas)):
        escolhas = Radiobutton(window,font=('Arial',20),
                                text=lista_escolhas[index],
                                variable=X,
                                value=lista_escolhas[index])


        if index == 0:
            escolhas.place(x=120,y=300)
            escolhas.select()
        if index == 1:
            escolhas.place(x=120,y=350)


        if index == 2:
            escolhas.place(x=120,y=400)

        if index == 3:
            escolhas.place(x=120,y=450)

        lista_radio_buttons.append(escolhas)



### creat the window
window = Tk()
window.title('Quiz game')
window.config(bg='purple')
window.geometry('500x600')
icon = PhotoImage(file='icon_quiz_game.png')
window.iconphoto(True, icon)

### first window
image_title = PhotoImage(file='title quiz game.png')
image_start = PhotoImage(file='start buttom.png')
title = Label(image=image_title).pack()
label_name = Label(window,text='Digite seu nome',bg='purple',fg='white',font='Arial 20')
label_name.pack()
entry_name = Entry(font=('Arial',40),width=11,bg='black',fg='green')
entry_name.place(x=93, y=200)
start_buttom = Button(image=image_start,command=try_user)
start_buttom.place(x=100, y=400)


window.update()

window.mainloop()
