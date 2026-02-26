#5.Automated Config "Validator"
import os
import json, configparser, yaml

FOLDER = "./configs"

def valid_port(v):
    return isinstance(v, int) and 1024 <= v <= 65535

def check(data, file):
    ok = valid_port(data.get("port"))
    print(file, "OK" if ok else "INVALID")

for f in os.listdir(FOLDER):
    path = os.path.join(FOLDER, f)

    if f.endswith(".json"):
        d = json.load(open(path))
        check(d, f)

    elif f.endswith((".yml",".yaml")):
        d = yaml.safe_load(open(path))
        check(d, f)

    elif f.endswith(".ini"):
        c = configparser.ConfigParser()
        c.read(path)
        d = {k:int(v) for k,v in c["DEFAULT"].items()}
        check(d, f)