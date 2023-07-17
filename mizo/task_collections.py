data = [{"age": 16, "name": "John", "sex": "M"},
        {"age": 34, "name": "Marry", "sex": "F"},
        {"age": 25, "name": "Mathew", "sex": "M"}]
sorted(data, key=lambda i: i["age"])  # ascending order
# Output: [{'age': 16, 'name': 'John', 'sex': 'M'},
#          {'age': 25, 'name': 'Mathew', 'sex': 'M'},
#          {'age': 34, 'name': 'Marry', 'sex': 'F'}]
sorted(data, key=lambda i: i["age"], reverse=True)
# Output: [{'age': 34, 'name': 'Marry', 'sex': 'F'},
#          {'age': 25, 'name': 'Mathew', 'sex': 'M'},
#          {'age': 16, 'name': 'John', 'sex': 'M'}]
sorted(data, key=lambda i: i["name"])
# Output  [{"age": 16, "name": "John", "sex": "M"},
#         {"age": 34, "name": "Marry", "sex": "F"},
#         {"age": 25, "name": "Mathew", "sex": "M"}])
sorted(data, key=lambda i: i["name"], reverse=True)
# Output [{"age": 25, "name": "Mathew", "sex": "M"}])
#         {"age": 34, "name": "Marry", "sex": "F"},
#          [{"age": 16, "name": "John", "sex": "M"}])
list(map(lambda i: i["name"], data))
# retrieves the "name" attribute from each dictionary, returns a list of those names
