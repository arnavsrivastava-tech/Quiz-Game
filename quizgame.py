
from tkinter import * #Asterisk means importing all the functions
from tkinter import ttk  #ttk is another important function(helps multiple windows of same size to be flashed)

y = 0
a =  ttk.Notebook()      #notebook(built-in) function helps us to questions are displayed properly 

frame1 = ttk.Frame(a) # frames = number of questions
frame2 = ttk.Frame(a)
frame3 = ttk.Frame(a)
frame4 = ttk.Frame(a)
frame5 = ttk.Frame(a)
frame6 = ttk.Frame(a)
frame7 = ttk.Frame(a)
frame8 = ttk.Frame(a)
frame9 = ttk.Frame(a)
frame10 = ttk.Frame(a)
frame11 = ttk.Frame(a)
frame12 = ttk.Frame(a)
ResultFrame = ttk.Frame(a)



root = ttk.Frame(a)  #window/root for ttk

def quiz(a): 
    a.add(frame1, text= "Q1")
    a.add(frame2, text= "Q2")
    a.add(frame3, text= "Q3")
    a.add(frame4, text= "Q4")
    a.add(frame5, text= "Q5")
    a.add(frame6, text= "Q6")
    a.add(frame7, text= "Q7")
    a.add(frame8, text= "Q8")
    a.add(frame9, text= "Q9")
    a.add(frame10, text= "Q10")
    a.add(frame11, text= "Q11")    
    a.add(frame12, text= "Q12")
    a.add(ResultFrame, text="Result")

    
   
    Label (frame1, text = "What is the largest organ in the human body by weight?", font=("Lexend", 30,"bold")).grid(row=2,column=2)
    Button(frame1, text= "Kidney", font= ("Lexend",20,"bold"), bg="light blue",command=a_wrong).grid(row=3, column=1 )
    Button(frame1, text= "Liver", font= ("Lexend",20,"bold"),bg="light blue",command=a_correct).grid(row=3, column=2 )
    Button(frame1, text= "Skin", font= ("Lexend",20,"bold"),bg="light blue",command=a_wrong).grid(row=4, column=1 )
    Button(frame1, text= "Intestine", font= ("Lexend",20,"bold"),bg="light blue",command=a_wrong).grid(row=4, column=2 )

    Label (frame2, text = "Who is the highest wicket-taker in the history of Test cricket?", font=("Lexend", 30,"bold")).grid(row=2,column=2)
    Button(frame2, text= "James Anderson", font= ("Lexend",20,"bold"),bg="light blue",command=a2_wrong).grid(row=3, column=1 )
    Button(frame2, text= "Anil Kumble", font= ("Lexend",20,"bold"),bg="light blue",command=a2_wrong).grid(row=3, column=2 )
    Button(frame2, text= "Muttiah Muralitharan", font= ("Lexend",20,"bold"),bg="light blue",command=a2_correct).grid(row=4, column=1 )
    Button(frame2, text= "Shane Warne", font= ("Lexend",20,"bold"),bg="light blue",command=a2_wrong).grid(row=4, column=2 )

    Label (frame3, text = "Which Indian city is considered the Silicon Valley of India?", font=("Lexend", 30,"bold")).grid(row=2,column=2)
    Button(frame3, text= "Mumbai", font= ("Lexend",20,"bold"),bg="light blue",command=a3_wrong).grid(row=3, column=1 )
    Button(frame3, text= "Heydrabad", font= ("Lexend",20,"bold"),bg="light blue",command=a3_wrong).grid(row=3, column=2)
    Button(frame3, text= "Kolkata", font= ("Lexend",20,"bold"),bg="light blue",command=a3_wrong).grid(row=4, column=1 )
    Button(frame3, text= "Bengaluru", font= ("Lexend",20,"bold"),bg="light blue",command=a3_correct).grid(row=4, column=2 )

    Label (frame4, text = "What car is the fastest fuel car till 2023 in the world?", font=("Lexend", 30,"bold")).grid(row=2,column=2)
    Button(frame4, text= "Lamborghini Revuelto", font= ("Lexend",20,"bold"),bg="light blue",command=a4_wrong).grid(row=3, column=1 )
    Button(frame4, text= "Buggati Chiron Supersport", font= ("Lexend",20,"bold"),bg="light blue",command=a4_wrong).grid(row=3, column=2 )
    Button(frame4, text= "Nissan GTR", font= ("Lexend",20,"bold"),bg="light blue",command=a4_wrong).grid(row=4, column=1 )
    Button(frame4, text= "Koenigsegg Jesko Absolut", font= ("Lexend",20,"bold"),bg="light blue",command=a4_correct).grid(row=4, column=2 )

    Label(frame5, text="Which movie has generated the most money till date?", font=("Lexend", 30, "bold")).grid(row=2, column=2)
    Button(frame5, text="Avengers: Endgame", font=("Lexend", 20, "bold"), bg="light blue",command=a5_wrong).grid(row=3, column=1)
    Button(frame5, text="Avatar", font=("Lexend", 20, "bold"), bg="light blue",command=a5_correct).grid(row=3, column=2)
    Button(frame5, text="Avatar: Way of water", font=("Lexend", 20, "bold"), bg="light blue",command=a5_wrong).grid(row=4, column=1)
    Button(frame5, text="Titanic", font=("Lexend", 20, "bold"), bg="light blue",command=a5_wrong).grid(row=4, column=2)


    Label(frame6, text="Who was the first person to step on the moon?", font=("Lexend", 30, "bold")).grid(row=2, column=2)
    Button(frame6, text="Alexandar Graham Bell", font=("Lexend", 20, "bold"), bg="light blue",command=a6_wrong).grid(row=3, column=1)
    Button(frame6, text="Nikola Tesla", font=("Lexend", 20, "bold"), bg="light blue",command=a6_wrong).grid(row=3, column=2)
    Button(frame6, text="Niel Armstrong", font=("Lexend", 20, "bold"), bg="light blue",command=a6_correct).grid(row=4, column=1)
    Button(frame6, text="Lamar Junior", font=("Lexend", 20, "bold"), bg="light blue",command=a6_wrong).grid(row=4, column=2)

    Label(frame7, text="Who killed Mahatma Gandhi?", font=("Lexend", 30, "bold")).grid(row=2, column=2)
    Button(frame7, text="Nathuram Godse", font=("Lexend", 20, "bold"), bg="light blue",command=a7_correct).grid(row=3, column=1)
    Button(frame7, text="Subhash Chandra Bose", font=("Lexend", 20, "bold"), bg="light blue",command=a7_wrong).grid(row=3, column=2)
    Button(frame7, text="Jawahal Lal Nehru", font=("Lexend", 20, "bold"), bg="light blue",command=a7_wrong).grid(row=4, column=1)
    Button(frame7, text="Bhagat Singh", font=("Lexend", 20, "bold"), bg="light blue",command=a7_wrong).grid(row=4, column=2)

    Label(frame8, text="Which Youtube channel has the most Subscribers on the planet?", font=("Lexend", 30, "bold")).grid(row=2, column=2)
    Button(frame8, text="Pewdepie", font=("Lexend", 20, "bold"), bg="light blue",command=a8_wrong).grid(row=3, column=1)
    Button(frame8, text="T-Series", font=("Lexend", 20, "bold"), bg="light blue",command=a8_correct).grid(row=3, column=2)
    Button(frame8, text="Saurav joshi vlogs", font=("Lexend", 20, "bold"), bg="light blue",command=a8_wrong).grid(row=4, column=1)
    Button(frame8, text="Mr Beast", font=("Lexend", 20, "bold"), bg="light blue",command=a8_wrong).grid(row=4, column=2)

    Label(frame9, text="Which land animal is the fastest in the world?", font=("Lexend", 30, "bold")).grid(row=2, column=2)
    Button(frame9, text="Cheetah", font=("Lexend", 20, "bold"), bg="light blue",command=a9_correct).grid(row=3, column=1)
    Button(frame9, text="Black Horse", font=("Lexend", 20, "bold"), bg="light blue",command=a9_wrong).grid(row=3, column=2)
    Button(frame9, text="Leopard", font=("Lexend", 20, "bold"), bg="light blue",command=a9_wrong).grid(row=4, column=1)
    Button(frame9, text="Rabit", font=("Lexend", 20, "bold"), bg="light blue",command=a9_wrong).grid(row=4, column=2)

    Label(frame10, text="Who has the most hundreds in ODI cricket?", font=("Lexend", 30, "bold")).grid(row=2, column=2)
    Button(frame10, text="Virat Kohli", font=("Lexend", 20, "bold"), bg="light blue",command=a10_correct).grid(row=3, column=1)
    Button(frame10, text="Sachin Tendulkar", font=("Lexend", 20, "bold"), bg="light blue",command=a10_wrong).grid(row=3, column=2)
    Button(frame10, text="Ricky Ponting", font=("Lexend", 20, "bold"), bg="light blue",command=a10_wrong).grid(row=4, column=1)
    Button(frame10, text="AB De Villiers", font=("Lexend", 20, "bold"), bg="light blue",command=a10_wrong).grid(row=4, column=2)

    Label(frame11, text="Who is the fastest person in the DC comics?", font=("Lexend", 30, "bold")).grid(row=2, column=2)
    Button(frame11, text="The Runner", font=("Lexend", 20, "bold"), bg="light blue",command=a11_wrong).grid(row=3, column=1)
    Button(frame11, text="The Flash", font=("Lexend", 20, "bold"), bg="light blue",command=a11_correct).grid(row=3, column=2)
    Button(frame11, text="Superman", font=("Lexend", 20, "bold"), bg="light blue",command=a11_wrong).grid(row=4, column=1)
    Button(frame11, text="Zoom", font=("Lexend", 20, "bold"), bg="light blue",command=a11_wrong).grid(row=4, column=2)

    Label(frame12, text="Which game won the GAME OF THE YEAR award in 2018?", font=("Lexend", 30, "bold")).grid(row=2, column=2)
    Button(frame12, text="Read Dead Redemption II", font=("Lexend", 20, "bold"), bg="light blue",command=a12_wrong).grid(row=3, column=1)
    Button(frame12, text="God Of War 2018", font=("Lexend", 20, "bold"), bg="light blue",command=a12_correct).grid(row=3, column=2)
    Button(frame12, text="Resident Evil 2 Remake", font=("Lexend", 20, "bold"), bg="light blue",command=a12_wrong).grid(row=4, column=1)
    Button(frame12, text="Elden Ring", font=("Lexend", 20, "bold"), bg="light blue",command=a12_wrong).grid(row=4, column=2)

    Label(ResultFrame, text="Result", font=("Lexend", 30, "bold"), fg="dark green").grid(row=1, column=2, columnspan=8)
    Label(ResultFrame, text="You answered correctly:", font=("Arial", 30, "bold"), fg="dark blue").grid(row=2, column=5)
    Label(ResultFrame, textvariable=total, font=("Arial", 30, "bold"), fg="dark blue").grid(row=2, column=6)
    Label(ResultFrame, text="out of 12 times!", font=("Arial", 30, "bold"), fg="dark blue").grid(row=2, column=7)



  
def a_correct():
    Label(frame1,text="Correct Answer", font=("Arial",20,"bold"),background="green", fg="yellow").grid(row=1,column=1)
    Label(frame1,text="Marks obtained:1",font=("Arial",20),background="black",fg="white").grid(row=1,column=2)
    counter()

def a_wrong():
    Label(frame1,text="Wrong Answer", font=("Arial",20,"bold"),background="Red", fg="yellow").grid(row=1,column=1)
    Label(frame1,text="Marks obtained:0",font=("Arial",20),background="black",fg="white").grid(row=1,column=2)
    counter()

def a2_correct():
    Label(frame2,text="Correct Answer", font=("Arial",20,"bold"),background="green", fg="yellow").grid(row=1,column=1)
    Label(frame2,text="Marks obtained:1",font=("Arial",20),background="black",fg="white").grid(row=1,column=2)
    counter()

def a2_wrong():
    Label(frame2,text="Wrong Answer", font=("Arial",20,"bold"),background="Red", fg="yellow").grid(row=1,column=1)
    Label(frame2,text="Marks obtained:0",font=("Arial",20),background="black",fg="white").grid(row=1,column=2)
    counter()

def a3_correct():
    Label(frame3,text="Correct Answer", font=("Arial",20,"bold"),background="green", fg="yellow").grid(row=1,column=1)
    Label(frame3,text="Marks obtained:1",font=("Arial",20),background="black",fg="white").grid(row=1,column=2)
    counter()

def a3_wrong():
    Label(frame3,text="Wrong Answer", font=("Arial",20,"bold"),background="Red", fg="yellow").grid(row=1,column=1)
    Label(frame3,text="Marks obtained:0",font=("Arial",20),background="black",fg="white").grid(row=1,column=2)
    counter()

def a4_correct():
    Label(frame4,text="Correct Answer", font=("Arial",20,"bold"),background="green", fg="yellow").grid(row=1,column=1)
    Label(frame4,text="Marks obtained:1",font=("Arial",20),background="black",fg="white").grid(row=1,column=2)
    counter()

def a4_wrong():
    Label(frame4,text="Wrong Answer", font=("Arial",20,"bold"),background="Red", fg="yellow").grid(row=1,column=1)
    Label(frame4,text="Marks obtained:0",font=("Arial",20),background="black",fg="white").grid(row=1,column=2)
    counter()

def a5_correct():
    Label(frame5,text="Correct Answer", font=("Arial",20,"bold"),background="green", fg="yellow").grid(row=1,column=1)
    Label(frame5,text="Marks obtained:1",font=("Arial",20),background="black",fg="white").grid(row=1,column=2)
    counter()

def a5_wrong():
    Label(frame5,text="Wrong Answer", font=("Arial",20,"bold"),background="Red", fg="yellow").grid(row=1,column=1)
    Label(frame5,text="Marks obtained:0",font=("Arial",20),background="black",fg="white").grid(row=1,column=2)
    counter()

def a6_correct():
    Label(frame6,text="Correct Answer", font=("Arial",20,"bold"),background="green", fg="yellow").grid(row=1,column=1)
    Label(frame6,text="Marks obtained:1",font=("Arial",20),background="black",fg="white").grid(row=1,column=2)
    counter()

def a6_wrong():
    Label(frame6,text="Wrong Answer", font=("Arial",20,"bold"),background="Red", fg="yellow").grid(row=1,column=1)
    Label(frame6,text="Marks obtained:0",font=("Arial",20),background="black",fg="white").grid(row=1,column=2)
    counter()

def a7_correct():
    Label(frame7,text="Correct Answer", font=("Arial",20,"bold"),background="green", fg="yellow").grid(row=1,column=1)
    Label(frame7,text="Marks obtained:1",font=("Arial",20),background="black",fg="white").grid(row=1,column=2)
    counter()

def a7_wrong():
    Label(frame7,text="Wrong Answer", font=("Arial",20,"bold"),background="Red", fg="yellow").grid(row=1,column=1)
    Label(frame7,text="Marks obtained:0",font=("Arial",20),background="black",fg="white").grid(row=1,column=2)
    counter()

def a8_correct():
    Label(frame8,text="Correct Answer", font=("Arial",20,"bold"),background="green", fg="yellow").grid(row=1,column=1)
    Label(frame8,text="Marks obtained:1",font=("Arial",20),background="black",fg="white").grid(row=1,column=2)
    counter()

def a8_wrong():
    Label(frame8,text="Wrong Answer", font=("Arial",20,"bold"),background="Red", fg="yellow").grid(row=1,column=1)
    Label(frame8,text="Marks obtained:0",font=("Arial",20),background="black",fg="white").grid(row=1,column=2)
    counter()

def a9_correct():
    Label(frame9,text="Correct Answer", font=("Arial",20,"bold"),background="green", fg="yellow").grid(row=1,column=1)
    Label(frame9,text="Marks obtained:1",font=("Arial",20),background="black",fg="white").grid(row=1,column=2)
    counter()

def a9_wrong():
    Label(frame9,text="Wrong Answer", font=("Arial",20,"bold"),background="Red", fg="yellow").grid(row=1,column=1)
    Label(frame9,text="Marks obtained:0",font=("Arial",20),background="black",fg="white").grid(row=1,column=2)
    counter()

def a10_correct():
    Label(frame10,text="Correct Answer", font=("Arial",20,"bold"),background="green", fg="yellow").grid(row=1,column=1)
    Label(frame10,text="Marks obtained:1",font=("Arial",20),background="black",fg="white").grid(row=1,column=2)
    counter()

def a10_wrong():
    Label(frame10,text="Wrong Answer", font=("Arial",20,"bold"),background="Red", fg="yellow").grid(row=1,column=1)
    Label(frame10,text="Marks obtained:0",font=("Arial",20),background="black",fg="white").grid(row=1,column=2)
    counter()

def a11_correct():
    Label(frame11,text="Correct Answer", font=("Arial",20,"bold"),background="green", fg="yellow").grid(row=1,column=1)
    Label(frame11,text="Marks obtained:1",font=("Arial",20),background="black",fg="white").grid(row=1,column=2)
    counter()

def a11_wrong():
    Label(frame11,text="Wrong Answer", font=("Arial",20,"bold"),background="Red", fg="yellow").grid(row=1,column=1)
    Label(frame11,text="Marks obtained:0",font=("Arial",20),background="black",fg="white").grid(row=1,column=2)
    counter()

def a12_correct():
    Label(frame12,text="Correct Answer", font=("Arial",20,"bold"),background="green", fg="yellow").grid(row=1,column=1)
    Label(frame12,text="Marks obtained:1",font=("Arial",20),background="black",fg="white").grid(row=1,column=2)
    counter()

def a12_wrong():
    Label(frame12,text="Wrong Answer", font=("Arial",20,"bold"),background="Red", fg="yellow").grid(row=1,column=1)
    Label(frame12,text="Marks obtained:0",font=("Arial",20),background="black",fg="white").grid(row=1,column=2)



    
def counter():
     total.set(total.get() + 1)

total = IntVar()

quiz(a)

a.pack()    
root.mainloop()

