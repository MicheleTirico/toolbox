import os
import sys
import shutil

class HandleFiles:
    def __init__(self,logger):
        self.__logger =logger
        self.__cwd=os.getcwd()+"/"

    def getDefCwd(self):   return self.__cwd
    def setLogger(self,logger): self.__logger=logger

    def deleteDirectories(self,paths):
        for path in paths :
            if os.path.exists(path):
                self.__logger.log(cl=self,method=sys._getframe(),message="delete directory: " +path)
                os.system("rm -r "+path)

    def createDirectories(self,paths):
        for path in paths :
            if os.path.exists(path)==False:
                try:self.__logger.log(cl=self,method=sys._getframe(),message="create directory in: "+path)
                except AttributeError: pass

                try: os.mkdir(self.__cwd+path)
                except FileExistsError: self.__logger.warning(cl=self,method=sys._getframe(),message="directory: {} exist".format(path),doQuit=False)

    def copyFileInDirectory(self, defCwd,pathsIn,pathsOut):
        if defCwd==False: cwd=self.__cwd
        else:cwd=""
        for i in range(pathsIn):
            self.__logger.log(cl=self,method=sys._getframe(),message="copy file {} in {}".format(pathsIn[i],pathsOut[i]))
            shutil.copyfile(cwd+pathsIn[i],cwd+pathsOut[i])

