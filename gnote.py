import argparse




def gnote(args):
    print(args)

    if args.a != None:
        print(f'Note name {args.d}/{args.a}')
    if args.e != None:
        print(f'Editing note {args.e}')
    if args.u:
        print(f'update notes')
    if args.t != None:
        print(f'Adding tag {args.t} for note {args.a}')
    if args.rt != None:
        print(f'Removing {args.t} tag of note {args.e}')
    if args.l:
        print(f'List all notes')

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Create Notes and sync with git private repo")
    parser.add_argument('-a', metavar="add",required=False,help="use -a to add note")
    parser.add_argument('-d', default="others", metavar="directory",required=False,help="use -d to add directory for note")
    parser.add_argument('-e', metavar="edit",required=False,help="use -e to edit note")
    parser.add_argument('-u', '-update', required=False,help="use -u to add update note", action='store_true')
    parser.add_argument('-t', metavar="add/update tag",required=False,help="use -t to add or update note")
    parser.add_argument('-rt', metavar="remore tag",required=False,help="use -rt to add or update note")
    parser.add_argument('-l', '-list', required=False,help="use -l to list notes", action='store_true')
    args = parser.parse_args()
    gnote(args)