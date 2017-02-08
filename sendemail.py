import smtplib 
from_addr = 'richard.gooden5@gmail.com' 
to_addr  = 'richard.gooden@yahoo.com' 
from_name = 'richardgooden5'
to_name = 'richard.gooden'
subject = 'test'
message = """
From: 'richard.gooden5' <richard.gooden5@gmail.com>
To: 'richard.gooden' <richard.gooden@yahoo.com>
Subject: test
"""
msg= 'testing'
message_to_send = message.format(from_name, from_addr, to_name, to_addr, subject, msg) 
# Credentials (if needed) 
username = 'richard.gooden5@gmail.com' 
password = 'kecaraajycfwcxud' 
# The actual mail send 
server = smtplib.SMTP('smtp.gmail.com:587') 
server.starttls() 
server.login(username, password) 
server.sendmail(from_addr, to_addr, message_to_send) 
server.quit() 