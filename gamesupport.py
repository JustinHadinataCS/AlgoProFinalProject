from os import walk

def import_folder(path):
    
    for information in walk(path):
        print(information)

print('Hello')
import_folder('idle')