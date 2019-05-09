class Solution:
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        deck.sort()
        s = deck.count(0)  # 0
        if len(deck) == 1:  # []
            return False
        elif sum(deck)/len(deck) == deck[0]:  # [1,1,1,1]情况
            return True
        print(deck)

        j = 0
        while True:
            if deck[j] != 0:
                x = deck.count(deck[j])
                break
            else:
                j += 1

        i = 1
        if x <= 1:
            return False
        else:
            while True:  # 寻常形式
                if deck[(i-1)*x] != 0 and deck[i*x] != 0:
                    ave1 = sum(deck[(i-1)*x:i*x])/float(deck[(i-1)*x])
                    ave2 = sum(deck[i*x:(i+1)*x])/float(deck[i*x])
                    if ave1 != ave2:
                        return False
                i += 1
                if i*x > len(deck)-1:
                    break
        if s != 0 and x != s:  # 把0加入判断
            return False
        else:
            return True
