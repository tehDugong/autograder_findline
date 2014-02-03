__author__ = 'vincent'
import traceback

f = open("file", 'w')

f.write("this is a test")

try:
    1/0
except Exception as e:
    s = traceback.format_exc(e)
    print(s)
    f.write(s)