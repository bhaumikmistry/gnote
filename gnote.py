import argparse
import json
from notes import notes
from master_list_tag import master_list_tag
from jsonio import jsonio
import pathlib
from constants import constants

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
        # print(f'Note name {args.t}/{args.a}')
        if args.t is None:
            args.t = "general"
        jio = notes(args.t,args.a)
        jio.create(args.d)
        return
    if args.e != None:
        print(f'Editing note {args.e}')
        return
    if args.u:
        print(f'update notes')
        return
    if args.l or args.lnotes:
        mlt = master_list_tag()
        tags = mlt.get_list()

        if args.lnotes:
            if args.t is None:
                for tag in tags:
                    if not pathlib.Path(f'{tag}.json').exists():
                        print(f'Error: Tag {tag} not found, may have been deleted')
                        continue
                    js = jsonio()
                    tag_file = js.read(f'{tag}.json')
                    for note in tag_file[constants.CONTENT]:
                        print(f't: {tag[:8]}.. n {note[constants.NAME]}') if len(tag) > 10 else\
                            print(f't: {tag.ljust(10)} n: {note[constants.NAME]}')
            else:
                tag = args.t
                if not pathlib.Path(f'{tag}.json').exists():
                    print(f'Error: Tag {tag} not found')
                    return
                js = jsonio()
                tag_file = js.read(f'{tag}.json')
                for note in tag_file[constants.CONTENT]:
                    print(f't: {tag[:8]}.. n {note[constants.NAME]}') if len(tag) > 10 else\
                        print(f't: {tag.ljust(10)} n: {note[constants.NAME]}')
        else:
            for tag in tags:
                print(f't: {tag[:8]}..') if len(tag) > 10 else print(f't: {tag.ljust(10)}')
        return

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Create Notes and sync with git private repo")
    parser.add_argument('-a', metavar="add",required=False,help="use -a to add note")
    parser.add_argument('-t', default=None, metavar="add tag",required=False,help="use -t to add or update note")
    parser.add_argument('-d', default=None, metavar="pass on data",required=False,help="use -d to supply and add data from command line")
    parser.add_argument('-e', metavar="edit",required=False,help="use -e to edit note")
    parser.add_argument('-u', '-update', required=False,help="use -u to add update note", action='store_true')
    parser.add_argument('-l', '-list', required=False,help="use -l to list default tags", action='store_true')
    parser.add_argument('-lnotes', required=False,help="use -l to list notes", action='store_true')
    
    args = parser.parse_args()
    navigator(args)
