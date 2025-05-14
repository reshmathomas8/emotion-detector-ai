''' Executing this function initiates the application of 
emotion detection to be executed over the Flask channel 
and deployed on localhost:5000.
'''
# Import Flask, render_template, request from the flask pramework package : TODO
from flask import Flask, render_template, request
# Import the emotion detector function from the package created
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app
app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def emotion_detection():
    """
    Analyze the user-provided text for emotions and return the result.
    """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')
    # Pass the text to the sentiment_analyzer function and store the response
    response = emotion_detector(text_to_analyze)
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again."
    return (
        f"For the given statement, the system response is 'anger': {response['anger']} "
        f"'disgust': {response['disgust']}, 'fear': {response['fear']}, "
        f"'joy': {response['joy']} and 'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )

@app.route("/")
def render_index_page():
    """
    Initiates the rendering of the main application page over the Flask channel
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
