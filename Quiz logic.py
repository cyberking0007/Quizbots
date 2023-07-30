# quiz_bot.py

user_score = 0

def handle_quiz(event):
    global user_score
    question_number = event['question_number']
    user_answer = event['user_answer']

    correct_option = quiz_questions[question_number]['correct_option']
    if user_answer == correct_option:
        user_score += 1
        reply_message = "Correct! 🎉"
    else:
        reply_message = "Incorrect. 😕"

    if question_number < len(quiz_questions) - 1:
        next_question = quiz_questions[question_number + 1]['question']
        answers = quiz_questions[question_number + 1]['answers']
        reply_message += f"\n\nNext Question: {next_question}\n{', '.join(answers)}"
        question_number += 1
    else:
        # Quiz completed, show the final score
        reply_message += f"\n\nQuiz Completed! Your Score: {user_score}/{len(quiz_questions)}"
        user_score = 0  # Reset the score for the next quiz

    send_reply(reply_message)

def send_reply(message):
    # Implement the code to send a reply message to the user using the LINE Messaging API SDK
    # For example, you can use the LINE-bot-sdk-python's functions to send replies.
    pass
