from flask import Flask, request, jsonify, send_file
import openai

app = Flask(__name__)

openai.api_key = 'sk-proj-TALBx8lGB3ZJDcAvKbgqT3BlbkFJ7ViDypPHibEECBNCQzF3'

# Serve the HTML file
@app.route('/')
def home():
    return send_file('interface.html')

# Handle chat functionality
@app.route('/chat', methods=['POST'])
def chat():
    try:
        # Receive user input from the frontend
        user_input = request.json.get('user_input')

        if user_input:
            # Generate bot response using ChatGPT
            bot_response = generate_bot_response(user_input)
            return jsonify({'bot_response': bot_response})
        else:
            return jsonify({'error': 'Invalid request: No user input provided'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
def generate_bot_response(user_input):
    try:
        # Generate response using ChatGPT
        response = openai.ChatCompletion.create(
            model="text-davinci-003",  # Specify the model
            messages=[
                {"role": "user", "content": user_input}
            ],
            max_tokens=100,  # Adjust as needed
            temperature=0.7  # Adjust as needed
        )

        if response.choices:
            bot_response = response.choices[0].message.strip()
            return bot_response
        else:
            return "Sorry, I couldn't understand that."
    except Exception as e:
        return "An error occurred: " + str(e)


if __name__ == '__main__':
    app.run(debug=True)
