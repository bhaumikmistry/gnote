



class display:
    def __init__(self):
        self.mlt = master_list_tag()
        self.tag_list = self.mlt.get_list()
        ''' 
        Number of char to print of a tag in 
        the print section to make the list 
        sync visually
        '''
        self.number_char = 10
        pass

    def list_tag(self):
        for tag in self.tag_list:
            print(f't: {tag[:self.number_char-2]}..') if len(tag) > self.number_char else print(f't: {tag.ljust(self.number_char)}')

    def list_tag_note_name(self,args_t):
        if args_t is None:
            for tag in self.tag_list:
                if not pathlib.Path(f'{tag}.json').exists():
                    print(f'Error: Tag {tag} not found, may have been deleted')
                    continue
                js = jsonio()
                tag_file = js.read(f'{tag}.json')
                for note in tag_file[constants.CONTENT]:
                    print(f't: {tag[:self.number_char-2]}.. n {note[constants.NAME]}') if len(tag) > self.number_char \ 
                    else print(f't: {tag.ljust(self.number_char)} n: {note[constants.NAME]}')
        else:
            tag = args_t
            if not pathlib.Path(f'{tag}.json').exists():
                print(f'Error: Tag {tag} not found')
                return
            js = jsonio()
            tag_file = js.read(f'{tag}.json')
            for note in tag_file[constants.CONTENT]:
                print(f't: {tag[:self.number_char-2]}.. n {note[constants.NAME]}') if len(tag) > self.number_char else\
                    print(f't: {tag.ljust(self.number_char)} n: {note[constants.NAME]}')

    def list_tag_note_name_with_data(self):
        pass