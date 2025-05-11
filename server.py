from flask import Flask, request, jsonify
from emotion_predictor import emotion_predictor

app = Flask(__name__)

@app.route('/detect', methods=['POST'])
def detect_emotion():
    data = request.get_json()
    text = data.get('text', '')
    
    if not text:
        return jsonify({
            'status': 400,
            'message': 'No text provided'
        }), 400
        
    result = emotion_predictor(text)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)