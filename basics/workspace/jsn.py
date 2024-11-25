import json

py_data = {
    1 : {
        "date" : "2024-12-01",
        "question" : "Znění otázky",
        "answer" : 123,
        "location" : "Where is it?"
    },
    2 : {
        "date" : "2024-12-02",
        "question" : "Znění otázky",
        "answer" : 123,
        "location" : "Where is it?"
    },
    3 : {
        "date" : "2024-12-03",
        "question" : "Znění otázky",
        "answer" : 123,
        "location" : "Where is it?"
    },
    4 : {
        "date" : "2024-12-04",
        "question" : "Znění otázky",
        "answer" : 123,
        "location" : "Where is it?"
    },
    5 : {
        "date" : "2024-12-05",
        "question" : "Znění otázky",
        "answer" : 123,
        "location" : "Where is it?"
    }
}

with open('./basics/workspace/vanoce.json', 'w') as json_file:
    json.dump(py_data, json_file, indent = 4)
