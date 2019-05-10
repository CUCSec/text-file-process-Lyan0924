import os
a='201811123017.log'
b=' 学号：201811123017'
s=0
path=r'C:\Users\dell\Desktop\text-file-process-Lyan0924\text-file-process\log_files'

for file in os.listdir(path):
    if file==a:
        full=path+'\\'+file
        with open(full,encoding='utf8') as f:
            for line in f:
                num=line.split(',')[1] #分割字符串
                if num==b:
                    s=s+1
print(s)