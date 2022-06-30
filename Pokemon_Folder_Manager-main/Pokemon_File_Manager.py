#Pokemon_file_rename

import imp
from lib2to3.pgen2.token import NAME, NUMBER
import os
import shutil
import glob
import re
from tokenize import Number

src_path = r"C:\Users\JASON LEE\Documents\1Python\Pokemon_Game\gen8 - Copy"


def rename_pokemon():
    list_of_pokemon = input("please insert list of pokemon here").split()
    print(list_of_pokemon)

    for i in range(int(len(list_of_pokemon)/2)):
        NUMBER = list_of_pokemon[2*i]
        if i == 0:
            NUMBER = list_of_pokemon[0]
        NAME = list_of_pokemon[(2*i)+1]
        if i == 0:
            NAME = list_of_pokemon[1]
        

        for image_filename in glob.iglob(src_path+r"/*.png"): 
            if re.search(f'{NUMBER}', image_filename):
                try:
                    os.rename(image_filename,src_path+"\\"+f"{NAME}"+".png")
                    print(image_filename)
                except:
                    os.rename(image_filename,image_filename.replace(f'{NUMBER}',f'{NAME}'))
dir_list= []


rename_pokemon(dir_list)
