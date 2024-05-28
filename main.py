import os
from dotenv import load_dotenv
from flask import Flask, request, render_template, jsonify


app = Flask(__name__)

load_dotenv()
TOKEN = os.getenv("YOUR_BOT_TOKEN")
CALLBACK_LINK = os.getenv("CALLBACK_LINK")


@app.route('/auth/login')
def auth_login():
    return render_template("login.html", link=CALLBACK_LINK)

@app.route('/auth/telegram/callback')
def telegram_callback():
    data = request.args.to_dict()

    # Bu yerda foydalanuvchi uchun sessiya yaratishingiz, foydalanuvchi ma'lumotlarini saqlashingiz mumkin.
    return jsonify({'status': 'ok', 'user': data})


if __name__ == '__main__':
    app.run(debug=True)
