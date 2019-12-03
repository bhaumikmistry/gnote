import argparse
import json

class gnote:

    def __init__(self):
        pass

    def create_note(self,name,list_of_tag):
        pass
    
    def edit_note(self,note_to_edit):
        pass

    def delete_note(self,note_to_delete):
        pass


def navigator(args):
    print(args)

    if args.a != None:
        print(f'Note name {args.t}/{args.a}')
    if args.e != None:
        print(f'Editing note {args.e}')
    if args.u:
        print(f'update notes')
    if args.l:
        print(f'List all notes')

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Create Notes and sync with git private repo")
    parser.add_argument('-a', metavar="add",required=False,help="use -a to add note")
    parser.add_argument('-t', default="others", metavar="add/update tag",required=False,help="use -t to add or update note")
    parser.add_argument('-e', metavar="edit",required=False,help="use -e to edit note")
    parser.add_argument('-u', '-update', required=False,help="use -u to add update note", action='store_true')
    parser.add_argument('-l', '-list', required=False,help="use -l to list notes", action='store_true')
    args = parser.parse_args()
    navigator(args)

    p = '{\
        "tag":"some_tag",\
        "notes":[\
            {\
                "name":"test_one",\
                "created":"some_date",\
                "edited":"last_date",\
                "data":[\
                    "some text",\
                    "some test seconde note same name and tag"\
                ]\
            },\
            {\
                "name":"test_two",\
                "created":"some_date",\
                "edited":"last_date",\
                "data":[\
                    "some text",\
                    "some test seconde note same name and tag"\
                ]\
            }\
        ]\
        }'

    
    p_dict = json.loads(p)
    print(p_dict)
    p_dict["notes"] += [{\
                "name":"test_one",\
                "created":"some_date",\
                "edited":"last_date",\
                "data":[\
                    "some text",\
                    "some test seconde note same name and tag"\
                ]\
            }]

    for note in p_dict["notes"]:
        print(note["name"])

    PATH_TO_JSON = 'data.json'
    
    with open(PATH_TO_JSON,'w') as jsonfile:
        json.dump(p_dict, jsonfile, indent=4)
