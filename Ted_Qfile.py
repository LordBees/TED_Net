import os
## file objects##
class file_prog:
    filelist = os.listdir()##dont really need mainly for debug (line)
    data = []##line = one entry
    name =''
    linelen = 0
    def __init__(self):
        pass
        #self.linelen = len(self.data)
        #self.name = fname
        #self.executor()
        
    def readfile(self,fname):##internal method for filereading
        f = open(fname,'r')
        self.data = f.readlines()
        f.close()
        self.name = fname
        
    def writefile(self,fname):##internal method for filewriting
        f = open(fname,'w')
        f.write(array2csv(self.data))
        #self.data = f.readlines()
        f.close()
        #self.name = fname
    def update_fobj(self):##internal update class
        self.linelen = len(self.data)
        
    def readup(self,filename):
        if os.path.isfile(filename):
            self.readfile(filename)
            self.update_fobj()
        else:
            print('file: '+str(filename)+' not found!')
        
    def get_name(self):
        return self.name
    
    def get_linelen(self):
        return self.linelen
    
    def get_data(self):
        return self.data
    
    def get_dataline(self,lineno):
        '''first line is zero '''
        return self.data[lineno]
    ##temp here till beelib sorted out should'nt be here
    def csv2dot(self,strng):##replaces , with . char for  sub 'csvising them'
        temp = ''
        for x in range(len(strng)):
            if strng[x] == ',':
                temp += '.'
            else:
                temp += strng[x]
        return temp

    def dot2csv(self,strng):##replaces . with , char for  sub 'uncsvising them'
        temp = ''
        for x in range(len(strng)):
            if strng[x] == '.':
                temp += ','
            else:
                temp += strng[x]
        return temp
    
class configfile_prog (file_prog):##file obj for config file
    def __init__(self):
        self.readup('SETTINGS.CFF')##settings.configfilecustomlinkfile

class customfile_prog (file_prog):##file obj for custom link file
    def __init__(self):
        #if os.path.isfile('CUSTOM.CLF'):
        self.readup('CUSTOM.CLF')##custom.customlinkfile
    def save_customdata(self,dat):
        #self.data = array2csv(dat)
        self.data = dat##csv done in filewriting itself
        print(self.data)
        self.writefile('CUSTOM.CLF')
    def save_customdata2(self,dat):##improvement of the first iteration assumes raw input
        #self.data = array2csv(dat)
        self.data = dat##csv done in filewriting itself(will move at some point)
        self.data[3] = csv2dot(self.data[3])#dotting subcsv
        print(self.data)
        self.writefile('CUSTOM.CLF')
        
class customlinkfile_prog (file_prog):
    def __init__(self):
        self.readup('PRESET.dat')
    def save_customdata(self,dat):
        #self.data = array2csv(dat)
        self.data = dat##csv done in filewriting itself
        print(self.data)
        self.writefile('PRESET.dat')
    def save_customdata2(self,dat):##improvement of the first iteration assumes raw input
        #self.data = array2csv(dat)
        self.data = dat##csv done in filewriting itself(will move at some point)
        self.data[3] = csv2dot(self.data[3])#dotting subcsv
        print(self.data)
        self.writefile('PRESET.dat')
    
        
##class file_reader(file_prog):
##    def readfile(self,fname):
##        if fname == '-1':
##            pass
##        else:
##            f = open(fname,'r')
##            self.data = f.readlines()
##            f.close()
##    
##class conf_file(file_prog):
##    #def executor(self):