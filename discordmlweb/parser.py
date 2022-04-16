# -*- coding: utf-8 -*-
"""
Created on Sat Apr 16 16:02:19 2022

@author: Johnny
"""

file = open("messages.txt", "r");    
output = open("output.txt", "w");

lines = file.readlines();
res = ["name,line\n"];

USER = "'\\u1cbc\\u1cbc'";
USERNAME = "'username': " + USER; 

for i in lines:
    #print(i.find("'username': '\\u1cbc\\u1cbc'"));
    if i.find(USERNAME) != -1:
        left = i.index("content") + 11;
        right = i.index("channel_id") - 4;
        msg = "";
        for j in range(left, right):
            if (i[j] == '<'):
                break;
            msg += i[j];
        msg.strip();
        if (len(msg) > 0):
            res.append(USER + "," + msg + "\n") ;
    elif i.find("'username'") != -1:
        left = i.index("content") + 11;
        right = i.index("channel_id") - 4;
        msg = "";
        for j in range(left, right):
            if (i[j] == '<'):
                break;
            msg += i[j];
        msg.strip();
        if (len(msg) > 0):
            res.append("anonymous" + "," + msg + "\n");
output.writelines(res);
output.write("");
print("parsed");

        

    
        
        
        
    

