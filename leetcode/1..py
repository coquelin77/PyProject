class summer():
    def s(self,nums,target):
        dict = {}
        sums=[]

        for i in range(0, len(nums)):
            a = target-nums[i]
            if a in dict:

                sums.append(dict[a])
                sums.append(i)
                return sums
            else:
                dict[nums[i]]=i

if __name__ == '__main__':
    target = 9
    nums = [2,7,11,15]
    x= summer()
    p=x.s(nums,target)
    print(p)