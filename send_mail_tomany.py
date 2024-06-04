import smtplib as sm
from email.mime.text import MIMEText

obj=sm.SMTP('smtp.gmail.com',587)
obj.ehlo()
obj.starttls()
obj.login('smrutirekha.softwaredv@gmail.com','lqxr asgr conl vmwi')
subject="Testing Mail"
body="Hi how are you"
message="subject: {}\n\n{}".format(subject,body)
listadd=['charmy.smrutidash@gmail.com','smrutirekha.softwaredv@gmail.com','smrutiit2016@gmail.com','charmy.smrutidash.github@gmail.com']
obj.sendmail('smrutirekha.softwaredv@gmail.com',listadd,message)
print("yes mail has been sent")
obj.quit()
