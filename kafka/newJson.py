import json
from ff import userinfo
userif = userinfo(12,12)
#in_json = json.dumps(userif) # Encode the data
#print(in_json)

def student2dict(std):
    return {
        'pid': std.pid,
        'score': std.score
    }
print(json.dumps(userif, default=lambda obj: obj.__dict__))
print(json.dumps(userif, default=student2dict))