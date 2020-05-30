f=open("./accuracy.txt","r")
y=[]
file=f.readlines()
for line in file:
    y.append(float(line.strip()))
accuracy=str(y[0])
f.close()
print("accurcacy for your model:",accuracy)


import smtplib, ssl

port = 465 #For SSL
smtp_server ="smtp.gmail.com"
sender_email="sivanaikk0903@gmail.com"    #Sender's Mail Address
receiver_email="sivanaikk143@gmail.com"      #Receiver's Mail Address
password="$iv@@.9.32..1"
if accuracy > "90":
    message="""    Subject: ML Training Report | Prediction Program


    
    CONGRATULATIONS! 
    
    
    Your code achieved {}% accuracy.""".format(accuracy)

else:
    message="""    Subject: ML Training  Report | Prediction Program
    
    TRained with all the Hyperparameters Train Again! by changing the Dataset.. 
    Your code got {}% accuracy.""".format(accuracy)
    
context=ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email,password)
    server.sendmail(sender_email, receiver_email, message)
