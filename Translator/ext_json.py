import json 

def Convert(jsonData):
    res_dct = {jsonData[i]: jsonData[i + 1] for i in range(0, len(jsonData), 2)}
    return res_dct

with open(r"D:\UPES\Project\Project Auto_Dub\Transcribe\all_words.json","r") as jsonf:
    jsonData = json.load(jsonf)
    
    # Driver code
    jsonData_out = Convert(jsonData)
    print(jsonData_out)

    print("Datatype of variable: ", type(jsonData_out))
   
              

# print(data["word"]+'/n')