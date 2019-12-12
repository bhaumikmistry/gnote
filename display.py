from jsonio import jsonio
from master_list_tag import master_list_tag
from constants import constants
import pathlib
import subprocess
import errno

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
        with tempfile.NamedTemporaryFile(mode='w+t') as temp_file:
            for tag in self.tag_list:
                temp_file.writelines(f't: {tag[:self.number_char-2]}..') if len(tag) > self.number_char else temp_file.writelines(f't: {tag.ljust(self.number_char)}\n')
            temp_file.seek(0)
            subprocess.call(['more',temp_file.name])
        

    def list_tag_note_name(self,args_t):
        with tempfile.NamedTemporaryFile(mode='w+t') as temp_file:
            if args_t is None:
                for tag in self.tag_list:
                    if not pathlib.Path(f'{tag}.json').exists():
                        temp_file.writelines(f'Error: Tag {tag} not found, may have been deleted\n')
                        continue
                    js = jsonio()
                    tag_file = js.read(f'{tag}.json')
                    for note in tag_file[constants.CONTENT]:
                        temp_file.writelines(f't: {tag[:self.number_char-2]}.. n {note[constants.NAME]}\n') if len(tag) > self.number_char else temp_file.writelines(f't: {tag.ljust(self.number_char)} n: {note[constants.NAME]}\n')
            else:
                tag = args_t
                if not pathlib.Path(f'{tag}.json').exists():
                    temp_file.writelines(f'Error: Tag {tag} not found\n')
                    return
                js = jsonio()
                tag_file = js.read(f'{tag}.json')
                for note in tag_file[constants.CONTENT]:
                    temp_file.writelines(f't: {tag[:self.number_char-2]}.. n {note[constants.NAME]}\n') if len(tag) > self.number_char else\
                        temp_file.writelines(f't: {tag.ljust(self.number_char)} n: {note[constants.NAME]}\n')
            temp_file.seek(0)
            subprocess.call(['less',temp_file.name])

    def list_tag_note_name_with_data(self):
        pass