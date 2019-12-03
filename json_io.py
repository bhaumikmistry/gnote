import json
import os

class constants:
    NOTES="notes"
    CONTENT="content"
    CREATED="created"
    EDITED="edited"
    REVISED="revised"
    DATA="data"
    NAME="name"
    TAG="tag"
    empty_tag = '{\
        "tag":"",\
        "content":[]\
        }'
            
    empty_notes_holder = [{\
        "name":"",\
        "notes":[]\
        }]

    empty_note = [{\
        "created":"some_date",\
        "edited":"last_date",\
        "revised":"last_revised",\
        "data":""\
        }]
    
class json_io:
    
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
        tag_file = json.loads(constants.empty_tag)
        # add empty note to note structure notes list 
        tag_file[constants.CONTENT]+=constants.empty_notes_holder
        # add empty single note structure to notes list
        for notes in tag_file[constants.CONTENT]:
            notes[constants.NOTES]+=constants.empty_note
        return tag_file

    def create(self):
        # check of the note with tag name exists
        if not self._if_json_exists:
            # add tag and note name 
            empty_file = self.__create_empty_json_note()
            empty_file[constants.TAG]=self._tag
            for name in empty_file[constants.CONTENT]:
                if name[constants.NAME] == '':
                    name[constants.NAME] = self._name
            print(empty_file)
            self.__save(empty_file)
        else:
            print(f"{self._json_name} already present")
        
    def __save(self,data_to_save):
        with open(self._json_name,'w') as jsonfile:
            json.dump(data_to_save, jsonfile, indent=4)

    def delete(self):
        pass

    def edit(self):
        pass

if __name__ == "__main__":
    jio = json_io("cpp","test")
    jio.create()
