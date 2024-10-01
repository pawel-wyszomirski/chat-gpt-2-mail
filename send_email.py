from flask import Flask, request, jsonify
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

app = Flask(__name__)

def send_email(conversation, recipient_email):
    sender_email = "twojemail@example.com"
    sender_password = "twojehaslo"

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = "Chat Conversation"
    body = f"Here is the conversation:\n\n{conversation}"
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.example.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(msg)
        server.quit()
        return "Email sent successfully"
    except Exception as e:
        return f"Failed to send email. Error: {str(e)}"

@app.route('/send-email', methods=['POST'])
def send_email_route():
    data = request.json
    conversation = data.get('conversation')
    email = data.get('email')
    result = send_email(conversation, email)
    return jsonify({"message": result})

if __name__ == '__main__':
    app.run(debug=True)
