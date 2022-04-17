import requests
import json

def rm(ci,mid = -1):
    headers = {
            'authorization' : 'secret'
    }
    r = '';
    if mid==-1:
        r = requests.get(f'https://discord.com/api/v8/channels/{ci}/messages?limit=100', headers =headers);
    else:
        r = requests.get(f'https://discord.com/api/v8/channels/{ci}/messages?before={mid}&limit=100', headers =headers);
    js = json.loads(r.text);
    for i in js:
        try:
            print(i);
        except:
            print("RIP");
    print();
    try:
        lst = js[-1]['id'];
    except:
        lst = mid;
    #lst = js[-1];
    return lst;
cid = '847123003842101250';
cur  = rm(cid);
i = 0;
while i<9:
    cur = rm(cid, cur);
    i+=1;
print("DONE");
