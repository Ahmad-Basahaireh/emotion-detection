from emotion_detector import emotion_detector

def emotion_predictor(text):
    emotions = emotion_detector(text)
    if 'status' in emotions:
        return emotions
        
    return {
        'anger': emotions['anger'],
        'disgust': emotions['disgust'],
        'fear': emotions['fear'],
        'joy': emotions['joy'],
        'sadness': emotions['sadness'],
        'dominant_emotion': max(emotions, key=emotions.get)
    }