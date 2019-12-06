import json 
import copy

class jsonio:

    def __init__(self):
        self._file_name = ""
        self._json_data = []

    def read(self,filename):
        """[summary]
        Arguments:
            filename {[string]} -- [add json file name to read]
        """          
        self._file_name = filename
        with open(filename,'r') as jsonfile:
            tag_file = json.load(jsonfile)
            self._json_data = tag_file
        return copy.deepcopy(self._json_data)

    def write(self,json_data,filename,indent=4):
        """[summary]
        
        Arguments:
            json_data {[dict]} -- [json data to write]
            filename {[string]} -- [file namt to write to]
        
        Keyword Arguments:
            indent {int} -- [description] (default: {4})
        """        
        self._file_name = filename
        self._json_data = json_data
        with open(filename,'w') as jsonfile:
            json.dump(tag_file, json_data, indent=indent)
