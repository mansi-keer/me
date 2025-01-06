from tkinter import *
def story(win):
 def final(tl: Toplevel, name, place, city,year,enagedyear, marriedyear):
   text= f'''
      story  
      one day me and {name} 💖 met at {place} 🌆 in {city} 🏙️ but that time we are just friends we enjoyed alot together but never think about each other. Then, slowly-slowly our friendship turns into relationship
      and start dating in {year} 💑 . After, spending so many years we get to know each other better than befor and we decided to get marry . In {enagedyear } 💍 we engaged and lastly,  {marriedyear} 👰💖🤵 we got happily married .'''
   tl.geometry(newGeometry='500x500')

   Label(tl, text=text, font=("Georgia" ,14),wraplength=tl.winfo_width()).place(x=100, y=600)
 NewScreen = Toplevel(win, bg='yellow')

 NewScreen.title("Love story")
 x_position = 800
 NewScreen.geometry('500x500')
 Label(NewScreen,text='Cute Love story',font=("Georgia",20)).place(relx=0.5, y=40, anchor="center")

 Label(NewScreen,text='Enter the name of person you love 💖 :',font=("Georgia",12)).place(x=x_position, y=100)

 Label(NewScreen,text='Enter the place where you met first 🌆 :',font=("Georgia",12)).place(x=x_position, y=150)
 Label(NewScreen,text='Enter the name of city where you met 🏙️ :',font=("Georgia",12)).place(x=x_position, y=200)
 Label(NewScreen,text='Enter the year you start dating 💑:',font=("Georgia",12)).place(x=x_position, y=250)
 Label(NewScreen,text='Enter the year you got engaged 💍 :',font=("Georgia",12)).place(x=x_position, y=300)
 Label(NewScreen,text='Enter the year you got married 👰💖🤵:',font=("Georgia",12)).place(x=x_position, y=350)

 x_position = 1200
 name = Entry(NewScreen, width=17)
 name.place(x=x_position, y=100)
 place=Entry(NewScreen,width=17)
 place.place(x=x_position, y=150)
 city = Entry(NewScreen, width=17)
 city.place(x=x_position, y=200)
 year = Entry(NewScreen, width=17)
 year.place(x=x_position, y=250)
 enagedyear= Entry(NewScreen, width=17)
 enagedyear.place(x=x_position, y=300)
 marriedyear = Entry(NewScreen, width=17)
 marriedyear.place(x=x_position, y=350)
 SubmitButton = Button(NewScreen, text="Submit", background="Blue", font=('Times', 12),
 command=lambda:final(NewScreen, name.get(), place.get(), city.get(), year.get(), enagedyear.get(), marriedyear.get()))
 SubmitButton.place(x=800, y=400)
 NewScreen.mainloop()




"""this is for window setting how will message box open"""
screen = Tk()
screen.title("mad lib calcultor")
screen.geometry=('400x400')
screen.config(bg="darkblue")

Label(screen, text='welcome to mad calculator ',font=("Courier", 20)).place(relx=0.5,y=20 ,anchor="center")
Label(screen, text='Hello ! i am mad calculator . Just clicked on  the below button it will open a dialog box then fill the details it will create a cute story  ',font=("Helvetica", 12)).place(relx=0.5,y=150 ,anchor="center")

storyButton=Button(screen,text='clicked me ', font=("Times New Roman",20),command=lambda :story(screen),bg='white')
storyButton.place(relx=0.5, y=200, anchor="center")

screen.update()
screen.mainloop()