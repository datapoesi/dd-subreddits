import json
import jsonpickle


def set2json(set):
    sampleJson = jsonpickle.encode(set)
    saveJSON(sampleJson)


def json2set(json):
    loaded_json = loadJSON(json)
    decodedSet = jsonpickle.decode(loaded_json)
    return decodedSet


def loadJSON(fileName):
    with open(f"{fileName}.json", encoding="utf8") as f:
        data = json.load(f)
    return data


def saveJSON(output_data, path):
    with open(f"{path}.json", "w", encoding="utf-8") as f:
        json.dump(output_data, f, ensure_ascii=False, indent=4)


def list_to_txt(list, path="output_file"):
    with open(f"{path}.txt", "w") as f:
        f.write(",".join(list))


def sort_dict(dict):
    return {k: v for k, v in sorted(dict.items(), key=lambda item: item[1])}


def txtFile_to_list(txtFile):
    txt_file = open(f"{txtFile}.txt", "r")
    list = txt_file.read().split(",")
    txt_file.close()
    return list
