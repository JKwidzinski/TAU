import json

def getdata(file_name, function):
    if '.json' in file_name:
        f = open(file_name)
        data = json.load(f)
        result_data = data["data"][function]
        f.close()
        return result_data
    elif '.xml' in file_name:
        print('sPAIN')
    else:
        print('What is this file?')
        