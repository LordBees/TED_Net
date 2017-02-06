##network stuff
import urllib.request
import urllib.parse
##
SERVER = 'http://playground.fireleafstudios.uk/elliot/ted/ted.php'
ENCODER = 'utf-8'

def URL_GetData(url,server = SERVER):##requester/getter
    with urllib.request.urlopen(server+url) as response:
        html = response.read()
    return html

#def URL_send_data(datx):
#    xurl = 'http://www.someserver.com/cgi-bin/register.cgi'
#    values = {'name' : 'Michael Foord',
#          'location' : 'Northampton',
#          'language' : 'Python' }

#    data = urllib.parse.urlencode(values)
#    data = data.encode('ascii') # data should be bytes
#    req = urllib.request.Request(url, data)
#    with urllib.request.urlopen(req) as response:
#        the_page = response.read()

def URL_request_Gen():#gens link
     #reqd = URL_GetData(url = SERVER+'?f=gen')
     reqd = URL_GetData('?f=gen')
     reqd = reqd.decode(ENCODER)
     reqd = reqd.split(',')
     if reqd[0] == 'F':
         return ['ERROR',reqd]#debugginf
     else:
         return reqd

def URL_request_State(gpin):#state request of game
    #return URL_GetData(url = SERVER+'?f=state')
    return URL_GetData('?f=state&gid='+gpin)

def URL_join_session(gpin,name):#join game
    jstr = '?f=join&gid='+gpin+'&pname='+name
    reqd = URL_GetData(jstr)
    reqd = reqd.decode(ENCODER)
    reqd = reqd.split(',')
    if reqd[0] == 'F':
        return ['ERROR',reqd]#debugginf
    else:
        return reqd


def URL_sublink(gpin,ppin,lnk):#submit a link
    jstr = '?f=link&gid='+gpin+'&pid='+ppin+'&pl='+lnk
    reqd = URL_GetData(jstr)
    reqd = reqd.decode(ENCODER)
    reqd = reqd.split(',')
    if reqd[0] == 'F':
        return ['ERROR',reqd]#debugginf
    else:
        return reqd

def get_state_desc(gs):#debug
    gst = [ 'Session is live and players can join',
            'Players can no longer join and need to submit a link',
            'All links have been submitted, players need to cast vote',
            'All votes recieved, players need to get winning link'
          ]
    return gst[gs]


