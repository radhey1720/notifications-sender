import pandas as pd
import datetime
import smtplib #library used to send email 


GMAIL_ID = "hackerspider1720@gmail.com"
GMAIL_PSWD = "Mnnit@156"


def sendEmail(to,sub,msg): 
    print(f"Email to {to} sent with subject: {sub} and message : {msg}")
    s = smtplib.SMTP("smtp.gmail.com",587) #smtp ka gmail server hai
    s.starttls() # its always to be put up for secure tls server
    s.login(GMAIL_ID,GMAIL_PSWD)

    s.sendmail(GMAIL_ID,to,msg) # from,to,msg
    s.quit


#sendEmail(GMAIL_ID,"subject","test message")
df = pd.read_excel("radhey.xlsx") #df function is used to take data from excel sheet(dataframe)
#print(df)

today = datetime.datetime.now().strftime("%d-%m") # isko use karte hai for date and time
#print(today) # d -- se date print hone ke liye

for index,item in df.iterrows(): # data frame is used to get the particular rows or column
    #print(index,item["BIRTHDAY"])
    bday = item["BIRTHDAY"].strftime("%d-%m")
    #print(bday)
    if (today == bday):
        sendEmail(item["EMAIL ID"],"happy birthday",item["MESSAGE"])# item use kar rahe to access and rows and column
          #iska automatic matlab hai ki execute karo isse










 



