import requests

SWE_URL='https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
SWE_HEADERS={'grpc-metadata-mm-model-id': 'emotion_aggregated-workflow_lang_en_stock'}

def emotion_detector(text_to_analyze):
    response = requests.post(SWE_URL, 
        headers=SWE_HEADERS, 
        json={'raw_document': {'text': text_to_analyze}}
    )

    data = {
        'anger': None,
        'disgust': None,
        'fear': None,
        'joy': None,
        'sadness': None,
        'dominant_emotion': None
    }
    
    if response.status_code == 200:
        emotions = response.json()['emotionPredictions'][0]['emotion']
        for k in data.keys():
            data[k] = emotions.get(k)
        data['dominant_emotion'] = max(emotions, key=lambda x: emotions[x])
    
    return data
