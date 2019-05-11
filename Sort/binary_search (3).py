class BinarySearch():
	def binarySearch(self,key,nums):
		start=0
		end=len(nums)
		while start <= end:	
			mid = start + (end -start)//2
			if nums[mid] <key:
				start=mid+1
			elif nums[mid]>key:
				end = mid- 1
			else:
				print('its index is'+str(mid))
				return mid
		return False
if __name__ == '__main__':
	l=[1,2,3,5,6,7,9]
	hk=3
	a=BinarySearch()
	print(a.binarySearch(nums=l,key=hk))