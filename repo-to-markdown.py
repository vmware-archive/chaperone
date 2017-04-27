#!/usr/bin/env python

from __future__ import print_function

import xmltodict
import sys
import urllib2



shorturls = []
markdown_longurls = []

for arg in sys.argv[1:]:
    with open(arg) as fd:
        doc = xmltodict.parse(fd.read())

        orgname = doc['manifest']['remote']['@name']
        orgurl = doc['manifest']['remote']['@fetch']

        if orgname == 'vmwareorg':
            orgname = 'vmware'

        #print(vmwareorg)
        for project in doc['manifest']['project']:
            if '@name' in project:
                if '/' in project['@name']:
                    shorturls.append('repo:%s' % (project['@name']))
                else:
                    shorturls.append('repo:%s/%s' % (orgname, project['@name']))


                # link repos, and add travis gif?
                # markdown_longurls.append(
                #     '  - [%s](%s) [![Build Status](https://travis-ci.org/%s/%s.svg?branch=master)](https://travis-ci.org/%s/%s) ' % (
                #     project['@name'], orgurl + '/' + project['@name'], orgname, project['@name'], orgname,
                #     project['@name']))

                markdown_longurls.append('  - [%s](%s)' % (project['@name'], orgurl + '/' + project['@name']))

print('  - [link to PRs](http://github.com/search?q=' + urllib2.quote('is:pr ' + " ".join(shorturls) ) +')')
print("---------------")
print('  - [link to Issues](http://github.com/search?q=' + urllib2.quote('is:issue ' + " ".join(shorturls) ) +')')
print("---------------")
print("\n".join(markdown_longurls))

