
# Set your OpenAI API key
# openai.api_key =  'sk-proj-TALBx8lGB3ZJDcAvKbgqT3BlbkFJ7ViDypPHibEECBNCQzF3'

from flask import Flask, request, jsonify, send_file

app = Flask(__name__)

# Serve the HTML file
@app.route('/')
def home():
    return send_file('index.html')

# Handle chat functionality
@app.route('/chat', methods=['POST'])
def chat():
    # Receive user input from the frontend
    user_input = request.json['user_input']

    # Process user input and generate bot response (replace with your actual logic)
    bot_response = generate_bot_response(user_input)

    # Return bot response to frontend
    return jsonify({'bot_response': bot_response})

# def generate_bot_response(user_input):
#     # Implement your chatbot logic here (e.g., using NLP libraries, database queries, etc.)
#     # For now, let's just echo the user input
#     return f"You said: {user_input}"


    return bot_response

def generate_bot_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input:
        bot_response = "Hello! How can I assist you today?"
    elif "what are your visiting hours?" in user_input:
        bot_response = "Our visiting hours are from 10:00 AM to 8:00 PM every day."
    elif "how can I schedule an appointment?" in user_input:
        bot_response = "You can schedule an appointment by calling our reception or visiting our website."
    elif "do you offer psychological services?" in user_input:
        bot_response = "Yes, we have psychologists available to assist with various mental health concerns."
    elif "what should I do if I'm feeling anxious?" in user_input:
        bot_response = "If you're feeling anxious, you can speak with one of our psychologists or schedule an appointment for further assistance."
    elif "how can I reach your customer support?" in user_input:
        bot_response = "You can reach our customer support team by phone, email, or live chat."
    elif "where can I find your FAQs?" in user_input:
        bot_response = "You can find our FAQs on our website's support page."
    elif "what are the features of your products?" in user_input:
        bot_response = "Our products include [list of features]."
    elif "how can I schedule a product demo?" in user_input:
        bot_response = "You can schedule a product demo by contacting our sales team or filling out the demo request form on our website."
    elif "can you help me with a technical issue?" in user_input:
        bot_response = "Sure, please provide more details about the technical issue you're experiencing."
    else:
        bot_response = "I'm sorry, I'm not sure how to respond to that. Could you please rephrase?"

    return bot_response


if __name__ == '__main__':
    app.run(debug=True)







