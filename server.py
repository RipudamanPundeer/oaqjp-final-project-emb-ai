"""
Emotion Detection Flask Application.

This module provides a web interface and an API endpoint to analyze text
and detect underlying emotions using the EmotionDetection library.
"""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

# Flask application instance named in uppercase to satisfy pylint's
# constant naming style requirement at the module level.
APP = Flask(__name__)


@APP.route("/")
def index():
    """
    Render the main index page of the application.

    Returns:
        str: Rendered HTML template for the index page.
    """
    return render_template('index.html')


@APP.route("/emotionDetector", methods=["GET"])
def detect_emotion():
    """
    Analyze the query string parameter 'textToAnalyze' for emotions.

    Returns:
        tuple: A formatted response string and HTTP status code 400 if invalid,
               otherwise a formatted string with emotion scores.
    """
    text_to_analyze = request.args.get("textToAnalyze")
    if not text_to_analyze or not text_to_analyze.strip():
        return "Invalid text! Please try again!", 400

    response = emotion_detector(text_to_analyze)

    if response.get('dominant_emotion') is None:
        return "Invalid text! Please try again!", 400

    return (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']}, "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )


if __name__ == "__main__":
    APP.run(host='0.0.0.0', port=5000)
