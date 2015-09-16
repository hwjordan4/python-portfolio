#!c:/python34/python.exe
#import sys
import os
import re
import sys
import cgitb
cgitb.enable()
 
print("Content-Type: text/html; charset=UTF-8")
print( )

print('''
<!DOCTYPE html>
<html>
    <head>
        <title>PrintEnv</title>
        <link rel="Stylesheet" type="text/css" href="/style1.css"/>
    </head>
    <body>
''')

print( "<h1>Hello!</h1>")

print("<table>")

keys = sorted(os.environ.keys())


for k in keys :
 print("<tr><td>{}</td><td>{}</td></tr>".format(k, os.environ[k]))
 
print("</table>")

print("<hr/>")

x = os.environ['QUERY_STRING']
print( "<h2>Query is </h2>", x)
if x:
    print("<table class='grid'>")
    comps = re.split('&', x)
    for c in comps:
        print("<tr>")
        print("<td>{}</td>".format(c))
        (key, val) = re.split('=', c)
        print( "<td>{}</td><td>{}</td>".format(key,val))
        print("</tr>")
    print("</table>")

print("<hr/>")

print("<table>")
print("<tr><td>{}</td><td>{}</td></tr>".format("sys.path", sys.path))
print("<tr><td>{}</td><td>{}</td></tr>".format("__file__", __file__))
print("<tr><td>{}</td><td>{}</td></tr>".format("__name__", __name__))
print("</table>")

print("<h2>Body is </h2>")
print(sys.stdin.read())