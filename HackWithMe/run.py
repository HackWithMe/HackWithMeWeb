#!flask/bin/python

from app import Groups, theapp
theapp.run(debug=True)

from flask import *
from main import MakeGroups


def OnMakeGroups():
    app.Groups = MakeGroups(5)
    
    for i in range(len(app.Groups)):
        print "GROUP " + str(i) + ": "
        for interest in app.Groups[i]:
            print "    " + interest
            
        print


OnMakeGroups()

