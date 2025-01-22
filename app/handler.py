from flask import jsonify, request, render_template
from transformers import pipeline
import torch

device = 0 if torch.cuda.is_available() else -1
print("Using ", "GPU" if device >= 0 else "CPU")
answer_pipeline = pipeline('text-generation', model='gpt2', device=device, max_length=5120)
correct_pipeline = pipeline('text2text-generation', model='ayakiri/sentence-correction', device=device, max_length=5120)


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

        response = answer_pipeline(message, max_length=50, num_return_sequences=1)

        return jsonify({
            'input': message,
            'response': response[0]['generated_text']
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
