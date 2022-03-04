# Complete the method/function so that it converts dash/underscore delimited words into camel casing.
#  The first word within the output should be capitalized only if the original word was capitalized
#  (known as Upper Camel Case, also often referred to as Pascal case).
# Should also be able to take in strings that contain both delimiters

# Examples
# "the-stealth-warrior" gets converted to "theStealthWarrior"
# "The_Stealth_Warrior" gets converted to "TheStealthWarrior"
# "The_Stealth-Warrior" gets converted to "TheStealthWarrior"

def to_camel_case(text):
    #your code here
    emptystring = ''
   
    if '-' in text:

        mod_text = (' ').join(text.split('-'))
        for i in mod_text:
            if i== '_':
                list = mod_text.split('_')
        newlistofstrings = ((' ').join(list)).split()

        if newlistofstrings[0][0].isupper() == True:
            new_lst = ((' ').join(newlistofstrings).title()).split(' ')
            for i in new_lst:
                emptystring+= i
        else:
            emptystring+= newlistofstrings[0]
            new_lst = ((' ').join(newlistofstrings[1:]).title()).split(' ')
            for i in new_lst:
                emptystring+= i
        
    elif '_' in text:
        new_text = (' ').join(text.split('_'))
        newlistofstrings = new_text.split(' ')
        if newlistofstrings[0][0].isupper() == True:
            new_lst = ((' ').join(newlistofstrings).title()).split(' ')
            for i in new_lst:
                emptystring+= i
        else:
            emptystring+= newlistofstrings[0]
            new_lst = ((' ').join(newlistofstrings[1:]).title()).split(' ')
            for i in new_lst:
                emptystring+= i
        
    elif '-' and '_' not in text:
        return text
    
    return emptystring
print(to_camel_case('And-it_was_such-that_it-was unknown',))
