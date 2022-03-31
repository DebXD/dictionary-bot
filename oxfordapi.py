import requests
import json
from decouple import config

app_id = config("OXFORD_APP_ID")
app_key = config("OXFORD_APP_KEY")



def get_result(word):
    language = "en-gb"
    word_id = word
    url = "https://od-api.oxforddictionaries.com:443/api/v2/entries/" + language + "/" + word_id.lower()
    headers = {"app_id":app_id, "app_key":app_key}
    r = requests.get(url, headers = headers)
    #print(r)
    #print(r.text)
    #print(type(r.text))
    data = json.loads(r.text)
    #print(type(data))
    if data.get("results") is None:
        print(data.get("error"))
    else:
        result = data.get("results")[0]
        print(type(result))
        return result
        
def get_audio(result):
    print(type(result))
    try:
        audio = result.get("lexicalEntries")[0].get("entries")[0].get("pronunciations")[0].get("audioFile")
        print(audio)
        return audio
    except:
        audio = "None"
        return audio
    
def get_meaning(result):
    #data = json.loads(r.text)
    #result = data.get("results")[0]
    meaning = result.get("lexicalEntries")[0].get("entries")[0].get("senses")[0].get("definitions")[0]
    print(meaning)
    return meaning
    
def get_example(result):
    try:
        example = result.get("lexicalEntries")[0].get("entries")[0].get("senses")[0].get("examples")[0].get("text")
        print(example)
        return example
    except:
        example = "None"
        return example
        
#result = get_result("awkward")
#print(result)
