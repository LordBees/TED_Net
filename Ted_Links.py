##generated links ##link getters
import os,random
import BeeLibv3 as Blib

vchars = [ '0', '1', '2', '3', '4', '5', '6', '7', '8', '9','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L','M','N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']




def get_tinyurl():   
    link = ''
    leng = random.randint(4,6)#4-6 chars
    for x in range(0,leng):
        link+=vchars[random.randint(0,len(vchars))]
    return 'http://tinyurl.com/'+link


def get_BitLy():
    link = ''
    leng = random.randint(4,6)#4-6 chars
    for x in range(0,leng):##can be longer as https://bit.ly/zzzzzzzzzzzzzzzzz is valid
        link+=vchars[random.randint(0,len(vchars))]
    return 'http://bit.ly/'+link


def get_googl():
    link = ''
    leng = 7##7 imgur has fixed 7charsrandom.randint(4,6)#4-6 chars
    for x in range(0,leng):
        link+=vchars[random.randint(0,len(vchars))]
    return 'http://goo.gl/'+link

##image sites
def get_imgur():
    link = ''
    leng = random.randint(4,7)#4-6 chars
    for x in range(0,leng):##can be longer as https://bit.ly/zzzzzzzzzzzzzzzzz is valid
        link+=vchars[random.randint(0,len(vchars))]
    return 'http://i.imgur.com/'+link##+'.jpg'##check format may need detecting from file

##custom
def get_custom():##youtube thing bndPy1MHm8E
    f = open('CUSTOM.CLF','r')
    dat = f.readline()
    f.close()
    data = Blib.csv2array(dat)##to solve type prob
    print('//##//\n',data,'\n\\##\\')
    #data = Blib.csv2array(dat)
    print(data[3])
    print(Blib.dot2csv(data[3]))
    data[3] = Blib.csv2array(Blib.dot2csv(data[3]))
    print('\n\n//##//\n',data,'\n\\##\\')
    enabled = data[4]
    if enabled  == 1 or '1':
        link = ''
        leng = random.randint(int(data[2]),int(data[1]))#chars
        for x in range(0,leng):##can be longer as https://bit.ly/zzzzzzzzzzzzzzzzz is valid
            link+=data[3][random.randint(0,len(vchars))]
        return data[0]+link##+'.jpg'##check format may need detecting from file