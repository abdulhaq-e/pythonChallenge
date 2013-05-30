def sol1 (f):
    """"""
    import re
    
    text = open(f).read()
    search = re.findall('([a-zA-Z])', text)
    print ''.join(search)

def sol2 (f):
    import string

    text = open(f).read()
    indices = []
    for j in range(26):
        
        indices.append([i for i, x in enumerate(text) if x == string.ascii_lowercase[j]])
    indices = [x[0] for x in filter(None, indices)]
    
    solution = [text[j] for j in indices]
    print solution

#thoughts
'''
sol2 is not quite good because it gives a scrambled answer: aeilqtuy, difficult to spot it
as 'equality'
sol1 is the way to do it, regular expressions maybe a kill in small situations but they are
powerfull. we assumed that the special characters are members of the alphabetical group, this
assumption is not quite good, some of the solutions on the wiki do not rely on this.

this one is not very efficient ( O(n^2) ) but i liked count:
'''
def sol3 (f):
    import string
    text = open(f).read()
    
    for a in text:
        c = text.count(a)
        if c < 20:
            print a, ':', c
'''
this is probably the shortest slowest code, lprun gives 13.6968 seconds, massive, 99.2%
of the time is spen on....drums...COUNT!, it's not even foolproof, we just guessed that 
rare chars will appear less than 20 times!

another counting method but this seems better:
'''

def sol4 (f):
    """"""
    import string
    text = open(f).read()

    charlist = [chr(a) for a in range(256)] #all possible chars
    for x in text:
        c = text.count(x)
        if c < 20:
            print x, ':', c
'''
the above is slow as well, this is why regular expressions rock

in general though, this question is asking for a way to do it using counting
because it's not explicitly said that the rare charecters are alphabets so the usage
of regular expressions may not lead to correct results, I like this method best:

'''
def sol5 (f):
    """"""
    # when "rare" means less than average
    from collections import Counter
    text = open(f).read().replace('\n','')
    freq = Counter(text)
    avg_freq = sum(freq.values()) // len(freq)
    print ''.join([c for c in text if freq[c] < avg_freq ])


'''
the above is amazingle fast, it doesn't assume alphabets, and uses average frequency
'''
    
