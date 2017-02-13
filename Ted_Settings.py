##used for storing inter class settings
settings = []

###mpgame
ppin = ''
gpin = ''
pname = ''
apin = ''
ADMIN = False##temp added
mp_prompt = True
InGame = False

#quick method for resetting state
def reset():
    global ppin
    global gpin
    global pname
    ppin = ''
    gpin = ''
    pname = ''
    apin = ''
    ADMIN = False