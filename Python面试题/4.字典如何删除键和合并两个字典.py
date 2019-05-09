dict={'name':'alex','age':18,'sex':'female'}
del dict['sex']
print(dict)#{'name': 'alex', 'age': 18}
dict1={'sex':'female'}
dict.update(dict1)
print('更新后的dic：',dict)#更新后的dic： {'name': 'alex', 'age': 18, 'sex': 'female'}