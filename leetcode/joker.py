class joke(object):
    def kidding(self,name1,name2):
        print("一天,美国总统候选人"+name2+"和"+name1+"走在街上突然饿了,\n但两个人都没有现金,无奈之下找到了一家面包店\n"+name2+"说,我有办法在不付钱的情况下得到面包,\n就在店员没有看到的地方偷了三块面包,并且装到了自己的兜里,\n"+name1+"很不满意,就对"+name2+"说:\n我们是要竞选总统的人,作为美国总统不应该去做一些小偷小摸的事儿。\n于是他就找到店员说:我是美国总统候选人"+name1+",\n我今天到这儿来就是为了给你变一个魔术,\n说完之后,向店员要了一块面包,并且吃了下去,\n接着又要了一块面包,还是吃了下去,\n然后又要了一块面包,而且也吃得下去,店员看了一头雾水,就问"+name1+": \n你要给我变的魔术在哪呢?\n"+name1+"说,其实那些面包刚才我并没有真的吃下去,\n我已经把他们变到了"+name2+"的口袋里")
        return 0
if __name__ == '__main__':
    a=joke()
    n1='特朗普'
    n2='希拉里'
    a.kidding(name1=n1,name2=n2)