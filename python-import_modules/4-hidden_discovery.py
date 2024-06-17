#!/usr/bin/python3
import os
import imp

module_path = '/tmp/hidden_4.pyc'

module = imp.load_compiled('module', module_path)

for name in dir(module):
    if not name.startswith('__'):
        print(name)

if __name__ == '__main__':
    main()
