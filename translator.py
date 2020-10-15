# -*- coding: utf-8 -*-
# Auto translator for wolfram U localization project
# made by JaeHeon Jeong (SKKU)

from googletrans import Translator
from hanspell import spell_checker

translator = Translator()

def check_index(content) :
    count=0
    record=[]
    for i in range(10) :
        if (content[i].find("-->")!=-1) :
            count+=1
            record.append(i)
            if (count == 2) :
                return record       

def main() :
    print()
    print("Input 0 to exit")
    print("Note : your source files must be located at same directory with translator.py")
    print()
    while (True) :
        source_name = input("input the name of source file including .srt to translate : ")
        if (source_name==0) :
            break

        source = open(source_name, "r")
        target = open("result_"+source_name, "w")
        content = source.read().split("\n")

        start = check_index(content)[0]+1
        end = len(content)
        interval = check_index(content)[1]-check_index(content)[0]

        for i in range(end) :
            if (i % interval == start) :
                sentence=translator.translate(content[i], dest='ja').text
                spell_checked=spell_checker.check(translator.translate(content[i], dest='ko').text).checked
                target.write(content[i]+"\n")
                target.write(spell_checked+"\n")
            else :
                target.write(content[i]+"\n")
            
if __name__ == "__main__":
    main()