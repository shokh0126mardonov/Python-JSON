import json

with open('students.json','r') as jsonfile:
    json_str = jsonfile.read()
    students = json.loads(json_str)

score_rating = list(sorted(students,key=lambda score:score['score'],reverse=True))

json_score_rating = json.dumps(score_rating,indent = 4)

with open('rating.json','w') as f2:
    f2.write(json_score_rating)
    