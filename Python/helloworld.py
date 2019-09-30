#/usr/bin/python3
from random import randint
try:
    # Fix UTF8 output issues on Windows console.
    # Does nothing if package is not installed
    from win_unicode_console import enable
    enable()
except ImportError:
    pass

f=open('helloworld.txt',encoding='utf-8')
hellos=[line for line in f]
hello=hellos[randint(0,77)]
hello=hello.split(' ')
print("Hello world in %s is %s"%(hello[0],''.join(hello[1:])))
