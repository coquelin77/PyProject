#import list_test1
from list_test1 import names
names = ['old_driver','rain','jack','shanshan','peiqi','black_girl',1,2,3,4,2,5,6,2]
first_index = names.index(2)
new_list = names[first_index+1:]
second_index = new_list.index(2)
second_val = names[first_index+second_index+1]
print(new_list,first_index,second_index)
print("second values", second_val)