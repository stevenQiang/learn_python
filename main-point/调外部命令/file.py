# -*- coding: utf-8 -*-
import os, subprocess

# 调用shell脚本 ls
os.system("ls")

print os.popen('ls').read()

subprocess.Popen('pwd', shell=True)
