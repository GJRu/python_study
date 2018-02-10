#!/usr/bin/python
#coding: utf-8
#from __future__ import division
#from __future__ import unicode_literals
try:
    import json
    print 'jason'
except ImporError:
    import simplejson as json
    print 'simplejson'
print json.dumps({'python':2.7})

print 10/3
print 10//3

s = 'unicode?'
print isinstance(s, unicode)  #s是否为unicode类型

