import requests  
import json

def emotion_detector(text_to_analyse): 
    # Define the URL for the emotion detector API
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Create the payload with the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyse } }

    # Set the headers with the required model ID for the API
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Make a POST request to the API with the payload and headers
    response = requests.post(url, json = myobj, headers=header)  # Send a POST request to the API with the text and headers

    # Parsing the JSON response from the API
    formatted_response = json.loads(response.text)
    
    
    # If the response status code is 200, extract the values from the response
    if response.status_code == 200:
        # Extracting sentiment label and score from the response
        emotions =  formatted_response['emotionPredictions'][0]['emotion']
        anger_score = emotions['anger']
        disgust_score = emotions['disgust']
        fear_score = emotions['fear']
        joy_score = emotions['joy']
        sadness_score = emotions['sadness']
        dominant_emotion = max(emotions, key= emotions.get)
        # Returning a dictionary containing emotion detection results
        return {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': dominant_emotion
        }
    # If the response status code is 500, set the values to None
    elif response.status_code == 500:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
