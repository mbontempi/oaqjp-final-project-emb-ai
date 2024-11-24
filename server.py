from flask import Flask, request

from EmotionDetection import emotion_detection as ed

app = Flask('Emotion Detection App')

@app.route("/emotionDetector")
def emotion_detector():
    text = request.args.get('text')
    res = ed.emotion_detector(text)

    if res['dominant_emotion'] is None:
        return 'Invalid text! Please try again!'
        
    return ('For the given statement, the system response is '
        f"'anger': {res['anger']}, 'disgust': {res['disgust']}, "
        f"'fear\': {res['fear']}, \'joy\': {res['joy']} and "
        f"'sadness\': {res['sadness']}. "
        f"The dominant emotion is {res['dominant_emotion']}.")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
