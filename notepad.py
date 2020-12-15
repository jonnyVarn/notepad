import os
from os import getcwd as getcwd
from os.path import isfile as isfile
from os.path import isdir as isdir
from StringsToList import StringsToList
from StringsToList import StringsToList
from msvcrt import getwch as getwch


class notepad():
    def __init__(self):
        self.os_version_str="none"
        pass

    def os_version(self):
        print(os.name)
        os_version_str=os.name
        self.os_version_str=os_version_str
        print(type(os_version_str))
        return os_version_str

    def write_note(self, os_version_str):
        note_name = input("input filename ")
        # the current working directory will be pwd
        pwd = getcwd()
        print("---------")
        print(pwd)
        print("--------")
        #if os_version==linux
        # new_name will be cwd+/+inputed note_name
        if os_version_str=="linux":
            new_name = pwd + "/" + note_name
        if os_version_str=="nt":
            new_name = pwd +"\\" + note_name +".txt"
            print(new_name)
        else:
            new_name = pwd + "/" + note_name
        # if path provided already is a file:
        if isfile(new_name):
            try:
                # open the file in read mode
                file = open(new_name, 'r+')
                # take input from keyboard and present the file content in input prompt
                note_input=sl.editor(file.read(),"nt")
                #note_input = input(file.read())
                # close the file
                file.close()
                # open the file in append mode
                file = open(new_name, 'w+')
                # write the input to the file
                file.write(note_input)
                # close the file again.
                file.close()

            except:
                print("no go append")

        if isfile(new_name) == False:
            try:
                file = open(new_name, 'w+')
                note_input = input("i ")
                file.write(note_input)
                file.close()
            except:
                print("shit pomesfrites")

sl=StringsToList()

note = notepad()
note.write_note(str(note.os_version()))
