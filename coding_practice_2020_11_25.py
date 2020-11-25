#codingbat 
#---------------

#Question: Hello Name

def hello_name(name):
    return "Hello " + name + '!'

#Question: make_out_word

def make_out_word(out, word):
    return out[0:2] + word + out[2:5]

#Question: first_half

def first_half(str):
    return str[0:len(str)/2]

#Question: without_end

def without_end(str):
    return str[1:len(str)-1]

#Question: combo_string

def combo_string(a, b):
    if (len(a) > len(b)):
        return b + a + b
    else:
        return a+b+a
    
#Question: non_start

def non_start(a, b):
    return a[1:len(a)]+b[1:len(b)]

#Question: left2

def left2(str):
    return str[2:len(str)]+str[0:2]

#Question: make_abba

def make_abba(a, b):
    return a+b+b+a

#Question: make_tags

def make_tags(tag, word):
    return '<' + tag + '>' + word + '<' + '/' + tag + '>' 

#Question: extra_end

def extra_end(str):
    temp = str[len(str)-2:len(str)]
    return temp+temp+temp

#Question: first_two

def first_two(str):
    return str[0:2]

#Python Workbook if_else
#------------------------
