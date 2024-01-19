import requests
import json


def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyze } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url , json = myobj, headers = header)
    res=json.loads(response.text)
    formatted_response=res["emotionPredictions"][0]["emotion"]
    maxValue = max(formatted_response.values())
    maxKey=""
    for key, value in formatted_response.items():
        if(value == maxValue):
            maxKey = key
            break
    formatted_response.update({"dominant_emotion": maxKey})
    return formatted_response














