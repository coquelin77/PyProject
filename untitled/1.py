class zhidao(object):
    def baidu(self,words):
        list(words)
        sdrow = []
        for i in words:
            sdrow.append(i)
        sdrow.reverse()
        p=()
        return ''.join(sdrow)

if __name__ == '__main__':
    w = '''Tobeornottobe,that'saquestion.-莎士比亚'''
    a=zhidao()
    show = a.baidu(w)
    print(show)