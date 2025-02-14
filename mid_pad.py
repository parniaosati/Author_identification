import re
import numpy as np
import pandas as pd



def mid_padding(text , max_len , words_dict):

    text_words_len = len(text.split())
    input_text_len = len(text)
    print(text_words_len)
    if text_words_len > max_len :
        
        first_half = " ".join(text.split()[:int(max_len/2)])
        a = re.finditer("\." , first_half)
        z=0
        for i in a:
            z = i.span()[1]
        first_half=first_half[:z]

        second_half = " ".join(text.split()[-int(max_len/2):])
        a = re.finditer("\." , second_half)
        z=0
        for i in a:
            z = i.span()[1]
            break
        second_half = second_half[z:]

        join_text = " [...] ".join([first_half.strip() , second_half.strip()])

        li = []
        text_len = len(join_text.split())
        for i in join_text.split():
            if i == "[...]":
                li+=[0]*(max_len-text_len+1)
            else:
                li.append(words_dict[i])

        return join_text , li 
    
    else:
        is_assign = False
        dots = re.finditer("\." , text)
        for i in dots:
            o = i.span()[1]

            if o<int(input_text_len/2):
                break_point = o
                is_assign = True
            else:
                if is_assign:
                    break
                else:
                    break_point = o
                    break
                
        first_half = text[:break_point]
        second_half = text[break_point:]
        
        join_text = " [...] ".join([first_half.strip() , second_half.strip()])
        
        li = []
        text_len = len(join_text.split())
        for i in join_text.split():
            if i == "[...]":
                li+=[0]*(max_len-text_len+1)
            else:
                li.append(words_dict[i])
        
        return join_text , li