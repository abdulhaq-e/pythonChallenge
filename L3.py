def sol1 (f):
    """"""
    import re

    text = open(f).read()
    
    newText = re.findall('[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]',text)
    print ''.join(newText)
    

#some thoughts from other solutions
'''
the title of the level page hints at using re module, so that's probably the best solution,
in the wiki page, other solutions exist but they're mostly horrible, really horrible, some are
okay though, here's a good one:

'''

def sol2(f):

    text = open(f).read()
    cycle = 0
    checklist = range(9)
    for i in text:
        checklist = checklist[1:9] #very clever
        if i.islower():
            checklist.append(0)
        elif i.isupper():
            checklist.append(1)
        else:
            checklist.append(2)
        if checklist == [0, 1, 1, 1, 0, 1, 1, 1, 0]:
            print text[cycle - 4],
        cycle += 1

'''a great solution above'''
