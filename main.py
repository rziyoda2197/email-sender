import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class EmailSender:
    def __init__(self, host, port, from_addr, password):
        self.host = host
        self.port = port
        self.from_addr = from_addr
        self.password = password

    def send_email(self, to_addr, subject, message):
        msg = MIMEMultipart()
        msg['From'] = self.from_addr
        msg['To'] = to_addr
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))

        server = smtplib.SMTP(self.host, self.port)
        server.starttls()
        server.login(self.from_addr, self.password)
        text = msg.as_string()
        server.sendmail(self.from_addr, to_addr, text)
        server.quit()

# Misol foydalanish:
sender = EmailSender('smtp.gmail.com', 587, 'your_email@gmail.com', 'your_password')
sender.send_email('to_email@example.com', 'Subject', 'Hello, world!')
```

Kodni ishlatish uchun quyidagilar kerak:

1. `your_email@gmail.com` va `your_password` o'rniga o'zingizning Gmail yoki boshqa post-serverga kirish ma'lumotlarini kiritib, `EmailSender` klassining `__init__` metodiga berib qo'yin.
2. `to_email@example.com` o'rniga qabul qiluvchi email manzilini kiritib, `send_email` metodiga berib qo'yin.
3. `Subject` va `Hello, world!` o'rniga emailning mavzusi va matni kiritib, `send_email` metodiga berib qo'yin.
