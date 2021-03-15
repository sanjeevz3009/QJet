#Imports the necessary stmp modules.
import smtplib 
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import random 
from emailValid import *

#Recieves the email and password as agruements from the password reset window. 
def sendCode(email, password):
    userInput = email
    subject = "Password reset:"
    recievePassword = "Your password is: " + password

    #SMTP server username.
    username = "qjetbot1111@gmail.com"
    #SMTP server password.
    password = "Qjet1010"
    message = MIMEMultipart("mixed")
    
    #Subject for the email.
    message["Subject"] = subject
    #Message for the email.
    message["From"] = username
    #The email address to send the email.
    message["To"] = userInput

    #Text to send in the email, in this case the password for the email address requested to be resetted..
    textMessage = MIMEText(recievePassword, "plain")
    #htmlMessage = MIMEText(, "html")
    #Attaches the message
    message.attach(textMessage)
    #message.attach(htmlMessage)

    #Connects to the gmail server, in this case uisng gmail SMTP server and using port 587.
    mailServer = smtplib.SMTP("smtp.gmail.com", 587) #Alternative ports: 8025, 587 and 25.
    #Identify yourself to an ESMTP server using EHLO.
    mailServer.ehlo()
    #Puts the SMTP connection in TLS(Transport Layer Security) mode.
    #All SMTP commands that follow will be encrypted.
    mailServer.starttls()
    mailServer.ehlo()
    #Logins to the gmail server using the username and password provided.
    mailServer.login(username, password)
    #Sends the email to the email address with it's content.
    mailServer.sendmail(userInput, userInput, message.as_string())
    #Closes the mail server.
    mailServer.close()

    print(f"Your verification code has been sent to {userInput}.")

if __name__ == "__main__":
    sendCode()



