from cv2 import *
import xlsxwriter
from xlsxwriter.utility import xl_rowcol_to_cell
import xlrd
import otp
import sms
import time
from face import *
from res import *
from ress import *
#258652289867
myPath= 'dataset.xlsx'
myPath1='party.xlsx'
data =[]
partyy=[]
mobile =""
otpp=""
img=""
addr=""
voteid=""
aadhar=[]

def takeSnap():
    print("Taking Snapshot")
    cam= VideoCapture(0)
    s,img=cam.read()
    if s:
        temp1="target.jpg"
        imwrite(temp1,img)
    cam.release()
    print("Snapshot taken")

def readdata(a):
    for sh in xlrd.open_workbook(myPath).sheets():  
        for row in range(sh.nrows):
            data.clear()
            for col in range(sh.ncols):
                myCell = sh.cell(row, col)
                data.append(myCell)
                if myCell.value == int(a):
                    return(data,"Found")
    else:
        return("Node","None")
def readparty(b):
    for sh in xlrd.open_workbook(myPath1).sheets():  
        for row in range(sh.nrows):
            partyy.clear()
            for col in range(sh.ncols):
                myCell = sh.cell(row, col)
                partyy.append(myCell)
                if myCell.value == b:
                    return(partyy,"Found")
    else:
        return("Node","None")
    
while True:
    y=input("\nEnter Aadhar Number :")
    for i in aadhar:
        if(i==y):
            print("Your are not allowed to cast your vote again.\nYour Vote has been casted before.")
            break
    else:
        t=readdata(y)
        #print(t)
        if(t[1]=="Found"):
            dd=t[0]
            #print(dd)
            for i in range(len(dd)):
                x=str(dd[i]).split(':')[1].replace("'","")
                #x=x.split(":")[1]
                if(i==0):
                    print("Name Of The Candidate :" + x)
                elif(i==1):
                    print("Ph No Of The Candidate :" + str(int(float(x))))
                    mobile=str(int(float(x)))
                elif(i==2):
                    print("Email Of The Candidate :" + x)
                elif(i==3):
                    print("Address Of The Candidate :" + x)
                    addr=x
                elif(i==4):
                    print("Voter ID No Of The Candidate :" + x)
                    voteid=x
                elif(i==5):
                    print("Image No Of The Candidate :" + x)
                    img=x
                elif(i==6):
                    print("Aadhar No Of The Candidate :" + str(int(float(x))))
                    aadhar.append(str(int(float(x))))
            #print("+91"+mobile)
            idd=input("\nEnter Your Voter Id Number :")
            if(idd==voteid):
                print("Your Voter ID Matched \n")
                print("Your Mobile number is "+mobile+'\n')
                f=input("Enter Y/y to Send OTP & N to change Mobile Number : ")
                if(f=='Y' or f=='y'):
                    pass
                else:
                    mobile=input('Enter Mobile Number:')
                    #print("Your Mobile was changed to "+mobile)
                print('Sending OTP to Your Mobile Number :' +mobile)
                otpp=otp.otp()
                #print(otpp)
                sms.sendsms("+91"+mobile,"Your Verification Code is "+otpp)
                tt=input("Enter Your Verification Code:")
                if(tt==otpp):
                    print("You are Verified\n")
                    print("Place your face infront of camera") 
                    time.sleep(2)
                    takeSnap()
                    img='1.jpg'
                    t=face_reg(REGION,ACCESS_ID,ACCESS_KEY,source='images/'+img,target='target.jpg')
                    #print(t)
                    #t=1
                    if(t==1):
                        k=readparty(addr)
                        #print(t)
                        if(k[1]=="Found"):
                            ddd=k[0]
                            #print(ddd)
                            for i in range(len(ddd)):
                                x=str(ddd[i]).split(':')[1].replace("'","")
                                if(i==0):
                                    print("\nYSRCP Candidate : "+x)
                                elif(i==1):
                                    print("TDP Candidate : "+x)
                                elif(i==2):
                                    print("JENASENA Candidte : "+x)
                                elif(i==3):
                                    print("BJP Candidte : "+x)
                            print("\nEnter A to Vote for YSRCP Party\nEnter B to Vote for TDP Party \nEnter C to Vote for JENASENA Party \nEnter D to Vote for BJP Party\n")
                            s=readres()
                            votee=input()
                            if(votee=="A" or votee=="a"):
                                val=1+int(s[0])
                                updateres(2,1,val)
                                votee='YSRCP'
                            elif(votee=='B' or votee=='b'):
                                val=1+int(s[1])
                                updateres(2,2,val)
                                votee='TDP'
                            elif(votee=='C' or votee=='c'):
                                val=1+int(s[2])
                                updateres(2,3,val)
                                votee='JENASENA'
                            elif(votee=='D' or votee=='d'):
                                val=1+int(s[3])
                                updateres(2,4,val)
                                votee='BJP'
                            print("You Have voted for "+votee+" Party \nThank You")
                    else:
                        print("Your are Not Verified to cast vote")
                else:
                    print("You are Not Verified")
            else:
                print("No Voter ID Found")
        else:
            print("No Aadhar Found")
