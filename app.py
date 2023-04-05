from flask import Flask, request, session
from twilio.twiml.messaging_response import MessagingResponse
from chatbot import askgpt

app = Flask(__name__)
app.config['SECRET_KEY'] = 'top-secret!'


@app.route('/sms', methods=['POST'])
def bot():
    incoming_msg = request.values['Body']
    chat_log = session.get('chat_log')

    answer, chat_log = askgpt(incoming_msg, chat_log)
    session['chat_log'] = chat_log

    r = MessagingResponse()
    r.message(answer)
    return str(r)