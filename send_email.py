import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(conversation, recipient_email):
    sender_email = "twojemail@example.com"
    sender_password = "twojehaslo"

    # Tworzenie obiektu wiadomości email
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = "Chat Conversation"

    # Treść emaila
    body = f"Here is the conversation:\n\n{conversation}"
    msg.attach(MIMEText(body, 'plain'))

    # Konfiguracja serwera SMTP
    try:
        server = smtplib.SMTP('smtp.example.com', 587)  # Zastąp odpowiednim serwerem SMTP
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(msg)
        server.quit()
        return "Email sent successfully"
    except Exception as e:
        return f"Failed to send email. Error: {str(e)}"
