import imp
from lib2to3.pgen2.token import NAME, NUMBER
import os
import shutil
import glob
import re
from tokenize import Number

import re


src_path = r"C:\Users\JASON LEE\Documents\1Python\Pokemon_Game\gen8"

def delete_back_shinies_gigashiny(dir_list):
    regex = r'.+?sb.png|.+?b.png|.+?s.png'


    for x in range(len(dir_list)):
        for sprite in glob.iglob(dir_list[x]+r"/*.png"):
            if re.search(regex, sprite):
                print(sprite)
                os.remove(sprite)

def rename_pokemon(dir_list):
    list_of_pokemon = input("please insert list of pokemon here").split()
    print(list_of_pokemon)

    for i in range(int(len(list_of_pokemon)/2)):
        NUMBER = list_of_pokemon[2*i]
        if i == 0:
            NUMBER = list_of_pokemon[0]
        NAME = list_of_pokemon[(2*i)+1]
        if i == 0:
            NAME = list_of_pokemon[1]
            
        print(NUMBER+" "+NAME)

        for x in range(int(len(dir_list))):
            PATH=dir_list[x]
            PATH_FOR_REG = dir_list[x].replace("\\","\\\\")
            for image_filename in glob.iglob(fr'{PATH}'+fr"/{NUMBER}.png"):
                print(image_filename)
                os.rename(image_filename,fr'{PATH}'+"\\"+f"{NAME}"+".png")
            for image_filename in glob.iglob(fr'{PATH}'+fr"/*.png"):
                if re.search(f"{NUMBER}_",image_filename):
                    print("_")
                    os.rename(image_filename,image_filename.replace(f'{NUMBER}',f'{NAME}'))
#There are a lot of changes in the formatting of these names which makes using regex to search for them tedious. So are there any solutions to that? I was thinking making more if statements. As you see in the folders, there are pokemon with "m" and "f" or "type-" in the filename. I didn't account for those in this iteration.

dir_list= []


for dirpath, dirs, files in os.walk(r'C:\Users\JASON LEE\Documents\1Python\Pokemon_Game', topdown=False): #returns 3-tuple (dirpath, dirnames, filenames)
    print(dirpath)
    if re.search("gen",dirpath):
        dir_list.append(dirpath)

delete_back_shinies_gigashiny(dir_list)
rename_pokemon(dir_list)