#!/usr/bin/env python3

'''
Functions can return function
Function can also take a function as an argument

Decorator is a function that takes a function as an argument,
and returns a wrapper function, which is nothing, but a decorated  version of 
the passed function.

Decorators are used to tap on extra functionality to a function.
They can be turned  on and off simply.

'''

def install_weblogic(some_function):
    def weblogic_wrapper():
        print('pre-req: Clean up 500MB on system')
        some_function()
        print('post install: Verify Functionality')
    return weblogic_wrapper

#Install Weblogic Can be Turned ON/OFF by commenting the next line
@install_weblogic
def install_java():
    print('Installing Java')

install_java()
