# app.py

from flask import Flask, request, abort

app = Flask(__name__)

@app.route("/callback", methods=['POST'])
def webhook():
    # Verify the request is from LINE platform
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

if __name__ == "__main__":
    app.run()
