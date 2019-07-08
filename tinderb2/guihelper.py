# -*- coding: utf-8 -*-
from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
class GUIhelper:
#This constructor will load the sign in window 
    def __init__(self,f,g): 
        self._root=Tk()
        self._root.title("Tinder Login")
        self._root.minsize(300,500)
        self._root.configure(background="#fe3c72")
        label1=Label(self._root,text='Tinder',bg="#fe3c72",fg="#fff")
        label1.configure(font=("arial",24,"bold","italic","underline"))
        label1.pack(pady=(30,20))
        
        self.label2=Label(self._root,text='Kindly login to proceed',bg="#fe3c72",fg="#fff")
        self.label2.configure(font=("vaerdana",12,"bold"))
        self.label2.pack(pady=(5,10))
        
        label3=Label(self._root,text='Email',bg="#fe3c72",fg="#fff")
        label3.configure(font=("system",12))
        label3.pack(pady=(10,5))
        
        self._emailInput=Entry(self._root)
        self._emailInput.pack(ipadx=50,ipady=7,pady=(1,10))
        
        label4=Label(self._root,text='Password',bg="#fe3c72",fg="#fff")
        label4.configure(font=("Constantia",12,"bold"))
        label4.pack(pady=(10,5))
        
        self._passwordInput=Entry(self._root)
        self._passwordInput.pack(ipadx=50,ipady=7,pady=(1,30))
        
        btn1=Button(self._root,text="Sign In",fg="#fe3c72",bg="gray89",command=lambda:f())
        btn1.configure(width=20,height=2,font=("verdana",10,"bold"))
        btn1.pack()
        
        label5=Label(self._root,text='Not a member? sign up now',bg="#fe3c72",fg="#fff")
        label5.configure(font=("Constantia",10))
        label5.pack(pady=(10,5))
        
        btn2=Button(self._root,text="Sign up now",fg="#fe3c72",bg="gray89",command=lambda:g())
        btn2.pack()
        
        self._root.mainloop()
        
#This method will load the registration window if the user is not registered        
    def regWindow(self,f):
        self._root.destroy()
        self._root=Tk()
        
        self._root.title("Tinder Registration")
        self._root.minsize(300,650)
        self._root.configure(background="#fe3c72")
            
        label1=Label(self._root, text="Tinder", bg="#fe3c72",fg="#fff")
        label1.configure(font=("Constantia", 24, "bold","italic","underline"))
        label1.pack(pady=(10,5))
            
        self.label2=Label(self._root, text="Register yourself below", bg="#fe3c72",fg="#fff")
        self.label2.configure(font=("Verdana", 12, "bold"))
        self.label2.pack(pady=(5,5))
        
        label3=Label(self._root, text="Name", bg="#fe3c72",fg="#fff")
        label3.configure(font=("Verdana", 12, "bold"))
        label3.pack(pady=(5,5))
        
        self._nameInput=Entry(self._root)
        self._nameInput.pack(ipadx=50,ipady=7,pady=(1,5))
        
        label4=Label(self._root, text="Email", bg="#fe3c72",fg="#fff")
        label4.configure(font=("Verdana", 12, "bold"))
        label4.pack(pady=(5,5))
        
        self._emailInput=Entry(self._root)
        self._emailInput.pack(ipadx=50,ipady=7,pady=(1,5))
        
        label5=Label(self._root, text="Password", bg="#fe3c72",fg="#fff")
        label5.configure(font=("Verdana", 12, "bold"))
        label5.pack(pady=(5,5))
        
        self._passwordInput=Entry(self._root)
        self._passwordInput.pack(ipadx=50,ipady=7,pady=(1,5))
        
        label6=Label(self._root, text="City", bg="#fe3c72",fg="#fff")
        label6.configure(font=("Verdana", 12, "bold"))
        label6.pack(pady=(5,5))
        
        self._cityInput=Entry(self._root)
        self._cityInput.pack(ipadx=50,ipady=7,pady=(1,10))
        
        label7=Label(self._root, text="Gender", bg="#fe3c72",fg="#fff")
        label7.configure(font=("Verdana", 12, "bold"))
        label7.pack(pady=(5,5))
        
        self._genderInput=Entry(self._root)
        self._genderInput.pack(ipadx=50,ipady=7,pady=(1,10))
        
        label8=Label(self._root, text="Age", bg="#fe3c72",fg="#fff")
        label8.configure(font=("Verdana", 12, "bold"))
        label8.pack(pady=(5,5))
        
        self._ageInput=Entry(self._root)
        self._ageInput.pack(ipadx=50,ipady=7,pady=(1,10))
        
        label9=Label(self._root, text="Dp", bg="#fe3c72",fg="#fff")
        label9.configure(font=("Verdana", 12, "bold"))
        label9.pack(pady=(5,5))
        
        self._dpInput=Entry(self._root)
        self._dpInput.pack(ipadx=50,ipady=7,pady=(1,10))
             
        btn1=Button(self._root, text="Sign up" ,fg="#fe3c72",bg="gray89", command=lambda :f())
        btn1.configure(width=20,height=2, font=("verdana", 10, "bold"))
        btn1.pack()
        
        
        
        '''label5=Label(self._root, text="Not a member? Sign Up now!", bg="#fd5068",fg="#fff")
        label5.configure(font=("Verdana", 10))
        label5.pack(pady=(10,5))
        
        btn2=Button(self._root, text="SignUp Now" ,fg="#fd5068",bg="#fff",command=lambda :g())
        btn2.pack()'''
        
        self._root.mainloop()
        
        
#This method will load after the successful sign in and it will display the details of the user        
    
    def mainWindow(self,other,data,mode,num=0):
        self.clear()
        self._root.configure(bg="light blue")
        
        self._root.minsize=(500,650)
        self._root.title("My Profile")
        
        menu=Menu(self._root)
        self._root.configure(menu=menu)
        
        homeMenu=Menu(menu)
        menu.add_cascade(label="Home",menu=homeMenu)
        homeMenu.add_command(label="My Profile",command=lambda:other.loadProfile())
        homeMenu.add_command(label="Edit Profile",command=lambda:other.editProfile())
        homeMenu.add_command(label="View Profile",command=lambda:other.viewProfile(num)) 
        homeMenu.add_command(label="Logout",command=lambda:other.logout())
        
        proposalMenu=Menu(menu)
        menu.add_cascade(label="HProposals",menu=proposalMenu)
        proposalMenu.add_command(label="My Proposals",command=lambda:other.viewProposal(0))
        proposalMenu.add_command(label="My Requests",command=lambda:other.viewRequest(0)) 
        proposalMenu.add_command(label="My Matches",command=lambda:other.viewMatching(0))
        
        url="img/"+data[0][-1]
        load = Image.open(url)
        load=load.resize((200,200), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)
        
        img = Label(image=render)
        img.image = render
        img.pack(pady=(30,10))
        
        name=data[0][1]
        label1=Label(self._root,text=name,bg="light blue",fg="#000")
        label1.configure(font=("times",20,"bold"))
        label1.pack(pady=(10,5))
        
        city="From: "+data[0][-2]
        label2=Label(self._root,text=city,bg="light blue",fg="#000")
        label2.configure(font=("Constantia",16,"bold"))
        label2.pack(pady=(10,10))
        
        gender="Not interested in: "+data[0][4]
        label3=Label(self._root,text=gender,bg="light blue",fg="#000")
        label3.configure(font=("Constantia",16,"bold"))
        label3.pack(pady=(10,10))
        
        age="Age: "+ str(data[0][5])
        label4=Label(self._root,text=age,bg="light blue",fg="#000")
        label4.configure(font=("Constantia",16,"bold"))
        label4.pack(pady=(10,10))
        
        if mode==2:
            frame=Frame(self._root)
            frame.pack()
            
            btn1=Button(frame,text="Previous",fg="#fff",bg="#fd5068",command=lambda:other.viewProfile(num-1))
            btn1.configure(height=3,width=10)
            btn1.pack(side=LEFT)
            btn2=Button(frame,text="Purpose",fg="#000",bg="dodger blue",command=lambda:other.propose(data[0][0]))
            btn2.configure(height=3,width=10)
            btn2.pack(side=LEFT)
            btn3=Button(frame,text="Next",bg="#fd5068",fg="#fff",command=lambda:other.viewProfile(num+1))
            btn3.configure(height=3,width=10)
            btn3.pack(side=LEFT)
        
        if mode==3:
            frame=Frame(self._root)
            frame.pack()
            btn1=Button(frame, text="Previous" ,fg="#fff",bg="#fd5068",command=lambda:other.viewProposal(num-1))
            btn1.configure(width=10,height=2)
            btn1.pack(side=LEFT)
            btn3=Button(frame, text="Next" ,fg="#fff",bg="#fd5068",command=lambda:other.viewProposal(num+1))
            btn3.configure(width=10,height=2)
            btn3.pack(side=LEFT) 
            label4=Label(self._root, text="Proposal number : {}".format(num+1), bg="light blue",fg="#000")
            label4.configure(font=("Verdana", 14, "bold"))
            label4.pack(pady=(10,5))
            
        if mode==4:
            frame=Frame(self._root)
            frame.pack()
            btn1=Button(frame, text="Previous" ,fg="#fff",bg="#fd5068",command=lambda:other.viewRequest(num-1))
            btn1.configure(width=10,height=2)
            btn1.pack(side=LEFT)
            btn2=Button(frame,text="Purpose",fg="#000",bg="dodger blue",command=lambda:other.propose(data[0][0]))
            btn2.configure(height=2,width=10)
            btn2.pack(side=LEFT)
            btn3=Button(frame, text="Next" ,fg="#fff",bg="#fd5068",command=lambda:other.viewRequest(num+1))
            btn3.configure(width=10,height=2)
            btn3.pack(side=LEFT)
            label5=Label(self._root, text="Request number : {}".format(num+1), bg="light blue",fg="#000")
            label5.configure(font=("Verdana", 14, "bold"))
            label5.pack(pady=(10,5))
            
        if mode==5:
            self._root.title("It's a Match!!!!")
            frame=Frame(self._root)
            frame.pack()
            btn1=Button(frame, text="Previous" ,fg="#fff",bg="#fd5068",command=lambda:other.viewMatching(num-1))
            btn1.configure(width=10,height=2)
            btn1.pack(side=LEFT)
            btn3=Button(frame, text="Next" ,fg="#fff",bg="#fd5068",command=lambda:other.viewMatching(num+1))
            btn3.configure(width=10,height=2)
            btn3.pack(side=LEFT)
            label5=Label(self._root, text="Matching number : {}".format(num+1), bg="light blue",fg="#000")
            label5.configure(font=("Verdana", 14, "bold"))
            label5.pack(pady=(10,5))
        self._root.mainloop()
        
        self._root.mainloop()

#this method will open the window which will allow the user to change their details when
#they will click the Edit Profile option in the menu after the successful sign in
        
    def editWindow(self,data,f):
        self.clear()
        
        self._root.title("Edit Profile")
        self._root.minsize=(300,650)
        self._root.configure(background="#fe3c72")
            
            
        self.label2=Label(self._root, text="Edit Your Profile", bg="#fe3c72",fg="#fff")
        self.label2.configure(font=("Verdana", 12, "bold"))
        self.label2.pack(pady=(5,5))
        
        label3=Label(self._root, text="Name", bg="#fe3c72",fg="#fff")
        label3.configure(font=("Verdana", 12, "bold"))
        label3.pack(pady=(5,5))
        
        self._nameInput=Entry(self._root)
        self._nameInput.insert(0,data[0][1])
        self._nameInput.pack(ipadx=50,ipady=7,pady=(1,5))
        
        label4=Label(self._root, text="Email", bg="#fe3c72",fg="#fff")
        label4.configure(font=("Verdana", 12, "bold"))
        label4.pack(pady=(5,5))
        
        self._emailInput=Entry(self._root)
        self._emailInput.insert(0,data[0][2])
        self._emailInput.pack(ipadx=50,ipady=7,pady=(1,5))
        
        label5=Label(self._root, text="Password", bg="#fe3c72",fg="#fff")
        label5.configure(font=("Verdana", 12, "bold"))
        label5.pack(pady=(5,5))
        
        self._passwordInput=Entry(self._root)
        self._passwordInput.insert(0,data[0][3])
        self._passwordInput.pack(ipadx=50,ipady=7,pady=(1,5))
        
        label6=Label(self._root, text="City", bg="#fe3c72",fg="#fff")
        label6.configure(font=("Verdana", 12, "bold"))
        label6.pack(pady=(5,5))
        
        self._cityInput=Entry(self._root)
        self._cityInput.insert(0,data[0][6])
        self._cityInput.pack(ipadx=50,ipady=7,pady=(1,10))
        
        label7=Label(self._root, text="Gender", bg="#fe3c72",fg="#fff")
        label7.configure(font=("Verdana", 12, "bold"))
        label7.pack(pady=(5,5))
        
        self._genderInput=Entry(self._root)
        self._genderInput.insert(0,data[0][4])
        self._genderInput.pack(ipadx=50,ipady=7,pady=(1,10))
        
        label8=Label(self._root, text="Age", bg="#fe3c72",fg="#fff")
        label8.configure(font=("Verdana", 12, "bold"))
        label8.pack(pady=(5,5))
        
        self._ageInput=Entry(self._root)
        self._ageInput.insert(0,data[0][5])
        self._ageInput.pack(ipadx=50,ipady=7,pady=(1,10))
        
        label9=Label(self._root, text="Dp", bg="#fe3c72",fg="#fff")
        label9.configure(font=("Verdana", 12, "bold"))
        label9.pack(pady=(5,5))
        
        self._dpInput=Entry(self._root)
        self._dpInput.insert(0,data[0][7])
        self._dpInput.pack(ipadx=50,ipady=7,pady=(1,10))
             
        btn1=Button(self._root, text="Save Changes" ,fg="#fd5068",bg="gray89", command=lambda :f())
        btn1.configure(width=20,height=2, font=("verdana", 10, "bold"))
        btn1.pack()
        
        self._root.mainloop()
        
#this method will be called when we don't want destroy the window and display different
#content in the same window       
    def clear(self):
        for i in self._root.pack_slaves():
            i.destroy()
#this method will be called when when we want to display any important message on the screen        
    def message(self,title,text):
        messagebox.showinfo(title,text)
        
