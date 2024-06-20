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


    # """ It does not work
    # """
    def copyFileInDirectory(self, defCwd,pathsIn,pathsOut):
        if defCwd==False: cwd=self.__cwd
        else:cwd=""
        for i in range(len(pathsIn)):
            self.__logger.log(cl=self,method=sys._getframe(),message="copy file {} in {}".format(pathsIn[i],pathsOut[i]))
            shutil.copyfile(cwd+pathsIn[i],cwd+pathsOut[i])


    def copyFilesFromDirectory(self,source_folder,destination_folder):
        for file_name in os.listdir(source_folder):
            # construct full file path
            source = source_folder + file_name
            destination = destination_folder + file_name
            # copy only files
            if os.path.isfile(source):
                shutil.copy(source, destination)
                self.__logger.log(cl=self,method=sys._getframe(),message="copy file {} from {} to {}".format(file_name,source_folder,destination_folder))


    """ It does not work
    """
    def copyDirectory(self,pathsIn,pathsOut,removeIfExist):
        for i in range(pathsIn):
            if removeIfExist:
                if os.path.exists(pathsOut[i])==True: os.remove(pathsIn[i])
            self.__logger.log(cl=self,method=sys._getframe(),message="copy file {} in {}".format(pathsIn[i],pathsOut[i]))
            shutil.move(pathsIn,pathsOut)