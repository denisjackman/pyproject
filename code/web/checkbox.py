#!/usr/bin/python
'''
    CGI handling
'''
# Import modules for CGI handling
import cgi

# Create instance of FieldStorage
form = cgi.FieldStorage()

# Get data from fields
if form.getvalue('maths'):
    MATH_FLAG = "ON"
else:
    MATH_FLAG = "OFF"

if form.getvalue('physics'):
    PHYSICS_FLAG = "ON"
else:
    PHYSICS_FLAG = "OFF"

print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title>Checkbox - Third CGI Program</title>")
print("</head>")
print("<body>")
print(f"<h2> CheckBox Maths is : {MATH_FLAG}</h2>")
print(f"<h2> CheckBox Physics is : {PHYSICS_FLAG}</h2>")
print("</body>")
print("</html>")
