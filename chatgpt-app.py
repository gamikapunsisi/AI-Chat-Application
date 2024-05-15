import openai
from flask import Flask, request, jsonify, send_file
from langchain import GPT3LanguageModel
from groq import Groq

app = Flask(__name__)

# Configure OpenAI API
openai.api_key = 'sk-proj-TALBx8lGB3ZJDcAvKbgqT3BlbkFJ7ViDypPHibEECBNCQzF3'

# Initialize LangChain generator
generator = GPT3LanguageModel(api_key=openai.api_key, model_name="text-davinci-003")

# Initialize Groq client
# client = Groq(api_key=os.environ.get("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"))
client = Groq(api_key="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")

# Dummy dataset of call center problems and solutions
call_center_data = {
    "issue1": "solution1",
    "issue2": "solution2",
    "issue3": "solution3",
    # Add more entries as needed
}

def retrieve_solution(user_query):
    # Retrieve solution from the dataset based on user query
    return call_center_data.get(user_query.lower(), "Sorry, I couldn't find a solution for that problem.")

def generate_response(user_query):
    # Retrieve solution for the user query
    solution = retrieve_solution(user_query)
    
    # Generate additional context or details using OpenAI API
    generated_text = generator.generate(prompt=solution, max_tokens=50)
    
    # Combine retrieved solution with generated text
    final_response = f"Solution for '{user_query}':\n{solution}\n\nAdditional context:\n{generated_text}"
    
    return final_response

# Define a route to serve the HTML file
@app.route('/')
def index():
    return send_file('gpt.html')

# Define a route to handle incoming chat requests
@app.route('/chat', methods=['POST'])
def chat():
    # Get the user message from the request
    data = request.get_json()
    user_query = data.get('message')

    # Generate response using RAG-based chatbot
    response = generate_response(user_query)
    
    # Return the response to the frontend
    return jsonify({"message": response})

# Define a route to handle incoming chat requests for Groq-based chatbot
@app.route('/groq-chat', methods=['POST'])
def groq_chat():
    # Get the user message from the request
    data = request.get_json()
    messages = data.get('messages', [])
    
    # Create a chat completion using Groq API
    chat_completion = client.chat.completions.create(messages=messages, model="mixtral-8x7b-32768")
    
    # Return the response to the frontend
    return jsonify(chat_completion.choices[0].message.content)

if __name__ == '__main__':
    app.run(debug=True)
