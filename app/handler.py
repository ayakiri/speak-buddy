from flask import jsonify, request, render_template
from transformers import pipeline
import torch

device = 0 if torch.cuda.is_available() else -1
print("Using ", "GPU" if device >= 0 else "CPU")

answer_pipeline = pipeline(
    'text-generation',
    model='TinyLlama/TinyLlama-1.1B-Chat-v1.0',
    device=device,
    max_length=1024,
    max_new_tokens=1024
)
correct_pipeline = pipeline(
    'text2text-generation',
    model='ayakiri/sentence-correction',
    device=device,
    max_length=1024,
    max_new_tokens=1024
)


def configure_routes(app):
    """
    Configures the routes for the Flask application.

    Args:
        app (Flask): The Flask application instance.
    """
    @app.route('/')
    def home():
        """
        Renders the home page.

        Returns:
            Response: The rendered HTML template.
        """
        return render_template('index.html')

    @app.route('/answer', methods=['POST'])
    def answer():
        """
        Generates a child-friendly response to the given input message.

        Expects JSON input with a 'message' field.

        Returns:
            JSON: A JSON response containing the original message and the AI-generated response.
            HTTP Status 400: If the 'message' field is missing in the request.
        """

        data = request.get_json()
        if not data or 'message' not in data:
            return jsonify({'error': 'No message provided in JSON'}), 400

        message = data['message']

        prompt = f'''<|system|>
                    You are a friendly chatbot who loves talking with children about their day.</s>
                    <|user|>
                    {message}</s>
                    <|assistant|>'''

        response = answer_pipeline(prompt, max_length=50, num_return_sequences=1)

        generated_text = response[0]['generated_text']

        child_response = generated_text.split("<|assistant|>")[-1].strip()

        return jsonify({
            'input': message,
            'response': child_response
        })

    @app.route('/correct', methods=['POST'])
    def correct():
        """
        Corrects grammatical errors in the given input text.

        Expects JSON input with a 'message' field.

        Returns:
            JSON: A JSON response containing the original message and the corrected text.
            HTTP Status 400: If the 'message' field is missing in the request.
        """
        data = request.get_json()
        if not data or 'message' not in data:
            return jsonify({'error': 'No message provided in JSON'}), 400

        message = data['message']

        corrected = correct_pipeline(message, max_length=100, num_return_sequences=1)

        return jsonify({
            'input': message,
            'corrected': corrected[0]['generated_text']
        })
