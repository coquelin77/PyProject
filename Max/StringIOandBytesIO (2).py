from io import StringIO
import io
f = io.StringIO()
f.write('this is a str')
f.write(' , ')
f.write('just a str')
print(f.getvalue())
fi=StringIO('hello\nhi\ngoodbye')
while 1:
    s=fi.readline()
    if s=='':
        break
    print(s.strip())
fil=io.BytesIO()
fil.write('chinese'.encode('gbk'))
print(fil)