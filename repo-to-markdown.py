#!/usr/bin/python

import xmltodict
import sys


with open(sys.argv[1]) as fd:
    doc = xmltodict.parse(fd.read())

    vmwareorg = doc['manifest']['remote']['@fetch']

    print(vmwareorg)
    for project in doc['manifest']['project']:
        project
        if project['@remote'] == 'vmwareorg' and '@name' in project:
            print('  - [%s](%s)' % (project['@name'], vmwareorg + '/' + project['@name']))

