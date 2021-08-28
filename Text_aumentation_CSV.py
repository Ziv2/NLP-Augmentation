import requests
import pandas as pd
from tqdm import tqdm

def parse_suggestions(response, sentence):
    if response.ok:
        data = response.json()
        output = [] * data.__len__()
        for index, suggestion in enumerate(data['suggestions']):
            if suggestion[1][0] != 0:
                middle1 = suggestion[1][0]
                middle2 = suggestion[1][1]
                if middle2 == len(sentence):
                    output.append(sentence[0:middle1] + suggestion[0])
                else:
                    output.append(sentence[0:middle1] + suggestion[0] + sentence[middle2:])
            else:
                middle = suggestion[1][1]
                if middle < len(sentence):
                    output.append(suggestion[0] + sentence[middle:])
                else:
                    output.append(suggestion[0])
        return output

def get_data(text):
    url = "https://api.wordtune.com/rewrite"
    headers = {'token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE2Mjg5NzcyNDksInN1YiI6Ijk4YTg2NDQ5LWY3OWItNDgwMS04NjJkLTg4MWJkNDYxNzQzOSIsInBsYW5fdHlwZSI6IkZSRUUiLCJwbGFuX2V4cGlyYXRpb24iOm51bGwsImV4cCI6MTYzMTU2OTI0OSwiZXhwZXJpbWVudCI6bnVsbCwiZmxhZ3MiOltdLCJzY29wZXMiOlsicmVmaW5lLmZ1bGwiLCJjb3JyZWN0aW9ucy5mdWxsIiwicmVjb21tZW5kYXRpb25zLmZ1bGwiLCJ0cmF2ZXJzaW5nLmZ1bGwiLCJyZXdyaXRlLmdlbmVyaWMuZnVsbCJdLCJzY29wZXNDb25maWciOnsicmVmaW5lLmZ1bGwiOnsiaXNUcmlhbCI6ZmFsc2V9LCJjb3JyZWN0aW9ucy5mdWxsIjp7ImlzVHJpYWwiOmZhbHNlfSwicmVjb21tZW5kYXRpb25zLmZ1bGwiOnsiaXNUcmlhbCI6ZmFsc2V9LCJ0cmF2ZXJzaW5nLmZ1bGwiOnsiaXNUcmlhbCI6ZmFsc2V9LCJyZXdyaXRlLmdlbmVyaWMuZnVsbCI6eyJpc1RyaWFsIjpmYWxzZX19LCJ0cmlhbF9zdGFydF90cmlnZ2VyIjoiT05fQ0MiLCJ0cmlhbF9leHBpcmF0aW9uIjpudWxsLCJ0cmFjZWxlc3MiOmZhbHNlLCJ3aXhfaW5zdGFuY2VfaWQiOm51bGwsInF1b3RhX2xpbWl0IjpudWxsLCJxdW90YV9jeWNsZSI6bnVsbCwicmVhZF9wbGFuX3R5cGUiOm51bGx9.tAFNg3WVBZ7s5DZCxDPwOpCEJster_M_QExfwqte3CE'}
    params = {
            "text": text,
            "action": "REWRITE",
            "start": 0,
            "end": len(text),
            "selection": {
                "wholeText": text,
                "bulletText": "",
                "start": 0,
                "end": len(text)
            },
            "draftId": None,
            "emailAccount": None,
            "emailMetadata": {
                "to": [],
                "cc": [],
                "bcc": [],
                "selectedFrom": {
                    "emailAddress": None,
                    "name": None
                },
                "fromOptions": [
                    {
                        "emailAddress": None,
                        "name": None}
                ]
            },
            "lookaheadIndex": 0
    }
    return requests.post(url, json=params, headers=headers)

if __name__ == "__main__":
    DF = pd.read_csv(r'HandQ.csv',
                     error_bad_lines=False) #encoding="utf-8" , encoding = "cp1252" , encoding = "ISO-8859-1"
    DF = DF.dropna()
    DF.drop_duplicates(inplace=True)
    # DF.to_csv('DF.csv')
    # DF = pd.read_csv('DF.csv')
    New_DF = DF.iloc[[0]]
    length = DF.shape[0]
    New_index = 1
    for i in tqdm(range(0, length)):
        New_DF = pd.concat([New_DF, DF.iloc[[i]]])
        New_DF.iloc[[New_index], 0] = New_index
        New_index += 1
        # Prepare the augmentation:
        sentence = DF['Sample Questions'][i]
        data = get_data(sentence)
        for result in parse_suggestions(data, sentence):
            New_DF = pd.concat([New_DF, DF.iloc[[i]]])
            New_DF.iloc[[New_index], 4] = result
            New_DF.iloc[[New_index], 0] = New_index
            New_index += 1
    New_DF = New_DF.drop_duplicates(subset='Sample Questions', keep='first')
    New_DF.to_csv('Out.csv', index=False)
