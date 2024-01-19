from flask import Flask , request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app=Flask("__name__")
@app.route("/emotionDetector")
def message():
    mess= str(request.args.get("textToAnalyze"))
    
    res = emotion_detector(mess)
    ans="For the given statement, the system response is 'anger': "+str(res["anger"])+", 'disgust': "+str(res["disgust"])+", 'fear': "+str(res["fear"])+", 'joy': "+str(res["joy"])+" and 'sadness': "+str(res["sadness"])+". The dominant emotion is <b>"+res["dominant_emotion"]+"</b>."
    return ans


@app.route("/")
def render_index_page():
    return render_template("index.html")





















