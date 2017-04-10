#!/usr/bin/env python

from __future__ import print_function

import xmltodict
import sys



for arg in sys.argv[1:]:
    with open(arg) as fd:
        doc = xmltodict.parse(fd.read())

        orgname = doc['manifest']['remote']['@name']
        orgurl = doc['manifest']['remote']['@fetch']

        #print(vmwareorg)
        for project in doc['manifest']['project']:
            if '@name' in project:
                if '/' in project['@name']:
                    print('repo:%s' % (project['@name']), end=' ')
                else:
                    print('repo:%s/%s' % (orgname, project['@name']), end=' ')

                #print('  - [%s](%s)' % (project['@name'], orgurl + '/' + project['@name']))

