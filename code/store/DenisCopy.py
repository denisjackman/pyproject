#!/usr/bin/env python
import os 
os.system("say here we go")
os.system("say starting transfer")
sourceFile = '/Users/username/Documents/workspace/PythonTutorials/*.txt'
destFile = '.'
userName='username'
serverName='servername'
os.system("scp "+sourceFile+" "+userName+"@"+serverName+":"+destFile)
os.system("say transfer complete")
