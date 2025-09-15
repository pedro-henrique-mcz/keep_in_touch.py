'''This module is responsible for small and 
general function which helps the '''
import json


def open_json_file(json_file:str):
    '''This function helps the controller to 
    open json files and return the data.''' 
    try:
        with open(json_file) as file:
            data = json.load(file)
    except FileNotFoundError:
        raise FileNotFoundError(f'File "{json_file}" Not Found')
    else:
        return data