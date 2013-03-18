def sol1(f):
    
    text = open(f).read()
    import string
    shufd = [string.ascii_lowercase[x+2] for x in xrange(24)]
    shufd.append('a')
    shufd.append('b')

    nonshufd = [string.ascii_lowercase[x] for x in xrange(26)]
    
    #for i in range(26):
    newText = [string.replace(text,nonshufd[i],shufd[i]) for i in range(26)]
    print shufd[0], nonshufd[0]
    #print newText
    
    
