import smtplib

def sendemail(from_name, from_addr, to_name,to_addr, subject, msg):
    from_addr = 'keronthelevite@gmail.com'
    from_name= "Keron"
    to_name= 'Keron'
    to_addr = 'keronyoungjr@yahoo.com'
    Subject= 'Lab 3  Email Test'
    message = """From: {} <{}> To: {} <{}> Subject: {} {} """ 

    
     
    
    message_to_send = message.format(from_name, from_addr, to_name,to_addr, subject, msg)
    # Credentials (if needed)
    
    username = ''
    password = ''
    
    # The actual mail send
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(username, password)
    server.sendmail(from_addr, to_addr, message_to_send)
    server.quit() 