import random as r
import tkinter as tk
import mysql.connector as my
from pygame import mixer as m
from math import sqrt,pow,ceil

user=''
pwd=''
db=''

m.init()
sound_button= m.Sound("supportfile/ButtonClick.wav")
overall_volume=1
connect=my.connect(host ='localhost',user=user,passwd=pwd,database=db)
def check_score(game_number):
    global score,total_score,overall_total_score,current_login,cur
    cur=connect.cursor()
    cur.execute('select * from userpwd where status="Y"')
    current_login=cur.fetchall() 
    try:
        print(current_login)
        current_login=current_login[0][0]
        cur.execute('select * from leaderboard where username="'+str(current_login)+'"')
        total_score=cur.fetchall()
        overall_total_score=int(total_score[0][11])
        total_score=int(total_score[0][game_number])
        score=0
    except:
        current_login=None
        score=total_score=0
        overall_total_score=0
    finally:
        cur.close()
def sound_player(sound_object,closer=None):
    if overall_volume==1:
        sound_object.play()
    if closer!=None:
        closer.destroy()
def gamemenu():
    global game,cur
    game='m'
    quote_num=r.randint(0,36)
    cur=connect.cursor()
    cur.execute('select * from quote')
    current_quote_author=cur.fetchall()[quote_num]
    cur.close()
    current_quote=current_quote_author[0]
    current_author=current_quote_author[1]
    temp_list=current_quote.split()
    current_quote=''
    c=0
    for i in temp_list: 
        try:
            i=i.replace('?','\'')
        except:
            pass
        current_quote+=i+' '
        c+=len(i+' ')
        if c>75:
            current_quote+='\n'
            c=0
    def unmutemute():
        sound_player(sound_button)
        global overall_volume
        if overall_volume==0:
            overall_volume=1
            button_unmutemute.configure(image=tk_photoimage_unmute)
        elif overall_volume==1:
            overall_volume=0
            button_unmutemute.configure(image=tk_photoimage_mute)
    def mainmenu(GAME):
        sound_player(sound_button)
        global game
        game=GAME
        screen.after(500,screen.destroy)
    screen=tk.Tk()
    screen.attributes('-fullscreen',True)
    screen.focus_force()
    tk_photoimage_background=tk.PhotoImage(file='supportfile/MainMenuBG.png')
    label_background=tk.Label(text='HAPPY GAMES\nMAIN MENU\n\n\n\n\n\n\n\n\n\n\n',font=('Copperplate Gothic Bold',35,'bold'),compound='c',image=tk_photoimage_background,fg='white')
    label_background.place(x=0,y=0)
    label_quote=tk.Label(text=current_quote,font=('Copperplate Gothic Bold',17),bg='white',fg='red')
    label_quote.place(x=683-640,y=647,width=1280,height=56)
    label_author=tk.Label(text='---'+current_author,font=('Copperplate Gothic Bold',16),bg='white',fg='red')
    label_author.place(x=683+320,y=707,width=320)
    tk_photoimage_HC=tk.PhotoImage(file='supportfile/GAME\\HC.png')
    tk_photoimage_TTT=tk.PhotoImage(file='supportfile/GAME\\TTT.png')
    tk_photoimage_RPS=tk.PhotoImage(file='supportfile/GAME\\RPS.png')
    tk_photoimage_SAL=tk.PhotoImage(file='supportfile/GAME\\SAL.png')
    tk_photoimage_HM=tk.PhotoImage(file='supportfile/GAME\\HM.png')
    tk_photoimage_MATH=tk.PhotoImage(file='supportfile/GAME\\MATH.png')
    tk_photoimage_NG=tk.PhotoImage(file='supportfile/GAME\\NG.png')
    tk_photoimage_QE=tk.PhotoImage(file='supportfile/GAME\\QE.png')
    tk_photoimage_MEM=tk.PhotoImage(file='supportfile/GAME\\MEM.png')
    tk_photoimage_TR=tk.PhotoImage(file='supportfile/GAME\\TR.png')
    tk_photoimage_U=tk.PhotoImage(file='supportfile/GAME\\U.png')
    tk_photoimage_BL=tk.PhotoImage(file='supportfile/GAME\\BL.png')
    tk_photoimage_mute=tk.PhotoImage(file='supportfile/Mute.png')
    tk_photoimage_unmute=tk.PhotoImage(file='supportfile/Unmute.png')
    button_game1=tk.Button(text="Tic Tac Toe",image=tk_photoimage_TTT,bg='#00ffff',activebackground='#00ffff',font=('Copperplate Gothic Bold',20),compound='top',command=lambda:mainmenu('a'))
    button_game1.place(x=683-320-320,y=135+30,height=160,width=320)
    button_game2=tk.Button(text="Rock,Paper,Scissors",image=tk_photoimage_RPS,bg='#e205e2',activebackground='#e205e2',font=('Copperplate Gothic Bold',18),compound='top',command=lambda:mainmenu('b'))
    button_game2.place(x=683-320,y=135+30,height=160,width=320)
    button_game3=tk.Button(text="Snakes and ladders",image=tk_photoimage_SAL,bg='white',fg='#660500',activeforeground='#660500',activebackground='white',font=('Copperplate Gothic Bold',20),compound='top',command=lambda:mainmenu('c'))
    button_game3.place(x=683,y=135+30,height=160,width=320)
    button_game4=tk.Button(text='Handcricket',image=tk_photoimage_HC,bg='#c3c3c3',activebackground='#c3c3c3',font=('Copperplate Gothic Bold',20),compound='top',command=lambda:mainmenu('d'))
    button_game4.place(x=683+320,y=135+30,height=160,width=320)
    button_game5=tk.Button(text='Quadratic Equation',image=tk_photoimage_QE,bg='#9c0000',fg='#0245ff',activeforeground='#0245ff',activebackground='#9c0000',font=('Copperplate Gothic Bold',20),compound='top',command=lambda:mainmenu('e'))
    button_game5.place(x=683-320-320,y=135+160+30,height=160,width=320)
    button_game6=tk.Button(text='Cards',image=tk_photoimage_BL,bg='#00ff00',fg='#333333',activeforeground='#333333',activebackground='#00ff00',font=('Copperplate Gothic Bold',20),compound='top',command=lambda:mainmenu('f'))
    button_game6.place(x=683-320,y=135+160+30,height=160,width=320)
    button_game7=tk.Button(text='Memory Game',image=tk_photoimage_MEM,bg='#040345',fg='white',activeforeground='white',activebackground='#040345',font=('Copperplate Gothic Bold',20),compound='top',command=lambda:mainmenu('g'))
    button_game7.place(x=683,y=135+160+30,height=160,width=320) 
    button_game8=tk.Button(text='Hangman',image=tk_photoimage_HM,bg='#ff0077',fg='white',activeforeground='white',activebackground='#ff0077',font=('Copperplate Gothic Bold',20),compound='top',command=lambda:mainmenu('h'))
    button_game8.place(x=683+320,y=135+160+30,height=160,width=320)
    button_game9=tk.Button(text="Guess the Integer",image=tk_photoimage_NG,bg='#ffa200',fg='#21277c',activeforeground='#21277c',activebackground='#ffa200',font=('Copperplate Gothic Bold',20),compound='top',command=lambda:mainmenu('i'))
    button_game9.place(x=683-320-320,y=135+160+160+30,height=160,width=320)
    button_game10=tk.Button(text='Leaderboard',image=tk_photoimage_TR,bg='#0d0d0d',fg='#e0ae17',activeforeground='#e0ae17',activebackground='#0d0d0d',font=('Copperplate Gothic Bold',20),compound='top',command=lambda:mainmenu('j'))
    button_game10.place(x=683-320,y=135+160+160+30,height=160,width=320)
    button_game11=tk.Button(text='User Status',image=tk_photoimage_U,bg='#948039',activebackground='#948039',font=('Copperplate Gothic Bold',20),compound='top',command=lambda:mainmenu('k'))
    button_game11.place(x=683,y=135+160+160+30,height=160,width=320)
    button_game12=tk.Button(text='Math Game',image=tk_photoimage_MATH,bg='#ffff00',activebackground='#ffff00',font=('Copperplate Gothic Bold',20),compound='top',command=lambda:mainmenu('l'))
    button_game12.place(x=683+320,y=135+160+160+30,height=160,width=320)
    button_quit=tk.Button(text="QUIT",font=('Copperplate Gothic Bold',20,'bold'),command=lambda:mainmenu('m'),fg='red',bg='white',activeforeground='red',activebackground='white')
    button_quit.place(x=683+460,y=90,height=60,width=180)
    button_unmutemute=tk.Button(command=unmutemute,bg='white',activebackground='white')
    button_unmutemute.place(x=683+390,y=90,height=60,width=60)
    cur=connect.cursor()
    cur.execute('select * from userpwd where status="Y"')
    try:
        current_login='\n'+cur.fetchall()[0][0]
    except:
        current_login=''
    cur.close()
    label_login=tk.Label(text='HEY THERE%s'%(current_login),font=(None,18,'bold'),bg='white',fg='red')
    label_login.place(x=683-640,y=90,width=320,height=60)
    if overall_volume==0:
        button_unmutemute.configure(image=tk_photoimage_mute)
    else:
        button_unmutemute.configure(image=tk_photoimage_unmute)
    screen.mainloop()
def widgets_text(text,list_widgets):
    for i in range(len(list_widgets)):
        list_widgets[i].configure(text=text[i])
def widgets_state(state,list_widgets):
    for i in list_widgets:
        i.configure(state=state)
def widgets_destroy(list_widgets,event=None):
    for i in list_widgets:
        i.destroy()

while True:
    gamemenu()
    if game=='a':
        check_score(1)
        screen=tk.Tk()
        screen.attributes('-fullscreen',True)
        screen.focus_force()
        list_pieces=['','','','','','','','','']
        time_taken_pc=[2000,3000,1000,500,1500,2500]
        def fun_diff(x):
            global difficulty
            label_diff.configure(text='\n\n\n\n\n\n\n\n\n%s Level'%(x))
            difficulty=x
        def fun_start(x):
            global starter
            label_start.configure(text='\n\n\n\n\n\n\n\n\n%s goes first'%(x))
            starter=x
        def game_start():
            sound_player(sound_button)
            global starter,difficulty,list_pieces,list_available,playing_chance,win,increment,decrement
            win=False
            try:
                print(starter)
            except:
                starter='User'
            try:
                print(difficulty)
            except:
                difficulty='Easy'
            if difficulty=='Easy':
                increment=1
                decrement=-1
            else:
                if starter=='User':
                    increment=3
                else:
                    increment=5
                decrement=0
            playing_chance=starter
            list_pieces=['','','','','','','','','']
            list_available=[0,1,2,3,4,5,6,7,8]
            button_start.destroy()
            label_game.configure(text='%s is thinking\n\n\n\n\n\n\n\n\n\n\n'%(starter))
            widgets_state('disabled',[button_start_pc,button_start_user,button_diff_easy,button_diff_hard])
            widgets_state('normal',[but0,but1,but2,but3,but4,but5,but6,but7,but8])
            if playing_chance=='PC':
                screen.after(r.choice(time_taken_pc),pc_move)
        def final(parameter):
            global but0,but1,but2,but3,but4,but5,but6,but7,but8,label_game,button_repeat,label_total_score,total_score,score
            widgets_state('disabled',[but0,but1,but2,but3,but4,but5,but6,but7,but8])
            if parameter=='Tie':
                label_game.configure(text='It is a tie\n\n\n\n\n\n\n\n\n\n\n')
            else:
                label_game.configure(text='%s has won\n\n\n\n\n\n\n\n\n\n\n'%(parameter))
                if parameter=='PC':
                    sound_final=m.Sound('supportfile/Loss1.wav')
                if parameter=='User':
                    sound_final=m.Sound('supportfile/Win.wav')
                sound_player(sound_final)
            print(current_login)
            if current_login!=None:
                label_total_score.configure(text='Total Score\n%s\nScore this session\n%s'%(total_score,score))
            button_repeat=tk.Button(text='Continue',bg='black',fg='lime',font=('Copperplate gothic bold',20,'bold'),command=delete_objects)
            button_repeat.place(x=800,y=630,height=50)
        def delete_objects():
            global but0,but1,but2,but3,but4,but5,but6,but7,but8,button_diff_easy,button_diff_hard,button_start_pc,button_start_user,label_game,button_repeat,button_start
            widgets_text(['','','','','','','','',''],[but0,but1,but2,but3,but4,but5,but6,but7,but8])
            label_game.configure(text='TIC TAC TOE\n\n\n\n\n\n\n\n\n\n\n')
            widgets_state('normal',[button_start_pc,button_start_user,button_diff_easy,button_diff_hard])
            button_start=tk.Button(text='Start',bg='black',fg='lime',font=('Copperplate gothic bold',20,'bold'),command=game_start)
            button_start.place(x=833,y=630,height=50)
            button_repeat.destroy()
        def user_move(x):
            global starter,difficulty,list_pieces,list_available,playing_chance,label_game,win,score,total_score
            if playing_chance=='User':
                user_input=x
                if user_input in list_available:
                    list_pieces[user_input]='X'
                    widgets_text(list_pieces,[but0,but1,but2,but3,but4,but5,but6,but7,but8])
                    list_available.remove(user_input)
                    playing_chance='PC'
                    if list_pieces[0]==list_pieces[3]==list_pieces[6]=='X' or list_pieces[1]==list_pieces[4]==list_pieces[7]=='X'or list_pieces[2]==list_pieces[5]==list_pieces[8]=='X' :
                        score+=increment
                        win=True
                        total_score+=increment
                        final('User')
            
                    elif list_pieces[0]==list_pieces[1]==list_pieces[2]=='X' or list_pieces[3]==list_pieces[4]==list_pieces[5]=='X' or list_pieces[6]==list_pieces[7]==list_pieces[8]=='X':    
                        score+=increment
                        total_score+=increment
                        win=True
                        final('User')
                        
                    elif list_pieces[2]==list_pieces[4]==list_pieces[6]=='X' or list_pieces[0]==list_pieces[4]==list_pieces[8]=='X':
                        score+=increment
                        total_score+=increment
                        win=True
                        final('User')
                        
                    elif '' not in list_pieces:            
                        win=True
                        final('Tie')
                    if win==False:
                        screen.after(r.choice(time_taken_pc),pc_move)
                        label_game.configure(text='%s is thinking\n\n\n\n\n\n\n\n\n\n\n'%(playing_chance))
                        
        def pc_move():
            global playing_chance,difficulty,list_available,list_available,label_game,score,total_score,win
            try:
                pc_input=r.choice(list_available)
            except:
                print()
            if difficulty=='Hard':
                for i in list_available:
                    copy=list(list_pieces)
                    copy[i]='X'
                    if copy[0]==copy[3]==copy[6]=='X' or copy[1]==copy[4]==copy[7]=='X'or copy[2]==copy[5]==copy[8]=='X' or copy[2]==copy[4]==copy[6]=='X' or copy[0]==copy[4]==copy[8]=='X' or copy[0]==copy[1]==copy[2]=='X' or copy[3]==copy[4]==copy[5]=='X' or copy[6]==copy[7]==copy[8]=='X':
                        pc_input=i
                        break
                for i in list_available:
                    copy=list(list_pieces)
                    copy[i]='O'
                    if copy[0]==copy[3]==copy[6]=='O' or copy[1]==copy[4]==copy[7]=='O'or copy[2]==copy[5]==copy[8]=='O' or copy[2]==copy[4]==copy[6]=='O' or copy[0]==copy[4]==copy[8]=='O' or copy[0]==copy[1]==copy[2]=='O' or copy[3]==copy[4]==copy[5]=='O' or copy[6]==copy[7]==copy[8]=='O':
                        pc_input=i
                        break
            if win==False:
                list_pieces[pc_input]='O'
                widgets_text(list_pieces,[but0,but1,but2,but3,but4,but5,but6,but7,but8])
                list_available.remove(pc_input)
                playing_chance='User'
                label_game.configure(text='%s is thinking\n\n\n\n\n\n\n\n\n\n\n'%(playing_chance))
            if list_pieces[0]==list_pieces[3]==list_pieces[6]=='O' or list_pieces[1]==list_pieces[4]==list_pieces[7]=='O'or list_pieces[2]==list_pieces[5]==list_pieces[8]=='O' :
                score+=decrement
                total_score+=decrement
                win=True
                final('PC')
            elif list_pieces[0]==list_pieces[1]==list_pieces[2]=='O' or list_pieces[3]==list_pieces[4]==list_pieces[5]=='O' or list_pieces[6]==list_pieces[7]==list_pieces[8]=='O':
                score+=decrement
                total_score+=decrement
                win=True
                final('PC')        
            elif list_pieces[2]==list_pieces[4]==list_pieces[6]=='O' or list_pieces[0]==list_pieces[4]==list_pieces[8]=='O':
                score+=decrement
                total_score+=decrement
                win=True
                final('PC')
            elif '' not in list_pieces:
                win=True
                final('Tie')

        tk_photoimage_start=tk.PhotoImage(file='supportfile/Tic Tac Toe\\Start.png')
        tk_photoimage_diff=tk.PhotoImage(file='supportfile/Tic Tac Toe\\Diff.png')
        tk_photoimage_game=tk.PhotoImage(file='supportfile/Tic Tac Toe\\Game.png')
        tk_photoimage_diff_hard=tk.PhotoImage(file='supportfile/Tic Tac Toe\\Hard.png')
        tk_photoimage_diff_easy=tk.PhotoImage(file='supportfile/Tic Tac Toe\\Easy.png')
        tk_photoimage_start_user=tk.PhotoImage(file='supportfile/Tic Tac Toe\\Human.png')
        tk_photoimage_start_pc=tk.PhotoImage(file='supportfile/Tic Tac Toe\\Robot.png')

        label_diff=tk.Label(text='\n\n\n\n\n\n\n\n\nEasy Level',image=tk_photoimage_diff,bg='black',fg='white',compound='c',font=('Copperplate gothic bold',20,'bold'))
        label_diff.place(x=0,y=0)
        label_start=tk.Label(text='\n\n\n\n\n\n\n\n\nUser goes first',image=tk_photoimage_start,bg='black',fg='white',compound='c',font=('Copperplate gothic bold',20,'bold'))
        label_start.place(x=0,y=386)
        label_game=tk.Label(text='TIC TAC TOE\n\n\n\n\n\n\n\n\n\n\n',image=tk_photoimage_game,font=('Copperplate gothic bold',35,'bold'),fg='white',bg='black',compound='c')
        label_game.place(x=400,y=0)

        button_start=tk.Button(text='Start',bg='black',fg='lime',font=('Copperplate gothic bold',20,'bold'),command=game_start)
        button_start.place(x=833,y=630,height=50)
        button_quit=tk.Button(text='Quit',bg='black',fg='red',font=('Copperplate gothic bold',20,'bold'),command=lambda:sound_player(sound_button,screen))
        button_quit.place(x=843,y=685,height=50)

        button_diff_hard=tk.Button(text='',image=tk_photoimage_diff_hard,bg='white',compound='c',font=('Copperplate gothic bold',20,'bold'),command=lambda:fun_diff('Hard'))
        button_diff_hard.place(x=210,y=150,width=100)
        button_diff_easy=tk.Button(text='',image=tk_photoimage_diff_easy,bg='white',compound='c',font=('Copperplate gothic bold',20,'bold'),command=lambda:fun_diff('Easy'))
        button_diff_easy.place(x=80,y=150,width=100)
        button_start_pc=tk.Button(text='',image=tk_photoimage_start_pc,bg='white',compound='c',font=('Copperplate gothic bold',20,'bold'),command=lambda:fun_start('PC'))
        button_start_pc.place(x=210,y=536,width=100)
        button_start_user=tk.Button(text='',image=tk_photoimage_start_user,bg='white',compound='c',font=('Copperplate gothic bold',20,'bold'),command=lambda:fun_start('User'),)
        button_start_user.place(x=80,y=536,width=100)

        but0=tk.Button(text=list_pieces[0],fg='white',bg='black',font=('Copperplate gothic bold',50,'bold'),state='disabled',command=lambda: user_move(0))
        but1=tk.Button(text=list_pieces[1],fg='white',bg='black',font=('Copperplate gothic bold',50,'bold'),state='disabled',command=lambda: user_move(1))
        but2=tk.Button(text=list_pieces[2],fg='white',bg='black',font=('Copperplate gothic bold',50,'bold'),state='disabled',command=lambda: user_move(2))
        but3=tk.Button(text=list_pieces[3],fg='white',bg='black',font=('Copperplate gothic bold',50,'bold'),state='disabled',command=lambda: user_move(3))
        but4=tk.Button(text=list_pieces[4],fg='white',bg='black',font=('Copperplate gothic bold',50,'bold'),state='disabled',command=lambda: user_move(4))
        but5=tk.Button(text=list_pieces[5],fg='white',bg='black',font=('Copperplate gothic bold',50,'bold'),state='disabled',command=lambda: user_move(5))
        but6=tk.Button(text=list_pieces[6],fg='white',bg='black',font=('Copperplate gothic bold',50,'bold'),state='disabled',command=lambda: user_move(6))
        but7=tk.Button(text=list_pieces[7],fg='white',bg='black',font=('Copperplate gothic bold',50,'bold'),state='disabled',command=lambda: user_move(7))
        but8=tk.Button(text=list_pieces[8],fg='white',bg='black',font=('Copperplate gothic bold',50,'bold'),state='disabled',command=lambda: user_move(8))

        but0.place(x=668,y=161,height=145,width=145)
        but1.place(x=814,y=161,height=145,width=145)
        but2.place(x=960,y=161,height=145,width=145)
        but3.place(x=668,y=307,height=146,width=145)
        but4.place(x=814,y=307,height=146,width=145)
        but5.place(x=960,y=307,height=146,width=145)
        but6.place(x=668,y=454,height=145,width=145)
        but7.place(x=814,y=454,height=145,width=145)
        but8.place(x=960,y=454,height=145,width=145)
        print(current_login)
        if current_login!=None:
            label_total_score=tk.Label(text='Total Score\n%s\nScore this round\n%s'%(total_score,score),font=('copperplate gothic bold',15,'bold'),fg='purple',bg='white')
            label_total_score.place(x=1115,y=35,width=220)
        screen.mainloop()
        try:
            overall_total_score+=score
            connect=my.connect(host ='localhost',user=user,passwd=pwd,database=db)
            cur=connect.cursor()
            cur.execute('update leaderboard set tictactoe='+str(total_score)+',overall='+str(overall_total_score)+' where username="'+str(current_login)+'"')
            print('update leaderboard set tictactoe='+str(total_score)+',overall='+str(overall_total_score)+' where username="'+str(current_login)+'"')
            connect.commit()
        except:
            print(current_login)
    elif game=='b':

        screen=tk.Tk()
        screen.attributes('-fullscreen',True)
        screen.focus_force()
        pc_moves=['Rock','Paper','Scissors']
        check_score(2)
        list_history=['','','','','']
        tk_photoimage_location=tk.PhotoImage(file='supportfile/Rock Paper Scissors\\Location.png')
        tk_photoimage_history=tk.PhotoImage(file='supportfile/Rock Paper Scissors\\History.png')
        tk_photoimage_game=tk.PhotoImage(file='supportfile/Rock Paper Scissors\\Game.png')
        label_location=tk.Label(image=tk_photoimage_location)
        label_location.place(x=0,y=0)
        label_game=tk.Label(text='ROCK,PAPER,SCISSORS\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n',image=tk_photoimage_game,compound='c',font=('Copperplate gothic bold',26,'bold'))
        label_game.place(x=500,y=0)
        label_history=tk.Label(text='THIS ROUND\n\n\n%s\n\n\n%s\n\n\n%s\n\n\n%s\n\n\n%s\n\n'%(list_history[0],list_history[1],list_history[2],list_history[3],list_history[4]),image=tk_photoimage_history,compound='c',font=('Copperplate gothic bold',26,'bold'))
        label_history.place(x=1068,y=0)
        def history_checker():
            global tk_photoimage_pchistory1,tk_photoimage_pchistory2,tk_photoimage_pchistory3,tk_photoimage_pchistory4,tk_photoimage_pchistory5,tk_photoimage_userhistory1,tk_photoimage_userhistory2,tk_photoimage_userhistory3,tk_photoimage_userhistory4,tk_photoimage_userhistory5
            tk_photoimage_userhistory1=tk.PhotoImage(file=list_user_move[0])
            tk_photoimage_userhistory2=tk.PhotoImage(file=list_user_move[1])
            tk_photoimage_userhistory3=tk.PhotoImage(file=list_user_move[2])
            tk_photoimage_userhistory4=tk.PhotoImage(file=list_user_move[3])
            tk_photoimage_userhistory5=tk.PhotoImage(file=list_user_move[4])
            tk_photoimage_pchistory1=tk.PhotoImage(file=list_pc_move[0])
            tk_photoimage_pchistory2=tk.PhotoImage(file=list_pc_move[1])
            tk_photoimage_pchistory3=tk.PhotoImage(file=list_pc_move[2])
            tk_photoimage_pchistory4=tk.PhotoImage(file=list_pc_move[3])
            tk_photoimage_pchistory5=tk.PhotoImage(file=list_pc_move[4])
            user_history1.configure(image=tk_photoimage_userhistory1)
            user_history2.configure(image=tk_photoimage_userhistory2)
            user_history3.configure(image=tk_photoimage_userhistory3)
            user_history4.configure(image=tk_photoimage_userhistory4)
            user_history5.configure(image=tk_photoimage_userhistory5)
            pc_history1.configure(image=tk_photoimage_pchistory1)
            pc_history2.configure(image=tk_photoimage_pchistory2)
            pc_history3.configure(image=tk_photoimage_pchistory3)
            pc_history4.configure(image=tk_photoimage_pchistory4)
            pc_history5.configure(image=tk_photoimage_pchistory5)
            screen.after(500,history_checker)
        def game_start():
            global button_rock,button_pap,button_sci,tk_photoimage_rock,tk_photoimage_pap,tk_photoimage_sci,label_count,count,list_history,list_user_move,list_pc_move,user_history1,user_history2,user_history3,user_history4,user_history5,pc_history1,pc_history2,pc_history3,pc_history4,pc_history5
            sound_player(sound_button)
            button_start.destroy()
            count=1
            tk_photoimage_rock=tk.PhotoImage(file='supportfile/Rock Paper Scissors\\RockButton.png')
            tk_photoimage_pap=tk.PhotoImage(file='supportfile/Rock Paper Scissors\\PaperButton.png')
            tk_photoimage_sci=tk.PhotoImage(file='supportfile/Rock Paper Scissors\\ScissorsButton.png')
            list_history=['','','','','']
            list_pc_move=['supportfile/Rock Paper Scissors\\Container.png']*5
            list_user_move=['supportfile/Rock Paper Scissors\\Container.png']*5
            button_rock=tk.Button(image=tk_photoimage_rock,bg='black',activebackground='black',command=lambda:next_move('Rock'))
            button_pap=tk.Button(image=tk_photoimage_pap,bg='black',activebackground='black',command=lambda:next_move('Paper'))
            button_sci=tk.Button(image=tk_photoimage_sci,bg='black',activebackground='black',command=lambda:next_move('Scissors'))
            button_rock.place(x=500+80,y=425)
            button_pap.place(x=500+87+131,y=425)
            button_sci.place(x=500+94+262,y=425)
                
            user_history1=tk.Label()
            user_history2=tk.Label()
            user_history3=tk.Label()
            user_history4=tk.Label()
            user_history5=tk.Label()
            pc_history1=tk.Label()
            pc_history2=tk.Label()
            pc_history3=tk.Label()
            pc_history4=tk.Label()
            pc_history5=tk.Label()
            l=[user_history1,user_history2,user_history3,user_history4,user_history5,pc_history1,pc_history2,pc_history3,pc_history4,pc_history5]
            placement=[[1250]*5+[1100]*5,[130,245,360,480,600]*2]
            for i in range(len(l)):
                l[i].place(x=placement[0][i],y=placement[1][i])
            history_checker()
            label_count=tk.Label(text='CHANCE 1',font=('Copperplate gothic bold',20,'bold'),bg='black',fg='white')
            label_count.place(x=783-100,y=575,width=200,height=75)
        def next_move(move):
            def finish():
                global button_start,button_finish,label_game,label_history,list_user_move,list_pc_move
                button_finish.destroy()
                label_game.configure(text='ROCK,PAPER,SCISSORS\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
                label_history.configure(text='THIS ROUND\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
                button_start=tk.Button(text='Start',bg='black',fg='lime',font=('Copperplate gothic bold',20,'bold'),command=game_start)
                button_start.place(x=783-70,y=630,height=50,width=140)
                list_pc_move=['supportfile/Rock Paper Scissors\\Container.png']*5
                list_user_move=['supportfile/Rock Paper Scissors\\Container.png']*5
            def clear():
                global button_rock,button_pap,button_sci,tk_photoimage_rock,tk_photoimage_pap,tk_photoimage_sci,label_user_move,label_pc_move,label_pc,label_user,label_winner,button_continue,label_count,count,button_start,button_finish,tk_photoimage_location,label_location,label_history,label_game
                count+=1
                if count==6:
                    button_finish=tk.Button(text='Finish',font=('Copperplate gothic bold',20,'bold'),bg='black',fg='lime',command=finish)
                    button_finish.place(x=500+80,y=425,width=131*3+20,height=136)
                    label_game.configure(text='ROCK,PAPER,SCISSORS\n\n\nHEAD TO HEAD\n\n  PC\tUSER\n'+str(list_history.count('C'))+'\t '+str(list_history.count('U'))+'\n\n\n\n\n\n\n\n\n\n\n')
                    widgets_destroy([label_count,button_rock,button_sci,button_pap])
                else:
                    label_count.configure(text='CHANCE '+str(count))
                    widgets_state('normal',[button_rock,button_sci,button_pap])
                button_continue.destroy()
                tk_photoimage_location=tk.PhotoImage(file='supportfile/Rock Paper Scissors\\Location.png')
                label_location.configure(image=tk_photoimage_location)
                widgets_destroy([label_pc,label_pc_move,label_user,label_user_move,label_winner])

            def check():
                global button_rock,button_pap,button_sci,tk_photoimage_rock,tk_photoimage_pap,tk_photoimage_sci,label_user_move,label_pc_move,label_pc,label_user,label_winner,button_continue,label_location,tk_photoimage_location,list_history,label_history,total_score,score,label_total_score
                pc_move=r.choice(pc_moves)
                user_move=move
                label_pc=tk.Label(text='PC MOVE',font=('Copperplate gothic bold',20,'bold'),bg='black',fg='white')
                label_user=tk.Label(text='USER MOVE',font=('Copperplate gothic bold',20,'bold'),bg='black',fg='white')
                label_pc.place(x=541,y=200,width=200,height=50)
                label_user.place(x=824,y=200,width=200,height=50)

                label_pc_move=tk.Label(text=pc_move,font=('Copperplate gothic bold',20,'bold'),bg='black',fg='white')
                label_user_move=tk.Label(text=user_move,font=('Copperplate gothic bold',20,'bold'),bg='black',fg='white')
                label_pc_move.place(x=541,y=250,width=200,height=50)
                label_user_move.place(x=824,y=250,width=200,height=50)
                if pc_move=='Rock':
                    list_pc_move[count-1]='supportfile/Rock Paper Scissors\\HistoryRock.png'
                    if user_move=='Rock':
                        winner='It is a TIE'
                        music_track='supportfile/Rock Paper Scissors\\Tie.wav'
                        image_file='supportfile/Rock Paper Scissors\\RRT.png'
                        list_history[count-1]='T'
                        list_user_move[count-1]='supportfile/Rock Paper Scissors\\HistoryRock.png'
                        value=0
                    if user_move=='Paper':
                        winner='USER has won'
                        music_track='supportfile/Rock Paper Scissors\\PAP.wav'
                        image_file='supportfile/Rock Paper Scissors\\RPU.png'
                        list_history[count-1]='U'
                        list_user_move[count-1]='supportfile/Rock Paper Scissors\\HistoryPaper.png'
                        value=2
                    if user_move=='Scissors':
                        winner='PC has won'
                        music_track='supportfile/Rock Paper Scissors\\ROCK.wav'
                        image_file='supportfile/Rock Paper Scissors\\RSC.png'
                        list_history[count-1]='C'
                        list_user_move[count-1]='supportfile/Rock Paper Scissors\\HistorySci.png'
                        value=-1
                if pc_move=='Paper':
                    list_pc_move[count-1]='supportfile/Rock Paper Scissors\\HistoryPaper.png'
                    if user_move=='Rock':
                        winner='PC has won'
                        music_track='supportfile/Rock Paper Scissors\\PAP.wav'
                        image_file='supportfile/Rock Paper Scissors\\PRC.png'
                        list_history[count-1]='C'
                        list_user_move[count-1]='supportfile/Rock Paper Scissors\\HistoryRock.png'
                        value=-1
                    if user_move=='Paper':
                        winner='It is a TIE'
                        music_track='supportfile/Rock Paper Scissors\\Tie.wav'
                        image_file='supportfile/Rock Paper Scissors\\PPT.png'
                        list_history[count-1]='T'
                        list_user_move[count-1]='supportfile/Rock Paper Scissors\\HistoryPaper.png'
                        value=0
                    if user_move=='Scissors':
                        winner='USER has won'
                        music_track='supportfile/Rock Paper Scissors\\SCI.wav'
                        image_file='supportfile/Rock Paper Scissors\\PSU.png'
                        list_history[count-1]='U'
                        list_user_move[count-1]='supportfile/Rock Paper Scissors\\HistorySci.png'
                        value=2
                if pc_move=='Scissors':
                    list_pc_move[count-1]='supportfile/Rock Paper Scissors\\HistorySci.png'
                    if user_move=='Rock':
                        winner='USER has won'
                        music_track='supportfile/Rock Paper Scissors\\ROCK.wav'
                        image_file='supportfile/Rock Paper Scissors\\SRU.png'
                        list_history[count-1]='U'
                        list_user_move[count-1]='supportfile/Rock Paper Scissors\\HistoryRock.png'
                        value=2
                    if user_move=='Paper':
                        winner='PC has won'
                        music_track='supportfile/Rock Paper Scissors\\SCI.wav'
                        image_file='supportfile/Rock Paper Scissors\\SPC.png'
                        list_history[count-1]='C'
                        list_user_move[count-1]='supportfile/Rock Paper Scissors\\HistoryPaper.png'
                        value=-1
                    if user_move=='Scissors':
                        winner='It is a TIE'                                
                        music_track='supportfile/Rock Paper Scissors\\Tie.wav'
                        image_file='supportfile/Rock Paper Scissors\\SST.png'
                        list_history[count-1]='T'
                        list_user_move[count-1]='supportfile/Rock Paper Scissors\\HistorySci.png'
                        value=0
                total_score+=value
                score+=value
                if current_login!=None:
                    label_total_score.configure(text='Total Score\n%s\nScore this round\n%s'%(total_score,score))
                sound_rps=m.Sound(music_track)
                tk_photoimage_location=tk.PhotoImage(file=image_file)
                label_location.configure(image=tk_photoimage_location)        
                label_winner=tk.Label(text=winner,font=('Copperplate gothic bold',20,'bold'),bg='black',fg='white')
                button_continue=tk.Button(text='Continue',font=('Copperplate gothic bold',20,'bold'),bg='black',fg='lime',command=clear)
                screen.after(2000,lambda:button_continue.place(x=500+80,y=425,width=131*3+20,height=136))       
                screen.after(1000,lambda:label_history.configure(text='THIS ROUND\n\n\n%s\n\n\n%s\n\n\n%s\n\n\n%s\n\n\n%s\n\n'%(list_history[0],list_history[1],list_history[2],list_history[3],list_history[4])))
                screen.after(1000,lambda:label_winner.place(x=783-150,y=350,width=300))
                screen.after(500,lambda:sound_player(sound_rps))
            widgets_state('disabled',[button_rock,button_sci,button_pap])
            screen.after(1000,check)

        button_start=tk.Button(text='Start',bg='black',fg='lime',font=('Copperplate gothic bold',20,'bold'),command=game_start)
        button_start.place(x=783-70,y=630,height=50,width=140)
        button_quit=tk.Button(text='Quit',bg='black',fg='red',font=('Copperplate gothic bold',20,'bold'),command=lambda:sound_player(sound_button,screen))
        button_quit.place(x=783-60,y=685,height=50,width=120)

        if current_login!=None:
            label_total_score=tk.Label(text='Total Score\n%s\nScore this round\n%s'%(total_score,score),font=('copperplate gothic bold',15,'bold'),fg='lime',bg='black')
            label_total_score.place(x=147,y=100,width=220)
            
        screen.mainloop()
        try:
            overall_total_score+=score
            connect=my.connect(host ='localhost',user=user,passwd=pwd,database=db)
            cur=connect.cursor()
            cur.execute('update leaderboard set rockpaperscissors='+str(total_score)+',overall='+str(overall_total_score)+' where username="'+str(current_login)+'"')
            connect.commit()
        except:
            print(current_login)
    elif game=='c':

        d_user={}
        d_comp={}
        for i in range(100,0,-1):
            if ceil(i/10)%2==0:
                d_user.update({i:(5+19+(10-i%10)*70,35+31+(10-ceil(i/10))*70)})
                if i%10==0:
                    d_user.update({i:(5+19,d_user[i][1])})
            else:
                d_user.update({i:(5+19+(i%10-1)*70,35+31+(10-ceil(i/10))*70)})
                if i%10==0:
                    d_user.update({i:(635+19,d_user[i][1])})
        for i in d_user:
            d_comp.update({i:(d_user[i][0]+31,d_user[i][1])})    
        ladder1=[(115,695),(125,665),(135,640),(145,610),(155,585),(165,565),(175,545)]
        ladder2=[(375,675),(370,650),(365,625),(360,600),(355,575),(350,550),(345,525),(340,500),(330,475),(325,450),(320,425)]
        ladder3=[(50,600),(55,575),(60,550),(70,525),(75,500),(85,475),(90,450),(95,425),(100,400),(110,375),(115,350)]
        ladder4=[(591,340),(591,310),(591,280),(591,250),(591,220)]
        ladder5=[(250,310),(255,285),(260,265),(265,240),(275,215),(280,190),(290,165),(295,140),(300,120),(310,95),(315,70),(320,60)]
        ladder6=[(665,205),(660,190),(655,170),(650,150),(645,135),(640,115),(635,105),(630,90),(620,70)]
        snake1=[(180,65),(140,70),(110,80),(90,100),(80,120),(80,150),(80,165),(85,190),(90,225),(100,230),(105,245),(110,260),(115,270),(115,290),(115,310),(110,330),(110,350),(90,365),(75,380),(60,395),(45,415),(35,435),(20,460),(20,485)]
        snake2=[(480,140),(530,130),(560,140),(585,145),(600,155),(610,175),(625,185),(640,205),(640,235),(640,265),(630,300),(610,330),(600,360),(585,380),(585,400),(595,415)]
        snake3=[(280,135),(320,130),(350,140),(365,155),(375,180),(355,200),(325,210),(285,220),(255,225),(225,240),(200,265),(200,290),(200,325)]
        snake4=[(525,210),(460,210),(430,230),(410,265),(405,295),(415,340),(425,375),(430,410),(430,440),(415,470),(390,490),(370,510),(355,540),(355,570),(370,595),(390,615)]
        snake5=[(325,335),(360,330),(430,325),(460,335),(480,345),(500,360),(510,375),(515,395),(520,415),(515,440),(505,465),(495,490),(485,520),(480,550),(490,585),(500,610),(515,630),(520,645),(525,670),(530,695)]
        snake6=[(680,415),(630,420),(605,445),(590,480),(570,505),(545,520),(510,530),(475,555),(455,575),(440,620),(425,655),(415,670),(385,690),(350,705)]
        snake7=[(200,405),(250,410),(280,425),(300,435),(310,455),(300,470),(280,490),(265,510),(245,535),(235,565),(230,595),(240,620)]
        special_d={(2,23):ladder1,(6,45):ladder2,(20,59):ladder3,(52,72):ladder4,(57,96):ladder5,(71,92):ladder6,(98,40):snake1,(87,49):snake2,(84,58):snake3,(73,15):snake4,(56,8):snake5,(50,5):snake6,(43,17):snake7}
        check_score(3)
        
        def die_roll(final1,final2):
            global tk_photoimage_dice1,tk_photoimage_dice2,tk_photoimage_dice3,tk_photoimage_dice4,tk_photoimage_dice5,tk_photoimage_dice6,c,label_diceholder1,label_diceholder2
            try:
                label_diceholder1.destroy()
                label_diceholder2.destroy()
            except:
                pass
            label_diceholder1=tk.Label()
            label_diceholder2=tk.Label()
            label_diceholder1.place(x=900,y=325)
            label_diceholder2.place(x=1050,y=325)
            tk_photoimage_dice1=tk.PhotoImage(file='supportfile/Snakes and Ladders\\1.png')
            tk_photoimage_dice2=tk.PhotoImage(file='supportfile/Snakes and Ladders\\2.png')
            tk_photoimage_dice3=tk.PhotoImage(file='supportfile/Snakes and Ladders\\3.png')
            tk_photoimage_dice4=tk.PhotoImage(file='supportfile/Snakes and Ladders\\4.png')
            tk_photoimage_dice5=tk.PhotoImage(file='supportfile/Snakes and Ladders\\5.png')
            tk_photoimage_dice6=tk.PhotoImage(file='supportfile/Snakes and Ladders\\6.png')
            l=[tk_photoimage_dice1,tk_photoimage_dice2,tk_photoimage_dice3,tk_photoimage_dice4,tk_photoimage_dice5,tk_photoimage_dice6]
            l1=[]
            l2=[]
            for i in range(10):
                l1+=[r.choice(l)]
                l2+=[r.choice(l)]
            l1+=[l[final1-1]]
            l2+=[l[final2-1]]
            c=0
            def change_dice():
                global c
                if c<11:
                    label_diceholder1.configure(image=l1[c])
                    label_diceholder2.configure(image=l2[c])
                    c+=1
                    screen.after(r.choice([100,150,200,250,300,350,400,450,500]),change_dice)
                else:
                    label_die_outcome=tk.Label(text='DIE OUTCOME IS \n%s'%(final1+final2),font=('copperplate gothic bold',20,'bold'),bg='black',fg='yellow')
                    label_die_outcome.after(1000,lambda:label_die_outcome.place(x=902,y=327,width=300,height=150)) 
                    label_die_outcome.after(3000,label_die_outcome.destroy)
                    screen.after(3000,lambda:movement(final1,final2))
            change_dice()
            
        
        def game_start():
            global comp_post,user_post,label_user_piece,label_comp_piece,button_roll,current_playing,label_positions
            comp_post=0
            user_post=0
            sound_player(sound_button)
            button_start.destroy()
            label_dice.configure(text='USER IS ROLLING\n\n\n\n\n\n\n\n\n\n\n\n\n')
            label_positions=tk.Label(text='USER POSITION             COMP POSITION\n%s\t\t     %s'%(user_post,comp_post),font=('copperplate gothic bold',20),bg='black',fg='white')
            label_positions.place(x=1054-290,y=200,width=580)
            label_user_piece=tk.Label(text='U',fg='yellow',bg='blue',font=(None,15,'bold'))
            label_user_piece.place(x=1054-35,y=225,width=30,height=30)
            label_comp_piece=tk.Label(text='C',fg='white',bg='blue',font=(None,15,'bold'))
            label_comp_piece.place(x=1054+5,y=225,width=30,height=30)
            button_roll=tk.Button(text='ROLL DICE',font=('copperplate gothic bold',30,'bold'),bg='black',fg='yellow',command=roll_dice)
            button_roll.place(x=1054-175,y=500,width=350)
            current_playing='user'
        def movement(x,y):
            global user_post,comp_post,current_playing,label_positions,c,label_diceholder1,label_diceholder2,total_score,score
            special=False
            if current_playing=='user':
                user_post+=x+y
                user_move(user_post-(x+y),user_post)
                current_playing='comp'
                if user_post>100:
                    user_post=100
                for i in special_d:
                    if i[0]==user_post:
                        special=True
                        path=i
                        break
                    else:
                        special=False
            else:
                comp_post+=x+y
                comp_move(comp_post-(x+y),comp_post)
                if comp_post>100:
                    comp_post=100
                current_playing='user'
                for i in special_d:
                    if i[0]==comp_post:
                        special=True
                        path=i
                        break
                    else:
                        special=False
            label_positions.configure(text='USER POSITION             COMP POSITION\n%s\t\t     %s'%(user_post,comp_post))
            if comp_post==100 or user_post==100:
                def reset():
                    global button_start,score,total_score
                    widgets_destroy([label_gameover,label_diceholder1,label_diceholder2,label_comp_piece,label_user_piece,label_positions,button_roll])
                    label_dice.configure(text='SNAKES AND LADDERS\n\n\n\n\n\n\n\n\n\n\n\n\n')
                    button_start=tk.Button(text='START',font=('copperplate gothic bold',20),bg='black',fg='lime',command=game_start)
                    button_start.place(x=1054-75,y=350,width=150)
                    if current_login!=None:
                        label_total_score.configure(text='Total Score\n%s\nScore this round\n%s'%(total_score,score))
                if comp_post==100:
                    winner='COMPUTER'
                    total_score+=-10
                    score+=-10
                else:
                    winner='USER'
                    total_score+=20
                    score+=20
                label_gameover=tk.Label(text='%s IS THE WINNER'%(winner),font=('copperplate gothic bold',35,'bold'),bg='black',fg='yellow')
                label_gameover.after(2000,lambda:label_gameover.place(x=683-400,y=300,width=800))
                label_gameover.after(5000,reset)
            else:
                if special==True:
                    special=False
                    def special_movement():
                        global c,user_post,comp_post,o
                        if current_playing=='comp':
                            o=special_d[path]+[d_user[path[1]]]
                            if path[0]>path[1]:
                                label_prompt=tk.Label(text='YOU ARE\nGOING DOWN',font=('copperplate gothic bold',20,'bold'),bg='black',fg='yellow')
                                sound_hiss=m.Sound('supportfile/Snakes and Ladders\\Hiss.wav')
                                sound_player(sound_hiss)
                            else:
                                label_prompt=tk.Label(text='YOU ARE\nGOING UP',font=('copperplate gothic bold',20,'bold'),bg='black',fg='yellow')
                                sound_ladder=m.Sound('supportfile/Snakes and Ladders\\Ladder.wav')
                                sound_player(sound_ladder)
                            label_prompt.after(1,lambda:label_prompt.place(x=902,y=327,width=300,height=150)) 
                            label_prompt.after(3000,label_prompt.destroy)            
                            c=0
                            user_post=path[1]
                            user_move_path(o)
                        else:
                            o=special_d[path]+[d_comp[path[1]]]
                            c=0
                            if path[0]>path[1]:
                                label_prompt=tk.Label(text='COMPUTER IS\nGOING DOWN',font=('copperplate gothic bold',20,'bold'),bg='black',fg='yellow')
                                sound_hiss=m.Sound('supportfile/Snakes and Ladders\\Hiss.wav')
                                sound_player(sound_hiss)
                            else:
                                label_prompt=tk.Label(text='COMPUTER IS\nGOING UP',font=('copperplate gothic bold',20,'bold'),bg='black',fg='yellow')
                                sound_ladder=m.Sound('supportfile/Snakes and Ladders\\Ladder.wav')
                                sound_player(sound_ladder)
                            label_prompt.after(1,lambda:label_prompt.place(x=902,y=327,width=300,height=150)) 
                            label_prompt.after(3000,label_prompt.destroy)  
                            comp_post=path[1]
                            comp_move_path(o)
                        label_positions.configure(text='USER POSITION             COMP POSITION\n%s\t\t     %s'%(user_post,comp_post))
                    screen.after(400*(x+y)+1000,special_movement)
                    screen.after(350*(x+y+len(special_d[path]+[d_user[path[1]]]))+2000,next)
                    label_positions.configure(text='USER POSITION             COMP POSITION\n%s\t\t     %s'%(user_post,comp_post))
                    
                else:
                    screen.after(350*(x+y)+2000,next)

        def next():
            if current_playing=='user':
                label_dice.configure(text='USER IS ROLLING\n\n\n\n\n\n\n\n\n\n\n\n\n')
                button_roll.configure(state='normal')
            elif current_playing=='comp':
                global a,b
                label_dice.configure(text='COMPUTER IS ROLLING\n\n\n\n\n\n\n\n\n\n\n\n\n')
                a=r.randint(1,6)   
                b=r.randint(1,6)
                a=b=3
                die_roll(a,b)
        def comp_move_path(x):
            global label_comp_piece,c
            if c<len(x):
                label_comp_piece.place(x=x[c][0],y=x[c][1])
                c+=1
                screen.after(350,lambda:comp_move_path(x))
        def user_move_path(x):
            global label_user_piece,c
            if c<len(x):
                label_user_piece.place(x=x[c][0],y=x[c][1])
                c+=1
                screen.after(350,lambda:user_move_path(x))
        def user_move(pos1,pos2):
            global label_user_piece
            if pos1==0:
                pos1=1
            if pos2>100:
                pos2=100
            if pos1<=pos2:
                label_user_piece.place(x=d_user[pos1][0],y=d_user[pos1][1])
                pos1+=1
                screen.after(350,lambda:user_move(pos1,pos2))
        def comp_move(pos1,pos2):
            global label_comp_piece
            if pos1==0:
                pos1=1
            if pos2>100:
                pos2=100
            if pos1<=pos2:
                label_comp_piece.place(x=d_comp[pos1][0],y=d_comp[pos1][1])
                pos1+=1
                screen.after(350,lambda:comp_move(pos1,pos2))
        def roll_dice():
            global user_post,a,b
            button_roll.configure(state='disabled')
            a=r.randint(1,6)   
            b=r.randint(1,6)
            a=b=3
            die_roll(a,b)

        screen=tk.Tk()
        screen.attributes('-fullscreen',True)
        screen.focus_force()
        
        tk_photoimage_board=tk.PhotoImage(file='supportfile/Snakes and Ladders\\Board.png')
        tk_photoimage_dice=tk.PhotoImage(file='supportfile/Snakes and Ladders\\Dice.png')
        label_board=tk.Label(image=tk_photoimage_board)
        label_board.place(x=3,y=0,width=740,height=768)
        label_dice=tk.Label(image=tk_photoimage_dice,text='SNAKES AND LADDERS\n\n\n\n\n\n\n\n\n\n\n\n\n',font=('copperplate gothic bold',32),fg='white',compound='c')
        label_dice.place(x=740)
        button_start=tk.Button(text='START',font=('copperplate gothic bold',20),bg='black',fg='lime',command=game_start)
        button_start.place(x=1054-75,y=350,width=150)
        button_quit=tk.Button(text='BACK',font=('copperplate gothic bold',20,'bold'),fg='red',bg='black',activebackground='black',command=lambda:sound_player(sound_button,screen))
        button_quit.place(x=1000,y=680,width=100)
        if current_login!=None:
            label_total_score=tk.Label(text='Total Score\n%s\nScore this round\n%s'%(total_score,score),font=('copperplate gothic bold',15,'bold'),fg='white',bg='black')
            label_total_score.place(x=1115,y=635,width=220)
        screen.mainloop()
        try:
            overall_total_score+=score
            connect=my.connect(host ='localhost',user=user,passwd=pwd,database=db)
            cur=connect.cursor()
            cur.execute('update leaderboard set snakesandladders='+str(total_score)+',overall='+str(overall_total_score)+' where username="'+str(current_login)+'"')
            connect.commit()
        except:
            print(current_login)
    elif game=='d':
        check_score(4)
        def game_function():
            def binder(func):
                screen.bind('1',lambda screen :func(1))
                screen.bind('2',lambda screen :func(2))
                screen.bind('3',lambda screen :func(3))
                screen.bind('4',lambda screen :func(4))
                screen.bind('5',lambda screen :func(5))
                screen.bind('6',lambda screen :func(6))
            def delete():
                global button_start
                widgets_destroy([button_1,button_2,button_3,button_4,button_5,button_6,label_actual_userscore,label_actual_compscore,label_user_actualmove,label_comp_actualmove,label_userscore,label_user_move,label_comp_move,label_compscore])
                for i in range(1,7):
                    screen.unbind(str(i))
                label_game.configure(text='HANDCRICKET\n\n\n\n\n\n\n\n\n\n\n')
                button_start=tk.Button(text='START',font=('copperplate gothic bold',20,'bold'),bg='black',fg='lime',command=game_start)
                button_start.place(x=683-75,y=300,width=150)
                screen.bind('<Return>',game_start)
                label_total_score.configure(text='Total Score\n%s\nScore this round\n%s'%(total_score,score))
            def button_place():
                global button_1,button_2,button_3,button_4,button_5,button_6
                button_1=tk.Button(text=1,font=('copperplate gothic bold',30,'bold'),bg='black',fg='#fd6b76',command=lambda:first_innings(1))
                button_2=tk.Button(text=2,font=('copperplate gothic bold',30,'bold'),bg='black',fg='#fd6b76',command=lambda:first_innings(2))
                button_3=tk.Button(text=3,font=('copperplate gothic bold',30,'bold'),bg='black',fg='#fd6b76',command=lambda:first_innings(3))
                button_4=tk.Button(text=4,font=('copperplate gothic bold',30,'bold'),bg='black',fg='#fd6b76',command=lambda:first_innings(4))
                button_5=tk.Button(text=5,font=('copperplate gothic bold',30,'bold'),bg='black',fg='#fd6b76',command=lambda:first_innings(5))
                button_6=tk.Button(text=6,font=('copperplate gothic bold',30,'bold'),bg='black',fg='#fd6b76',command=lambda:first_innings(6))
                button_1.place(x=683-300,y=550,width=100,height=100)
                button_2.place(x=683-200,y=550,width=100,height=100)
                button_3.place(x=683-100,y=550,width=100,height=100)
                button_4.place(x=683,y=550,width=100,height=100)
                button_5.place(x=683+100,y=550,width=100,height=100)
                button_6.place(x=683+200,y=550,width=100,height=100)
                binder(first_innings)
            def first_innings(user_move):
                global second_batter
                def reset():
                    global comp_score,user_score
                    print(first_batter)
                    if first_batter=='COMPUTER':
                        comp_score+=comp_move
                        label_actual_compscore.configure(text=comp_score)
                    elif first_batter=='USER':
                        user_score+=user_move
                        label_actual_userscore.configure(text=user_score)
                    label_comp_actualmove.configure(text='')
                    label_user_actualmove.configure(text='')
                    widgets_state('normal',[button_1,button_2,button_3,button_4,button_5,button_6])
                    binder(first_innings)
                for i in range(1,7):
                    screen.unbind(str(i))
                widgets_state('disabled',[button_1,button_2,button_3,button_4,button_5,button_6])
                comp_move=r.randint(1,6)
                label_comp_actualmove.configure(text=comp_move)
                label_user_actualmove.configure(text=user_move)
                if comp_move==user_move:
                    if first_batter=='USER':
                        second_batter='COMPUTER'
                        target=user_score
                    else:
                        second_batter='USER'
                        target=comp_score
                    screen.after(2000,lambda:widgets_state('normal',[button_1,button_2,button_3,button_4,button_5,button_6]))
                    screen.after(2000,lambda:label_comp_actualmove.configure(text=''))
                    screen.after(2000,lambda:label_user_actualmove.configure(text=''))
                    screen .after(2000,lambda:label_game.configure(text='SECOND INNINGS\n%s IS BATTING\n\n\n\n\n\n\nSCORE TO BEAT IS %s\n\n\n'%(second_batter,target)))
                    button_1.configure(command=lambda:second_innings(1))
                    button_2.configure(command=lambda:second_innings(2))
                    button_3.configure(command=lambda:second_innings(3))
                    button_4.configure(command=lambda:second_innings(4))
                    button_5.configure(command=lambda:second_innings(5))
                    button_6.configure(command=lambda:second_innings(6))
                    binder(second_innings)
                else:
                    screen.after(1500,reset)
            def second_innings(user_move):
                global total_score,score
                def reset():
                    global comp_score,user_score,total_score,score
                    print(first_batter)
                    win=''
                    if second_batter=='COMPUTER':
                        comp_score+=comp_move
                        label_actual_compscore.configure(text=comp_score)
                        if comp_score>user_score:
                            win='COMPUTER'
                            score+=-2
                            total_score+=-2
                    elif second_batter=='USER':
                        user_score+=user_move
                        label_actual_userscore.configure(text=user_score)
                        if comp_score<user_score:
                            win='USER'
                            score+=5
                            total_score+=5
                    label_comp_actualmove.configure(text='')
                    label_user_actualmove.configure(text='')
                    print(win)
                    if win=='':
                        binder(second_innings)
                        widgets_state('normal',[button_1,button_2,button_3,button_4,button_5,button_6])
                    else:
                        screen.after(1000,lambda:label_game.configure(text='\n\n\n\n\n\n\n%s IS THE WINNER\n\n\n\n'%(win)))    
                        screen.after(4000,delete)
                for i in range(1,7):
                    screen.unbind(str(i))
                widgets_state('disabled',[button_1,button_2,button_3,button_4,button_5,button_6])
                comp_move=r.randint(1,6)
                label_comp_actualmove.configure(text=comp_move)
                label_user_actualmove.configure(text=user_move)
                if comp_move==user_move:
                    if comp_score>user_score:
                        win='COMPUTER'
                        score+=-2
                        total_score+=-2
                    elif comp_score<user_score:
                        win='USER'
                        score+=5
                        total_score+=5
                    else:
                        win=''
                    screen.after(1000,lambda:label_game.configure(text='\n\n\n\n\n\n\n%s IS THE WINNER\n\n\n\n'%(win)))   
                    if win=='':
                        screen.after(1000,lambda:label_game.configure(text='\n\n\n\n\n\n\nIT IS A TIE\n\n\n\n'))    
                    screen.after(4000,delete)
                else:
                    screen.after(1500,reset)
            button_place()
        def score_card():
            global label_actual_userscore,label_actual_compscore,label_user_actualmove,label_comp_actualmove,label_user_move,label_comp_move,label_userscore,label_compscore
            label_userscore=tk.Label(text='USER SCORE',font=('copperplate gothic bold',20,'bold'),bg='black',fg='#fd6b76')    
            label_userscore.place(x=683-600,y=200,width=300)
            label_user_move=tk.Label(text='USER MOVE',font=('copperplate gothic bold',20,'bold'),bg='black',fg='#fd6b76')    
            label_user_move.place(x=683-300,y=200,width=300)
            label_comp_move=tk.Label(text='PC MOVE',font=('copperplate gothic bold',20,'bold'),bg='black',fg='#fd6b76')    
            label_comp_move.place(x=683,y=200,width=300)
            label_compscore=tk.Label(text='PC SCORE',font=('copperplate gothic bold',20,'bold'),bg='black',fg='#fd6b76')    
            label_compscore.place(x=683+300,y=200,width=300)
            
            label_actual_compscore=tk.Label(text=comp_score,font=('copperplate gothic bold',25,'bold'),bg='black',fg='#fd6b76')
            label_actual_userscore=tk.Label(text=user_score,font=('copperplate gothic bold',25,'bold'),bg='black',fg='#fd6b76')
            label_comp_actualmove=tk.Label(text='',font=('copperplate gothic bold',30,'bold'),bg='black',fg='#fd6b76')
            label_user_actualmove=tk.Label(text='',font=('copperplate gothic bold',30,'bold'),bg='black',fg='#fd6b76')

            screen.after(500,lambda:label_actual_userscore.place(x=683-500,y=300,width=100,height=100))
            screen.after(500,lambda:label_user_actualmove.place(x=683-200,y=300,width=100,height=100))
            screen.after(500,lambda:label_comp_actualmove.place(x=683+100,y=300,width=100,height=100))
            screen.after(500,lambda:label_actual_compscore.place(x=683+400,y=300,width=100,height=100))
            
            screen.after(1000,game_function)

        def bat_bowl():
            global tk_photoimage_bat,tk_photoimage_bowl,batbowl_choice,comp_score,user_score,first_batter
            user_score=comp_score=0
            if toss_win==True:
                def bat_bowl_button(option):
                    global batbowl_choice,first_batter
                    batbowl_choice=option
                    screen.unbind('a')
                    screen.unbind('b')
                    screen.after(1000,button_bowl.destroy)
                    screen.after(1000,button_bat.destroy)
                    screen.after(1000,lambda:label_game.configure(text='USER CHOOSES TO\n%s\n\n\n\n\n'%(batbowl_choice)))
                    if batbowl_choice=='BAT':
                        x='USER IS BATTING'
                        first_batter='USER'
                    else:
                        x='COMPUTER IS BATTING'
                        first_batter='COMPUTER'
                    button_bowl.configure(state='disabled')
                    button_bat.configure(state='disabled')
                    label_game.after(4000,lambda:label_game.configure(text='FIRST INNINGS\n%s\n\n\n\n\n\n\n\n\n\n'%(x)))
                    label_game.after(4500,score_card)
                label_game.configure(text='DO YOU WANT TO\nBAT FIRST OR BOWL FIRST\n\n\n\n\n\n\n\n\n\n')
                tk_photoimage_bat=tk.PhotoImage(file='supportfile/Handcricket\\Bat.png')
                tk_photoimage_bowl=tk.PhotoImage(file='supportfile/handcricket\\Bowl.png')
                button_bat=tk.Button(image=tk_photoimage_bat,bg='black',borderwidth=5,command=lambda:bat_bowl_button('BAT'))
                button_bowl=tk.Button(image=tk_photoimage_bowl,bg='black',borderwidth=5,command=lambda:bat_bowl_button('BOWL'))
                screen.bind('a',lambda screen:bat_bowl_button('BAT'))
                screen.bind('o',lambda screen:bat_bowl_button('BOWL'))
                button_bat.place(x=683-170,y=450)
                button_bowl.place(x=683+8,y=450)
                print('user decide')
            else:
                batbowl_choice=r.choice(['BAT','BOWL'])
                label_game.configure(text='COMPUTER CHOOSES TO\n%s\n\n\n\n\n'%(batbowl_choice))
                if batbowl_choice=='BAT':
                    x='COMPUTER IS BATTING'
                    first_batter='COMPUTER'
                else:
                    x='USER IS BATTING'
                    first_batter='USER'
                label_game.after(4000,lambda:label_game.configure(text='FIRST INNINGS\n%s\n\n\n\n\n\n\n\n\n\n'%(x)))
                label_game.after(4500,score_card)
                print('comp decides')


        def toss_ani(final):
            global tk_photoimage_coinhead,tk_photoimage_cointail,c
            try:
                label_coinholder.destroy()
            except:
                pass
            label_coinholder=tk.Label(bg='black')
            label_coinholder.place(x=600,y=300)
            tk_photoimage_coinhead=tk.PhotoImage(file='supportfile/Handcricket\\Heads.png')
            tk_photoimage_cointail=tk.PhotoImage(file='supportfile/handcricket\\Tails.png')
            l=[tk_photoimage_coinhead,tk_photoimage_cointail]
            l=l*5+[l[final-1]]
            c=0
            def change_coin():
                global c
                if c<11:
                    label_coinholder.configure(image=l[c])
                    c+=1
                    screen.after(300,change_coin)
                else:
                    if toss_win==True:
                        x='USER HAS WON THE TOSS'
                    else:
                        x='COMPUTER HAS WON TOSS'
                    screen.after(2000,label_prompt.destroy)
                    screen.after(2000,label_coinholder.destroy)
                    label_coin_outcome=tk.Label(text='COIN OUTCOME IS %s\n\n%s'%(['HEADS','TAILS'][final-1],x),font=('copperplate gothic bold',28,'bold'),bg='black',fg='#fd6b76')
                    label_coin_outcome.after(2000,lambda:label_coin_outcome.place(x=683-300,y=200,width=600,height=300)) 
                    label_coin_outcome.after(7000,label_coin_outcome.destroy)
                    screen.after(8000,bat_bowl)
            change_coin()
        def game_start(event=None):
            sound_player(sound_button)
            def toss_time():
                global tk_photoimage_coinhead,tk_photoimage_cointail
                def user_toss(option):
                    global toss_win,label_prompt
                    button_heads.configure(state='disabled')
                    button_tails.configure(state='disabled')
                    screen.unbind('h')
                    screen.unbind('t')
                    userchoice=['Heads','Tails'][option-1]
                    outcome=r.randint(1,2)
                    match=['Heads','Tails'][outcome-1]
                    label_prompt=tk.Label(text='%s is the call'%(userchoice),fg='#fd6b76',bg='black',font=('copperplate gothic bold',30,'bold'))
                    label_prompt.place(x=683-225,y=200,width=450)
                    screen.after(1000,button_tails.destroy)
                    screen.after(1000,button_heads.destroy)
                    screen.after(2000,lambda:toss_ani(outcome))
                    if match==userchoice:
                        toss_win=True
                    else:
                        toss_win=False
                    print(toss_win,match,userchoice)
                tk_photoimage_coinhead=tk.PhotoImage(file='supportfile/Handcricket\\Heads.png')
                tk_photoimage_cointail=tk.PhotoImage(file='supportfile/handcricket\\Tails.png')
                button_heads=tk.Button(image=tk_photoimage_coinhead,bg='black',borderwidth=10,command=lambda:user_toss(1))
                button_tails=tk.Button(image=tk_photoimage_cointail,bg='black',borderwidth=10,command=lambda:user_toss(2))
                button_heads.place(x=683-170,y=450)
                button_tails.place(x=683+8,y=450)
                screen.bind('h',lambda screen:user_toss(1))
                screen.bind('t',lambda screen:user_toss(2))
            button_start.destroy()
            screen.unbind('<Return>')
            label_game.configure(text='TOSS TIME\n\n\n\n\n\n\n\n\n\n\n')
            toss_time()
        screen=tk.Tk()
        screen.attributes('-fullscreen',True)

        screen.focus_force()

        tk_photoimage_game=tk.PhotoImage(file='supportfile/Handcricket\\Game.png')
        label_game=tk.Label(text='HANDCRICKET\n\n\n\n\n\n\n\n\n\n\n',font=('copperplate gothic bold',35,'bold'),image=tk_photoimage_game,compound='c')
        label_game.place(x=-1,y=-1)

        button_start=tk.Button(text='START',font=('copperplate gothic bold',20,'bold'),bg='black',fg='lime',command=game_start)
        button_start.place(x=683-75,y=300,width=150)
        button_quit=tk.Button(text='BACK',font=('copperplate gothic bold',20,'bold'),fg='red',bg='black',activebackground='black',command=lambda:sound_player(sound_button,screen))
        button_quit.place(x=683-50,y=678,width=100)
        screen.bind('<Return>',game_start)
        def des(event):
            screen.destroy()
        screen.bind('<Escape>',des)
        if current_login!=None:
            label_total_score=tk.Label(text='Total Score\n%s\nScore this round\n%s'%(total_score,score),font=('copperplate gothic bold',15,'bold'),fg='#fd6b76',bg='black')
            label_total_score.place(x=1110,y=35,width=220)

        screen.mainloop()
        try:
            overall_total_score+=score
            connect=my.connect(host ='localhost',user=user,passwd=pwd,database=db)
            cur=connect.cursor()
            cur.execute('update leaderboard set handcricket='+str(total_score)+',overall='+str(overall_total_score)+' where username="'+str(current_login)+'"')
            connect.commit()
        except:
            print(current_login)
    elif game=='e':
        check_score(5)
        screen=tk.Tk()
        screen.attributes('-fullscreen',True)
        screen.focus_force()
        
        tk_photoimage_bg=tk.PhotoImage(file='supportfile/Quadratic Equation\\Background.png')
        tk_photoimage_game=tk.PhotoImage(file='supportfile/Quadratic Equation\\Game.png')
        tk_photoimage_solve=tk.PhotoImage(file='supportfile/Quadratic Equation\\Solve.png')
        label_bg=tk.Label(text='QUADRATIC EQUATION\n\n\n\n\n\n\n\n\n\n',font=('copperplate gothic bold',40,'bold'),compound='c',image=tk_photoimage_bg)
        label_bg.place(x=0,y=0)
        def goback_menu():
            global button_game,button_solve,button_quit
            button_game=tk.Button(text='PLAY GAME',font=('copperplate gothic bold',14,'bold'),image=tk_photoimage_game,compound='top',bg='black',fg='white',command=button_game_press)
            button_game.place(x=683-160,y=300)
            button_solve=tk.Button(text='SOLVE',font=('copperplate gothic bold',14,'bold'),image=tk_photoimage_solve,compound='top',bg='black',fg='white',command=button_solve_press)
            button_solve.place(x=683+10,y=300)
            button_quit.configure(command=lambda:sound_player(sound_button,screen))
            label_bg.configure(text='QUADRATIC EQUATION\n\n\n\n\n\n\n\n\n\n')    
            try:
                button_start.destroy()
            except:
                pass
            try:
                widgets_destroy([entry_root1,entry_root2,label_root1,label_root2,button_proceed])
            except:
                pass
            try:
                widgets_destroy([button_calc,entry_coef1,entry_coef2,entry_coef3])
            except:
                pass
        def button_game_press():
            global button_final,button_start,num_correct
            chance=0
            num_correct=0
            try:
                button_final.destroy()
            except:
                pass
            def game_continue():
                def end():
                    global button_final,label_bg
                    button_proceed.destroy()
                    button_final=tk.Button(text='CONTINUE',font=('copperplate gothic bold',20,'bold'),bg='black',fg='lime',command=button_game_press)
                    button_final.place(x=683-100,y=300,width=200)
                    label_bg.configure(text='FIVE QUESTIONS ARE OVER\n\n\n\n\n\n\nYOU GOT '+str(num_correct)+' OUT OF 5\n\n\n')
                global chance,button_game_press,button_proceed,label_bg,label_root1,label_root2,entry_root1,entry_root2
                def game_proceed():
                    global total_score,score,num_correct,label_total_score
                    button_proceed.configure(state='disabled')
                    def delete():
                        global button_proceed,label_root1,label_root2,entry_root1,entry_root2
                        widgets_destroy([entry_root1,entry_root2,label_root1,label_root2,button_proceed])
                        game_continue()
                    root1=entry_root1.get()
                    root2=entry_root2.get()
                    try:
                        roots=[int(root1),int(root2)]
                        datatype='int'
                    except:
                        roots=['','']
                        datatype='something'
                    roots.sort()
                    solution.sort()
                    if roots[0]==solution[0] and roots[1]==solution[1]:
                        label_error=tk.Label(text='CORRECT ANSWER',font=('copperplate gothic bold',14,'bold'),bg='black',fg='lime')
                        label_error.place(x=683-250,y=450,width=500) 
                        label_error.after(1000,label_error.destroy)
                        screen.after(1000,delete)
                        score+=2
                        total_score+=2
                        num_correct+=1
                        if current_login!=None:
                            label_total_score.configure(text='Total Score\n%s\nScore this round\n%s'%(total_score,score))
                    else:
                        if datatype=='something':
                            label_error=tk.Label(text='PLEASE ENTER INTEGERS ONLY',font=('copperplate gothic bold',14,'bold'),bg='black',fg='red')
                            label_error.place(x=683-250,y=450,width=500)
                            label_error.after(2500,label_error.destroy)
                        else:
                            label_error=tk.Label(text='WRONG ROOTS',font=('copperplate gothic bold',14,'bold'),bg='black',fg='red')
                            label_error.place(x=683-250,y=450,width=500)
                            label_error.after(1000,label_error.destroy)
                            screen.after(1000,delete)
                    screen.after(2500,lambda:button_proceed.configure(state='normal'))
                if chance<5:
                    equation=list_equation[chance]
                    solution=list_solution[chance]                  
                    chance+=1
                    label_bg.configure(text='SOLVE THE EQUATION\n\n'+equation+'\n\n\n\n\n\n\n\n')
                    button_proceed=tk.Button(text='CONFIRM',font=('copperplate gothic bold',14,'bold'),bg='black',fg='lime',command=game_proceed)
                    button_proceed.place(x=683-100,y=550,width=200)
                    label_root1=tk.Label(text='ROOT  1',font=('copperplate gothic bold',25,'bold'),bg='black',fg='orange')
                    label_root1.place(x=683-275,y=300,width=225)
                    label_root2=tk.Label(text='ROOT  2',font=('copperplate gothic bold',25,'bold'),bg='black',fg='orange')
                    label_root2.place(x=683+50,y=300,width=225)
                    entry_root1=tk.Entry(font=('copperplate gothic bold',24,'bold'))
                    entry_root1.place(x=683-200,y=350,width=75,height=75)
                    entry_root2=tk.Entry(font=('copperplate gothic bold',24,'bold'))
                    entry_root2.place(x=683+125,y=350,width=75,height=75)
                else:
                    label_bg.configure(text='FIVE QUESTIONS ARE OVER\n\n\n\n\n\n\n\n\n\n')
                    button_proceed=tk.Button(text='CONTINUE',font=('copperplate gothic bold',14,'bold'),bg='black',fg='lime',command=end)
                    button_proceed.place(x=683-100,y=550,width=200)
            def start_game():
                global list_solution,list_equation,chance
                sound_player(sound_button)
                chance=0
                list_solution=[]
                list_equation=[]
                for i in range(5):
                    list_solution+=[[r.randint(-25,25),r.randint(-25,25)]]
                    sum_=list_solution[i][0]+list_solution[i][1]
                    prod=list_solution[i][0]*list_solution[i][1]
                    if sum_>=0:
                        sum_='+'+str(sum_)
                    if prod>=0:
                        prod='+'+str(prod)
                    list_equation+=['x²'+str(sum_)+'x'+str(prod)]
                    list_solution[i]=[int(-1*list_solution[i][0]),int(-1*list_solution[i][1])]
                print(list_solution)
                print(list_equation)
                button_start.destroy()   
                game_continue()
            button_game.destroy()
            button_solve.destroy()
            button_quit.configure(command=goback_menu)
            label_bg.configure(text='SOLVE THE EQUATION\n\n\n\n\n\n\n\n\n\n')
            button_start=tk.Button(text='START',font=('copperplate gothic bold',20,'bold'),bg='black',fg='lime',command=start_game)
            button_start.place(x=683-75,y=350,width=150)
        def button_solve_press():
            global entry_coef1,entry_coef2,entry_coef3,button_calc
            def solve():
                a=entry_coef1.get()
                b=entry_coef2.get()
                c=entry_coef3.get()
                try:
                    a=float(a)
                    b=float(b)
                    c=float(c)
                except:
                    a=b=c=''
                if type(a)==float and type(b)==float and type(c)==float:
                    try:
                        root1=(-1*b+(sqrt(pow(b,2)-4*a*c)))/(2*a)
                        root2=(-1*b-(sqrt(pow(b,2)-4*a*c)))/(2*a)
                        label_bg.configure(text='ENTER EQUATION TO SOLVE\n\nAx²+Bx+C\n\nA                   B                   C\n\n\nROOTS ARE\n'+str(root1)+'\n'+str(root2)+'\n')        
                    except ValueError:
                        label_bg.configure(text='ENTER EQUATION TO SOLVE\n\nAx²+Bx+C\n\nA                   B                   C\n\n\nIMAGINARY ROOTS\n\n\n')        
                else:
                    label_error=tk.Label(text='PLEASE ENTER NUMERIC DATA',font=('copperplate gothic bold',14,'bold'),bg='black',fg='red')
                    label_error.place(x=683-250,y=450,width=500)
                    label_error.after(2000,label_error.destroy)
            button_game.destroy()
            button_solve.destroy()
            button_quit.configure(command=goback_menu)
            label_bg.configure(text='ENTER EQUATION TO SOLVE\n\nAx²+Bx+C\n\nA                   B                   C\n\n\n\n\n\n')
            entry_coef1=tk.Entry(font=('copperplate gothic bold',24,'bold'))
            entry_coef1.place(x=683-400,y=350,width=200,height=75)
            entry_coef2=tk.Entry(font=('copperplate gothic bold',24,'bold'))
            entry_coef2.place(x=683-100,y=350,width=200,height=75)
            entry_coef3=tk.Entry(font=('copperplate gothic bold',24,'bold'))
            entry_coef3.place(x=683+200,y=350,width=200,height=75)
            button_calc=tk.Button(text='CALCULATE',font=('copperplate gothic bold',20,'bold'),bg='black',fg='lime',command=solve)
            button_calc.place(x=683-125,y=550,width=250)

        if current_login!=None:
            label_total_score=tk.Label(text='Total Score\n%s\nScore this round\n%s'%(total_score,score),font=('copperplate gothic bold',15,'bold'),fg='orange',bg='black')
            label_total_score.place(x=1115,y=35,width=220)

        button_game=tk.Button(text='PLAY GAME',font=('copperplate gothic bold',14,'bold'),image=tk_photoimage_game,compound='top',bg='black',fg='white',command=button_game_press)
        button_game.place(x=683-160,y=300)
        button_solve=tk.Button(text='SOLVE',font=('copperplate gothic bold',14,'bold'),image=tk_photoimage_solve,compound='top',bg='black',fg='white',command=button_solve_press)
        button_solve.place(x=683+10,y=300)
        button_quit=tk.Button(text='BACK',font=('copperplate gothic bold',14,'bold'),fg='red',bg='black',activebackground='black',command=lambda:sound_player(sound_button,screen))
        button_quit.place(x=683-50,y=650,width=100)

        screen.mainloop()
        try:
            overall_total_score+=score
            connect=my.connect(host ='localhost',user=user,passwd=pwd,database=db)
            cur=connect.cursor()
            cur.execute('update leaderboard set quadraticequation='+str(total_score)+',overall='+str(overall_total_score)+' where username="'+str(current_login)+'"')
            connect.commit()
        except:
            print(current_login)
    elif game=='f':
        check_score(6)      
        screen=tk.Tk()
        screen.attributes('-fullscreen',True)
        screen.focus_force()
        
        def place_cards():    
            global tk_photoimage_compcards,label_count_usercards,label_count_compcards,tk_photoimage_usercard1,tk_photoimage_usercard2,tk_photoimage_usercard3,tk_photoimage_usercard4,tk_photoimage_usercard5,button_card_holder1,button_card_holder2,button_card_holder3,button_card_holder4,button_card_holder5,tk_slider,button_maindeck,playing_card,tk_photoimage_playingcard,label_playingcard,cards_pics,cards,page_num,label_compcards,label_count_cards
            label_game.configure(text='CRAZY 8\n\n\n\n\n\n\n\n\n\n\n\n')
            page_num=1
            tk_photoimage_compcards=tk.PhotoImage(file='supportfile/Cards\\BackCard.png')
            label_compcards=tk.Label(image=tk_photoimage_compcards)
            label_compcards.place(x=683-405,y=30)
            label_count_usercards=tk.Label(text=len(user_cards),fg='white',bg='#1c0a01',font=('copperplate gothic bold',30,'bold'))
            label_count_usercards.place(x=683+500,y=625,height=75,width=75)
            label_count_compcards=tk.Label(text=len(comp_cards),fg='white',bg='#1c0a01',font=('copperplate gothic bold',30,'bold'))
            label_count_compcards.place(x=683-575,y=125,height=75,width=75)
            label_count_cards=tk.Label(text=len(cards),fg='white',bg='#1c0a01',font=('copperplate gothic bold',30,'bold'))
            label_count_cards.place(x=683-37,y=265+225//2-75,height=75,width=75)
            tk_photoimage_usercard1=tk.PhotoImage(file=user_deck_pics[page_num*5-5+0])
            tk_photoimage_usercard2=tk.PhotoImage(file=user_deck_pics[page_num*5-5+1])
            tk_photoimage_usercard3=tk.PhotoImage(file=user_deck_pics[page_num*5-5+2])
            tk_photoimage_usercard4=tk.PhotoImage(file=user_deck_pics[page_num*5-5+3])
            tk_photoimage_usercard5=tk.PhotoImage(file=user_deck_pics[page_num*5-5+4])
            button_card_holder1=tk.Button(image=tk_photoimage_usercard1,command=lambda:user_playing(page_num*5-5+0))
            button_card_holder1.place(x=683-83-165-165,y=500,width=165,height=230)
            button_card_holder2=tk.Button(image=tk_photoimage_usercard2,command=lambda:user_playing(page_num*5-5+1))
            button_card_holder2.place(x=683-83-165,y=500,width=165,height=230)
            button_card_holder3=tk.Button(image=tk_photoimage_usercard3,command=lambda:user_playing(page_num*5-5+2))
            button_card_holder3.place(x=683-83,y=500,width=165,height=230)
            button_card_holder4=tk.Button(image=tk_photoimage_usercard4,command=lambda:user_playing(page_num*5-5+3))
            button_card_holder4.place(x=683+83,y=500,width=165,height=230)
            button_card_holder5=tk.Button(image=tk_photoimage_usercard5,command=lambda:user_playing(page_num*5-5+4))
            button_card_holder5.place(x=683+83+165,y=500,width=165,height=230)
            button_maindeck=tk.Button(image=tk_photoimage_compcards,command=main_deck)
            button_maindeck.place(x=683-83-165,y=265,width=165,height=230)
            tk_photoimage_playingcard=tk.PhotoImage(file=cards_pics[0])
            label_playingcard=tk.Label(image=tk_photoimage_playingcard)
            label_playingcard.place(x=683+80,y=265)               
            playing_card=cards[0]
            cards_pics=cards_pics[1:]
            cards=cards[1:]
            label_count_cards.configure(text=len(cards))
            
        def game_over():
            global score,total_score,button_game
            if winner=='Comp':
                score+=-3
                total_score+=-3
            elif winner=='User':
                score+=7
                total_score+=7
            if current_login!=None:
                label_total_score.configure(text='Total Score\n%s\nScore this round\n%s'%(total_score,score))
            if winner in ['Comp','User']:
                label_gameover=tk.Label(text='%s is the winner'%(winner),bg='#1c0a01',fg='white',font=('copperplate gothic bold',30,'bold'))
            else:
                label_gameover=tk.Label(text='IT IS A DRAW',bg='#1c0a01',fg='white',font=('copperplate gothic bold',30,'bold'))
            label_gameover.place(x=683-350,y=300,width=700)
            label_gameover.after(2500,label_gameover.destroy)
            button_game=tk.Button(text='START',font=('copperplate gothic bold',20,'bold'),bg='#1c0a01',fg='lime',command=game_start)
            screen.after(3500,lambda:button_game.place(x=683-100,y=300,width=200))
        def user_deck_update(temp):
            global page_num,button_card_holder1,button_card_holder2,button_card_holder3,button_card_holder4,button_card_holder5,tk_photoimage_usercard1,tk_photoimage_usercard2,tk_photoimage_usercard3,tk_photoimage_usercard4,tk_photoimage_usercard5,user_deck_pics,user_cards,pages,tk_photoimage_compcards
            try:
                page_num=tk_slider.get()
            except:
                page_num=1
            pages=ceil(len(user_cards)/5)
            try:
                tk_photoimage_usercard1=tk.PhotoImage(file=user_deck_pics[page_num*5-5+0])
            except:
                tk_photoimage_usercard1=tk_photoimage_compcards
            try:
                tk_photoimage_usercard2=tk.PhotoImage(file=user_deck_pics[page_num*5-5+1])
            except:
                tk_photoimage_usercard2=tk_photoimage_compcards
            try:
                tk_photoimage_usercard3=tk.PhotoImage(file=user_deck_pics[page_num*5-5+2])
            except:
                tk_photoimage_usercard3=tk_photoimage_compcards
            try:
                tk_photoimage_usercard4=tk.PhotoImage(file=user_deck_pics[page_num*5-5+3])
            except:
                tk_photoimage_usercard4=tk_photoimage_compcards
            try:
                tk_photoimage_usercard5=tk.PhotoImage(file=user_deck_pics[page_num*5-5+4])
            except:
                tk_photoimage_usercard5=tk_photoimage_compcards
            l=[(button_card_holder1,button_card_holder2,button_card_holder3,button_card_holder4,button_card_holder5),(tk_photoimage_usercard1,tk_photoimage_usercard2,tk_photoimage_usercard3,tk_photoimage_usercard4,tk_photoimage_usercard5)]
            for i in range(5):
                l[0][i].configure(image=l[1][i])
            
        def main_deck():
            global cards_pics,cards,user_cards,user_deck_pics,tk_slider,page_num,pages,winner
            if len(cards)==0:
                label_gameover=tk.Label(text='NO MORE CARDS IN THE DECK',bg='#1c0a01',fg='white',font=('copperplate gothic bold',30,'bold'))
                label_gameover.place(x=683-350,y=300,width=700)
                label_gameover.after(2500,label_gameover.destroy)
                if len(user_cards)>len(comp_cards):
                    winner='Comp'
                elif len(user_cards)<len(comp_cards):
                    winner='User'
                else:
                    winner='Tie'
                screen.after(2500,delete_obj)
            else:
                user_cards+=(cards[0],)
                user_deck_pics+=[cards_pics[0]]
                cards_pics=cards_pics[1:]
                cards=cards[1:]
                pages=ceil(len(user_cards)/5)
                user_deck_update(True)
                if len(user_cards)>5:
                    try:
                        tk_slider.configure(to=pages)
                    except:
                        tk_slider=tk.Scale(from_=1,to=pages,orient='horizontal',length=220,bg='#1c0a01',fg='white',highlightbackground='white',font=(None,20,'bold'),command=user_deck_update)
                        tk_slider.place(x=40,y=550)
                label_count_usercards.configure(text=len(user_cards))
                label_count_cards.configure(text=len(cards))
        def comp_playing():
            global cards_pics,cards,comp_cards,comp_deck_pics,tk_photoimage_playingcard,playing_card,comp_playing_card
            play_value=playing_card[0]
            play_suites=playing_card[1]
            comp_playing_card=()
            def loop_checker():
                global cards_pics,cards,comp_cards,comp_deck_pics,tk_photoimage_playingcard,playing_card,comp_playing_card,winner
                if len(cards)==0:
                    label_gameover=tk.Label(text='NO MORE CARDS IN THE DECK',bg='#1c0a01',fg='white',font=('copperplate gothic bold',30,'bold'))
                    label_gameover.place(x=683-350,y=300,width=700)
                    label_gameover.after(2500,label_gameover.destroy)
                    if len(user_cards)>len(comp_cards):
                        winner='Comp'
                    elif len(user_cards)<len(comp_cards):
                        winner='User'
                    else:
                        winner='Tie'
                    screen.after(2500,delete_obj)
                else:
                    if comp_playing_card==():
                        comp_cards+=[cards[0]]
                        if cards[0][0]==play_value or cards[0][1]==play_suites:
                            comp_playing_card=cards[0]
                        cards=cards[1:]
                        cards_pics=cards_pics[1:]
                        label_count_compcards.configure(text=len(comp_cards))
                        label_count_cards.configure(text=len(cards))
                        screen.after(1000,loop_checker)
                    else:
                        comp_cards.remove(comp_playing_card)
                        label_count_compcards.configure(text=len(comp_cards))
                        tk_photoimage_playingcard=tk.PhotoImage(file='supportfile/Cards\\'+comp_playing_card[0]+comp_playing_card[1]+'.png')
                        label_playingcard.configure(image=tk_photoimage_playingcard)
                        playing_card=comp_playing_card
                        print(comp_cards)
                        if len(comp_cards)==0:
                            winner='Comp'
                            screen.after(2500,delete_obj)
                        else:
                            widgets_state('normal',[button_card_holder1,button_card_holder2,button_card_holder3,button_card_holder4,button_card_holder5,button_maindeck])
            for i in comp_cards:
                if i[0]=='8':
                    comp_playing_card=i
                    break
            for i in comp_cards:
                if i[0]==play_value or i[1]==play_suites:
                    comp_playing_card=i
                    break
            loop_checker()
        def delete_obj():
            widgets_destroy([button_card_holder1,button_card_holder2,button_card_holder3,button_card_holder4,button_card_holder5,button_maindeck,label_count_compcards,label_count_usercards,label_playingcard,label_compcards,label_count_cards])
            try:
                tk_slider.destroy()
            except:
                print()
            game_over()
        def user_playing(card):
            global cards_pics,cards,user_cards,comp_cards,user_deck_pics,comp_deck_pics,tk_photoimage_playingcard,playing_card,button_card_holder1,button_card_holder2,button_card_holder3,button_card_holder4,button_card_holder5,winner
            user_card=user_cards[card]
            if user_card[0]==playing_card[0] or user_card[1]==playing_card[1] or user_card[0]=='8':
                tk_photoimage_playingcard=tk.PhotoImage(file=user_deck_pics[card])
                label_playingcard.configure(image=tk_photoimage_playingcard)
                playing_card=user_card
                user_cards.remove(playing_card)
                user_deck_pics.remove(user_deck_pics[card])
                user_deck_update(True)
                if len(user_cards)<=5:
                    try:
                        tk_slider.destroy()
                        user_deck_update(True)
                    except:
                        print()
                if len(user_cards)/5==pages:
                    try:
                        tk_slider.configure(to=ceil(len(user_cards)/5))
                        user_deck_update(True)
                    except:
                        print()
                widgets_state('disabled',[button_card_holder1,button_card_holder2,button_card_holder3,button_card_holder4,button_card_holder5,button_maindeck])
                label_count_usercards.configure(text=len(user_cards))
                if len(user_cards)==0:
                    winner='User'            
                    screen.after(2500,delete_obj)
                else:
                    screen.after(1000,comp_playing)
        def game_start():
            sound_player(sound_button)
            sound_cards=m.Sound('supportfile/Cards\\Cards.wav')
            sound_player(sound_cards)
            global cards_pics,cards,user_cards,comp_cards,user_deck_pics,comp_deck_pics
            button_game.destroy()
            value=['2', '3', '4', '5', '6', '7', '8', '9', '10', 'ACE', 'JACK', 'QUEEN', 'KING']
            suit=['DIAMOND', 'SPADE', 'HEART', 'CLUB']
            cards_pics=[]
            cards=[]
            for i in suit:
                for j in value:
                    cards+=[(j,i)]
            r.shuffle(cards)
            r.shuffle(cards)
            r.shuffle(cards)
            r.shuffle(cards)
            r.shuffle(cards)
            for i in cards:
                cards_pics+=['supportfile/Cards\\'+i[0]+i[1]+'.png']
            user_deck_pics=[]
            comp_deck_pics=[]
            user_cards=[]
            comp_cards=[]
            for i in range(10):
                if i%2==0:
                    user_deck_pics+=[cards_pics[i]]
                    user_cards+=[cards[i]]
                else:
                    comp_deck_pics+=[cards_pics[i]]
                    comp_cards+=[cards[i]]
            cards_pics=cards_pics[10:]
            cards=cards[10:]
            screen.after(3000,place_cards)
            label_game.configure(text='\n\n\n\n\n\nCARDS ARE BEING DEALT\n\n\n\n\n\n')
        tk_photoimage_game=tk.PhotoImage(file='supportfile/Cards\\Game.png')
        label_game=tk.Label(text='CRAZY 8\n\n\n\n\n\n\n\n\n\n\n\n',image=tk_photoimage_game,fg='white',compound='c',font=('copperplate gothic bold',35,'bold'))
        label_game.place(x=0,y=0)
        button_game=tk.Button(text='START',font=('copperplate gothic bold',20,'bold'),bg='#1c0a01',fg='lime',command=game_start)
        button_game.place(x=683-100,y=300,width=200)
        button_quit=tk.Button(text='BACK',font=('copperplate gothic bold',20,'bold'),fg='red',bg='#1c0a01',activebackground='black',command=lambda:sound_player(sound_button,screen))
        button_quit.place(x=40,y=680,width=100)
        if current_login!=None:
            label_total_score=tk.Label(text='Total Score\n%s\nScore this round\n%s'%(total_score,score),font=('copperplate gothic bold',15,'bold'),fg='#1c0a01',bg='white')
            label_total_score.place(x=1115,y=35,width=220)
        screen.mainloop()
        try:
            overall_total_score+=score
            connect=my.connect(host ='localhost',user=user,passwd=pwd,database=db)
            cur=connect.cursor()
            cur.execute('update leaderboard set cards='+str(total_score)+',overall='+str(overall_total_score)+' where username="'+str(current_login)+'"')
            connect.commit()
        except:
            print(current_login)
    elif game=='g':
        check_score(7)
        screen=tk.Tk()
        screen.attributes('-fullscreen',True)
        screen.focus_force()
        
        tk_photoimage_game=tk.PhotoImage(file='supportfile/Memory\\Game.png')
        label_game=tk.Label(image=tk_photoimage_game)
        label_game.place(x=0,y=0)
        button_quit=tk.Button(text='Quit',font=('copperplate gothic bold',20,'bold'),fg='red',bg='grey',command=lambda:sound_player(sound_button,screen))
        button_quit.place(x=683-50,y=650,width=100)
        def timer():
            global time
            color=['blue','blue','blue','blue','blue','blue','blue']
            time=0
            def time_change():
                global time
                color[time]='white' 
                l=[label_timer1,label_timer2,label_timer3,label_timer4,label_timer5,label_timer6,label_timer7]
                for i in range(len(l)):
                    l[i].configure(bg=color[i])
                time+=1
                if time<7:
                    screen.after(1000,time_change)
                else:
                    widgets_destroy([label_timer1,label_timer2,label_timer3,label_timer4,label_timer5,label_timer6,label_timer7])
            label_timer1=tk.Label(bg='blue')
            label_timer1.place(x=100,y=75,width=35,height=100)
            label_timer2=tk.Label(bg='blue')
            label_timer2.place(x=100,y=80+75,width=35,height=100)
            label_timer3=tk.Label(bg='blue')
            label_timer3.place(x=100,y=160+75,width=35,height=100)
            label_timer4=tk.Label(bg='blue')
            label_timer4.place(x=100,y=240+75,width=35,height=100)
            label_timer5=tk.Label(bg='blue')
            label_timer5.place(x=100,y=320+75,width=35,height=100)
            label_timer6=tk.Label(bg='blue')
            label_timer6.place(x=100,y=400+75,width=35,height=100)
            label_timer7=tk.Label(bg='blue')
            label_timer7.place(x=100,y=480+75,width=35,height=100)
            time_change()

        def game_start():
            sound_player(sound_button)
            global over_list,label_info,color_list,color1,color2,color3,color4,color5,color6,color7,color8,color9,color10,color11,color12,color13,color14,color15,color16,button_tile1,button_tile2,button_tile3,button_tile4,button_tile5,button_tile6,button_tile7,button_tile8,button_tile9,button_tile10,button_tile11,button_tile12,button_tile13,button_tile14,button_tile15,button_tile16,current_choice,first,chance
            color1=color2=color3=color4=color5=color6=color7=color8=color9=color10=color11=color12=color13=color14=color15=color16=16
            chance=0
            first=True
            over_list=[]
            full_color=[['#ff4000', '#034748', '#5adbff', '#120d31', '#93032e', '#99621e', '#d38b5d', '#f3ffb6'], ['#a67599', '#fc7753', '#66d7d1', '#fab2ea', '#2a4d14', '#390040', '#730071', '#33658a'], ['#00120b', '#84714f', '#f0386b', '#eee82c', '#31e981', '#e8ebf7', '#006494', '#4bb3fd'], ['#091540', '#17bebb', '#ed1c24', '#fdfffc', '#f1d302', '#9b287b', '#04471c', '#46351d'], ['#59cd90', '#012622', '#a07178', '#f4d35e', '#400406', '#ed6a5a', '#5ca4a9', '#c179b9']]
            color_list=r.choice(full_color)
            color_list=color_list*2
            current_choice=()
            r.shuffle(color_list)
            r.shuffle(color_list)
            r.shuffle(color_list)
            r.shuffle(color_list)
            r.shuffle(color_list)
            color_list+=['black']
            button_start.destroy()
            actual_game()
            label_info=tk.Label(text='You have 7 seconds to\nmemorize the colors in the grid\nCLick confirm to start playing',font=('Copperplate gothic bold',25,'bold'),fg='white',bg='black')
            label_info.place(x=683-399,y=127,width=796,height=496)

        def show_color(parameter):
            status='disabled'
            if parameter == False:
                status='normal'
            global button_proceed,color_list,color1,color2,color3,color4,color5,color6,color7,color8,color9,color10,color11,color12,color13,color14,color15,color16,button_tile1,button_tile2,button_tile3,button_tile4,button_tile5,button_tile6,button_tile7,button_tile8,button_tile9,button_tile10,button_tile11,button_tile12,button_tile13,button_tile14,button_tile15,button_tile16
            l=[button_tile1,button_tile2,button_tile3,button_tile4,button_tile5,button_tile6,button_tile7,button_tile8,button_tile9,button_tile10,button_tile11,button_tile12,button_tile13,button_tile14,button_tile15,button_tile16]
            l_=[color1,color2,color3,color4,color5,color6,color7,color8,color9,color10,color11,color12,color13,color14,color15,color16]
            widgets_text(['']*16,l)
            widgets_state(status,l)
            for i in range(16):
                l[i].configure(bg=color_list[l_[i]])
        def reset_current_choice():
            global current_choice,button_tile1,button_tile2,button_tile3,button_tile4,button_tile5,button_tile6,button_tile7,button_tile8,button_tile9,button_tile10,button_tile11,button_tile12,button_tile13,button_tile14,button_tile15,button_tile16
            current_choice=()
            l=[button_tile1,button_tile2,button_tile3,button_tile4,button_tile5,button_tile6,button_tile7,button_tile8,button_tile9,button_tile10,button_tile11,button_tile12,button_tile13,button_tile14,button_tile15,button_tile16]
            widgets_text(['']*16,l)            
        def back_orginal():
            global button_proceed,button_proceed,color1,color2,color3,color4,color5,color6,color7,color8,color9,color10,color11,color12,color13,color14,color15,color16,button_tile1,button_tile2,button_tile3,button_tile4,button_tile5,button_tile6,button_tile7,button_tile8,button_tile9,button_tile10,button_tile11,button_tile12,button_tile13,button_tile14,button_tile15,button_tile16
            color1=color2=color3=color4=color5=color6=color7=color8=color9=color10=color11=color12=color13=color14=color15=color16=16
            button_proceed.configure(state='normal')
            show_color(False)
        def button_choice(number,tile):
            global current_choice,over_list,button_skip
            if number not in current_choice and number not in over_list:
                current_choice+=(number,)
                tile.configure(text='✓')
            button_skip.configure(state='normal')
        def delete_tiles():
            global button_continue,button_reset,button_skip,label_info,button_tile1,button_tile2,button_tile3,button_tile4,button_tile5,button_tile6,button_tile7,button_tile8,button_tile9,button_tile10,button_tile11,button_tile12,button_tile13,button_tile14,button_tile15,button_tile16
            try:
                button_continue.destroy()
            except:
                print()
            try:
                button_proceed.destroy()
                button_reset.destroy()
                button_skip.destroy()
            except:
                print()
            print(chance)
            if current_login!=None:
                label_total_score.configure(text='Total Score\n%s\nScore this round\n%s'%(total_score,score))
            widgets_destroy([label_info,button_tile1,button_tile2,button_tile3,button_tile4,button_tile5,button_tile6,button_tile7,button_tile8,button_tile9,button_tile10,button_tile11,button_tile12,button_tile13,button_tile14,button_tile15,button_tile16])
            button_start=tk.Button(text='START',fg='lime',bg='grey',font=('copperplate gothic bold',20,'bold'),command=game_start)
            button_start.place(x=683-75,y=300,width=150)
        def proceed():
            global button_continue,button_skip,button_reset,label_info,over_list,button_proceed,current_choice,first,color1,color2,color3,color4,color5,color6,color7,color8,color9,color10,color11,color12,color13,color14,color15,color16,chance,total_score,score
            if first==True:
                color1,color2,color3,color4,color5,color6,color7,color8,color9,color10,color11,color12,color13,color14,color15,color16=0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15
                first=False
                label_info.destroy()
                show_color(True)
                timer()
                screen.after(7000,back_orginal)
            else:
                chance+=1
                if len(current_choice)==2:
                    def color_match(tile_num,color_change_to=[16]*16):
                        global color1,color2,color3,color4,color5,color6,color7,color8,color9,color10,color11,color12,color13,color14,color15,color16
                        if current_choice[tile_num]==0:
                            color1=color_change_to[0]
                        elif current_choice[tile_num]==1:
                            color2=color_change_to[1]
                        elif current_choice[tile_num]==2:
                            color3=color_change_to[2]
                        elif current_choice[tile_num]==3:
                            color4=color_change_to[3]
                        elif current_choice[tile_num]==4:
                            color5=color_change_to[4]
                        elif current_choice[tile_num]==5:
                            color6=color_change_to[5]
                        elif current_choice[tile_num]==6:
                            color7=color_change_to[6]
                        elif current_choice[tile_num]==7:
                            color8=color_change_to[7]
                        elif current_choice[tile_num]==8:
                            color9=color_change_to[8]
                        elif current_choice[tile_num]==9:
                            color10=color_change_to[9]
                        elif current_choice[tile_num]==10:
                            color11=color_change_to[10]
                        elif current_choice[tile_num]==11:
                            color12=color_change_to[11]
                        elif current_choice[tile_num]==12:
                            color13=color_change_to[12]
                        elif current_choice[tile_num]==13:
                            color14=color_change_to[13]
                        elif current_choice[tile_num]==14:
                            color15=color_change_to[14]
                        elif current_choice[tile_num]==15:
                            color16=color_change_to[15]
                    color_match(0,[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
                    color_match(1,[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
                    show_color(False)
                    if color_list[current_choice[0]]!=color_list[current_choice[1]]:
                        show_color(True)
                        color_match(0)
                        color_match(1)
                        screen.after(500,lambda:show_color(False))
                    else:
                        over_list+=list(current_choice)
                        if len(over_list)==16:
                            button_proceed.destroy()
                            button_reset.destroy()
                            button_skip.destroy()
                            label_info=tk.Label(text='Congragulations you have won\nYou took %s chances'%(chance),font=('Copperplate gothic bold',25,'bold'),fg='white',bg='black')
                            label_info.place(x=683-400,y=125,width=800,height=500)
                            total_score+=18-chance
                            score+=18-chance
                            button_continue=tk.Button(text='Continue',fg='lime',bg='grey',font=('copperplate gothic bold',20,'bold'),command=delete_tiles)
                            button_continue.place(x=683-100,y=450,width=200)
                    current_choice=()
        def actual_game():
            global button_proceed,button_reset,button_skip,color_list,color1,color2,color3,color4,color5,color6,color7,color8,color9,color10,color11,color12,color13,color14,color15,color16,button_tile1,button_tile2,button_tile3,button_tile4,button_tile5,button_tile6,button_tile7,button_tile8,button_tile9,button_tile10,button_tile11,button_tile12,button_tile13,button_tile14,button_tile15,button_tile16
            button_tile1=tk.Button(command=lambda:button_choice(0,button_tile1),state='disabled',font=('copperplate gothic bold',45),bg='black',fg='white')
            button_tile1.place(x=683-400,y=125,width=200,height=125)
            button_tile2=tk.Button(command=lambda:button_choice(1,button_tile2),state='disabled',font=('copperplate gothic bold',45),bg='black',fg='white')
            button_tile2.place(x=683-200,y=125,width=200,height=125)
            button_tile3=tk.Button(command=lambda:button_choice(2,button_tile3),state='disabled',font=('copperplate gothic bold',45),bg='black',fg='white')
            button_tile3.place(x=683,y=125,width=200,height=125)
            button_tile4=tk.Button(command=lambda:button_choice(3,button_tile4),state='disabled',font=('copperplate gothic bold',45),bg='black',fg='white')
            button_tile4.place(x=683+200,y=125,width=200,height=125)
            button_tile5=tk.Button(command=lambda:button_choice(4,button_tile5),state='disabled',font=('copperplate gothic bold',45),bg='black',fg='white')
            button_tile5.place(x=683-400,y=250,width=200,height=125)
            button_tile6=tk.Button(command=lambda:button_choice(5,button_tile6),state='disabled',font=('copperplate gothic bold',45),bg='black',fg='white')
            button_tile6.place(x=683-200,y=250,width=200,height=125)
            button_tile7=tk.Button(command=lambda:button_choice(6,button_tile7),state='disabled',font=('copperplate gothic bold',45),bg='black',fg='white')
            button_tile7.place(x=683,y=250,width=200,height=125)
            button_tile8=tk.Button(command=lambda:button_choice(7,button_tile8),state='disabled',font=('copperplate gothic bold',45),bg='black',fg='white')
            button_tile8.place(x=683+200,y=250,width=200,height=125)
            button_tile9=tk.Button(command=lambda:button_choice(8,button_tile9),state='disabled',font=('copperplate gothic bold',45),bg='black',fg='white')
            button_tile9.place(x=683-400,y=375,width=200,height=125)
            button_tile10=tk.Button(command=lambda:button_choice(9,button_tile10),state='disabled',font=('copperplate gothic bold',45),bg='black',fg='white')
            button_tile10.place(x=683-200,y=375,width=200,height=125)
            button_tile11=tk.Button(command=lambda:button_choice(10,button_tile11),state='disabled',font=('copperplate gothic bold',45),bg='black',fg='white')
            button_tile11.place(x=683,y=375,width=200,height=125)
            button_tile12=tk.Button(command=lambda:button_choice(11,button_tile12),state='disabled',font=('copperplate gothic bold',45),bg='black',fg='white')
            button_tile12.place(x=683+200,y=375,width=200,height=125)
            button_tile13=tk.Button(command=lambda:button_choice(12,button_tile13),state='disabled',font=('copperplate gothic bold',45),bg='black',fg='white')
            button_tile13.place(x=683-400,y=500,width=200,height=125)
            button_tile14=tk.Button(command=lambda:button_choice(13,button_tile14),state='disabled',font=('copperplate gothic bold',45),bg='black',fg='white')
            button_tile14.place(x=683-200,y=500,width=200,height=125)
            button_tile15=tk.Button(command=lambda:button_choice(14,button_tile15),state='disabled',font=('copperplate gothic bold',45),bg='black',fg='white')
            button_tile15.place(x=683,y=500,width=200,height=125)
            button_tile16=tk.Button(command=lambda:button_choice(15,button_tile16),state='disabled',font=('copperplate gothic bold',45),bg='black',fg='white')
            button_tile16.place(x=683+200,y=500,width=200,height=125)
            button_proceed=tk.Button(text='CONFIRM',fg='lime',bg='grey',font=('copperplate gothic bold',20,'bold'),command=proceed)
            button_proceed.place(x=683-100,y=50,width=200)
            button_reset=tk.Button(text='RESET',fg='lime',bg='grey',font=('copperplate gothic bold',20,'bold'),command=reset_current_choice)
            button_reset.place(x=683-400,y=50,width=200)
            button_skip=tk.Button(text='SKIP',fg='lime',bg='grey',font=('copperplate gothic bold',20,'bold'),command=delete_tiles,state='disabled')
            button_skip.place(x=683+200,y=50,width=200)
        button_start=tk.Button(text='START',fg='lime',bg='grey',font=('copperplate gothic bold',20,'bold'),command=game_start)
        button_start.place(x=683-75,y=300,width=150)
        if current_login!=None:
            label_total_score=tk.Label(text='Total Score\n%s\nScore this round\n%s'%(total_score,score),font=('copperplate gothic bold',15,'bold'),fg='black',bg='white')
            label_total_score.place(x=1115,y=35,width=220)
        screen.mainloop()
        try:
            overall_total_score+=score
            connect=my.connect(host ='localhost',user=user,passwd=pwd,database=db)
            cur=connect.cursor()
            cur.execute('update leaderboard set memorygame='+str(total_score)+',overall='+str(overall_total_score)+' where username="'+str(current_login)+'"')
            connect.commit()
        except:
            print(current_login)
    elif game=='h':

        check_score(8)
        cur=connect.cursor()
        cur.execute('select * from hangman')
        data_hangman=cur.fetchall()
        cur.close()
        dict_topic={0:'Countries',1:'Capitals',2:'Animals',3:'Mobiles',4:'Cars',5:'Fruits',6:'Vegetables',7:'Birds',8:'Flowers',9:'Prog Lang'}
        def duplicate(x):
            final=''
            for i in x:
                if i not in final:
                    final+=i
            return final
        def update_topic():
            global user_game_words,playing_word_counter
            user_choice_index=[]
            playing_category=[]
            user_choice=[intvar_countries.get(),intvar_capitals.get(),intvar_animals.get(),intvar_mobiles.get(),intvar_cars.get(),intvar_fruits.get(),intvar_vegetables.get(),intvar_birds.get(),intvar_flowers.get(),intvar_proglang.get()]
            user_game_words=[]
            for i in range(10):
                if user_choice[i]==1:
                    user_choice_index+=[i]
            if len(user_choice_index)==0:
                for i in range(10):
                    playing_category+=[dict_topic[i]]
                    for j in data_hangman:
                        user_game_words+=[j[i]]
            else:
                for i in user_choice_index:
                    playing_category+=[dict_topic[i]]
                    for j in data_hangman:
                        user_game_words+=[j[i]]
            playing_category.sort()
            playing_category_string=''
            for i in playing_category:
                playing_category_string+=i+','
            playing_category_string=playing_category_string[0:len(playing_category_string)-1]
            r.shuffle(user_game_words)
            r.shuffle(user_game_words)
            user_game_words=user_game_words[:15]
            r.shuffle(user_game_words)
            user_game_words=user_game_words[:10]
            r.shuffle(user_game_words)
            user_game_words=user_game_words[:5]
            playing_word_counter=0
            print(user_game_words)
            label_category.configure(text=playing_category_string)
            button_topic_ok.configure(state='disabled')
            widgets_state('normal',[butq,butw,bute,butr,butt,buty,butu,buti,buto,butp,buta,buts,butd,butf,butg,buth,butj,butk,butl,butz,butx,butc,butv,butb,butn,butm])
            start_game()
        def start_game():
            global hang_count,final_word,stop,counter,playing_word,final_word,display_word,label_letter,label_chance,button_cont,label_complete
            stop =True
            counter = 0
            if playing_word_counter==0:
                sound_player(sound_button)
                label_letter=tk.Label(text='',font=('Copperplate Gothic Bold',20),fg='white',bg='black')
                label_letter.place(x=450,y=300,width=50,height=50)
                label_chance=tk.Label(text='WORD: '+str(playing_word_counter+1),font=('Copperplate Gothic Bold',20),fg='white',bg='black')
                label_chance.place(x=375,y=50,width=200,height=50)
            if playing_word_counter==5:
                label_game.configure(text='')
                label_complete=tk.Label(text='Five words over',font=('Copperplate Gothic Bold',20),fg='white',bg='black')
                label_complete.place(x=375-50,y=50,width=300,height=50)
                button_cont=tk.Button(text='Continue',font=('Copperplate Gothic Bold',30,'bold'),fg='white',bg='black',command=cont)
                button_cont.place(x=350,y=300)
            else:
                playing_word=user_game_words[playing_word_counter]
                hang_count=0
                final_word=''
                display_word=['_']*len(playing_word)
                label_game.configure(text=' '.join(display_word))
                
        def cont():
            global button_cont,label_letter,label_complete,label_total_score
            global stop
            button_topic_ok.configure(state='normal')
            widgets_destroy([button_cont,label_complete,label_letter,label_chance])
            label_game.configure(text='')
            stop=False
        def feed_letter(letter):
            global user_letter,label_letter
            but_.configure(state='normal')
            label_letter.configure(text=letter)
            user_letter=letter
        def letter_give():
            global counter,label_chance,total_score,score,label_total_score,hang_count,final_word,playing_word_counter
            counter=hang_count
            but_.configure(state='disabled')
            label_letter.configure(text='')
            if hang_count<7:
                for i in range(len(playing_word)):
                    if playing_word[i]==user_letter:
                        sound_hangman=m.Sound('supportfile/Hangman\\Correct.wav')
                        sound_player(sound_hangman)
                        final_word+=user_letter
                        display_word[i]=user_letter
                if user_letter not in playing_word:
                    sound_hangman=m.Sound('supportfile/Hangman\\Wrong.wav')
                    sound_player(sound_hangman)
                    counter+=1
                    hang_count+=1
                label_game.configure(text=' '.join(display_word))
                a=duplicate(playing_word)
                b=duplicate(final_word)
                if sorted(a)==sorted(b):
                    playing_word_counter+=1
                    if playing_word_counter==5:
                        label_chance.configure(text='WORD: '+str(playing_word_counter))  
                    else:
                        label_chance.configure(text='WORD: '+str(playing_word_counter+1))     
                    total_score+=2
                    score+=2
                    if current_login!=None:
                        label_total_score.configure(text='Total Score\n%s\nScore this round\n%s'%(total_score,score))
                    label_game.configure(text='You got it')
                    label_game.after(2000,start_game)
            if hang_count==7:
                hang_count+=1
                playing_word_counter+=1
                if playing_word_counter==5:
                    label_chance.configure(text='WORD: '+str(playing_word_counter))  
                else:
                    label_chance.configure(text='WORD: '+str(playing_word_counter+1)) 
                label_game.configure(text='Word was,\n'+playing_word)
                total_score+=-1
                score+=-1
                if current_login!=None:
                    label_total_score.configure(text='Total Score\n%s\nScore this round\n%s'%(total_score,score))
                label_game.after(2000,start_game)

        stop=False
        c=0
        list_pic=['Hangman Pic (1).png','Hangman Pic (2).png','Hangman Pic (3).png','Hangman Pic (4).png','Hangman Pic (5).png','Hangman Pic (6).png','Hangman Pic (7).png','Hangman Pic (8).png']
        file_pic='supportfile/Hangman\\'+list_pic[c%8]
        def change():
            global c
            global tk_photoimage_hangman
            global stop
            file_pic='supportfile/Hangman\\'+list_pic[c%8]
            tk_photoimage_hangman=tk.PhotoImage(file=file_pic)
            label_hangman.configure(image=tk_photoimage_hangman)
            c+=1
            if stop==True:
                file_pic='supportfile/Hangman\\'+list_pic[counter%8]
                tk_photoimage_hangman=tk.PhotoImage(file=file_pic)
                label_hangman.configure(image=tk_photoimage_hangman)
            label_hangman.after(500,change)

        screen=tk.Tk()
        screen.state('zoomed')
        screen.attributes('-fullscreen',True)
        screen.focus_force()
        
        screen['bg']=('black')
        tk_photoimage_hangman=tk.PhotoImage(file=file_pic)
        tk_photoimage_keyboard=tk.PhotoImage(file='supportfile/Hangman\\Keyboard.png')
        tk_photoimage_topic=tk.PhotoImage(file='supportfile/Hangman\\Topics.png')
        tk_photoimage_game=tk.PhotoImage(file='supportfile/Hangman\\Game.png')
        tk_photoimage_category=tk.PhotoImage(file='supportfile/Hangman\\Category.png')
        label_hangman=tk.Label(image=tk_photoimage_hangman)
        label_hangman.place(x=1366-604,y=0)
        label_game=tk.Label(text='',image=tk_photoimage_game,font=('Copperplate Gothic Bold',30,'bold'),compound='c')

        label_game.place(x=178,y=0)
        label_keyboard=tk.Label(image=tk_photoimage_keyboard)
        label_keyboard.place(x=178,y=450)
        label_topic=tk.Label(image=tk_photoimage_topic)
        label_topic.place(x=0,y=0)
        label_category=tk.Label(text='',image=tk_photoimage_category,compound='c',font=('Copperplate Gothic Bold',19,'bold'))
        label_category.place(x=0,y=701)
        change()
        font_alpha=('Copperplate Gothic Bold',20)
        butq=tk.Button(text='Q',font=font_alpha,fg='white',bg='black',command=lambda:feed_letter('Q'))   
        butq.place(x=225+0,y=500,width=50,height=50)
        butw=tk.Button(text='W',font=font_alpha,fg='white',bg='black',command=lambda:feed_letter('W'))
        butw.place(x=225+50,y=500,width=50,height=50)
        bute=tk.Button(text='E',font=font_alpha,fg='white',bg='black',command=lambda:feed_letter('E'))
        bute.place(x=225+100,y=500,width=50,height=50)
        butr=tk.Button(text='R',font=font_alpha,fg='white',bg='black',command=lambda:feed_letter('R'))
        butr.place(x=225+150,y=500,width=50,height=50)
        butt=tk.Button(text='T',font=font_alpha,fg='white',bg='black',command=lambda:feed_letter('T'))
        butt.place(x=225+200,y=500,width=50,height=50)
        buty=tk.Button(text='Y',font=font_alpha,fg='white',bg='black',command=lambda:feed_letter('Y'))
        buty.place(x=225+250,y=500,width=50,height=50)
        butu=tk.Button(text='U',font=font_alpha,fg='white',bg='black',command=lambda:feed_letter('U'))
        butu.place(x=225+300,y=500,width=50,height=50)
        buti=tk.Button(text='I',font=font_alpha,fg='white',bg='black',command=lambda:feed_letter('I'))
        buti.place(x=225+350,y=500,width=50,height=50)
        buto=tk.Button(text='O',font=font_alpha,fg='white',bg='black',command=lambda:feed_letter('O'))
        buto.place(x=225+400,y=500,width=50,height=50)
        butp=tk.Button(text='P',font=font_alpha,fg='white',bg='black',command=lambda:feed_letter('P'))
        butp.place(x=225+450,y=500,width=50,height=50)
        buta=tk.Button(text='A',font=font_alpha,fg='white',bg='black',command=lambda:feed_letter('A'))
        buta.place(x=250+0,y=550,width=50,height=50)
        buts=tk.Button(text='S',font=font_alpha,fg='white',bg='black',command=lambda:feed_letter('S'))
        buts.place(x=250+50,y=550,width=50,height=50)
        butd=tk.Button(text='D',font=font_alpha,fg='white',bg='black',command=lambda:feed_letter('D'))
        butd.place(x=250+100,y=550,width=50,height=50)
        butf=tk.Button(text='F',font=font_alpha,fg='white',bg='black',command=lambda:feed_letter('F'))
        butf.place(x=250+150,y=550,width=50,height=50)
        butg=tk.Button(text='G',font=font_alpha,fg='white',bg='black',command=lambda:feed_letter('G'))
        butg.place(x=250+200,y=550,width=50,height=50)
        buth=tk.Button(text='H',font=font_alpha,fg='white',bg='black',command=lambda:feed_letter('H'))
        buth.place(x=250+250,y=550,width=50,height=50)
        butj=tk.Button(text='J',font=font_alpha,fg='white',bg='black',command=lambda:feed_letter('J'))
        butj.place(x=250+300,y=550,width=50,height=50)
        butk=tk.Button(text='K',font=font_alpha,fg='white',bg='black',command=lambda:feed_letter('K'))
        butk.place(x=250+350,y=550,width=50,height=50)
        butl=tk.Button(text='L',font=font_alpha,fg='white',bg='black',command=lambda:feed_letter('L'))
        butl.place(x=250+400,y=550,width=50,height=50)
        butz=tk.Button(text='Z',font=font_alpha,fg='white',bg='black',command=lambda:feed_letter('Z'))
        butz.place(x=275+0,y=600,width=50,height=50)
        butx=tk.Button(text='X',font=font_alpha,fg='white',bg='black',command=lambda:feed_letter('X'))
        butx.place(x=275+50,y=600,width=50,height=50)
        butc=tk.Button(text='C',font=font_alpha,fg='white',bg='black',command=lambda:feed_letter('C'))
        butc.place(x=275+100,y=600,width=50,height=50)
        butv=tk.Button(text='V',font=font_alpha,fg='white',bg='black',command=lambda:feed_letter('V'))
        butv.place(x=275+150,y=600,width=50,height=50)
        butb=tk.Button(text='B',font=font_alpha,fg='white',bg='black',command=lambda:feed_letter('B'))
        butb.place(x=275+200,y=600,width=50,height=50)
        butn=tk.Button(text='N',font=font_alpha,fg='white',bg='black',command=lambda:feed_letter('N'))
        butn.place(x=275+250,y=600,width=50,height=50)
        butm=tk.Button(text='M',font=font_alpha,fg='white',bg='black',command=lambda:feed_letter('M'))
        butm.place(x=275+300,y=600,width=50,height=50)
        but_=tk.Button(text='✔',font=font_alpha,fg='white',bg='black',command=letter_give)
        but_.place(x=275+350,y=600,width=50,height=50)
        but_.configure(state='disabled')
        widgets_state('disabled',[butq,butw,bute,butr,butt,buty,butu,buti,buto,butp,buta,buts,butd,butf,butg,buth,butj,butk,butl,butz,butx,butc,butv,butb,butn,butm])
        intvar_countries=tk.IntVar()
        intvar_capitals=tk.IntVar()
        intvar_animals=tk.IntVar()
        intvar_mobiles=tk.IntVar()
        intvar_cars=tk.IntVar()
        intvar_fruits=tk.IntVar()
        intvar_vegetables=tk.IntVar()
        intvar_birds=tk.IntVar()
        intvar_flowers=tk.IntVar()
        intvar_proglang=tk.IntVar()

        checkbutton_countries=tk.Checkbutton(text='Countries   ',variable=intvar_countries,font=('Copperplate Gothic Bold',),fg='white',bg='black',activeforeground='white',activebackground='black',selectcolor='black')
        checkbutton_capitals=tk.Checkbutton(text='Capitals      ',variable=intvar_capitals,font=('Copperplate Gothic Bold',),fg='white',bg='black',activeforeground='white',activebackground='black',selectcolor='black')
        checkbutton_animals=tk.Checkbutton(text='Animals       ',variable=intvar_animals,font=('Copperplate Gothic Bold',),fg='white',bg='black',activeforeground='white',activebackground='black',selectcolor='black')
        checkbutton_mobiles=tk.Checkbutton(text='Mobiles        ',variable=intvar_mobiles,font=('Copperplate Gothic Bold',),fg='white',bg='black',activeforeground='white',activebackground='black',selectcolor='black')
        checkbutton_cars=tk.Checkbutton(text='Cars              ',variable=intvar_cars,font=('Copperplate Gothic Bold',),fg='white',bg='black',activeforeground='white',activebackground='black',selectcolor='black')
        checkbutton_fruits=tk.Checkbutton(text='Fruits           ',variable=intvar_fruits,font=('Copperplate Gothic Bold',),fg='white',bg='black',activeforeground='white',activebackground='black',selectcolor='black')
        checkbutton_vegetables=tk.Checkbutton(text='Vegetables',variable=intvar_vegetables,font=('Copperplate Gothic Bold',),fg='white',bg='black',activeforeground='white',activebackground='black',selectcolor='black')
        checkbutton_birds=tk.Checkbutton(text='Birds             ',variable=intvar_birds,font=('Copperplate Gothic Bold',),fg='white',bg='black',activeforeground='white',activebackground='black',selectcolor='black')
        checkbutton_flowers=tk.Checkbutton(text='Flowers      ',variable=intvar_flowers,font=('Copperplate Gothic Bold',),fg='white',bg='black',activeforeground='white',activebackground='black',selectcolor='black')
        checkbutton_proglang=tk.Checkbutton(text='Prog.Lang.',variable=intvar_proglang,font=('Copperplate Gothic Bold',),fg='white',bg='black',activeforeground='white',activebackground='black',selectcolor='black')

        checkbutton_animals.place(x=30,y=100)
        checkbutton_birds.place(x=30,y=150)
        checkbutton_capitals.place(x=30,y=200)
        checkbutton_cars.place(x=30,y=250)
        checkbutton_countries.place(x=30,y=300)
        checkbutton_flowers.place(x=30,y=350)
        checkbutton_fruits.place(x=30,y=400)
        checkbutton_mobiles.place(x=30,y=450)
        checkbutton_proglang.place(x=30,y=500)
        checkbutton_vegetables.place(x=30,y=550)

        if current_login!=None:
            label_total_score=tk.Label(text='Total Score\n%s\nScore this round\n%s'%(total_score,score),font=('copperplate gothic bold',15,'bold'),fg='orange',bg='black')
            label_total_score.place(x=960,y=575,width=220)

        button_topic_ok=tk.Button(text='Go play',font=('Copperplate Gothic Bold',15),fg='white',bg='black',command=update_topic)
        button_topic_ok.place(x=30,y=580,height=50,width=120)

        button_quit=tk.Button(text='QUIT',font=('Copperplate Gothic Bold',15),fg='red',bg='black',command=lambda:sound_player(sound_button,screen))
        button_quit.place(x=30,y=635,height=50,width=120)
        screen.mainloop()

        try:
            overall_total_score+=score
            connect=my.connect(host ='localhost',user=user,passwd=pwd,database=db)
            cur=connect.cursor()
            cur.execute('update leaderboard set hangman='+str(total_score)+',overall='+str(overall_total_score)+' where username="'+str(current_login)+'"')
            connect.commit()
        except:
            print(current_login)
    elif game=='i':

        check_score(9)
        screen=tk.Tk()
        screen.attributes('-fullscreen',True)
        screen.focus_force() 
        def button_place():
            global g,button_1,button_2,button_3,button_4,button_5,button_6,button_7,button_8,button_9,button_10,button_11,button_12,button_13,button_14,button_15,button_16,button_17,button_18,button_19,button_20,button_21,button_22,button_23,button_24,button_25,button_26,button_27,button_28,button_29,button_30,button_31,button_32,button_33,button_34,button_35,button_36,button_37,button_38,button_39,button_40,button_41,button_42,button_43,button_44,button_45,button_46,button_47,button_48,button_49,button_50,button_51,button_52,button_53,button_54,button_55,button_56,button_57,button_58,button_59,button_60,button_61,button_62,button_63,button_64,button_65,button_66,button_67,button_68,button_69,button_70,button_71,button_72,button_73,button_74,button_75,button_76,button_77,button_78,button_79,button_80,button_81,button_82,button_83,button_84,button_85,button_86,button_87,button_88,button_89,button_90,button_91,button_92,button_93,button_94,button_95,button_96,button_97,button_98,button_99,button_100
            button_1=tk.Button(text=1,font=('copperplate gothic bold',17,'bold'),bg='black',fg='#a2cc4e',command=lambda:reply(1))
            button_2=tk.Button(text=2,font=('copperplate gothic bold',17,'bold'),bg='black',fg='#a2cc4e',command=lambda:reply(2))
            button_3=tk.Button(text=3,font=('copperplate gothic bold',17,'bold'),bg='black',fg='#a2cc4e',command=lambda:reply(3))
            button_4=tk.Button(text=4,font=('copperplate gothic bold',17,'bold'),bg='black',fg='#a2cc4e',command=lambda:reply(4))
            button_5=tk.Button(text=5,font=('copperplate gothic bold',17,'bold'),bg='black',fg='#a2cc4e',command=lambda:reply(5))
            button_6=tk.Button(text=6,font=('copperplate gothic bold',17,'bold'),bg='black',fg='#a2cc4e',command=lambda:reply(6))
            button_7=tk.Button(text=7,font=('copperplate gothic bold',17,'bold'),bg='black',fg='#a2cc4e',command=lambda:reply(7))
            button_8=tk.Button(text=8,font=('copperplate gothic bold',17,'bold'),bg='black',fg='#a2cc4e',command=lambda:reply(8))
            button_9=tk.Button(text=9,font=('copperplate gothic bold',17,'bold'),bg='black',fg='#a2cc4e',command=lambda:reply(9))
            button_10=tk.Button(text=10,font=('copperplate gothic bold',17,'bold'),bg='black',fg='#a2cc4e',command=lambda:reply(10))
            button_11=tk.Button(text=11,font=('copperplate gothic bold',17,'bold'),bg='black',fg='#a2cc4e',command=lambda:reply(11))
            button_12=tk.Button(text=12,font=('copperplate gothic bold',17,'bold'),bg='black',fg='#a2cc4e',command=lambda:reply(12))
            button_13=tk.Button(text=13,font=('copperplate gothic bold',17,'bold'),bg='black',fg='#a2cc4e',command=lambda:reply(13))
            button_14=tk.Button(text=14,font=('copperplate gothic bold',17,'bold'),bg='black',fg='#a2cc4e',command=lambda:reply(14))
            button_15=tk.Button(text=15,font=('copperplate gothic bold',17,'bold'),bg='black',fg='#a2cc4e',command=lambda:reply(15))
            button_16=tk.Button(text=16,font=('copperplate gothic bold',17,'bold'),bg='black',fg='#a2cc4e',command=lambda:reply(16))
            button_17=tk.Button(text=17,font=('copperplate gothic bold',17,'bold'),bg='black',fg='#a2cc4e',command=lambda:reply(17))
            button_18=tk.Button(text=18,font=('copperplate gothic bold',17,'bold'),bg='black',fg='#a2cc4e',command=lambda:reply(18))
            button_19=tk.Button(text=19,font=('copperplate gothic bold',17,'bold'),bg='black',fg='#a2cc4e',command=lambda:reply(19))
            button_20=tk.Button(text=20,font=('copperplate gothic bold',17,'bold'),bg='black',fg='#a2cc4e',command=lambda:reply(20))
            button_21=tk.Button(text=21,font=('copperplate gothic bold',17,'bold'),bg='black',fg='#a2cc4e',command=lambda:reply(21))
            button_22=tk.Button(text=22,font=('copperplate gothic bold',17,'bold'),bg='black',fg='#a2cc4e',command=lambda:reply(22))
            button_23=tk.Button(text=23,font=('copperplate gothic bold',17,'bold'),bg='black',fg='#a2cc4e',command=lambda:reply(23))
            button_24=tk.Button(text=24,font=('copperplate gothic bold',17,'bold'),bg='black',fg='#a2cc4e',command=lambda:reply(24))
            button_25=tk.Button(text=25,font=('copperplate gothic bold',17,'bold'),bg='black',fg='#a2cc4e',command=lambda:reply(25))
            button_26=tk.Button(text=26,font=('copperplate gothic bold',17,'bold'),bg='black',fg='#a2cc4e',command=lambda:reply(26))
            button_27=tk.Button(text=27,font=('copperplate gothic bold',17,'bold'),bg='black',fg='#a2cc4e',command=lambda:reply(27))
            button_28=tk.Button(text=28,font=('copperplate gothic bold',17,'bold'),bg='black',fg='#a2cc4e',command=lambda:reply(28))
            button_29=tk.Button(text=29,font=('copperplate gothic bold',17,'bold'),bg='black',fg='#a2cc4e',command=lambda:reply(29))
            button_30=tk.Button(text=30,font=('copperplate gothic bold',17,'bold'),bg='black',fg='#a2cc4e',command=lambda:reply(30))
            button_31=tk.Button(text=31,font=('copperplate gothic bold',17,'bold'),bg='black',fg='#a2cc4e',command=lambda:reply(31))
            button_32=tk.Button(text=32,font=('copperplate gothic bold',17,'bold'),bg='black',fg='#a2cc4e',command=lambda:reply(32))
            button_33=tk.Button(text=33,font=('copperplate gothic bold',17,'bold'),bg='black',fg='#a2cc4e',command=lambda:reply(33))
            button_34=tk.Button(text=34,font=('copperplate gothic bold',17,'bold'),bg='black',fg='#a2cc4e',command=lambda:reply(34))
            button_35=tk.Button(text=35,font=('copperplate gothic bold',17,'bold'),bg='black',fg='#a2cc4e',command=lambda:reply(35))
            button_36=tk.Button(text=36,font=('copperplate gothic bold',17,'bold'),bg='black',fg='#a2cc4e',command=lambda:reply(36))
            button_37=tk.Button(text=37,font=('copperplate gothic bold',17,'bold'),bg='black',fg='#a2cc4e',command=lambda:reply(37))
            button_38=tk.Button(text=38,font=('copperplate gothic bold',17,'bold'),bg='black',fg='#a2cc4e',command=lambda:reply(38))
            button_39=tk.Button(text=39,font=('copperplate gothic bold',17,'bold'),bg='black',fg='#a2cc4e',command=lambda:reply(39))
            button_40=tk.Button(text=40,font=('copperplate gothic bold',17,'bold'),bg='black',fg='#a2cc4e',command=lambda:reply(40))
            button_41=tk.Button(text=41,font=('copperplate gothic bold',17,'bold'),bg='black',fg='#a2cc4e',command=lambda:reply(41))
            button_42=tk.Button(text=42,font=('copperplate gothic bold',17,'bold'),bg='black',fg='#a2cc4e',command=lambda:reply(42))
            button_43=tk.Button(text=43,font=('copperplate gothic bold',17,'bold'),bg='black',fg='#a2cc4e',command=lambda:reply(43))
            button_44=tk.Button(text=44,font=('copperplate gothic bold',17,'bold'),bg='black',fg='#a2cc4e',command=lambda:reply(44))
            button_45=tk.Button(text=45,font=('copperplate gothic bold',17,'bold'),bg='black',fg='#a2cc4e',command=lambda:reply(45))
            button_46=tk.Button(text=46,font=('copperplate gothic bold',17,'bold'),bg='black',fg='#a2cc4e',command=lambda:reply(46))
            button_47=tk.Button(text=47,font=('copperplate gothic bold',17,'bold'),bg='black',fg='#a2cc4e',command=lambda:reply(47))
            button_48=tk.Button(text=48,font=('copperplate gothic bold',17,'bold'),bg='black',fg='#a2cc4e',command=lambda:reply(48))
            button_49=tk.Button(text=49,font=('copperplate gothic bold',17,'bold'),bg='black',fg='#a2cc4e',command=lambda:reply(49))
            button_50=tk.Button(text=50,font=('copperplate gothic bold',17,'bold'),bg='black',fg='#a2cc4e',command=lambda:reply(50))
            button_51=tk.Button(text=51,font=('copperplate gothic bold',17,'bold'),bg='black',fg='#a2cc4e',command=lambda:reply(51))
            button_52=tk.Button(text=52,font=('copperplate gothic bold',17,'bold'),bg='black',fg='#a2cc4e',command=lambda:reply(52))
            button_53=tk.Button(text=53,font=('copperplate gothic bold',17,'bold'),bg='black',fg='#a2cc4e',command=lambda:reply(53))
            button_54=tk.Button(text=54,font=('copperplate gothic bold',17,'bold'),bg='black',fg='#a2cc4e',command=lambda:reply(54))
            button_55=tk.Button(text=55,font=('copperplate gothic bold',17,'bold'),bg='black',fg='#a2cc4e',command=lambda:reply(55))
            button_56=tk.Button(text=56,font=('copperplate gothic bold',17,'bold'),bg='black',fg='#a2cc4e',command=lambda:reply(56))
            button_57=tk.Button(text=57,font=('copperplate gothic bold',17,'bold'),bg='black',fg='#a2cc4e',command=lambda:reply(57))
            button_58=tk.Button(text=58,font=('copperplate gothic bold',17,'bold'),bg='black',fg='#a2cc4e',command=lambda:reply(58))
            button_59=tk.Button(text=59,font=('copperplate gothic bold',17,'bold'),bg='black',fg='#a2cc4e',command=lambda:reply(59))
            button_60=tk.Button(text=60,font=('copperplate gothic bold',17,'bold'),bg='black',fg='#a2cc4e',command=lambda:reply(60))
            button_61=tk.Button(text=61,font=('copperplate gothic bold',17,'bold'),bg='black',fg='#a2cc4e',command=lambda:reply(61))
            button_62=tk.Button(text=62,font=('copperplate gothic bold',17,'bold'),bg='black',fg='#a2cc4e',command=lambda:reply(62))
            button_63=tk.Button(text=63,font=('copperplate gothic bold',17,'bold'),bg='black',fg='#a2cc4e',command=lambda:reply(63))
            button_64=tk.Button(text=64,font=('copperplate gothic bold',17,'bold'),bg='black',fg='#a2cc4e',command=lambda:reply(64))
            button_65=tk.Button(text=65,font=('copperplate gothic bold',17,'bold'),bg='black',fg='#a2cc4e',command=lambda:reply(65))
            button_66=tk.Button(text=66,font=('copperplate gothic bold',17,'bold'),bg='black',fg='#a2cc4e',command=lambda:reply(66))
            button_67=tk.Button(text=67,font=('copperplate gothic bold',17,'bold'),bg='black',fg='#a2cc4e',command=lambda:reply(67))
            button_68=tk.Button(text=68,font=('copperplate gothic bold',17,'bold'),bg='black',fg='#a2cc4e',command=lambda:reply(68))
            button_69=tk.Button(text=69,font=('copperplate gothic bold',17,'bold'),bg='black',fg='#a2cc4e',command=lambda:reply(69))
            button_70=tk.Button(text=70,font=('copperplate gothic bold',17,'bold'),bg='black',fg='#a2cc4e',command=lambda:reply(70))
            button_71=tk.Button(text=71,font=('copperplate gothic bold',17,'bold'),bg='black',fg='#a2cc4e',command=lambda:reply(71))
            button_72=tk.Button(text=72,font=('copperplate gothic bold',17,'bold'),bg='black',fg='#a2cc4e',command=lambda:reply(72))
            button_73=tk.Button(text=73,font=('copperplate gothic bold',17,'bold'),bg='black',fg='#a2cc4e',command=lambda:reply(73))
            button_74=tk.Button(text=74,font=('copperplate gothic bold',17,'bold'),bg='black',fg='#a2cc4e',command=lambda:reply(74))
            button_75=tk.Button(text=75,font=('copperplate gothic bold',17,'bold'),bg='black',fg='#a2cc4e',command=lambda:reply(75))
            button_76=tk.Button(text=76,font=('copperplate gothic bold',17,'bold'),bg='black',fg='#a2cc4e',command=lambda:reply(76))
            button_77=tk.Button(text=77,font=('copperplate gothic bold',17,'bold'),bg='black',fg='#a2cc4e',command=lambda:reply(77))
            button_78=tk.Button(text=78,font=('copperplate gothic bold',17,'bold'),bg='black',fg='#a2cc4e',command=lambda:reply(78))
            button_79=tk.Button(text=79,font=('copperplate gothic bold',17,'bold'),bg='black',fg='#a2cc4e',command=lambda:reply(79))
            button_80=tk.Button(text=80,font=('copperplate gothic bold',17,'bold'),bg='black',fg='#a2cc4e',command=lambda:reply(80))
            button_81=tk.Button(text=81,font=('copperplate gothic bold',17,'bold'),bg='black',fg='#a2cc4e',command=lambda:reply(81))
            button_82=tk.Button(text=82,font=('copperplate gothic bold',17,'bold'),bg='black',fg='#a2cc4e',command=lambda:reply(82))
            button_83=tk.Button(text=83,font=('copperplate gothic bold',17,'bold'),bg='black',fg='#a2cc4e',command=lambda:reply(83))
            button_84=tk.Button(text=84,font=('copperplate gothic bold',17,'bold'),bg='black',fg='#a2cc4e',command=lambda:reply(84))
            button_85=tk.Button(text=85,font=('copperplate gothic bold',17,'bold'),bg='black',fg='#a2cc4e',command=lambda:reply(85))
            button_86=tk.Button(text=86,font=('copperplate gothic bold',17,'bold'),bg='black',fg='#a2cc4e',command=lambda:reply(86))
            button_87=tk.Button(text=87,font=('copperplate gothic bold',17,'bold'),bg='black',fg='#a2cc4e',command=lambda:reply(87))
            button_88=tk.Button(text=88,font=('copperplate gothic bold',17,'bold'),bg='black',fg='#a2cc4e',command=lambda:reply(88))
            button_89=tk.Button(text=89,font=('copperplate gothic bold',17,'bold'),bg='black',fg='#a2cc4e',command=lambda:reply(89))
            button_90=tk.Button(text=90,font=('copperplate gothic bold',17,'bold'),bg='black',fg='#a2cc4e',command=lambda:reply(90))
            button_91=tk.Button(text=91,font=('copperplate gothic bold',17,'bold'),bg='black',fg='#a2cc4e',command=lambda:reply(91))
            button_92=tk.Button(text=92,font=('copperplate gothic bold',17,'bold'),bg='black',fg='#a2cc4e',command=lambda:reply(92))
            button_93=tk.Button(text=93,font=('copperplate gothic bold',17,'bold'),bg='black',fg='#a2cc4e',command=lambda:reply(93))
            button_94=tk.Button(text=94,font=('copperplate gothic bold',17,'bold'),bg='black',fg='#a2cc4e',command=lambda:reply(94))
            button_95=tk.Button(text=95,font=('copperplate gothic bold',17,'bold'),bg='black',fg='#a2cc4e',command=lambda:reply(95))
            button_96=tk.Button(text=96,font=('copperplate gothic bold',17,'bold'),bg='black',fg='#a2cc4e',command=lambda:reply(96))
            button_97=tk.Button(text=97,font=('copperplate gothic bold',17,'bold'),bg='black',fg='#a2cc4e',command=lambda:reply(97))
            button_98=tk.Button(text=98,font=('copperplate gothic bold',17,'bold'),bg='black',fg='#a2cc4e',command=lambda:reply(98))
            button_99=tk.Button(text=99,font=('copperplate gothic bold',17,'bold'),bg='black',fg='#a2cc4e',command=lambda:reply(99))
            button_100=tk.Button(text=100,font=('copperplate gothic bold',17,'bold'),bg='black',fg='#a2cc4e',command=lambda:reply(100))
            g=[button_1,button_2,button_3,button_4,button_5,button_6,button_7,button_8,button_9,button_10,button_11,button_12,button_13,button_14,button_15,button_16,button_17,button_18,button_19,button_20,button_21,button_22,button_23,button_24,button_25,button_26,button_27,button_28,button_29,button_30,button_31,button_32,button_33,button_34,button_35,button_36,button_37,button_38,button_39,button_40,button_41,button_42,button_43,button_44,button_45,button_46,button_47,button_48,button_49,button_50,button_51,button_52,button_53,button_54,button_55,button_56,button_57,button_58,button_59,button_60,button_61,button_62,button_63,button_64,button_65,button_66,button_67,button_68,button_69,button_70,button_71,button_72,button_73,button_74,button_75,button_76,button_77,button_78,button_79,button_80,button_81,button_82,button_83,button_84,button_85,button_86,button_87,button_88,button_89,button_90,button_91,button_92,button_93,button_94,button_95,button_96,button_97,button_98,button_99,button_100]
            x=[434,484,534,584,634,684,734,784,834,884]
            y=[150,200,250,300,350,400,450,500,550,600]
            for i in range(100):
                g[i].place(x=x[i%10],y=y[i//10],height=50,width=50)    
        def clues_selection():
            global list_clues
            list_clues=[]
            def prime(x):
                for i in range(2,x):
                    if x%i==0:
                        return False
                else:
                    return True 
            def factors(x):
                l=[]
                for i in range(1,x+1):
                    if x%i==0:
                        l+=[i]
                return l
            while True: 
                a=r.randint(1,100)   
                if a>number:
                    list_clues+=['IT IS LESSER\nTHAN %s'%(a)]
                    break
                elif a<number:
                    list_clues+=['IT IS GREATER\nTHAN %s'%(a)]
                    break
            if number%2==0:
                list_clues+=['IT IS AN\nEVEN NUMBER']
            else:
                list_clues+=['IT IS AN\nODD NUMBER']
            if not prime(number):
                list_clues+=['%s IS A\nFACTOR OF\nTHE NUMBER'%(r.choice(factors(number)))]
            else:
                list_clues+=['IT IS A\nPRIME NUMBER']
        def reset():
            global button_start
            label_clue.destroy()
            label_chance.destroy()
            widgets_destroy(g)
            button_start=tk.Button(text='START',font=('copperplate gothic bold',20,'bold'),bg='black',fg='lime',command=game_start)
            button_start.place(x=683-75,y=300,width=150)
            if current_login!=None:
                label_total_score.configure(text='Total Score\n%s\nScore this round\n%s'%(total_score,score))
        def game_start():
            sound_player(sound_button)
            global number,c,label_chance,label_clue
            c=1
            button_start.destroy()
            button_place()
            number=r.randint(1,100)
            print(number)
            clues_selection()
            label_chance=tk.Label(text='CHANCE\n%s'%(c),font=('copperplate gothic bold',20,'bold'),bg='black',fg='#a2cc4e')
            label_chance.place(x=683-550,y=300,width=250,height=150)
            label_clue=tk.Label(text='',font=('copperplate gothic bold',20,'bold'),bg='black',fg='#a2cc4e')
            label_clue.place(x=683+300,y=300,width=250,height=150)

        def reply(u_num):
            global c,total_score,score
            widgets_state('disabled',g)
            if u_num==number:
                label_clue.configure(text='YOU GOT IT\nNUMBER IS %s'%(number))
                total_score+=1
                score+=1
                screen.after(1500,reset)
            else:
                if c<=7:
                    if c%2==1:
                        if u_num>number:
                            label_clue.configure(text='THE GUESS\nIS HIGH')
                        elif u_num<number:
                            label_clue.configure(text='THE GUESS\nIS LOW')
                    else:
                        label_clue.configure(text=list_clues[int(c/2)-1])
                    screen.after(2000,lambda:label_clue.configure(text=''))
                    screen.after(2000,lambda:widgets_state('normal',g))
                    label_chance.configure(text='CHANCE\n%s'%(c))
                    c+=1
                else:
                    label_clue.configure(text='THE NUMBER\nIS %s'%(number))
                    screen.after(1500,reset)
        tk_photoimage_game=tk.PhotoImage(file='supportfile/Guess the integer\\Game.png')
        label_game=tk.Label(text='GUESS THE INTEGER\n\n\n\n\n\n\n\n\n\n\n',font=('copperplate gothic bold',35,'bold'),image=tk_photoimage_game,compound='c')
        label_game.place(x=-1,y=-1)

        button_start=tk.Button(text='START',font=('copperplate gothic bold',20,'bold'),bg='black',fg='lime',command=game_start)
        button_start.place(x=683-75,y=300,width=150)
        button_quit=tk.Button(text='BACK',font=('copperplate gothic bold',20,'bold'),fg='red',bg='black',activebackground='black',command=lambda:sound_player(sound_button,screen))
        button_quit.place(x=683-50,y=678,width=100)
        if current_login!=None:
            label_total_score=tk.Label(text='Total Score\n%s\nScore this round\n%s'%(total_score,score),font=('copperplate gothic bold',15,'bold'),fg='#a2cc4e',bg='black')
            label_total_score.place(x=1110,y=35,width=220)
        screen.mainloop()
        try:
            overall_total_score+=score
            connect=my.connect(host ='localhost',user=user,passwd=pwd,database=db)
            cur=connect.cursor()
            cur.execute('update leaderboard set guesstheinteger='+str(total_score)+',overall='+str(overall_total_score)+' where username="'+str(current_login)+'"')
            connect.commit()
        except:
            print(current_login)
    elif game=='j':
        def change_page(var):
            global page_number
            page_number=scale_page.get()
            
            label_tictactoe_points.configure(text='%s\n\n%s\n\n%s\n\n%s\n\n%s\n\n%s\n\n%s\n\n%s\n\n%s\n\n%s'%(display_scores_list[page_number*10-10+0][0],display_scores_list[page_number*10-10+1][0],display_scores_list[page_number*10-10+2][0],display_scores_list[page_number*10-10+3][0],display_scores_list[page_number*10-10+4][0],display_scores_list[page_number*10-10+5][0],display_scores_list[page_number*10-10+6][0],display_scores_list[page_number*10-10+7][0],display_scores_list[page_number*10-10+8][0],display_scores_list[page_number*10-10+9][0]))
            label_rockpapersci_points.configure(text='%s\n\n%s\n\n%s\n\n%s\n\n%s\n\n%s\n\n%s\n\n%s\n\n%s\n\n%s'%(display_scores_list[page_number*10-10+0][1],display_scores_list[page_number*10-10+1][1],display_scores_list[page_number*10-10+2][1],display_scores_list[page_number*10-10+3][1],display_scores_list[page_number*10-10+4][1],display_scores_list[page_number*10-10+5][1],display_scores_list[page_number*10-10+6][1],display_scores_list[page_number*10-10+7][1],display_scores_list[page_number*10-10+8][1],display_scores_list[page_number*10-10+9][1]))
            label_snakesandladders_points.configure(text='%s\n\n%s\n\n%s\n\n%s\n\n%s\n\n%s\n\n%s\n\n%s\n\n%s\n\n%s'%(display_scores_list[page_number*10-10+0][2],display_scores_list[page_number*10-10+1][2],display_scores_list[page_number*10-10+2][2],display_scores_list[page_number*10-10+3][2],display_scores_list[page_number*10-10+4][2],display_scores_list[page_number*10-10+5][2],display_scores_list[page_number*10-10+6][2],display_scores_list[page_number*10-10+7][2],display_scores_list[page_number*10-10+8][2],display_scores_list[page_number*10-10+9][2]))
            label_handcricket_points.configure(text='%s\n\n%s\n\n%s\n\n%s\n\n%s\n\n%s\n\n%s\n\n%s\n\n%s\n\n%s'%(display_scores_list[page_number*10-10+0][3],display_scores_list[page_number*10-10+1][3],display_scores_list[page_number*10-10+2][3],display_scores_list[page_number*10-10+3][3],display_scores_list[page_number*10-10+4][3],display_scores_list[page_number*10-10+5][3],display_scores_list[page_number*10-10+6][3],display_scores_list[page_number*10-10+7][3],display_scores_list[page_number*10-10+8][3],display_scores_list[page_number*10-10+9][3]))
            label_quadraticequation_points.configure(text='%s\n\n%s\n\n%s\n\n%s\n\n%s\n\n%s\n\n%s\n\n%s\n\n%s\n\n%s'%(display_scores_list[page_number*10-10+0][4],display_scores_list[page_number*10-10+1][4],display_scores_list[page_number*10-10+2][4],display_scores_list[page_number*10-10+3][4],display_scores_list[page_number*10-10+4][4],display_scores_list[page_number*10-10+5][4],display_scores_list[page_number*10-10+6][4],display_scores_list[page_number*10-10+7][4],display_scores_list[page_number*10-10+8][4],display_scores_list[page_number*10-10+9][4]))
            label_cards_points.configure(text='%s\n\n%s\n\n%s\n\n%s\n\n%s\n\n%s\n\n%s\n\n%s\n\n%s\n\n%s'%(display_scores_list[page_number*10-10+0][5],display_scores_list[page_number*10-10+1][5],display_scores_list[page_number*10-10+2][5],display_scores_list[page_number*10-10+3][5],display_scores_list[page_number*10-10+4][5],display_scores_list[page_number*10-10+5][5],display_scores_list[page_number*10-10+6][5],display_scores_list[page_number*10-10+7][5],display_scores_list[page_number*10-10+8][5],display_scores_list[page_number*10-10+9][5]))
            label_memory_points.configure(text='%s\n\n%s\n\n%s\n\n%s\n\n%s\n\n%s\n\n%s\n\n%s\n\n%s\n\n%s'%(display_scores_list[page_number*10-10+0][6],display_scores_list[page_number*10-10+1][6],display_scores_list[page_number*10-10+2][6],display_scores_list[page_number*10-10+3][6],display_scores_list[page_number*10-10+4][6],display_scores_list[page_number*10-10+5][6],display_scores_list[page_number*10-10+6][6],display_scores_list[page_number*10-10+7][6],display_scores_list[page_number*10-10+8][6],display_scores_list[page_number*10-10+9][6]))
            label_hangman_points.configure(text='%s\n\n%s\n\n%s\n\n%s\n\n%s\n\n%s\n\n%s\n\n%s\n\n%s\n\n%s'%(display_scores_list[page_number*10-10+0][7],display_scores_list[page_number*10-10+1][7],display_scores_list[page_number*10-10+2][7],display_scores_list[page_number*10-10+3][7],display_scores_list[page_number*10-10+4][7],display_scores_list[page_number*10-10+5][7],display_scores_list[page_number*10-10+6][7],display_scores_list[page_number*10-10+7][7],display_scores_list[page_number*10-10+8][7],display_scores_list[page_number*10-10+9][7]))
            label_guess_points.configure(text='%s\n\n%s\n\n%s\n\n%s\n\n%s\n\n%s\n\n%s\n\n%s\n\n%s\n\n%s'%(display_scores_list[page_number*10-10+0][8],display_scores_list[page_number*10-10+1][8],display_scores_list[page_number*10-10+2][8],display_scores_list[page_number*10-10+3][8],display_scores_list[page_number*10-10+4][8],display_scores_list[page_number*10-10+5][8],display_scores_list[page_number*10-10+6][8],display_scores_list[page_number*10-10+7][8],display_scores_list[page_number*10-10+8][8],display_scores_list[page_number*10-10+9][8]))
            label_math_points.configure(text='%s\n\n%s\n\n%s\n\n%s\n\n%s\n\n%s\n\n%s\n\n%s\n\n%s\n\n%s'%(display_scores_list[page_number*10-10+0][9],display_scores_list[page_number*10-10+1][9],display_scores_list[page_number*10-10+2][9],display_scores_list[page_number*10-10+3][9],display_scores_list[page_number*10-10+4][9],display_scores_list[page_number*10-10+5][9],display_scores_list[page_number*10-10+6][9],display_scores_list[page_number*10-10+7][9],display_scores_list[page_number*10-10+8][9],display_scores_list[page_number*10-10+9][9]))
            label_total_points.configure(text='%s\n\n%s\n\n%s\n\n%s\n\n%s\n\n%s\n\n%s\n\n%s\n\n%s\n\n%s'%(display_scores_list[page_number*10-10+0][10],display_scores_list[page_number*10-10+1][10],display_scores_list[page_number*10-10+2][10],display_scores_list[page_number*10-10+3][10],display_scores_list[page_number*10-10+4][10],display_scores_list[page_number*10-10+5][10],display_scores_list[page_number*10-10+6][10],display_scores_list[page_number*10-10+7][10],display_scores_list[page_number*10-10+8][10],display_scores_list[page_number*10-10+9][10]))

            label_username1.configure(text=display_username_list[page_number*10-10+0],bg=display_colors_list[page_number*10-10+0][0],fg=display_colors_list[page_number*10-10+0][1])
            label_username2.configure(text=display_username_list[page_number*10-10+1],bg=display_colors_list[page_number*10-10+1][0],fg=display_colors_list[page_number*10-10+1][1])
            label_username3.configure(text=display_username_list[page_number*10-10+2],bg=display_colors_list[page_number*10-10+2][0],fg=display_colors_list[page_number*10-10+2][1])
            label_username4.configure(text=display_username_list[page_number*10-10+3],bg=display_colors_list[page_number*10-10+3][0],fg=display_colors_list[page_number*10-10+3][1])
            label_username5.configure(text=display_username_list[page_number*10-10+4],bg=display_colors_list[page_number*10-10+4][0],fg=display_colors_list[page_number*10-10+4][1])
            label_username6.configure(text=display_username_list[page_number*10-10+5],bg=display_colors_list[page_number*10-10+5][0],fg=display_colors_list[page_number*10-10+5][1])
            label_username7.configure(text=display_username_list[page_number*10-10+6],bg=display_colors_list[page_number*10-10+6][0],fg=display_colors_list[page_number*10-10+6][1])
            label_username8.configure(text=display_username_list[page_number*10-10+7],bg=display_colors_list[page_number*10-10+7][0],fg=display_colors_list[page_number*10-10+7][1])
            label_username9.configure(text=display_username_list[page_number*10-10+8],bg=display_colors_list[page_number*10-10+8][0],fg=display_colors_list[page_number*10-10+8][1])
            label_username10.configure(text=display_username_list[page_number*10-10+9],bg=display_colors_list[page_number*10-10+9][0],fg=display_colors_list[page_number*10-10+9][1])

        cur=connect.cursor()
        cur.execute('select * from leaderboard order by overall desc ,userNAME ')
        lead=cur.fetchall()
        cur.execute('select username from userpwd where status="Y"')
        current_login=cur.fetchall()
        cur.close()
        try:
            current_login=current_login[0][0]
        except:
            current_login=None
        cols=('User','TicTacToe','Rock Paper Scissors','Snakes And Ladders','Handcricket','Quadratic Equation','Cards','Memory','Hangman','Guess The Integer','Math Game','Overall')
        total_members=len(lead)
        total_pages=ceil(total_members/10)
        remaining_num=10-total_members%10
        display_username_list=[]
        display_scores_list=[]
        display_colors_list=[]
        for i in range(len(lead)):
            display_username_list+=[str(i+1)+'- '+lead[i][0]]
            display_scores_list+=[lead[i][1:12]]
            if current_login==lead[i][0]:
                display_colors_list+=[('gold','black')]
            else:
                display_colors_list+=[('black','white')]
        display_scores_list+=[('',)*11]*remaining_num
        display_username_list+=['']*remaining_num
        display_colors_list+=[('black','white')]*remaining_num
        screen=tk.Tk() 
        screen.attributes('-fullscreen',True)
        screen.focus_force()
        
        tk_photoimage_background=tk.PhotoImage(file='supportfile/Leaderboard\\LeaderboardBG.png')
        tk_photoimage_HC=tk.PhotoImage(file='supportfile/Leaderboard\\HC.png')
        tk_photoimage_TTT=tk.PhotoImage(file='supportfile/Leaderboard\\TTT.png')
        tk_photoimage_RPS=tk.PhotoImage(file='supportfile/Leaderboard\\RPS.png')
        tk_photoimage_SAL=tk.PhotoImage(file='supportfile/Leaderboard\\SAL.png')
        tk_photoimage_HM=tk.PhotoImage(file='supportfile/Leaderboard\\HM.png')
        tk_photoimage_MATH=tk.PhotoImage(file='supportfile/Leaderboard\\MATH.png')
        tk_photoimage_NG=tk.PhotoImage(file='supportfile/Leaderboard\\NG.png')
        tk_photoimage_QE=tk.PhotoImage(file='supportfile/Leaderboard\\QE.png')
        tk_photoimage_MEM=tk.PhotoImage(file='supportfile/Leaderboard\\MEM.png')
        tk_photoimage_TR=tk.PhotoImage(file='supportfile/Leaderboard\\TR.png')
        tk_photoimage_U=tk.PhotoImage(file='supportfile/Leaderboard\\U.png')
        tk_photoimage_BL=tk.PhotoImage(file='supportfile/Leaderboard\\BL.png')

        label_background=tk.Label(image=tk_photoimage_background)
        label_background.place(x=0,y=0)
        label_U=tk.Label(bg='black',image=tk_photoimage_U)
        label_U.place(x=34,y=38)
        label_TTT=tk.Label(bg='black',image=tk_photoimage_TTT)
        label_TTT.place(x=234,y=38)
        label_RPS=tk.Label(bg='black',image=tk_photoimage_RPS)
        label_RPS.place(x=334,y=38)
        label_SAL=tk.Label(bg='black',image=tk_photoimage_SAL)
        label_SAL.place(x=434,y=38)
        label_HC=tk.Label(bg='black',image=tk_photoimage_HC)
        label_HC.place(x=534,y=38)
        label_QE=tk.Label(bg='black',image=tk_photoimage_QE)
        label_QE.place(x=634,y=38)
        label_BL=tk.Label(bg='black',image=tk_photoimage_BL)
        label_BL.place(x=734,y=38)
        label_MEM=tk.Label(bg='black',image=tk_photoimage_MEM)
        label_MEM.place(x=834,y=38)
        label_HM=tk.Label(bg='black',image=tk_photoimage_HM)
        label_HM.place(x=934,y=38)
        label_NG=tk.Label(bg='black',image=tk_photoimage_NG)
        label_NG.place(x=1034,y=38)
        label_MATH=tk.Label(bg='black',image=tk_photoimage_MATH)
        label_MATH.place(x=1134,y=38)
        label_TR=tk.Label(bg='black',image=tk_photoimage_TR)
        label_TR.place(x=1234,y=38)

        label_username1=tk.Label(text=display_username_list[0],anchor='w',font=(None,15,'bold'),bg=display_colors_list[0][0],fg=display_colors_list[0][1])
        label_username1.place(x=39,y=175,width=198)
        label_username2=tk.Label(text=display_username_list[1],anchor='w',font=(None,15,'bold'),bg=display_colors_list[1][0],fg=display_colors_list[1][1])
        label_username2.place(x=39,y=175+48,width=198)
        label_username3=tk.Label(text=display_username_list[2],anchor='w',font=(None,15,'bold'),bg=display_colors_list[2][0],fg=display_colors_list[2][1])
        label_username3.place(x=39,y=175+48*2,width=198)
        label_username4=tk.Label(text=display_username_list[3],anchor='w',font=(None,15,'bold'),bg=display_colors_list[3][0],fg=display_colors_list[3][1])
        label_username4.place(x=39,y=175+48*3,width=198)
        label_username5=tk.Label(text=display_username_list[4],anchor='w',font=(None,15,'bold'),bg=display_colors_list[4][0],fg=display_colors_list[4][1])
        label_username5.place(x=39,y=175+48*4,width=198)
        label_username6=tk.Label(text=display_username_list[5],anchor='w',font=(None,15,'bold'),bg=display_colors_list[5][0],fg=display_colors_list[5][1])
        label_username6.place(x=39,y=175+48*5,width=198)
        label_username7=tk.Label(text=display_username_list[6],anchor='w',font=(None,15,'bold'),bg=display_colors_list[6][0],fg=display_colors_list[6][1])
        label_username7.place(x=39,y=175+48*6,width=198)
        label_username8=tk.Label(text=display_username_list[7],anchor='w',font=(None,15,'bold'),bg=display_colors_list[7][0],fg=display_colors_list[7][1])
        label_username8.place(x=39,y=175+48*7,width=198)
        label_username9=tk.Label(text=display_username_list[8],anchor='w',font=(None,15,'bold'),bg=display_colors_list[8][0],fg=display_colors_list[8][1])
        label_username9.place(x=39,y=175+48*8,width=198)
        label_username10=tk.Label(text=display_username_list[9],anchor='w',font=(None,15,'bold'),bg=display_colors_list[9][0],fg=display_colors_list[9][1])
        label_username10.place(x=39,y=175+48*9,width=198)

        page_number=1
        label_tictactoe_points=tk.Label(text='%s\n\n%s\n\n%s\n\n%s\n\n%s\n\n%s\n\n%s\n\n%s\n\n%s\n\n%s'%(display_scores_list[page_number*10-10+0][0],display_scores_list[page_number*10-10+1][0],display_scores_list[page_number*10-10+2][0],display_scores_list[page_number*10-10+3][0],display_scores_list[page_number*10-10+4][0],display_scores_list[page_number*10-10+5][0],display_scores_list[page_number*10-10+6][0],display_scores_list[page_number*10-10+7][0],display_scores_list[page_number*10-10+8][0],display_scores_list[page_number*10-10+9][0]),font=(None,15,'bold'),fg='black',bg='grey')
        label_rockpapersci_points=tk.Label(text='%s\n\n%s\n\n%s\n\n%s\n\n%s\n\n%s\n\n%s\n\n%s\n\n%s\n\n%s'%(display_scores_list[page_number*10-10+0][1],display_scores_list[page_number*10-10+1][1],display_scores_list[page_number*10-10+2][1],display_scores_list[page_number*10-10+3][1],display_scores_list[page_number*10-10+4][1],display_scores_list[page_number*10-10+5][1],display_scores_list[page_number*10-10+6][1],display_scores_list[page_number*10-10+7][1],display_scores_list[page_number*10-10+8][1],display_scores_list[page_number*10-10+9][1]),font=(None,15,'bold'),fg='black',bg='grey')
        label_snakesandladders_points=tk.Label(text='%s\n\n%s\n\n%s\n\n%s\n\n%s\n\n%s\n\n%s\n\n%s\n\n%s\n\n%s'%(display_scores_list[page_number*10-10+0][2],display_scores_list[page_number*10-10+1][2],display_scores_list[page_number*10-10+2][2],display_scores_list[page_number*10-10+3][2],display_scores_list[page_number*10-10+4][2],display_scores_list[page_number*10-10+5][2],display_scores_list[page_number*10-10+6][2],display_scores_list[page_number*10-10+7][2],display_scores_list[page_number*10-10+8][2],display_scores_list[page_number*10-10+9][2]),font=(None,15,'bold'),fg='black',bg='grey')
        label_handcricket_points=tk.Label(text='%s\n\n%s\n\n%s\n\n%s\n\n%s\n\n%s\n\n%s\n\n%s\n\n%s\n\n%s'%(display_scores_list[page_number*10-10+0][3],display_scores_list[page_number*10-10+1][3],display_scores_list[page_number*10-10+2][3],display_scores_list[page_number*10-10+3][3],display_scores_list[page_number*10-10+4][3],display_scores_list[page_number*10-10+5][3],display_scores_list[page_number*10-10+6][3],display_scores_list[page_number*10-10+7][3],display_scores_list[page_number*10-10+8][3],display_scores_list[page_number*10-10+9][3]),font=(None,15,'bold'),fg='black',bg='grey')
        label_quadraticequation_points=tk.Label(text='%s\n\n%s\n\n%s\n\n%s\n\n%s\n\n%s\n\n%s\n\n%s\n\n%s\n\n%s'%(display_scores_list[page_number*10-10+0][4],display_scores_list[page_number*10-10+1][4],display_scores_list[page_number*10-10+2][4],display_scores_list[page_number*10-10+3][4],display_scores_list[page_number*10-10+4][4],display_scores_list[page_number*10-10+5][4],display_scores_list[page_number*10-10+6][4],display_scores_list[page_number*10-10+7][4],display_scores_list[page_number*10-10+8][4],display_scores_list[page_number*10-10+9][4]),font=(None,15,'bold'),fg='black',bg='grey')
        label_cards_points=tk.Label(text='%s\n\n%s\n\n%s\n\n%s\n\n%s\n\n%s\n\n%s\n\n%s\n\n%s\n\n%s'%(display_scores_list[page_number*10-10+0][5],display_scores_list[page_number*10-10+1][5],display_scores_list[page_number*10-10+2][5],display_scores_list[page_number*10-10+3][5],display_scores_list[page_number*10-10+4][5],display_scores_list[page_number*10-10+5][5],display_scores_list[page_number*10-10+6][5],display_scores_list[page_number*10-10+7][5],display_scores_list[page_number*10-10+8][5],display_scores_list[page_number*10-10+9][5]),font=(None,15,'bold'),fg='black',bg='grey')
        label_memory_points=tk.Label(text='%s\n\n%s\n\n%s\n\n%s\n\n%s\n\n%s\n\n%s\n\n%s\n\n%s\n\n%s'%(display_scores_list[page_number*10-10+0][6],display_scores_list[page_number*10-10+1][6],display_scores_list[page_number*10-10+2][6],display_scores_list[page_number*10-10+3][6],display_scores_list[page_number*10-10+4][6],display_scores_list[page_number*10-10+5][6],display_scores_list[page_number*10-10+6][6],display_scores_list[page_number*10-10+7][6],display_scores_list[page_number*10-10+8][6],display_scores_list[page_number*10-10+9][6]),font=(None,15,'bold'),fg='black',bg='grey')
        label_hangman_points=tk.Label(text='%s\n\n%s\n\n%s\n\n%s\n\n%s\n\n%s\n\n%s\n\n%s\n\n%s\n\n%s'%(display_scores_list[page_number*10-10+0][7],display_scores_list[page_number*10-10+1][7],display_scores_list[page_number*10-10+2][7],display_scores_list[page_number*10-10+3][7],display_scores_list[page_number*10-10+4][7],display_scores_list[page_number*10-10+5][7],display_scores_list[page_number*10-10+6][7],display_scores_list[page_number*10-10+7][7],display_scores_list[page_number*10-10+8][7],display_scores_list[page_number*10-10+9][7]),font=(None,15,'bold'),fg='black',bg='grey')
        label_guess_points=tk.Label(text='%s\n\n%s\n\n%s\n\n%s\n\n%s\n\n%s\n\n%s\n\n%s\n\n%s\n\n%s'%(display_scores_list[page_number*10-10+0][8],display_scores_list[page_number*10-10+1][8],display_scores_list[page_number*10-10+2][8],display_scores_list[page_number*10-10+3][8],display_scores_list[page_number*10-10+4][8],display_scores_list[page_number*10-10+5][8],display_scores_list[page_number*10-10+6][8],display_scores_list[page_number*10-10+7][8],display_scores_list[page_number*10-10+8][8],display_scores_list[page_number*10-10+9][8]),font=(None,15,'bold'),fg='black',bg='grey')
        label_math_points=tk.Label(text='%s\n\n%s\n\n%s\n\n%s\n\n%s\n\n%s\n\n%s\n\n%s\n\n%s\n\n%s'%(display_scores_list[page_number*10-10+0][9],display_scores_list[page_number*10-10+1][9],display_scores_list[page_number*10-10+2][9],display_scores_list[page_number*10-10+3][9],display_scores_list[page_number*10-10+4][9],display_scores_list[page_number*10-10+5][9],display_scores_list[page_number*10-10+6][9],display_scores_list[page_number*10-10+7][9],display_scores_list[page_number*10-10+8][9],display_scores_list[page_number*10-10+9][9]),font=(None,15,'bold'),fg='black',bg='grey')
        label_total_points=tk.Label(text='%s\n\n%s\n\n%s\n\n%s\n\n%s\n\n%s\n\n%s\n\n%s\n\n%s\n\n%s'%(display_scores_list[page_number*10-10+0][10],display_scores_list[page_number*10-10+1][10],display_scores_list[page_number*10-10+2][10],display_scores_list[page_number*10-10+3][10],display_scores_list[page_number*10-10+4][10],display_scores_list[page_number*10-10+5][10],display_scores_list[page_number*10-10+6][10],display_scores_list[page_number*10-10+7][10],display_scores_list[page_number*10-10+8][10],display_scores_list[page_number*10-10+9][10]),font=(None,15,'bold'),fg='black',bg='grey')

        label_tictactoe_points.place(x=242,y=175,width=88)
        label_rockpapersci_points.place(x=342,y=175,width=88)
        label_snakesandladders_points.place(x=442,y=175,width=88)
        label_handcricket_points.place(x=542,y=175,width=88)
        label_quadraticequation_points.place(x=642,y=175,width=88)
        label_cards_points.place(x=742,y=175,width=88)
        label_memory_points.place(x=842,y=175,width=88)
        label_hangman_points.place(x=942,y=175,width=88)
        label_guess_points.place(x=1042,y=175,width=88)
        label_math_points.place(x=1142,y=175,width=88)
        label_total_points.place(x=1242,y=175,width=88)

        scale_page=tk.Scale(from_=1,to=total_pages,orient='horizontal',length=1294,bg='black',fg='white',highlightbackground='black',font=('copperplate gothic bold',25,'bold'),command=change_page,tickinterval=1)
        scale_page.place(x=34,y=650)
        button_quit=tk.Button(text='X',font=('Copperplate Gothic Bold',20,'bold'),fg='red',bg='black',command=lambda:sound_player(sound_button,screen))
        button_quit.place(x=1302,y=2,height=33,width=60)
        screen.mainloop()
    elif game=='k':
        bglist=['supportfile/Userstatus\\Background\\Background (1).png', 'supportfile/Userstatus\\Background\\Background (10).png', 'supportfile/Userstatus\\Background\\Background (11).png', 'supportfile/Userstatus\\Background\\Background (12).png', 'supportfile/Userstatus\\Background\\Background (2).png', 'supportfile/Userstatus\\Background\\Background (3).png', 'supportfile/Userstatus\\Background\\Background (4).png', 'supportfile/Userstatus\\Background\\Background (5).png', 'supportfile/Userstatus\\Background\\Background (6).png', 'supportfile/Userstatus\\Background\\Background (7).png', 'supportfile/Userstatus\\Background\\Background (8).png', 'supportfile/Userstatus\\Background\\Background (9).png']
        r.shuffle(bglist)
        bgcount=0
        cur=connect.cursor()
        def userdata():
            global data,status
            cur.execute('select * from userpwd')
            data=cur.fetchall()
            listdata=[]
            for i in data:
                listdata+=[[i[0],i[1],i[2]]]
            data=listdata
            status=''
            for i in data:
                if i[2]=='Y':
                    status=i[0]
                    break
        userdata()
        def signin():
            sound_player(sound_button)
            global data
            global eyeimg1
            global eyeimg2
            global show
            widgets_state('disabled',[sign,log,change,remove])
            def Back():
                widgets_destroy([headsign,usern,pawd,submit,eyebut,back,u,p])
                widgets_state('normal',[sign,log,change,remove])
            def sub():
                global data
                global status
                l=c=r=0
                user=usern.get()
                if user=='' or pawd.get()=='':
                    error=tk.Label(text='Username or Password cannot be None',font=('Copperplate gothic bold',15 ,'bold'))
                    error.place(x=683-250,y=400,width=500)
                    error.after(3000,error.destroy)
                    r=1
                if len(user)>15 or len(pawd.get())>15:
                    l=1
                    error=tk.Label(text='Username or Password cannot\nbe more than 15 characters',font=('Copperplate gothic bold',15 ,'bold'))
                    error.place(x=683-250,y=400,width=500)
                    error.after(3000,error.destroy)
                if r==0 and l==0:
                    for i in data:
                        if i[0]==user:
                            error=tk.Label(text='Username already in use',font=('Copperplate gothic bold',20 ,'bold'),fg='red')
                            error.place(x=683-200,y=400,width=400)
                            error.after(3000,error.destroy)
                            c=1
                            break
                    if c==0:
                        pwd=pawd.get()
                        cur.execute('insert into userpwd values'+str((user,pwd,'N')))
                        connect.commit()
                        cur.execute('insert into leaderboard values'+str((user,0,0,0,0,0,0,0,0,0,0,0)))
                        connect.commit()
                        userdata()
                        success=tk.Label(text='User added!',fg='Green',font=('Copperplate gothic bold',20,'bold'))
                        success.place(x=683-200,y=400,width=400)
                        success.after(3000,success.destroy)
                usern.delete(0,len(usern.get()))
                pawd.delete(0,len(pawd.get()))
                state.configure(text='HEY THERE\n%s'%(status))
                widgets_state('normal',[sign,log,change,remove])
                widgets_destroy([headsign,usern,pawd,submit,eyebut,back,u,p])
            def eye():
                global show
                if show==0:
                    pawd.configure(show='')
                    eyebut.configure(image=eyeimg1)
                    show=1
                else:# the but is open
                    pawd.configure(show='*')
                    eyebut.configure(image=eyeimg2)
                    show=0
            headsign=tk.Label(text='SIGN IN',font=('Copperplate gothic bold',20 ,'bold'),fg='white',bg='black')
            headsign.place(x=683-100,y=100,width=200)
            eyeimg1=tk.PhotoImage(file='supportfile/Userstatus/Eye1.png')
            eyeimg2=tk.PhotoImage(file='supportfile/Userstatus/Eye2.png')
            u=tk.Label(text='Username',font=('Copperplate gothic bold',20 ,'bold'))
            p=tk.Label(text='Password',font=('Copperplate gothic bold',20 ,'bold'))
            usern=tk.Entry(font=(None,15,'bold' ))
            pawd=tk.Entry(font=(None,15,'bold' ),show='*')
            eyebut=tk.Button(command=eye,image=eyeimg2)
            show=0
            submit=tk.Button(text='Submit',bg='light blue',font=('Copperplate gothic bold',15 ,'bold'),command=sub)
            back=tk.Button(text='Go back',font=('Copperplate gothic bold',15 ),bg='pink',command=Back)
            u.place(x=683-275,y=200,width=200)
            p.place(x=683-275,y=250,width=200)
            usern.place(x=683-50,y=200,width=300)
            pawd.place(x=683-50,y=250,width=275)
            eyebut.place(x=683+220,y=251)
            submit.place(x=683-100,y=300,width=200)
            back.place(x=683-75,y=350,width=150)

        def loginout():
            sound_player(sound_button)
            global data
            global eyeimg1
            global eyeimg2
            global show
            widgets_state('disabled',[sign,log,change,remove])
            def Back():
                widgets_destroy([headsign,usern,pawd,submit,eyebut,back,u,p])
                widgets_state('normal',[sign,log,change,remove])
            def sub():
                global data
                global status
                f=c=r=0
                user=usern.get()
                if user=='' or pawd.get()=='':
                    error=tk.Label(text='Username or Password not valid',font=('Copperplate gothic bold',15 ,'bold'))
                    error.place(x=683-250,y=400,width=500)
                    error.after(3000,error.destroy)
                    sign.configure(state='normal')
                    r=1
                if r==0:
                    for i in data:
                        if i[0]==user:
                            c=1
                            break
                    if c==1:
                        pwd=pawd.get()
                        for i in data:
                            if i[0]==user:
                                if i[1]==pwd:
                                    success=tk.Label(text='Logged in',fg='Green',font=('Copperplate gothic bold',20,'bold'))
                                    success.place(x=683-200,y=400,width=400)
                                    success.after(3000,success.destroy)
                                    log.configure(text='Logout')
                                    cur.execute('update userpwd set status="Y" where username="'+str(user)+'"')
                                    connect.commit()
                                    userdata()
                                    break
                                else:
                                    f=1
                        if f==1:
                            error=tk.Label(text='Password not right',fg='red',font=('Copperplate gothic bold',20,'bold'))
                            error.place(x=683-200,y=400,width=400)
                            error.after(3000,error.destroy)  
                            sign.configure(state='normal')  
                    else:
                        error=tk.Label(text='Username not available',fg='red',font=('Copperplate gothic bold',20,'bold'))
                        error.place(x=683-200,y=400,width=400)
                        error.after(3000,error.destroy)
                        sign.configure(state='normal')
                widgets_state('normal',[log,change,remove])
                widgets_destroy([headsign,usern,pawd,submit,eyebut,back,u,p])
                state.configure(text='HEY THERE\n%s'%(status))
            def Log():
                global status
                for i in data:
                    if i[0]==status:
                        cur.execute('update userpwd set status="N" where username="'+str(status)+'"')
                        connect.commit()
                        userdata()
                state.configure(text='HEY THERE\n%s'%(status))
                widgets_destroy([headsign,ask,notask])
                success=tk.Label(text='Logged out',fg='Green',font=('Copperplate gothic bold',20,'bold'))
                success.place(x=683-200,y=400,width=400)
                success.after(3000,success.destroy)
                widgets_state('normal',[sign,log,change,remove])
                log.configure(text='Login')
            def delete():
                widgets_state('normal',[log,change,remove])
                widgets_destroy([headsign,ask,notask])
            def eye():
                global show
                if show==0:
                    pawd.configure(show='')
                    eyebut.configure(image=eyeimg1)
                    show=1
                else:
                    pawd.configure(show='*')
                    eyebut.configure(image=eyeimg2)
                    show=0
            headsign=tk.Label(text='LOGIN/LOGOUT',font=('Copperplate gothic bold',19 ,'bold'),fg='white',bg='black')
            headsign.place(x=683-125,y=100,width=250)
            if status!='':
                ask=tk.Button(text='Already logged in!\nClick to log out',font=('Copperplate gothic bold',19 ,'bold'),command=Log,bg='light blue')
                ask.place(x=683-200,y=200,width=400)
                notask=tk.Button(text='Click to go back',font=('Copperplate gothic bold',19 ,'bold'),command=delete,bg='pink')
                notask.place(x=683-125,y=300,width=250)
            else:
                eyeimg1=tk.PhotoImage(file='supportfile/Userstatus/Eye1.png')
                eyeimg2=tk.PhotoImage(file='supportfile/Userstatus/Eye2.png')
                u=tk.Label(text='Username',font=('Copperplate gothic bold',20 ,'bold'))
                p=tk.Label(text='Password',font=('Copperplate gothic bold',20 ,'bold'))
                usern=tk.Entry(font=(None,15,'bold'))
                pawd=tk.Entry(font=(None,15,'bold'),show='*')
                eyebut=tk.Button(command=eye,image=eyeimg2)
                show=0
                submit=tk.Button(text='Submit',bg='light blue',font=('Copperplate gothic bold',15 ,'bold'),command=sub)
                back=tk.Button(text='Go back',font=('Copperplate gothic bold',15 ),bg='pink',command=Back)
                back.place(x=683-100,y=350,width=200)
                u.place(x=683-275,y=200,width=200)
                p.place(x=683-275,y=250,width=200)
                usern.place(x=683-50,y=200,width=300)
                pawd.place(x=683-50,y=250,width=275)
                eyebut.place(x=683+220,y=251)
                submit.place(x=683-100,y=300,width=200)
        def removeuser():
            sound_player(sound_button)
            global data
            global eyeimg1
            global eyeimg2
            global show
            widgets_state('disabled',[sign,log,change,remove])
            def Back():
                widgets_state('normal',[sign,log,change,remove])
                widgets_destroy([headsign,usern,pawd,submit,eyebut,back,u,p])
            def sub():
                global data
                global status
                f=c=r=0
                user=usern.get()
                if user=='' or pawd.get()=='':
                    error=tk.Label(text='Username or Password not valid',font=('Copperplate gothic bold',15 ,'bold'))
                    error.place(x=683-250,y=400,width=500)
                    error.after(3000,error.destroy)
                    sign.configure(state='normal')
                    r=1
                if r==0:
                    for i in data:
                        if i[0]==user:
                            c=1
                            break
                    if c==1:
                        pwd=pawd.get()
                        for i in data:
                            if i[0]==user:
                                if i[1]==pwd:
                                    success=tk.Label(text='Username removed',fg='Green',font=('Copperplate gothic bold',20,'bold'))
                                    success.place(x=683-200,y=400,width=400)
                                    success.after(3000,success.destroy)
                                    status='N'
                                    log.configure(text='Login')
                                    data.remove(i)
                                    cur.execute('delete from userpwd where username="'+str(user)+'"')
                                    connect.commit()
                                    userdata()
                                    break
                                else:
                                    f=1
                        if f==1:
                            error=tk.Label(text='Password not right',fg='red',font=('Copperplate gothic bold',20,'bold'))
                            error.place(x=683-200,y=400,width=400)
                            error.after(3000,error.destroy)  
                            sign.configure(state='normal')  
                    else:
                        error=tk.Label(text='Username not available',fg='red',font=('Copperplate gothic bold',20,'bold'))
                        error.place(x=683-200,y=400,width=400)
                        error.after(3000,error.destroy)
                        sign.configure(state='normal')
                widgets_state('normal',[sign,log,change,remove])
                widgets_destroy([headsign,usern,pawd,submit,eyebut,back,u,p])
                state.configure(text='HEY THERE\n%s'%(status))
            def Log():
                global status
                for i in data:
                    if i[0]==status:
                        cur.execute('delete from userpwd where username="'+str(status)+'"')
                        connect.commit()
                        userdata()
                state.configure(text='HEY THERE\n%s'%(status))
                log.configure(text='Login')
                success=tk.Label(text='Username removed',fg='Green',font=('Copperplate gothic bold',20,'bold'))
                success.place(x=683-200,y=400,width=400)
                success.after(3000,success.destroy)
                widgets_state('normal',[sign,log,change,remove])
                widgets_destroy([headsign,ask,notask])
                log.configure(text='Login')
            def delete():
                widgets_state('normal',[log,change,remove])
                widgets_destroy([headsign,ask,notask])
            def eye():
                global show
                if show==0:
                    pawd.configure(show='')
                    eyebut.configure(image=eyeimg1)
                    show=1
                else:# the but is open
                    pawd.configure(show='*')
                    eyebut.configure(image=eyeimg2)
                    show=0
            headsign=tk.Label(text='REMOVE USER',font=('Copperplate gothic bold',19 ,'bold'),fg='white',bg='black')
            headsign.place(x=683-125,y=100,width=250)
            if status!='':
                ask=tk.Button(text='Already logged in\nClick to Remove',font=('Copperplate gothic bold',19 ,'bold'),command=Log,bg='light blue')
                ask.place(x=683-200,y=200,width=400)
                notask=tk.Button(text='Click to go back',font=('Copperplate gothic bold',19 ,'bold'),command=delete,bg='pink')
                notask.place(x=683-125,y=300,width=250)
            else:
                eyeimg1=tk.PhotoImage(file='supportfile/Userstatus/Eye1.png')
                eyeimg2=tk.PhotoImage(file='supportfile/Userstatus/Eye2.png')
                u=tk.Label(text='Username',font=('Copperplate gothic bold',20 ,'bold'))
                p=tk.Label(text='Password',font=('Copperplate gothic bold',20 ,'bold'))
                usern=tk.Entry(font=(None,15,'bold' ))
                pawd=tk.Entry(font=(None,15,'bold' ),show='*')
                eyebut=tk.Button(command=eye,image=eyeimg2)
                show=0
                submit=tk.Button(text='Submit',bg='light blue',font=('Copperplate gothic bold',15 ,'bold'),command=sub)
                back=tk.Button(text='Go back',font=('Copperplate gothic bold',15 ),bg='pink',command=Back)
                back.place(x=683-75,y=350,width=150)
                u.place(x=683-275,y=200,width=200)
                p.place(x=683-275,y=250,width=200)
                usern.place(x=683-50,y=200,width=300)
                pawd.place(x=683-50,y=250,width=275)
                eyebut.place(x=683+220,y=251)
                submit.place(x=683-100,y=300,width=200)
        def changepass():
            sound_player(sound_button)
            global data
            global eyeimg1
            global eyeimg2
            global show
            widgets_state('disabkled',[sign,log,change,remove])
            def Back():
                widgets_state('normal',[sign,log,change,remove])
                widgets_destroy([headsign,usern,pawd,submit,eyebut,back,u,p,np,npass])
            def sub():
                global data
                global status
                f=c=r=0
                user=usern.get()
                if user=='' or pawd.get()=='' or npass.get()=='':
                    error=tk.Label(text='Username or Password not valid',font=('Copperplate gothic bold',15 ,'bold'))
                    error.place(x=683-250,y=400,width=500)
                    error.after(3000,error.destroy)
                    sign.configure(state='normal')
                    r=1
                if r==0:
                    for i in data:
                        if i[0]==user:
                            c=1
                            break
                    if c==1:
                        pwd=pawd.get()
                        for i in data:
                            if i[0]==user:
                                if i[1]==pwd:
                                    success=tk.Label(text='Password changed',fg='Green',font=('Copperplate gothic bold',20,'bold'))
                                    success.place(x=683-200,y=400,width=400)
                                    success.after(3000,success.destroy)
                                    cur.execute('update userpwd set password="'+str(npass.get())+'" where username="'+str(user)+'"')
                                    connect.commit()
                                    userdata()
                                    break
                                else:
                                    f=1
                        if f==1:
                            error=tk.Label(text='Password not right',fg='red',font=('Copperplate gothic bold',20,'bold'))
                            error.place(x=683-200,y=400,width=400)
                            error.after(3000,error.destroy)  
                            sign.configure(state='normal')  
                    else:
                        error=tk.Label(text='Username not available',fg='red',font=('Copperplate gothic bold',20,'bold'))
                        error.place(x=683-200,y=400,width=400)
                        error.after(3000,error.destroy)
                        sign.configure(state='normal')
                widgets_state('normal',[sign,log,change,remove])
                widgets_destroy([headsign,usern,pawd,submit,eyebut,back,u,p,np,npass])
                state.configure(text='HEY THERE\n%s'%(status))
            def Log():
                global status
                for i in data:
                    if i[0]==status:
                        chpass=npass.get()
                        if chpass=='':
                            error=tk.Label(text='Password cannot be None',fg='Green',font=('Copperplate gothic bold',20,'bold'))
                            error.place(x=683-200,y=400,width=400)
                            error.after(3000,error.destroy)
                            break
                        cur.execute('update userpwd set password="'+str(npass.get())+'" where username="'+str(status)+'"')
                        connect.commit()
                        userdata()
                        success=tk.Label(text='Password Changed',fg='Green',font=('Copperplate gothic bold',20,'bold'))
                        success.place(x=683-200,y=400,width=400)
                        success.after(3000,success.destroy)
                state.configure(text='HEY THERE\n%s'%(status))
                widgets_state('normal',[log,change,remove])
                widgets_destroy([headsign,ask,notask,np,npass,eyebut])
            def delete():
                widgets_state('normal',[log,change,remove])
                widgets_destroy([headsign,ask,notask,eyebut,np,npass])
            def eye():
                global show
                if show==0:
                    try:
                        pawd.configure(show='')
                    except:
                        print()
                    npass.configure(show='')
                    eyebut.configure(image=eyeimg1)
                    show=1
                else:
                    try:
                        pawd.configure(show='*')
                    except:
                        print()
                    npass.configure(show='*')
                    eyebut.configure(image=eyeimg2)
                    show=0
            headsign=tk.Label(text='CHANGE PASSWORD',font=('Copperplate gothic bold',19 ,'bold'),fg='white',bg='black')
            headsign.place(x=683-125,y=100,width=250)
            if status!='':
                eyeimg1=tk.PhotoImage(file='supportfile/Userstatus/Eye1.png')
                eyeimg2=tk.PhotoImage(file='supportfile/Userstatus/Eye2.png')
                ask=tk.Button(text='Already Logged in.\nClick to Change Password ',font=('Copperplate gothic bold',19 ,'bold'),command=Log,bg='light blue')
                ask.place(x=683-220,y=200,width=450)
                np=tk.Label(text='Password',font=('Copperplate gothic bold',20 ,'bold'))
                np.place(x=683-275,y=300,width=200)
                npass=tk.Entry(font=(None,15,'bold' ),show='*')
                npass.place(x=683-50,y=300,width=300)
                notask=tk.Button(text='Click to go back',font=('Copperplate gothic bold',19 ,'bold'),command=delete,bg='pink')
                notask.place(x=683-125,y=400,width=250)
                eyebut=tk.Button(command=eye,image=eyeimg2)
                eyebut.place(x=683+220,y=301)
                show=0
            else:
                eyeimg1=tk.PhotoImage(file='supportfile/Userstatus/Eye1.png')
                eyeimg2=tk.PhotoImage(file='supportfile/Userstatus/Eye2.png')
                u=tk.Label(text='Username',font=('Copperplate gothic bold',20 ,'bold'))
                p=tk.Label(text='Password',font=('Copperplate gothic bold',20 ,'bold'))
                np=tk.Label(text='New Password',font=('Copperplate gothic bold',19 ,'bold'))
                npass=tk.Entry(font=(None,15,'bold' ),show='*')
                usern=tk.Entry(font=(None,15,'bold' ))
                pawd=tk.Entry(font=(None,15,'bold' ),show='*')
                eyebut=tk.Button(command=eye,image=eyeimg2)
                show=0
                submit=tk.Button(text='Submit',bg='light blue',font=('Copperplate gothic bold',15 ,'bold'),command=sub)
                back=tk.Button(text='Go back',font=('Copperplate gothic bold',15 ),bg='pink',command=Back)
                u.place(x=683-275,y=200,width=200)
                p.place(x=683-275,y=250,width=200)
                np.place(x=683-275,y=300,width=200)
                usern.place(x=683-50,y=200,width=300)
                pawd.place(x=683-50,y=250,width=300)
                npass.place(x=683-50,y=300,width=300)
                eyebut.place(x=683+220,y=251)
                submit.place(x=683-100,y=350,width=200) 
                back.place(x=683-75,y=400,width=150)

        def backgroundchange():
            global bgcount
            global bgimg
            bgcount+=1
            bgimg=tk.PhotoImage(file=bglist[bgcount%len(bglist)])
            bg.configure(image=bgimg)
            bg.after(7500,backgroundchange)
        screen=tk.Tk()
        screen.attributes('-fullscreen',True)
        screen.focus_force()
        

        bgimg=tk.PhotoImage()
        bg=tk.Label(fg='white',font=('Copperplate gothic bold',35 ,'bold'),compound='c',image=bgimg)
        bg.place(x=-3,y=-3)
        backgroundchange()
        state=tk.Label(text='HEY THERE\n%s'%(status),font=(None,20,'bold'),fg='white',bg='black')
        state.place(x=683-200,y=625,width=400,height=75)
        sign=tk.Button(text='Sign Up',bg='black',fg='white',font=('Copperplate gothic bold',20 ,'bold'),command=signin)
        sign.place(x=683-200,y=450,width=400)
        log=tk.Button(text='Login',bg='black',fg='white',font=('Copperplate gothic bold',20 ,'bold'),command=loginout)
        log.place(x=683-200,y=510,width=400)
        if status!='':
            sign.configure(state='disabled')
            log.configure(text='Logout')
        change=tk.Button(text='Change password',bg='black',fg='white',font=('Copperplate gothic bold',13),command=changepass)
        change.place(x=683-200,y=575,width=190,height=40)
        remove=tk.Button(text='Remove account',bg='black',fg='white',font=('Copperplate gothic bold',13),command=removeuser)
        remove.place(x=683+10,y=575,width=190,height=40)
        button_quit=tk.Button(text='QUIT',font=('Copperplate Gothic Bold',20,'bold'),fg='red',bg='black',command=lambda:sound_player(sound_button,screen))
        button_quit.place(x=45,y=675,width=150)
        screen.mainloop()
        cur.close()
    elif game=='l':
        check_score(10)
        screen=tk.Tk()
        screen.attributes('-fullscreen',True)
        screen.focus_force()
        

        tk_photoimage_bg=tk.PhotoImage(file='supportfile/Math Game\\Game.png')
        label_bg=tk.Label(text='MATH GAME\n\n\n\n\n\n\n\n\n\n\n\n',font=('copperplate gothic bold',35,'bold'),compound='c',image=tk_photoimage_bg)
        label_bg.place(x=0,y=0)
        def game_start():
            sound_player(sound_button)
            global list_solution,list_equation,chance,num_correct
            num_correct=0
            chance=0
            list_solution=[]
            list_equation=[]
            for i in range(5):
                oper=r.choice(['+','-','*'])
                if oper=='+' or oper=='-':
                    equ=str(r.randint(10,100))+oper+''+str(r.randint(10,100))
                elif oper=='*':
                    equ=str(r.randint(5,25))+oper+''+str(r.randint(5,25))
                list_equation+=[equ]
                list_solution+=[eval(equ)]
            print(list_solution)
            print(list_equation)
            button_game.destroy()
            game_continue()

        def game_continue():
            global chance,label_bg,label_answer,entry_answer,button_proceed
            def end():
                global button_game,label_bg
                button_proceed.destroy()
                label_bg.configure(text='MATH GAME\n\n\n\n\n\n\n\n\n\n\n\n')
                button_game=tk.Button(text='START',font=('copperplate gothic bold',20,'bold'),bg='black',fg='lime',command=game_start)
                button_game.place(x=683-75,y=300)
            def game_proceed():
                global total_score,score,num_correct,label_total_score,chance
                def delete():
                    widgets_destroy([button_proceed,label_answer,entry_answer])                    
                    game_continue()
                try:
                    answer=entry_answer.get()
                    answer=int(answer)
                    datatype='int'
                except:
                    answer=''
                    datatype='something'
                if answer==solution:
                    label_error=tk.Label(text='CORRECT ANSWER',font=('copperplate gothic bold',14,'bold'),bg='black',fg='lime')
                    label_error.place(x=683-250,y=450,width=500) 
                    label_error.after(1000,label_error.destroy)
                    screen.after(1000,delete)
                    score+=2
                    total_score+=2
                    num_correct+=1
                    if current_login!=None:
                        label_total_score.configure(text='Total Score\n%s\nScore this round\n%s'%(total_score,score))
                else:
                    if datatype=='something':
                        label_error=tk.Label(text='PLEASE ENTER INTEGERS ONLY',font=('copperplate gothic bold',14,'bold'),bg='black',fg='red')
                        label_error.place(x=683-250,y=450,width=500)
                        label_error.after(2500,label_error.destroy)
                    else:
                        label_error=tk.Label(text='WRONG ANSWER',font=('copperplate gothic bold',14,'bold'),bg='black',fg='red')
                        label_error.place(x=683-250,y=450,width=500)
                        label_error.after(1000,label_error.destroy)
                        screen.after(1000,delete)
                button_proceed.configure(state='disabled')    
                button_proceed.after(2500,lambda: button_proceed.configure(state='normal'))
            if chance<5:
                equation=list_equation[chance]
                solution=list_solution[chance]
                chance+=1
                label_bg.configure(text='EVALUATE THE EXPRESSION\n\n\n'+equation+'=\n\n\n\n\n\n\n\n\n')
                button_proceed=tk.Button(text='CONFIRM',font=('copperplate gothic bold',14,'bold'),bg='black',fg='lime',command=game_proceed)
                button_proceed.place(x=683-100,y=550,width=200)
                label_answer=tk.Label(text='ANSWER',font=('copperplate gothic bold',25,'bold'),bg='black',fg='light blue')
                label_answer.place(x=683-100,y=300,width=200)
                entry_answer=tk.Entry(font=('copperplate gothic bold',24,'bold'))
                entry_answer.place(x=683-40,y=350,width=80,height=75)
            else:
                label_bg.configure(text='FIVE QUESTIONS ARE OVER\n\n\n\nYOU GOT %s OUT OF 5\n\n\n\n\n\n\n\n'%(num_correct))
                button_proceed=tk.Button(text='CONTINUE',font=('copperplate gothic bold',14,'bold'),bg='black',fg='lime',command=end)
                button_proceed.place(x=683-100,y=550,width=200)
        button_game=tk.Button(text='START',font=('copperplate gothic bold',20,'bold'),bg='black',fg='lime',command=game_start)
        button_game.place(x=683-75,y=300,width=150)
        button_quit=tk.Button(text='QUIT',font=('copperplate gothic bold',20,'bold'),bg='black',fg='red',command=lambda:sound_player(sound_button,screen))
        button_quit.place(x=683-75,y=600,width=150)
        if current_login!=None:
            label_total_score=tk.Label(text='Total Score\n%s\nScore this round\n%s'%(total_score,score),font=('copperplate gothic bold',15,'bold'),fg='#73f5fc',bg='black')
            label_total_score.place(x=1115,y=35,width=220)
        screen.mainloop()
        try:
            overall_total_score+=score
            connect=my.connect(host ='localhost',user=user,passwd=pwd,database=db)
            cur=connect.cursor()
            cur.execute('update leaderboard set mathgame='+str(total_score)+',overall='+str(overall_total_score)+' where username="'+str(current_login)+'"')
            connect.commit()
        except:
            print(current_login)
    elif game=='m': 
        break