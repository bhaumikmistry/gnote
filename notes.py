import json
import os
import string
import random
import copy
import datetime
import sys, tempfile, os
from subprocess import call
import pathlib
from constants import constants
from master_list_tag import master_list_tag

class notes:
    
    def __init__(self,tag,name):
        self._tag = tag
        self._name = name
        self._json_name = "%s.json" % self._tag
        self.__is_json_file_present()
        pass

    def __is_json_file_present(self):
        self._if_json_exists = os.path.exists(self._json_name)       

    def __create_empty_json_note(self):
        # create empty tag file
        tag_file = json.loads(copy.deepcopy(constants.empty_tag))
        tag_file = self.__create_empty_note(tag_file)
        return tag_file

    def __create_empty_note(self,tag_file):
        # add empty note to note structure notes list 
        tag_file[constants.CONTENT]+=copy.deepcopy(constants.empty_notes_holder)
        return tag_file

    def __get_data_from_user(self):
        EDITOR = os.environ.get('EDITOR','vim') #that easy!

        initial_message = b"" # if you want to set up the file somehow

        with tempfile.NamedTemporaryFile(suffix=".tmp") as tf:
            tf.write(initial_message)
            tf.flush()
            call([EDITOR, tf.name])

            # do the parsing with `tf` using regular File operations.
            # for instance:
            tf.seek(0)
            edited_message = tf.read()
        return edited_message.decode("utf-8")

    def __add_data_to(self,tag_file,tag_name,note_name,data_to_add=None):
        if tag_file[constants.TAG] == tag_name:
            for notes in tag_file[constants.CONTENT]:
                if notes[constants.NAME]==note_name:
                    empty_note = json.loads(copy.deepcopy(constants.empty_note))
                    
                    data_created_time = datetime.datetime.now().strftime("%H_%M_%S_%m_%d_%Y")

                    if data_to_add is not None:
                        data = data_to_add
                    else:
                        data = self.__get_data_from_user()
                    
                    print(data)
                    if data == "":
                        break

                    empty_note[0][constants.DATA] = data
                    empty_note[0][constants.CREATED] = data_created_time                    
                    notes[constants.NOTES] += empty_note
                    break
            return tag_file
        else:
            return tag_file

    def __add_tag_to_master_list(self,tag):
        pass

    def create(self,data_to_add=None):
        # check of the note with tag name exists
        ms = master_list_tag()
        ms.add_tag(self._tag)
        if not self._if_json_exists:
            # add tag and note name 
            empty_file = self.__create_empty_json_note()
            empty_file[constants.TAG]=self._tag
            for name in empty_file[constants.CONTENT]:
                if name[constants.NAME] == '':
                    name[constants.NAME] = self._name
                    empty_file = self.__add_data_to(empty_file,self._tag,self._name,data_to_add)
                    break
            self.__save(empty_file)
        else:
            # add note to the available tag file
            tag_file = {}
            # print(f"{self._json_name} already present")
            # open file and json object
            with open(self._json_name,'r') as jsonfile:
                tag_file = json.load(jsonfile)
            # check if the note name already present
            for name in tag_file[constants.CONTENT]:
                if name[constants.NAME] == self._name:
                    # print(f"{self._tag}\{self._name} already present append data to the note array")
                    tag_file = self.__add_data_to(tag_file,self._tag,self._name,data_to_add)
                    self.__save(tag_file)
                    return

            # check if the note is not present add new
            tag_file = self.__create_empty_note(tag_file)
            if tag_file[constants.TAG] == self._tag:
                for name in tag_file[constants.CONTENT]:
                    if name[constants.NAME]== '':
                        name[constants.NAME] = self._name
                        tag_file = self.__add_data_to(tag_file,self._tag,self._name)
                        break
            print(f"before save {tag_file}")
            self.__save(tag_file)

        
    def __save(self,data_to_save):
        with open(self._json_name,'w') as jsonfile:
            json.dump(data_to_save, jsonfile, indent=4)

    def delete(self):
        pass

    def edit(self):
        pass

# if __name__ == "__main__":
#     # jio = notes("java","test_one")
#     # jio.create()
#     letters = string.ascii_lowercase
#     data = ''.join(random.choice(letters) for i in range(10))
#     ms = master_list_tag()
#     ms.add_tag(data)
#     print(ms.get_list())