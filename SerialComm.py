# -*- coding: utf-8 -*-
from __future__ import division
import sys
from PyQt4 import QtCore, QtGui, uic
import serial
import Queue
#import threading
##import thread
import datetime
from serial_port import serial_ports
from PrintRecipe import print_FILE
queue = Queue.Queue(1000)
import time 
global i
import re
import MySQLdb
OperatorList=[]
recipe_DATA =[]
RecipeNAMELIST=[]
#ingredientList=[]
ingredientList1=[]
ingredientValueKGList=[]
ingredientValueGMList=[]
msg_box_list=[]
comportLIst=[]
comportListName=[]
COMPORTSaveLIST=[]
BAUDRATELIST=[]
PARITYLIST=[]
STOPBITLIST=[]
DATABITLIST=[]
baudrate_value=9600
baudrate_value2=9600
parityNAME="N"
parityNAME2="N"
stopBitValue="1"
stopBitValue2="1"
databitValue="8"
databitValue2="8"
msgBox_data=""
        
qtCreatorFile = "serialguicomm.ui" # Enter file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtGui.QMainWindow, Ui_MainWindow):
   

    ingredientList = []
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.combineDATA=False
        self.setWindowTitle("Weighing Scale R-PI")
        self.setFixedSize(933,480)
        self.threadclass=ThreadClass()
        self.comboBox1.addItem("Select Recipe")
        self.setDefault()
        self.parity_combox.setCurrentIndex(2)
        self.parity_combox.currentIndexChanged.connect(self.parity)
        self.parity_combox2.setCurrentIndex(2)
        self.parity_combox2.currentIndexChanged.connect(self.parity2)
        self.baud_combox.setCurrentIndex(5)
        self.baud_combox.currentIndexChanged.connect(self.baudRate)
        self.baud_combox2.setCurrentIndex(5)
        self.baud_combox2.currentIndexChanged.connect(self.baudRate2)
        self.stopbit_comboBox.setCurrentIndex(0)
        self.stopbit_comboBox.currentIndexChanged.connect(self.stopbit)
        self.stopbit_comboBox2.setCurrentIndex(0)
        self.stopbit_comboBox2.currentIndexChanged.connect(self.stopbit2)
        self.databit_comboBox_2.setCurrentIndex(1)
        self.databit_comboBox_2.currentIndexChanged.connect(self.databit)
        self.databit_comboBox_3.setCurrentIndex(1)
        self.databit_comboBox_3.currentIndexChanged.connect(self.databit2)
        self.comboBox2.addItem("Select Operator")
        self.comboBox2.currentIndexChanged.connect(self.operatorName)
        self.comport()
        self.comport_combox.setCurrentIndex(0)
        self.comport_combox2.setCurrentIndex(0)
        self.comport_combox.currentIndexChanged.connect(self.selectComPort)
        self.comport_combox2.currentIndexChanged.connect(self.selectComPort2)
        self.threadclass=ThreadClass()
#        thread=ThreadClass()
        global white
        white="#000000"
        global red
        red  = "#ff0000"
        global green
        green = "#00ff00"
        global blue
        blue="#0000ff"
        global yellow
        yellow = "#ffff00"
        global style_str1
        style_str1 = "QWidget {color: %s}"
        global style_str
        style_str="QWidget {background-color: %s}"
        global black
        black ="black"
        self.file_read()
        self.READ_text_FILE()
        self.connect(self.threadclass,QtCore.SIGNAL('SERIAL'),self.UPDATEVALUE)
        self.connect(self.threadclass,QtCore.SIGNAL('MSGBOX'),self.Comport_msgBox)
        self.connect(self.threadclass,QtCore.SIGNAL('combine'),self.CHECK_DATA)
        self.nextButton.clicked.connect(self.selectionchange)
        self.nextButton.hide()
        self.nextButton_2.clicked.connect(self.FilePortSetting)
        self.start.clicked.connect(self.startThread)
        self.checkBox.setChecked(True)
        self.checkBox.stateChanged.connect(self.doCheck)
        self.doCheck()
        self.checkBox_2.setChecked(False)
        self.checkBox_2.stateChanged.connect(self.doCheck2)
        self.doCheck2()

         



        """*

        * Function    :  setDefault

        *

        * Description :  (Set the Combox values.)

        *

        * parameters  :

        *          1  :  param1 = self

        *  

        *

        * Returns     :  0 => Ok, everything else is an error"""

    def file_read(self):
        File = open("secure.txt","r")
        for line in File:
            print line
            if((line.find('user = '))==0):
                global USER
                user = line
                print str(user)
                USER = user[7:(len(user)-1)]
            if((line.find('password = '))==0):
                global PASSWORD
                password = line
                print str(password)
                PASSWORD = password[11:(len(password))]


 
        
    def setDefault(self):
        BAUDRATELIST.append("300")
        BAUDRATELIST.append("600")
        BAUDRATELIST.append("1200")
        BAUDRATELIST.append("2400")
        BAUDRATELIST.append("4800")
        BAUDRATELIST.append("9600")
        BAUDRATELIST.append("19200")
        self.baud_combox.addItems(BAUDRATELIST)
        self.baud_combox2.addItems(BAUDRATELIST)
        PARITYLIST.append("EVEN")
        PARITYLIST.append("ODD")
        PARITYLIST.append("NONE")
        self.parity_combox.addItems(PARITYLIST)
        self.parity_combox2.addItems(PARITYLIST)
        STOPBITLIST.append("1")
        STOPBITLIST.append("2")
        self.stopbit_comboBox.addItems(STOPBITLIST)
        self.stopbit_comboBox2.addItems(STOPBITLIST)
        DATABITLIST.append("7")
        DATABITLIST.append("8")
        self.databit_comboBox_3.addItems(DATABITLIST)
        self.databit_comboBox_2.addItems(DATABITLIST)


        """*

        * Function    :  saveSetting

        *

        * Description :  (Function for save the Current settings.)

        *

        * parameters  :

        *          1  :  param1 = self

        *  

        *

        * Returns     :  0 => Ok, everything else is an error.

        *"""
                
        
    def saveSetting(self):
        msg1=QtGui.QMessageBox()
        msg1.setIcon(QtGui.QMessageBox.Information)
 
        self.setMinimumHeight(0)
        self.setMaximumHeight(16777215)
        self.setMinimumWidth(0)
        self.setMinimumWidth(16777215)
        
        msg1.setText("Save the current Settings \n Not yet implemented")

        msg1.exec_()

        """*

        * Function    :  FilePortSetting

        *

        * Description :  (Read the file and update last port settings.)

        *

        * parameters  :

        *          1  :  param1 = self

        *  

        *

        * Returns     :  0 => Ok, everything else is an error.

        *"""

                

    def FilePortSetting(self):
        f=open('write.txt','w')
        #print ComportName
        

        #print ComportName2
        #print baudrate_value
        #print baudrate_value2
        #print parityNAME
        #print parityNAME2

        #print stopBitValue
        #print stopBitValue2


        
        comportDATA1="COMPORT1"+"\t"+str(ComportName)+"\t"+ str(baudrate_value)+"\t"+ str(parityNAME)+"\t"+ str(databitValue)+"\t"+ str(stopBitValue)+"\n"
        comportDATA2="COMPORT2"+"\t"+str(ComportName2)+"\t"+ str(baudrate_value2)+"\t"+ str(parityNAME2)+"\t"+ str(databitValue2)+"\t"+ str(stopBitValue2)+"\n"

        ComportDATA=comportDATA1+comportDATA2
        f.write(ComportDATA)


        """*

        * Function    :  databit

        *

        * Description :  (For set the databit)

        *

        * parameters  :

        *          1  :  param1 = self

        *          2  :  param2 = databit_combox_indexvalue 

        *

        * Returns     :  0 => Ok, everything else is an error.

        *"""


        
        


    def  databit(self, databit):

        for count in range(self.databit_comboBox_2.count()):
            #print self.databit_comboBox_2.itemText(count)
        #print "Current index",databit,"selection changed ",self.databit_comboBox_2.currentText()
            global databitValue
            databitValue=self.databit_comboBox_2.currentText()

        # same function for second databit combox.


    def  databit2(self, databit):

        for count in range(self.databit_comboBox_3.count()):
            #print self.databit_comboBox_3.itemText(count)
        #print "Current index",databit,"selection changed ",self.databit_comboBox_3.currentText()
            global databitValue2
            databitValue2=self.databit_comboBox_3.currentText()


        """*

        * Function    :  doCheck

        *

        * Description :  (For Check the checkbox status.)

        *

        * parameters  :

        *          1  :  param1 = self

        *         

        *

        * Returns     :  0 => Ok, everything else is an error.

        *"""
                

    def doCheck(self):
        
        if self.checkBox.isChecked():
            self.checkBox_2.setChecked(False)
            global checkValueOne
            checkValueOne=True
            
        else:
            global checkValueOne
            checkValueOne=False
 #same function for another check box
            

    def doCheck2(self):
        
        if self.checkBox_2.isChecked():
            self.checkBox.setChecked(False)
            global checkValueTwo
            checkValueTwo=True
            
        else:
            global checkValueTwo
            checkValueTwo=False

            

            

    def stopbit(self,stopbit):
        for count in range(self.stopbit_comboBox.count()):
            #print self.stopbit_comboBox.itemText(count)
        #print "Current index",stopbit,"selection changed ",self.stopbit_comboBox.currentText()
            global stopBitValue
            stopBitValue=self.stopbit_comboBox.currentText()

        

    def stopbit2(self,stopbit2):
        for count in range(self.stopbit_comboBox2.count()):
            #print self.stopbit_comboBox2.itemText(count)
        #print "Current index",stopbit2,"selection changed ",self.stopbit_comboBox2.currentText()
            global stopBitValue2
            stopBitValue2=self.stopbit_comboBox2.currentText()

        
        
    def parity(self,parity):
        for count in range(self.parity_combox.count()):
            #print self.parity_combox.itemText(count)
        #print "Current index",parity,"selection changed ",self.parity_combox.currentText()
            global parityNAME
            parityNAME=self.parity_combox.currentText()

        
    def parity2(self,parity2):
        for count in range(self.parity_combox2.count()):
            #print self.parity_combox2.itemText(count)
        #print "Current index",parity2,"selection changed ",self.parity_combox2.currentText()
            global parityNAME2
            parityNAME2=self.parity_combox2.currentText()

 

        """*

        * Function    :  startThread

        *

        * Description :  (Start the Thread.)

        *

        * parameters  :

        *          1  :  param1 = self

        *         

        *

        * Returns     :  0 => Ok, everything else is an error.

        *"""        
        
        
    def startThread(self):
        #print "Start"
        indexcomboBox1=self.comboBox1.currentIndex()
        self.text_FILE(indexcomboBox1)
        time.sleep(.5)
        self.threadclass.start()
        
        """*

        * Function    :  comport

        *

        * Description :  (Update the all available comport list.)

        *

        * parameters  :

        *          1  :  param1 = self

        *         

        *

        * Returns     :  0 => Ok, everything else is an error.

        # Here we import a another module named "serial_ports()" , which returns the all available comport list.

        *"""        

        

    def comport(self):
        serial_comport = serial_ports()
        #print serial_comport
        for i in serial_comport:
            comportListName.append(i)
            I=i[5:len(i)]
            comportLIst.append(I)
        #print comportLIst
        global ComportName
        ComportName=comportListName[0]
        global ComportName2
        ComportName2=comportListName[0]



        self.comport_combox.addItems(comportLIst)
        self.comport_combox2.addItems(comportLIst)


            # If combox index is changed that function update the comport.
        
    def selectComPort(self,c):
        for count in range(self.comport_combox.count()):
            #print self.comport_combox.itemText(count)
        #print "Current index",c,"selection changed ",self.comport_combox.currentText()
            global ComportName
            ComportName=comportListName[c]
        #print ComportName
    def selectComPort2(self,c):
        for count in range(self.comport_combox2.count()):
            #print self.comport_combox2.itemText(count)
        #print "Current index",c,"selection changed ",self.comport_combox2.currentText()
            global ComportName2
            ComportName2=comportListName[c]
        #print ComportName2

                
        """*

        * Function    :  msgbox

        *

        * Description :  (To show the message if recipe is created.)

        *

        * parameters  :

        *          1  :  param1 = self

        *         

        *

        * Returns     :  0 => Ok, everything else is an error.



        *"""            

    def Comport_msgBox(self,val):
                
        msg1=QtGui.QMessageBox()
        msg1.setIcon(QtGui.QMessageBox.Information)
        msg1.setText( "Select a valid Comport.")
        msg1.exec_()




    msgBox_data=""
    def msgbox(self):
        self.nextButton.hide()
        
        msg=QtGui.QMessageBox()
        msg.setIcon(QtGui.QMessageBox.Information)
        
        self.setMinimumHeight(0)
        self.setMaximumHeight(16777215)
        self.setMinimumWidth(0)
        self.setMinimumWidth(16777215)

        
        #print "msgBox " + str(RcpNAME)
#        ValueKG=""
        #print ingredientValueKGList
        
        global msgBox_data
        weightTotal=0
        toleranceTotal=0
        

        msgBox_data1=""
        for DATA in msg_box_list:
            msgBox_data1+=DATA
            #print "-------msgBOX DATA " +str(DATA.split('\t'))
            weightdata= (str(DATA).split('\t'))
            #print weightdata
            
            weightTotal+= int(weightdata[1])
            
            toleranceTotal+= int(weightdata[2])
            
            #print msgBox_data1
        #print "wwww" +str(weightTotal) +str( toleranceTotal)
        Date= datetime.datetime.now().date()
        Time=datetime.datetime.now().time()
        msg.setText( "Recipe " +str(RcpNAME) +" Created")
        msg.setDetailedText("Operator : "+str(operator_value)+"\n"+str("Date ="+str(Date))+"\n"+str("Time ="+str(Time))+"\n"+str(msgBox_data1)+"\n"+"\t"+"Total "+str(weightTotal)+" , "+str(toleranceTotal))
        #msg.setText( "Recipe " +str(RcpNAME) +" Created")
        msg_box_list[:]=[]
        self.print_Recipe_Details(RcpNAME,msgBox_data1,weightTotal,toleranceTotal,operator_value)
        msg.exec_()

        """*

        * Function    :  print_Recipe_Details

        *

        * Description :  (Save the bill text file in same directory)

        *

        * parameters  :

        *          1  :  param1 = self

        *          2  :  param2 = Recipe Name

        *          3  :  param3 = Ingredients

        *          4  :  param4 = Total weight

        *          5  :  param5 = Total tolerance

        *          6  :  param6 = Operator Name

        *         

        *

        * Returns     :  0 => Ok, everything else is an error.



        *"""            


        

    def print_Recipe_Details(self,Name,values,weight1,weight2,operator_value):
        import datetime
        ingredientValues=""
        f=open('billTest.txt','w')
        #msg1="Company Name\n"
        msg1="Fosforera Centroamericana S.A." +"\n"
        msg2="Date: "+str(datetime.datetime.now().date())+"\n"
        msg3="Time: "+str(datetime.datetime.now().time())+"\n"
        #print msg3, msg2
        msg4="Recipe: "+str(Name)+"\n"+str(operator_value)+"\n"
        msg5=str("Components")+"\t"+"Weight"+"\t"+"%"+"\n"
        msg6="\n"
        ingredientValues=values
        msg7=ingredientValues

        msg8="\n"
        
      
        msg11="Total "+"\t"+'\t'+str(weight1)+"\t"+str(weight2)+"\n"
        
        msg=msg1+msg2+msg3+msg4+msg5+msg6+msg7+msg8+msg11
        f.write(msg)
        f.close()




        

    def baudRate(self,q):
        for count in range(self.baud_combox.count()):
            #print self.baud_combox.itemText(count)
        #print "Current index",q,"selection changed ",self.baud_combox.currentText()
            global baudrate_value
            baudrate_value=self.baud_combox.currentText()


    def baudRate2(self,baudRate2):
        for count in range(self.baud_combox.count()):
            #print self.baud_combox2.itemText(count)
        #print "Current index",baudRate2,"selection changed ",self.baud_combox2.currentText()
            global baudrate_value2
            baudrate_value2=self.baud_combox2.currentText()

        
    def operatorName(self,o):
        for count in range(self.baud_combox.count()):
            #print self.comboBox2.itemText(count)
        #print "Current index",o,"selection changed ",self.comboBox2.currentText()
            global operator_value
            operator_value=self.comboBox2.currentText()
        

                
        """*

        * Function    :  UPDATEVALUE

        *

        * Description :  (TO update the current weight on lcd ( GUI ).)

        *

        * parameters  :

        *          1  :  param1 = self

        *          2  :  param2 = Current Weight Value. 

        *

        * Returns     :  0 => Ok, everything else is an error.



        *"""            

        
    
    def UPDATEVALUE(self, val):
        
        
        #print single_ingredient_UNIT
        if ((default_value) and (UnitCheckKG)):
            
            self.lcdNumber2.display(float(val))
            self.lcdNumber.display("0")
        elif((default_value) and (UnitCheckGM)):

            self.lcdNumber.display(float(val))
            self.lcdNumber2.display("0")


            
            
        else:
            #print "NOne"
                global SERIAL_DATA_P
        
        
        SERIAL_DATA_P =val
        global default_value
        default_value =True
        
    def selectionchange(self):
        serial0.flushOutput()
        serial0.flushInput()
        serial1.flushOutput()
        serial1.flushInput()
        global default_value
        default_value =True
        global msgBox_data
        msgBox_data=""
        msgBox_data+=str(single_ingredient_NAME)
        msgBox_data+="\t"
        msgBox_data+=str(msg_data) 
        msgBox_data+="\t"
        msgBox_data+=str(msg_data_tolrnc)
        msgBox_data+="\n"

        msg_box_list.append(msgBox_data)
        
        global ingrNum
        ingrNum += 1
        if (ingrNum<len(self.ingredientList)):
            #print "IN IF Ingrd" + str(ingrd)
            self.Call(ingrNum)
            self.threadclass.start()
        else:
            self.text_label.setText("RECIPE "+ str(RcpNAME) +" CREATED")
            self.nextButton.hide()
            self.threadclass.stop()
            self.msgbox()
            self.combineDATA=False
            print_FILE()

            
            

    def CHECK_DATA(self,value):
        if(self.combineDATA):
            X1=((int(single_ingredient_WT)*(100+int(single_ingredient_TL)))/100)
            X2=((int(single_ingredient_WT)*(100-int(single_ingredient_TL)))/100)
            #if (single_ingredient_UNIT=="K"):
            if(UnitCheckKG):
                if ((float(SERIAL_DATA_P) >= float((X2))) and (float(SERIAL_DATA_P)<= float((X1))) ):
                    
                    self.lcdNumber2.setStyleSheet(style_str1 % green)
                    
                    global default_value
                    default_value = False
                    global weightKG_value
                   
                    weightKG_value=SERIAL_DATA_P
                    global msg_data
                    msg_data=weightKG_value
                    global msg_data_tolrnc
                    msg_data_tolrnc =single_ingredient_TL
                    self.nextButton.show()
                    self.threadclass.stop()
                    self.lcdNumber2.display(float(weightKG_value))

                    global default_value
                    default_value = True
                    global single_ingredient_UNIT
                    single_ingredient_UNIT ="Null"

                    
                elif(float(SERIAL_DATA_P)<float(single_ingredient_WT)):
                    self.nextButton.hide()  
                    self.lcdNumber2.setStyleSheet(style_str1 % yellow)
                    
                    
                    global default_value
                    default_value = True

                elif(float(SERIAL_DATA_P)>(float(single_ingredient_WT))):
                    self.nextButton.hide()
                    self.lcdNumber2.setStyleSheet(style_str1 % red)
                    global default_value
                    default_value = True


            #elif (single_ingredient_UNIT=="G"):
            elif (UnitCheckGM):
                if((float(SERIAL_DATA_P)>= float(X2)) and (float(SERIAL_DATA_P)<= float(X1))):
                    
                    self.lcdNumber.setStyleSheet(style_str1 % green)
                    
                    global default_value
                    default_value = False
                    
                    global weightGM_value

                    weightGM_value=SERIAL_DATA_P
                    global msg_data
                    msg_data=weightGM_value
                    global msg_data_tolrnc
                    msg_data_tolrnc =single_ingredient_TL
                    
                    self.nextButton.show()
                    self.threadclass.stop()
                    self.lcdNumber.display(float(weightGM_value))
                    
                    
                    global default_value
                    default_value = True
                    global single_ingredient_UNIT
                    single_ingredient_UNIT ="Null"

                

                    
                elif(float(SERIAL_DATA_P)<float(single_ingredient_WT)):
                    
                    self.lcdNumber.setStyleSheet(style_str1 % yellow)
                    
                    global default_value
                    default_value = True

                elif(float(SERIAL_DATA_P)>float(single_ingredient_WT)):
                    
                    self.lcdNumber.setStyleSheet(style_str1 % red)
                    
                    global default_value
                    default_value = True
            else:
                default_value = True
                
                



                
        """*

        * Function    :  READ_text_FILE

        *

        * Description :  (Read the Recipe.txt file and update the values.)

        *

        * parameters  :

        *          1  :  param1 = self

        *          2  :  param2 = Cur
rent Weight Value. 

        *

        * Returns     :  0 => Ok, everything else is an error.



        *"""            

        
    

   
            

    def READ_text_FILE(self):
        

        global default_value
        default_value=True
        
        RecipeNAMELIST[:]=[]
        OperatorList[:]=[]
        RecipeList=[]

        db = MySQLdb.connect(host="localhost",user=USER,passwd=PASSWORD,db="mysql")
        curs=db.cursor()
        with db:
            curs.execute("SELECT OPERATOR_NAME from OPERATOR")
        for operatorname in curs.fetchall():
            #print operatorname[0]
            OperatorList.append(operatorname[0])
        curs.close()

        db.close()

        db = MySQLdb.connect(host="localhost",user=USER,passwd=PASSWORD,db="mysql")
        curs=db.cursor()
        with db:
            curs.execute("SELECT RECIPE_NAME from RECIPE")
        for reciepname in curs.fetchall():
            #print reciepname[0]
            RecipeList.append(reciepname[0])
        curs.close()
        db.close()

        #File = open("RecipeData.txt","r")
        #print "RecipeList" +str(RecipeList)
        self.comboBox1.addItems(RecipeList)
        self.comboBox2.addItems(OperatorList)
        try:
            PortFile=open('write.txt','r')
            for portline in  PortFile:
                singleport=portline.split('\t')
                for k in range (len(singleport)):
                    if (k==0):
                        pass
                    else:
                        global COMPORTSaveLIST
                        COMPORTSaveLIST.append(singleport[k])
            for k2 in range (len(COMPORTSaveLIST)):
                        global ComportName
                       
                        global baudrate_value
                        
                        baudrate_value=COMPORTSaveLIST[1]
                        global parityNAME
                        parityNAME=COMPORTSaveLIST[2]
                        global databitValue
                        databitValue=COMPORTSaveLIST[3]
                        global stopBitValue
                        stopBitValue=COMPORTSaveLIST[4]
                        global ComportName2
                       
                        global baudrate_value2
                        baudrate_value2=COMPORTSaveLIST[6]
                        global parityNAME2
                        parityNAME2=COMPORTSaveLIST[7]
                        global databitValue2
                        databitValue2=COMPORTSaveLIST[8]
                        global stopBitValue2
                        
                        stopBitValue2=COMPORTSaveLIST[9]
            
            
            
            for Baudratei in range (len(BAUDRATELIST)):
                
                if (baudrate_value==BAUDRATELIST[Baudratei]):
                    self.baud_combox.setCurrentIndex(Baudratei)
                if(baudrate_value2==BAUDRATELIST[Baudratei]):
                    self.baud_combox2.setCurrentIndex(Baudratei)
              
            for parityi in range (len(PARITYLIST)):
                if (parityNAME==PARITYLIST[parityi]):
                    self.parity_combox.setCurrentIndex(parityi)
                if (parityNAME2==PARITYLIST[parityi]):
                    self.parity_combox2.setCurrentIndex(parityi)
            for stopi in range (len(STOPBITLIST)):
                if (stopBitValue==STOPBITLIST[stopi]):
                    self.stopbit_comboBox.setCurrentIndex(stopi)

                if (stopBitValue==STOPBITLIST[stopi]):
                    self.stopbit_comboBox2.setCurrentIndex(stopi)
            for databiti in range (len(DATABITLIST)):
                if (databitValue==DATABITLIST[databiti]):
                    
                    self.databit_comboBox_2.setCurrentIndex(databiti)
                if (databitValue2==DATABITLIST[databiti]):
                    self.databit_comboBox_3.setCurrentIndex(databiti)
        except:
            #print "File Not Found"
            pass
        #self.Comport_msgBox()
                
            
    #def set_text():
    def Call(self,j):

        #print "Call Function"

        #print ingredientList
  
        self.text_label.setText(self.ingredientList[j])
        single_ingredient=self.ingredientList[j]
        single_ingredient1=single_ingredient.split(',')
        global single_ingredient_UNIT
        global single_ingredient_WT
        global single_ingredient_TL
        global single_ingredient_NAME

        single_ingredient_NAME=single_ingredient1[0]
        single_ingredient_UNIT=single_ingredient1[1]
        single_ingredient_WT=single_ingredient1[2]
        single_ingredient_TL=single_ingredient1[3]
        
       
        self.combineDATA=True
            
            
            
            
        
        

  
    def text_FILE(self,i):
        self.threadclass.stop()
        time.sleep(.5)
        global RcpNAME
        for count in range(self.comboBox1.count()):
            #print self.comboBox1.itemText(count)
        #print "Current index",i,"selection changed ",self.comboBox1.currentText()
            RcpNAME=self.comboBox1.currentText()
        db = MySQLdb.connect(host="localhost",user=USER,passwd=PASSWORD,db="mysql")
        curs=db.cursor()

        with db:
            curs.execute("SELECT * from " + str(RcpNAME))
        self.ingredientList = []
        for reading in curs.fetchall():
            #print str(reading[0])
            self.ingredientList.append(str(reading[0]))

        curs.close()
        db.close()
        #print ingredientList
        global ingrNum
        ingrNum = 0
        self.Call(ingrNum)
        self.start.show()

                
                
                
        """*

        * Class    :  ThreadClass

        *

        * Description :  (Create a Thread Class.)

        *

        *"""            

                    


       
class ThreadClass(QtCore.QThread):
    stopFlag=False
    def __init__(self,parent= None):
        super(ThreadClass, self ).__init__(parent)
        


       


                
        """*

        * Function    :  run

        *

        * Description :  (TO start the thread.)

        *

        * parameters  :

        *          1  :  param1 = self

        *        

        *

        * Returns     :  0 => Ok, everything else is an error.



        *"""            

        
    

        

    def run(self):
       
        print "Enter in RUn "
        self.stopFlag=False
        #print "Comport NAme "+str(ComportName)
        #print baudrate_value
        #print baudrate_value2
        #print parityNAME
        #print parityNAME2
        #print databitValue
        parityValue=parityNAME[0:1]
        parityValue2=parityNAME[0:1]
        #print stopBitValue
        #print stopBitValue2
        #print checkValueOne
        #print checkValueTwo
        #print databitValue2
        global serial0
        global serial1
        
        serial0=serial.Serial(
            #port ='/dev/ttyACM0',
            port =ComportName,
            baudrate=baudrate_value,
            parity=parityValue,
            stopbits=int(stopBitValue),
            bytesize=int(databitValue),
            timeout=5
        )
        serial1=serial.Serial(
            #port ='/dev/ttyACM0',
            port =ComportName2,
            baudrate=baudrate_value2,
            parity=parityValue2,
            stopbits=int(stopBitValue2),
            bytesize=float(databitValue2),
            timeout=5
        )
        if (checkValueOne):
            #val=serial0.readline()
            global SerialPortAvailable
            SerialPortAvailable=serial0
            global UnitCheckKG
            UnitCheckKG = True
            global UnitCheckGM
            UnitCheckGM = False
        elif(checkValueTwo):
            #val=serial1.readline()
            global SerialPortAvailable
            SerialPortAvailable=serial1
            global UnitCheckGM
            UnitCheckGM = True
            global UnitCheckKG
            UnitCheckKG = False
            #sign=str(val[0:1])
            #SignValue="+"
        



        while True:
            #print "HERE"
       
            #print "Stop Flag " +str(stopFlag)
            if (self.stopFlag):
                print "Enter in stopFlag"
                global stopFlag
                #print stopFlag
                self.stopFlag=False
                #print stopFlag
                break
            else:
                try:
                    val =SerialPortAvailable.readline()
                    print "--------------------------------------------"
                    print val
                    if(val==''):
                    
                        msgBOXvalue="NULL"
                        self.emit(QtCore.SIGNAL('MSGBOX'),msgBOXvalue)
                        break
                    else:
                        weightKgValue=val.splitlines()
                        WKGValue=str(weightKgValue[0].strip())
                        WKGData=WKGValue.replace(" ","")
                        if(WKGData.find("kg")>0):
                            WKGData1=WKGData.split('kg')
                            WKGDATA=WKGData1[0]
                            try:                                
                                global SERIALDATA
                                SERIALDATA=str(WKGDATA)
                                float(SERIALDATA)
                            except:
                                #print "Exception "
                                continue
   
                        elif(WKGData.find("gram")>0):
                            WKGData1=WKGData.split('gram')
                            WKGDATA=WKGData1[0]
                                                      
                            try:
                                
                                global SERIALDATA
                                SERIALDATA=str(WKGDATA)
                                float(SERIALDATA)
                            except:
                                #print "Exception "
                                continue
                        else:
                            continue

                        
                        #time.sleep(1)
                        
                except serial.SerialException:
                    #print "ERRORRRRRRRRRRRRRRRRRRRRRRRRRR"
                    self.stop()
                    #print "ERRORRRRRRRRRRRRRRRRRRRRRRRRRR"
                #SERIALDATA=str(SignValue)+str(val[2:9])
                #VALUE=str(val).split(" ")
                #print ":::::::::::::::::::::::::::::::::::::::::::::::::::" +str(VALUE[1])
                #SERIALDATA=str(val[2:9])
            
                SERIALDATA_STRING=str(SERIALDATA)
                #print SERIALDATA_STRING
                global SERIAL_DATA_P
                SERIAL_DATA_P=SERIALDATA
                CHECK_DATA=str("Null")
                self.emit(QtCore.SIGNAL('SERIAL'),SERIALDATA_STRING)
                self.emit(QtCore.SIGNAL('combine'),CHECK_DATA)



                
        """*

        * Function    :  stop

        *

        * Description :  (TO Stop the thread.)

        *

        * parameters  :

        *          1  :  param1 = self

        *        

        *

        * Returns     :  0 => Ok, everything else is an error.



        *"""            

                
          

                
    def stop(self):
        #print "Thread Stop"
        self.stopFlag=True




if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    #print "Starting .."
    window = MyApp()
    window.show()
    #print "Starting ...."
    sys.exit(app.exec_())
    #print "3"


