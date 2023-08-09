import json,os
import configparser

## current working directory 

cwd = os.getcwd()

## config file

config=configparser.ConfigParser()
config.read("options.ini",encoding='utf-8')

## getting json

file = open(cwd+'\\data\\'+config['LANGUAGE']['lang']+'.json','r')
jsonText = "".join(file.readlines())

settings_data = json.loads(jsonText)

class jsonparser():
    def __init__(self) -> None:
        pass