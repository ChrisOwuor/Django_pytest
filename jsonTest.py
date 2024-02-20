import json

stu = {
    "name": "chris",
    "age": 23
}
stu_json = json.dumps(stu)
print(stu_json)
stu_dict = json.loads(stu_json)
print(stu_dict)