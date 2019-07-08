# -*- coding: utf-8 -*-

from guihelper import GUIhelper
from dbhelper import DBhelper
class Tinder(GUIhelper):
    def __init__(self,):
        self.db=DBhelper()   #It will call the DBhelper class to connect the web app to the database
        super(Tinder,self).__init__(self.login,self.load_reg_window)   #parent class can use methods of child class


#this method will check if the correct log in details are filled by the user 

    def login(self):
        if self._emailInput.get()=="" or self._passwordInput.get()=="":
            self.label2.configure(text="please fill both the fields",bg="yellow",fg="red")
        else:
            if '@' not in self._emailInput.get():
                self.label2.configure(text="Email input invalid",bg="yellow",fg="red")
            else:
                data=self.db.search("email",self._emailInput.get(),"password",self._passwordInput.get(),"users")
                if len(data)==1:
                    self.sessionId=(data[0][0])
                    self.loadProfile()
                    #self.mainWindow(data)
                else:
                    self.label2.configure(text="Login Failed",bg="red",fg="white")

                    
    def load_reg_window(self):
        num=0
        self.regWindow(lambda:self.handleRegistration(num))
        
    def handleRegistration(self,num):
        #print("handle reg")
       # print(num)
        if self._emailInput.get()=="" or self._passwordInput.get()=="" or self._nameInput.get()=="" or self._cityInput.get()=="" or self._genderInput.get()=="" or self._ageInput.get()=="" or self._dpInput.get()=="":
            self.label2.configure(text="Please fill all the fields",bg="yellow",fg="red")
        else:
            if len(self._passwordInput.get())<6:
                self.label2.configure(text="Password should be greater than 6 chars",bg="yellow",fg="red")
            else:
                #print("regdict")
                regDict={}
                #regDict['user_id']='NULL'
                regDict['name']=self._nameInput.get()
                regDict['email']=self._emailInput.get()
                regDict['password']=self._passwordInput.get()
                regDict['gender']=self._genderInput.get()
                regDict['age']=self._ageInput.get()
                regDict['city']=self._cityInput.get()
                regDict['dp']=self._dpInput.get()
                if num==0:
                    data=self.db.searchOne('email',self._emailInput.get(),'users','LIKE')
                    print(len(data))
                    if len(data)==1:
                        self.message("Registration Failed", "This Email Id is already registered")
                        self.regWindow(lambda:self.handleRegistration(num))
                    else:
                        response=self.db.insert(regDict,'users')
                        if response==1:
                            #GUIhelper(self.login,self.load_reg_window)
                            #self.label2.configure(text="Registration successful")
                            print("registration successful")
                            self._root.destroy()
                            Tinder()
                        else:
                            self.label2.configure(text="Registration failed")
                            print("registratioin failed")
                else:
                    response=self.db.update(regDict,'users',self.sessionId)
                
                    if response==1:
                        #GUIhelper(self.login,self.load_reg_window)
                        #self.label2.configure(text="Registration successful")
                        print("Update successful")
                        data=self.db.searchOne('user_id',self.sessionId,'users','LIKE')
                        self.mainWindow(self,data,mode=1)
                    
    def loadProfile(self):
        data=self.db.searchOne('user_id',self.sessionId,'users','LIKE')
        self.mainWindow(self,data,mode=1)

#this method will show profile of different people to the user 
        
    def viewProfile(self,num):
        data=self.db.searchOne('user_id',self.sessionId,'users','NOT LIKE')
        if num==0:
            self.mainWindow(self,data,mode=2,num=num)
        if num<0:
            self.message("Error", "hobe na!")
        if num>len(data)-1:
            self.message("Error", "hobe na!")
        else:
            new_data=[]
            new_data.append(data[num])
            self.mainWindow(self,new_data,mode=2,num=num)
   
#this method will be used to edit the profile of the user
    def editProfile(self):
        num=1
        data=self.db.searchOne('user_id',self.sessionId,'users','LIKE')
        self.editWindow(data,lambda:self.handleRegistration(num))

#this method will be triggered wwhen purpose button will be clicked        
    def propose(self,juliet_id):
        data=self.db.search('romeo_id',str(self.sessionId),'juliet_id',str(juliet_id),'proposals')
        if len(data)==0:
            propDict={}
            propDict['romeo_id']=str(self.sessionId)
            propDict['juliet_id']=str(juliet_id)
            response=self.db.insert(propDict,'proposals')
            if response==1:
                self.message("congrats","proposal sent")
            else:
                self.message("Error","proposal failed")
        else:
            self.message("Error","despo sala!")

#this method will be triggred when logout button will be clicked           
    def logout(self):
        self._root.destroy()
        Tinder()
#this method will be triggered when my proposal button will be clicked        
    def viewProposal(self,num):
        if self.sessionId!=0:
            data=self.db.searchOne('romeo_id',self.sessionId,'proposals',"LIKE")
            #print(data)
            l1 =[val[2] for val in data]
            l1=tuple(l1)
            #print(l1)
            if (len(l1)>1):
                data=self.db.searchOneFromList('user_id',l1,'users',"IN")
                print(data)
            
                if num==0:
                    new_data=[]
                    new_data.append(data[0])
                    self.mainWindow(self,new_data,mode=3,num=num)    #
                elif num<0:
                    self.message("Error","User Khtm")
                elif num>len(data)-1:
                    self.message("Error","User Khtm")
                else:
                    new_data=[]
                    new_data.append(data[num])
                    self.mainWindow(self,new_data,mode=3,num=num)
            elif(len(l1)==1):
                data=self.db.searchOne('user_id',l1[0],'users',"LIKE")
                if num==0:
                    new_data=[]
                    new_data.append(data[0])
                    self.mainWindow(self,new_data,mode=3,num=num)    #
                elif num<0:
                    self.message("Error","User Khtm")
                elif num>len(data)-1:
                    self.message("Error","User Khtm")
                else:
                    new_data=[]
                    new_data.append(data[num])
                    self.mainWindow(self,new_data,mode=3,num=num)
            else:
                self.message("","No proposal Found")
#this method will be triggerd when My Request button will be clicked                
    def viewRequest(self,num):
        if self.sessionId!=0:
            data=self.db.searchOne('juliet_id',self.sessionId,'proposals',"LIKE")
            print(data)
            l1 =[val[1] for val in data]
            l1=tuple(l1)
            print(l1)
            if(len(l1)>1):
                data=self.db.searchOneFromList('user_id',l1,'users',"IN")
                #print(data)

                if num==0:
                    new_data=[]
                    new_data.append(data[0])
                    self.mainWindow(self,new_data,mode=4,num=num)    #
                elif num<0:
                    self.message("Error","User Khtm")
                elif num>len(data)-1:
                    self.message("Error","User Khtm")
                else:
                    new_data=[]
                    new_data.append(data[num])
                    self.mainWindow(self,new_data,mode=4,num=num)
            elif(len(l1)==1):
                data=self.db.searchOne('user_id',l1[0],'users',"LIKE")
                if num==0:
                    new_data=[]
                    new_data.append(data[0])
                    self.mainWindow(self,new_data,mode=4,num=num)    #
                elif num<0:
                    self.message("Error","User Khtm")
                elif num>len(data)-1:
                    self.message("Error","User Khtm")
                else:
                    new_data=[]
                    new_data.append(data[num])
                    self.mainWindow(self,new_data,mode=4,num=num)
            else:
                self.message("So Sad!!","No Requests Found")
#this method will be triggered when My Matches button will be clicked                
    def viewMatching(self,num):
        if (self.sessionId!=0):
            proposal_data=self.db.searchOne('romeo_id',self.sessionId,'proposals',"LIKE")
            #print(proposal_data)
            proposal_list=[val[2] for val in proposal_data]
            #print(proposal_list)
            request_data=self.db.searchOne('juliet_id',self.sessionId,'proposals',"LIKE")
            request_list=[val[1] for val in request_data]
            #print(request_list)
            l1=tuple(set(proposal_list)&set(request_list))
            #print(l1)
            if(len(l1)>1):
                data=self.db.searchOneFromList('user_id',l1,'users',"IN")
                #print(data)

                if num==0:
                    new_data=[]
                    new_data.append(data[0])
                    self.mainWindow(self,new_data,mode=5,num=num)    
                elif num<0:
                    self.message("Error","User Khtm")
                elif num>len(data)-1:
                    self.message("Error","User Khtm")
                else:
                    new_data=[]
                    new_data.append(data[num])
                    self.mainWindow(self,new_data,mode=5,num=num)
            elif(len(l1)==1):
                data=self.db.searchOne('user_id',l1[0],'users',"LIKE")
                if num==0:
                    new_data=[]
                    new_data.append(data[0])
                    self.mainWindow(self,new_data,mode=5,num=num)    #
                elif num<0:
                    self.message("Error","User Khtm")
                elif num>len(data)-1:
                    self.message("Error","User Khtm")
                else:
                    new_data=[]
                    new_data.append(data[num])
                    self.mainWindow(self,new_data,mode=4,num=num)
            else:
                self.message("So Sad!!","No Matchings Found")


        
obj=Tinder()