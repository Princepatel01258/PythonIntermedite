import json

json_string = '''
   {
    "students": [
        {
           "id": 1,
           "name": "Prince",
           "age": 18,
           "full-time": true
        },
        {
           "id": 2,
           "name": "Joe",
           "age": 33,
           "full-time": false    
        }   
      ] 
   }  
'''

data = json.loads(json_string)
print(data['students'][0])