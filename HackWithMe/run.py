#!flask/bin/python

from app import *
from flask import *
theapp.run(debug=True)

from main import MakeGroups


def OnMakeGroups():
    print 'here'
    app.Groups = MakeGroups(5)
    
    

OnMakeGroups()
for i in range(len(app.Groups)):
    print "GROUP " + str(i) + ": "
    for interest in app.Groups[i]:
        print "    " + interest
        
    print