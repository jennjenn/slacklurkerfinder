import json
from urllib2 import Request, urlopen, URLError
from pprint import pprint

var token = "<YOUR SLACK TOKEN>"

request = Request('https://slack.com/api/users.list?token=' + token)

try:
    response = urlopen(request)
    userdump = json.loads(response.read())

    userlist = []
    statuslist = []
    for member in userdump['members']:
        if member['deleted'] is False and member['name'] != "slackbot":
            userid = member['id']
            username = member['name']
            userlist.append({"id": userid, "name": username})



    for user in userlist:
        billablerequest = Request("https://slack.com/api/team.billableInfo?token=" + token + "&user=" + user['id'])
        billableresponse = urlopen(billablerequest)
        userstatus = json.loads(billableresponse.read())
        
        userid = user['id']
        username = user['name']

        userinfo = userstatus['billable_info'][userid]['billing_active']

    
        print "is %s active? %s" % (username, userinfo)


except URLError, e:
    print 'Rut roh', e
