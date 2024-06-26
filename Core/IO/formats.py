import json
import yaml
import os
from Core.IO import file_reader,file_writer

@file_reader('json')
def read_json(filepath) -> dict:
    ''' 读取 Json 文件 '''
    with open(filepath,encoding='utf-8') as f:
        data = json.load(f)
        return data

@file_reader(['yml','yaml'])
def read_yaml(filepath:str) -> dict:
    ''' 读取 Yaml 文件 '''
    with open(filepath,encoding='utf-8') as f:
        data = yaml.load(f,Loader=yaml.FullLoader)
        if data is None:
            data = {}
        data.update({'file_path':filepath})
        return data

@file_reader('txt')
def read_string(filepath:str):
    '''读取字符串文件'''
    with open(filepath, "r+",encoding="utf-8") as file:
        return file.read()

@file_writer('txt')
def write_string(filepath:str,data:str):
    '''写入字符串文件'''
    with open(filepath, "w",encoding="utf-8") as file:
        return file.write(data)
