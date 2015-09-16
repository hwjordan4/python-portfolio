'''
Created on Oct 16, 2013

Error page for the function_table script


@author: ben
'''

import jinja2


##   func(Object... args)

def page(*messages):
    loader = jinja2.FileSystemLoader('templates')
    env = jinja2.Environment(loader=loader)

    print( "Content-Type: text/html; charset=UTF-8")
    print( "")
    
    template = env.get_template('error.html')
    print(template.render(title='Error', messages=messages))