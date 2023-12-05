def multilevel_index(documents, keys):
    index = {}

    for document in documents:
        iLevel = index
        for key in keys:
            value = document[key]
            if value not in iLevel:
                iLevel[value] = {}
                iLevel = iLevel[value]
        if keys[-1] not in iLevel:
            iLevel[keys[-1]] = []
        iLevel[keys[-1]].append(document)
    print(index)
            
objects = [
    {"age": 12, "name": "Mateo", "last_name": "González"},
    {"age": 12, "name": "Julián", "last_name": "Fernández"},
    {"age": 25, "name": "Arturo", "last_name": "González"},
]


multilevel_index(objects, ["age", "last_name"])