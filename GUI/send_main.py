import smtplib
import threading

from email import encoders
from tkinter import *
import tkinter.messagebox
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase


def sendMail():
    try:
        message = MIMEMultipart()
        message['From'] = txt_mail_from.get()
        message['To'] = txt_mail_to.get()
        message['Subject'] = 'This is test send mail from python'

        message.attach(MIMEText(txt_mail_message.get("1.0", END), 'plain'))

        attach_file_name = 'file/Intel_X86.pdf'
        attach_file = open(attach_file_name, 'rb')  # Open the file as binary mode
        payload = MIMEBase('application', 'octate-stream')
        payload.set_payload(attach_file.read())
        encoders.encode_base64(payload)  # encode the attachment
        # add payload header with filename
        payload.add_header('Content-Decomposition', 'attachment', filename=attach_file_name)
        message.attach(payload)

        smtp = smtplib.SMTP('smtp.gmail.com', 587)
        smtp.starttls()
        smtp.login('test@geniustree.co.th', 'mytestpassword')
        smtp.sendmail(txt_mail_from.get(), txt_mail_to.get(), message.as_string())
        smtp.quit()

        tkinter.messagebox.showinfo('Send mail', 'Successfully sent email')
    except smtplib.SMTPException:
        print('Error: unable to send email')


def sendMailAsync():
    if txt_mail_from.get() in '':
        tkinter.messagebox.showerror('Warring', 'Please insert mail from')
    elif txt_mail_to.get() in '':
        tkinter.messagebox.showerror('Warring', 'Please insert mail to')
    elif txt_mail_message.get("1.0", END) in '':
        tkinter.messagebox.showerror('Warring', 'Please insert mail message')
    else:
        threading.Thread.start_new_thread(sendMail)
        # sendMail()


main_form = Tk()
main_form.geometry("{}x{}".format(800, 500))

lb_mail_from = Label(main_form, text="Mail From : ")
lb_mail_to = Label(main_form, text="Mail To : ")
lb_message = Label(main_form, text="Mail Message : ")

txt_mail_from = Entry(main_form, width=50)
txt_mail_to = Entry(main_form, width=50)
txt_mail_message = Text(main_form)

btn_send = Button(main_form, text="Send Mail", command=sendMailAsync)

# set component layout
lb_mail_from.grid(row=0, column=0, sticky=N)
lb_mail_to.grid(row=1, column=0, sticky=N)
lb_message.grid(row=2, column=0, sticky=N)

txt_mail_from.grid(row=0, column=1, sticky=W)
txt_mail_to.grid(row=1, column=1, sticky=W)
txt_mail_message.grid(row=2, column=1, sticky=W)

btn_send.grid(row=3, column=1)

# pack component to form
# lb_mail_from.pack()
main_form.mainloop()
