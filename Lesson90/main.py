import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

msg = MIMEMultipart()
msg['From'] = 'nadawca@gmail.com'
msg['To'] = 'odbiorca@gmail.com'
msg['Subject'] = 'Temat wiadomości'

tekst = 'Cześć! Oto przykładowa wiadomość e-mail z załącznikiem dokumentu pdf.'
msg.attach(MIMEText(tekst, 'plain'))

with open('dokument.pdf', 'rb') as file:
    pdf = MIMEApplication(file.read(), _subtype='pdf')
    pdf.add_header('Content-Disposition', 'attachment', filename='dokument.pdf')
msg.attach(pdf)

ssl_pol = ssl.create_default_context()

server = smtplib.SMTP_SSL('smtp.gmail.com', 465, context=ssl_pol)
server.login('nadawca@gmail.com', 'haslo_aplikacji')
server.send_message(msg)
server.quit()
