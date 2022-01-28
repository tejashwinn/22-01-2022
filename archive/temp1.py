import json

# Opening JSON file
f = open('C:\\Users\\tejas\\Desktop\\22-01-22\\.qt_for_python\\uic\\settings.json')

# returns JSON object as
# a dictionary
data = json.load(f)

# Iterating through the json
# list
print(data)

# Closing file
f.close()
