import os
from flask import Flask, render_template, request, jsonify
from quiz_generator.generator import generate_quiz_question

app = Flask(__name__)

@app.route('/')
def home():
    """
    Render the simple web interface.
    """
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    if not data or 'learning_objective' not in data:
        return jsonify({'error': 'Missing learning_objective parameter'}), 400

    learning_objective = data['learning_objective']

    try:
        quiz_question = generate_quiz_question(learning_objective)
        # Convert the Pydantic model to a dict before serializing to JSON
        return jsonify({'question': quiz_question.model_dump()})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Use the PORT environment variable, otherwise default to 5000.
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, port=port)
