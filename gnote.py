import argparse
import json
from json_io import json_io

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
        jio = json_io(args.t,args.a)
        jio.create()
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
    parser.add_argument('-l', '-list', required=False,help="use -l to list default tags", action='store_true')
    parser.add_argument('-ltag', required=False,help="use -l to list tags", action='store_true')
    parser.add_argument('-lnotes', required=False,help="use -l to list notes", action='store_true')
    parser.add_argument('-lall', required=False,help="use -lall to list all notes with data", action='store_true')
    
    args = parser.parse_args()
    navigator(args)
