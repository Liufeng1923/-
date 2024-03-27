#!/bin/bash

# 调用Python执行脚本
# 注意：请根据实际安装的Python路径和脚本位置进行修改
python /Users/liufe/Desktop/ShokenGaimuInNote/generate_new_html.py

# 切换到脚本所在目录
cd /Users/liufe/Desktop/ShokenGaimuInNote/

# 添加文件到Git，提交并推送
git add .
git commit -m "quick commit"
git push -u origin master
