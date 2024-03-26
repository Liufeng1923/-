@echo off
call H:/anaconda/python.exe c:/Users/liufe/Desktop/ShokenGaimuInNote/generate_new_html.py
cd /d c:/Users/liufe/Desktop/ShokenGaimuInNote/
git add .
git commit -m "quick commit"
git push -u origin master