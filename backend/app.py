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
    nl= 0;
    for i in js:
        try:
            if i=='\n':
                nl+=1;
            else:
                print(i);
        except:
            print("RIP");
    print();
    if nl>5:
        return -1;
    try:
        lst = js[-1]['id'];
    except:
        lst = mid;
    #lst = js[-1];
    return lst;
cid = '844600766575542362';
cur  = rm(cid);
i = 0;
pcur = cur;
while i<100:
    cur = rm(cid, cur);
    i+=1;
    assert pcur!=cur
    if cur ==-1:
        break;
    pcur = cur;
print("DONE");
