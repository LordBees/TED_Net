##ted quick name gen
import random

prefixes = ['large','small','red','blue','green','orange','yellow','magenta','prickly']
suffixes = ['wizard','linker','space','cactus','lemon','walrus','keyboard','mouse','pear']

def genname():
    global prefixes,suffixes
    datx = [' ']*2
    datx[0] = prefixes[random.randint(0,len(prefixes)-1)].capitalize()
    datx[1] = suffixes[random.randint(0,len(suffixes)-1)].capitalize()+str(random.randint(0,999))
    return datx[0]+datx[1]