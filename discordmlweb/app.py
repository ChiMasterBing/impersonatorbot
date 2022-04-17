#You need to use following line [app Flask(__name__]

from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)
def rm(tok, ci,mid = -1):
    headers = {
            'authorization' : tok
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

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
@app.route('/result',methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        print(request.form);
        tok = secret
        cid = 844600766575542362
        cur = rm(tok, cid);
        i = 0;
        pcur = cur
        while i<100:
            cur = rm(cid, cur);
            i+=1;
            assert pcur!=cur
            if cur==-1:
                break;
            pcur = cur;
        user = (request.form['hi']);
        print(user);
    else:
        print("JMJ")
    return render_template('index.html')
if __name__ == '__main__':
    app.run(port=5000,debug=True)
