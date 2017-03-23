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

def URL_Datproc(data):##created to hnadle most common processing
    data = data.decode(ENCODER)
    data = data.strip('\n')
    data = data.split(',')
    return data

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

################
##ADMIN COMMANDS
################

def URL_request_Gen():#gens link
     #reqd = URL_GetData(url = SERVER+'?f=gen')
     reqd = URL_GetData('?f=gen')
     reqd = URL_Datproc(reqd)
     if reqd[0] == 'F':
         return ['ERROR',reqd]#debugginf
     else:
         return reqd

def URL_closesession(gpin,apin):
    jstr = '?f=close&gid='+gpin+'&pin='+apin
    reqd = URL_GetData(jstr)
    reqd = URL_Datproc(reqd)
    if reqd[0] == 'F':
        return ['ERROR',reqd]#debugginf
    else:
        return reqd

def URL_startsession(gpin,apin):
    jstr = '?f=start&gid='+gpin+'&pin='+apin
    reqd = URL_GetData(jstr)
    reqd = URL_Datproc(reqd)
    if reqd[0] == 'F':
        return ['ERROR',reqd]#debugginf
    else:
        return reqd

def URL_newround(gpin,ppin):
    jstr = '?f=nrnd&gid='+gpin+'&pid='+ppin
    reqd = URL_GetData(jstr)
    reqd = URL_Datproc(reqd)
    if reqd[0] == 'F':
        return ['ERROR',reqd]#debugginf
    else:
        return reqd




#################
##PLAYER COMMANDS
#################

def URL_request_State(gpin):#state request of game
    #return URL_GetData(url = SERVER+'?f=state')
    #return URL_GetData('?f=state&gid='+gpin)
    jstr = '?f=state&gid='+gpin
    reqd = URL_GetData(jstr)
    reqd = URL_Datproc(reqd)
    if reqd[0] == 'F':
        return ['ERROR',reqd]#debugginf
    else:
        return reqd

def URL_join_session(gpin,name):#join game
    jstr = '?f=join&gid='+gpin+'&pname='+name
    reqd = URL_GetData(jstr)
    reqd = URL_Datproc(reqd)
    if reqd[0] == 'F':
        return ['ERROR',reqd]#debugginf
    else:
        return reqd


def URL_sublink(gpin,ppin,lnk):#submit a link
    jstr = '?f=link&gid='+gpin+'&pid='+ppin+'&pl='+lnk
    reqd = URL_GetData(jstr)
    reqd = URL_Datproc(reqd)
    if reqd[0] == 'F':
        return ['ERROR',reqd]#debugginf
    else:
        return reqd

def URL_votelink(gpin,ppin,voteno):
    jstr = '?f=vote&gid='+gpin+'&pid='+ppin+'&v='+voteno
    reqd = URL_GetData(jstr)
    reqd = URL_Datproc(reqd)
    if reqd[0] == 'F':
        return ['ERROR',reqd]#debugginf
    else:
        return reqd

def URL_getwinning(gpin):
    jstr = '?f=winn&gid='+gpin
    reqd = URL_GetData(jstr)
    reqd = URL_Datproc(reqd)
    if reqd[0] == 'F':
        return ['ERROR',reqd]#debugginf
    else:
        return reqd




#################
##OTHER
#################

def URL_leavegame(gpin,ppin):
    jstr = '?f=leav&gid='+gpin+'&pid='+ppin
    reqd = URL_GetData(jstr)
    reqd = URL_Datproc(reqd)
    if reqd[0] == 'F':
        return ['ERROR',reqd]#debugginf
    else:
        return reqd

def URL_listallwin():
    jstr = '?f=list&l=win'
    reqd = URL_GetData(jstr)
    reqd = URL_Datproc(reqd)
    if reqd[0] == 'F':
        return ['ERROR',reqd]#debugginf
    else:
        return reqd
    
def URL_getlinks(gpin):##test
    jstr = '?f=list&gid='+gpin+'&l=glinks'
    reqd = URL_GetData(jstr)
    reqd = URL_Datproc(reqd)
    if reqd[0] == 'F':
        return ['ERROR',reqd]#debugginf
    else:
        return reqd

def URL_getplayers(gpin):#,apin):
    #return['player1','player2','player3','player4','player5','player6']
    jstr = '?f=list&l=gplayers&gid='+gpin
    reqd = URL_GetData(jstr)
    #reqd = URL_Datproc(reqd)
    reqd = reqd.decode(ENCODER)
    reqd = reqd.strip('\n')
    #reqd = reqd.stri
    ##reqd = reqd[1]
    ##reqd = reqd[2:]
    if reqd[0] == 'F':
        return ['ERROR',reqd]#debugginf
    else:
        print('td:',reqd)
        return reqd[2:]


def URL_nolinks(gpin):
    jstr = '?f=list&l=nlinks&gid=?'+gpin
    reqd = URL_GetData(jstr)
    reqd = URL_Datproc(reqd)
    if reqd[0] == 'F':
        return ['ERROR',reqd]#debugginf
    else:
        return reqd
    
def URL_plist(gpin):
    jstr = '?f=list&l=nplayers&gid='+gpin
    reqd = URL_GetData(jstr)
    reqd = URL_Datproc(reqd)
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


