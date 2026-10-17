import requests, json

def emotion_detector(text_to_analyze=""):
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    obj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(URL, headers=header, json=obj)
    
    if response.status_code == 400:
        return {'anger': None, 'disgust': None, 'fear': None, 'joy': None, 'sadness': None, 'dominant_emotion': None}

    formatted_text = json.loads(response.text)
    emotion = formatted_text.get('emotionPredictions')[0]['emotion']
    sorted_emotion = dict(sorted(emotion.items(), key=lambda x: x[1]))
    return {'anger': sorted_emotion['anger'], 'disgust': sorted_emotion['disgust'], 'fear': sorted_emotion['fear'], 'joy': sorted_emotion['joy'], 'sadness': sorted_emotion['sadness'], 'dominant_emotion': list(sorted_emotion.keys())[-1]}




