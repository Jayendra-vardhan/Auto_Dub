import json 

jsonf=open(r"D:\UPES\Project\Project Auto_Dub\Transcribe\response.json")
response = json.loads(jsonf)   
    
for alternatives in response.result:
    print(alternatives.words.word+'/n')    