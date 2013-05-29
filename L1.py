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
