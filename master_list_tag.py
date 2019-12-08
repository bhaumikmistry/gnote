import json
import pathlib
from jsonio import jsonio
from constants import constants
import os
import copy

class master_list_tag:
    def __init__(self):
        self._master_tag_list_dir = ".gnote"
        self._master_tag_list_file = "_list.json"
        self._master_tag_list = self._master_tag_list_dir + "/" + self._master_tag_list_file
        self._tag_file = []
        self.__check_master_list()
    
    def __check_master_list(self):
        dir = pathlib.Path(self._master_tag_list_dir)
        if not dir.is_dir():
            os.makedirs(self._master_tag_list_dir)
            dir = pathlib.Path(self._master_tag_list_dir)
            if not dir.is_dir():
                raise ValueError('Program not able to create .gnote directory') 
        else:
            pass
            #print("all ok dir")
        path = pathlib.Path(self._master_tag_list)
        if not path.exists():
            tag_file = json.loads(copy.deepcopy(constants.empty_master_list))
            js = jsonio()
            js.write(tag_file,self._master_tag_list)
            # with open(self._master_tag_list,'w') as jsonfile:
            #     json.dump(tag_file, jsonfile, indent=4)
        else:
            pass
        js = jsonio()
        self._tag_file = js.read(self._master_tag_list)
        # with open(self._master_tag_list,'r') as jsonfile:
        #     tag_file = json.load(jsonfile)
        #     self._tag_file = tag_file
    
    def add_tag(self,tag):     
        if constants.TAG in self._tag_file:
            if tag not in self._tag_file[constants.TAG]:
                self._tag_file[constants.TAG] += [f"{tag}"]
            with open(self._master_tag_list,'w') as jsonfile:
                json.dump(self._tag_file, jsonfile, indent=4)

    def get_list(self):
        if constants.TAG in self._tag_file:
            return self._tag_file[constants.TAG]