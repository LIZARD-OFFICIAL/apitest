import json
from pathlib import Path

def _write(file,dict):
    with open(file,"w") as f:
        json.dump(dict,f)
def _read(file):
    with open(file, 'r') as f:
        return json.load(f)
def _f_exists(filename):
    return Path(filename).is_file()


class JsonDatabase:
    def __init__(self,name="db.json"):
        self._fname = name
        self.db = {}
        if not _f_exists(name):
            _write(name,{})
        else:
            self.db = _read(name)
    def update(self,d):
        self.db.update(d)
        _write(self._fname,self.db)
    def __setitem__(self,key,value):
        self.db[key] = value
        self.update({})
    def __getitem__(self,key):
        return self.db[key]
    def __contains__(self,key):
        return key in self.db.keys()

