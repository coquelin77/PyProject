if __name__ == '__main__':
	a_list = [1, 2, 3, 4, 5]
	b_list = [1, 4, 5]
	ret_list = list(set(a_list).union(set(b_list)))
	print(ret_list)
