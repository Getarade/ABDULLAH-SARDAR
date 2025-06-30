import os
import openai
from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Set OpenAI API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

# Route for home page
@app.route('/')
def home():
    """Render the main interface"""
    return render_template('index.html')

# API endpoint for content generation
@app.route('/generate', methods=['POST'])
def generate():
    """Handle content generation requests"""
    topic = request.json['topic']
    try:
        # Call OpenAI API
        response = openai.Completion.create(
            engine="text-davinci-003",  # AI model to use
            prompt=f"Write a detailed paragraph about: {topic}",
            max_tokens=200  # Limit response length
        )
        return jsonify({'content': response.choices[0].text.strip()})
    except Exception as e:
        # Handle errors gracefully
        return jsonify({'error': str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)  # debug=True enables auto-reload on code changes