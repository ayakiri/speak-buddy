from flask import jsonify, request, render_template
from transformers import pipeline
import torch

device = 0 if torch.cuda.is_available() else -1
print("Using ", "GPU" if device >= 0 else "CPU")
answer_pipeline = pipeline('text-generation', model='TinyLlama/TinyLlama-1.1B-Chat-v1.0', device=device, max_length=1024, max_new_tokens=1024)
correct_pipeline = pipeline('text2text-generation', model='ayakiri/sentence-correction', device=device, max_length=1024, max_new_tokens=1024)


def configure_routes(app):
    @app.route('/')
    def home():
        return render_template('index.html')

    @app.route('/answer', methods=['POST'])
    def answer():

        data = request.get_json()
        if not data or 'message' not in data:
            return jsonify({'error': 'No message provided in JSON'}), 400

        message = data['message']

        # Create a prompt that leads to a playful, child-like response from the second child
        prompt = f'''<|system|>
                    You are a friendly chatbot who loves talking with children about their day.</s>
                    <|user|>
                    {message}</s>
                    <|assistant|>'''

        # Generate the response using TinyLlama or another model
        response = answer_pipeline(prompt, max_length=50, num_return_sequences=1)

        # Clean up the response to remove any prompt-related text
        generated_text = response[0]['generated_text']

        # Remove everything before the assistant's response (usually the prompt will include <|assistant|> token)
        child_response = generated_text.split("<|assistant|>")[-1].strip()

        return jsonify({
            'input': message,
            'response': child_response
        })

    @app.route('/correct', methods=['POST'])
    def correct():
        data = request.get_json()
        if not data or 'message' not in data:
            return jsonify({'error': 'No message provided in JSON'}), 400

        message = data['message']

        corrected = correct_pipeline(message, max_length=100, num_return_sequences=1)

        return jsonify({
            'input': message,
            'corrected': corrected[0]['generated_text']
        })
