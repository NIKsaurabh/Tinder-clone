
# -*- coding: utf-8 -*-
import mysql.connector

class DBhelper:
    def __init__(self):         #It will connect the web app to the database
        try:
            self._connection=mysql.connector.connect(host="127.0.0.1",user="root",password="",database="tinderb2")
            self._cursor=self._connection.cursor()
            print("connected to database")
        except:
            print("could not connect")
            exit(0)
    
# this method will search data in database by taking two details of the user
#it will be used during sign in process to validate email id and password of the user
    def search(self,key1,value1,key2,value2,table):
        self._cursor.execute("""SELECT * FROM `{}` WHERE `{}` LIKE '{}' AND `{}` LIKE '{}'""".format(table,key1,value1,key2,value2))
        data=self._cursor.fetchall()
        return data

# this method will search data in database by taking one detail of the user
  
    def searchOne(self,key1,value1,table,type):
         self._cursor.execute("""SELECT * FROM `{}` WHERE `{}` {} '{}' """.format(table,key1,type,value1))
         data=self._cursor.fetchall()
         
         return data
     
    def searchOneFromList(self,key1,value1,table,type):
        
        print("""select * from `{}` WHERE `{}` {} {}""".format(table,key1,type,value1))
        self._cursor.execute("""select * from `{}` WHERE `{}` {} {}""".format(table,key1,type,value1))
        data=self._cursor.fetchall()
        return data

#code to insert data in database
    
    def insert(self,insertDict,table):
        """ query=INSERT INTO `users`
        (`user_id`,`name`,`email`,`password`,`gender`,`age`,`city`)
        VALUES('NULL','xyz','xtz@gmail.com','1234567','male','21','Kolkata')"""
        
        colName=""
        valName=""
        for i in insertDict:
            colName=colName+"`"+i+"`,"
            #if i=='user_id':
              #  valName="NULL,"
           # else:
            valName=valName+"'"+insertDict[i]+"',"
        colName=colName[0:-1]
        valName=valName[0:-1]
        
        query="""INSERT INTO `{}` ({}) VALUES ({}) """.format(table,colName,valName)
        #print(query)
        try:
            self._cursor.execute(query)
            self._connection.commit()
            return 1
        except:
            return 0
 
#code to update database when user want to change their details       
    def update(self,insertDict,table,sessionId):
            query="""UPDATE `{}` SET `name`='{}',`email`='{}',`password`='{}',`gender`='{}',`age`='{}',`city`='{}',`dp`='{}' WHERE user_id={}""".format(table,insertDict['name'],insertDict['email'],insertDict['password'],insertDict['gender'],insertDict['age'],insertDict['city'],insertDict['dp'],sessionId)
            print(query)
            try:
                self._cursor.execute(query)
                self._connection.commit()
                return 1
            except:
                return 0
