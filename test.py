from flask import Flask, request, jsonify, send_file
import os
from groq import Groq

app = Flask(__name__)

# Define a route to serve the HTML file
@app.route('/')
def index():
     return send_file('gpt.html')

# Define a route to handle incoming chat requests
# @app.route('/chat', methods=['POST'])
# def chat():
#     # Initialize the Groq client
#     # client = Groq(api_key=os.environ.get("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"))
#     client = Groq(api_key="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")

    
#     # Get the user message from the request
#     data = request.get_json()
#     messages = data.get('messages', [])
    
#     # Create a chat completion using Groq API
#     chat_completion = client.chat.completions.create(messages=messages, model="mixtral-8x7b-32768")
    
#     # Return the response to the frontend
#     return jsonify(chat_completion.choices[0].message.content)


@app.route('/chat', methods=['POST'])
def chat():
    # Initialize the Groq client
    # client = Groq(api_key=os.environ.get("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"))
    client = Groq(api_key="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")

    # Get the user message from the request
    data = request.get_json()
    messages = data.get('messages', [])
    
    # Create a chat completion using Groq API
    chat_completion = client.chat.completions.create(messages=messages, model="mixtral-8x7b-32768")

    # Get the response message from the completion
    response_message = chat_completion.choices[0].message.content
    
    # Modify the response message based on some condition
    if "condition" in response_message:
        modified_response_message = "   " + response_message
    else:
        modified_response_message = "   " + response_message

    # Return the modified response to the frontend
    return jsonify(modified_response_message)


if __name__ == '__main__':
    app.run(debug=True)

