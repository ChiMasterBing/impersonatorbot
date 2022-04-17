# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 16:02:19 2022

@author: Johnny
"""

file = open("message.txt", "r");    
output = open("twoname.csv", "w");

lines = file.readlines();
res = ["name,line\n"];

USER = "'\\u1cbc\\u1cbc'";
USERNAME = "'username': " + USER; 
cons = True;
runningMsg = "";
other = [];
for i in lines:
    #print(i.find("'username': '\\u1cbc\\u1cbc'"));
    if i.find(USERNAME) != -1:
        if cons == False:
            cons = True;
            adds = "";
            for j in range(0, min(7, len(other))):   
                adds += " \\n " + other[len(other)-min(7, len(other))-1+j];             
            adds = adds[4:len(adds)];
            res.append("anonymous" + ",\"" + adds + "\"" + "\n");
            other = [];
        left = i.index("content") + 11;
        right = i.index("channel_id") - 4;
        msg = "";
        for j in range(left, right):
            if (i[j] == '<'):
                break;
            msg += i[j];
        msg.strip();
        if (len(msg) > 0):
            runningMsg += (" \\n " + msg);
            
    elif i.find("'username'") != -1:
        if cons == True:
            runningMsg = runningMsg[4:len(runningMsg)];
            res.append(USER + "," + "\"" + runningMsg +  "\"" + "\n");
            cons = False;
            runningMsg = "";
        
        left = i.index("content") + 11;
        right = i.index("channel_id") - 4;
        msg = "";
        for j in range(left, right):
            if (i[j] == '<'):
                break;
            msg += i[j];
        msg.strip();
        if (len(msg) > 0):
            other.append(msg);
            
output.writelines(res);
output.write("");
print("parsed");
