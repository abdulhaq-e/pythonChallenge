def sol1(f):
    
    import string

    text = open(f).read()
    shufd = [string.ascii_lowercase[x+2] for x in xrange(24)]
    shufd.append('a')
    shufd.append('b')

    nonshufd = [string.ascii_lowercase[x] for x in xrange(26)]
    
    newText = text
    for i in range(26):
        newText = string.replace(newText,nonshufd[i],shufd[i])
        print newText
    print shufd, nonshufd
    print newText


def sol2 (f):
    """"""

    import string
    text = open(f).read()
    
    shufd = [string.ascii_lowercase[x+2] for x in xrange(24)]
    shufd.append('a')
    shufd.append('b')
    shufd = string.join(shufd, '')
    nonshufd = [string.ascii_lowercase[x] for x in xrange(26)]
    nonshufd = string.join(nonshufd, '')

    trans_table = string.maketrans(nonshufd,shufd)
    newText = string.translate(text,trans_table)
    print newText


#Some general thoughts from different solutions.
'''
the first solution doesn't work, still don't know why!, after solving
this and looking at the other solutions posted on the wiki page, some were
written in stupid non-human languages but most were done using Python, afterall
it's called "Python Challenge" not "C++" or whatever. Improvements can be
made to the second solution, e.g.

string.ascii_lowercase[2:] + string.ascii_lowecase[:2] could have easily given a string
of the shuffled alphabet, no need for all this nonsense.

copied solution:'''

def sol3 (f):
    """"""

    import string
    text = open(f).read()

    trans_table = string.maketrans(string.ascii_lowercase, string.ascii_lowercase[2:] + 
                                   string.ascii_lowercase[:2])
    newText = string.translate(text,trans_table)
    print newText


'''
that was probably the best solution, another good one is brute forcing but there's no
fun in doing that, the funniest solution goes to this person, no debate, it's THE funniest:
%%%%%%%%%%%%%%%%%%
a = 'c'
b = 'd'
c = 'e'
d = 'f'
e = 'g'
f = 'h'
g = 'i'
h = 'j'
i = 'k'
j = 'l'
k = 'm'
l = 'n'
m = 'o'
n = 'p'
o = 'q'
p = 'r'
q = 's'
r = 't'
s = 'u'
t = 'v'
u = 'w'
v = 'x'
w = 'y'
x = 'z'
y = 'a'
z = 'b'
print g+ f+ m+ n+ c+ w+ m+ s+ b+ g+ b+ l+ r+ r+ p+ y+ l+ q+ j+ y+ r+ c+ g+ r+ z+ w+ f+ y+ l+ b+ r+ f+ y+ r+ q+ u+ f+ y+ r+ a+ m+ k+ n+ s +r+ c+ p+ q+ y+ p+ c+ d+ m+ p+ b+ m+ g+ l+ e+ g+ r+ g+ l+ z+ w+ f+ y+ l+ b+ g+ q+ g+ l+ c+ d+ d+ g+ a+ g+ c+ l+ r+ y+ l+ b+ r+ f+ y+ r+ q+ u+ f+ w+ r+ f+ g+ q+ r+ c+ v+ r+ g+ q+ q+ m+ j+ m+ l+ e+ s +q + g + l+ e+ q +r +p+ g+ l+ e+ k +y +i +c +r +p +y +l +q +g +q +p +c +a +m +k +k +c +l +b +c +b +l +m +u +y +n +n +j +w +m +l +r +f +c +s +p +j

>>> ihopeyoudidnttranslateitbyhandthatswhatcomputersarefordoingitinbyhandisinefficientandthatswhythistextissolongusingstringmaketransisrecommendednowapplyontheurl
'''
