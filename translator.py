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
    source = open('source.srt', "r")
    content = source.read().split("\n")
    start = check_index(content)[0]+1
    end = len(content)
    interval = check_index(content)[1]-check_index(content)[0]

    for i in range(start, end, interval) :
        sentence=translator.translate(content[i], dest='ko').text
        spell_checked=spell_checker.check(translator.translate(content[i], dest='ko').text).checked

        print(sentence)
        print(spell_checked)
        print()
main()