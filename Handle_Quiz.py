 @app.route("/callback", methods=['POST'])
def webhook():
    # ... (code from previous step)

    # Parse the received message event
    for event in events:
        if event.type == 'message':
            handle_quiz(event)

    return 'OK'
