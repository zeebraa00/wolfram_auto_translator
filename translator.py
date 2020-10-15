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
    print("*"*40);print()
    print("=> Input 0 to exit")
    print("=> Note : your source files must be located at same directory with translator.py")
    print();print("*"*40)
    while (True) :
        source_name = input("\ninput the name of source file including .srt to translate : ")
        if (source_name=="0") :
            break
        try :
            source = open(source_name, "r")
        except :
            print("no such file")
            continue
        target = open("result_"+source_name, "w")
        content = source.read().split("\n")

        start = check_index(content)[0]+1
        end = len(content)
        interval = check_index(content)[1]-check_index(content)[0]

        for i in range(end) :
            if (i % interval == start) :
                try :
                    sentence=translator.translate(content[i], dest='ko').text
                    spell_checked=spell_checker.check(translator.translate(content[i], dest='ko').text).checked
                    target.write(content[i]+"\n")
                    target.write(spell_checked+"\n")
                    print("Translation completed on line",content[i-2])
                except :
                    print("error occured at :", content[i-2])
            else :
                target.write(content[i]+"\n")
            
if __name__ == "__main__":
    main()