from testsuite.bin.entel_CI_PageObject import *


class DeployTDESolution(CIPageObject):

    def deployTDESolution(self):
# Downloading Solutions From FTP Server***************
        if self.startSSH(self.ftp_ip,self.ftp_uname,self.ftp_pwd):
            if self.downloadSolution(self.solname_tde):
                self.closeSSH()
            else:print('Sorry Some Error Occured in downloadSolution')
        else:print('Sorry Some Error Occured in startSSH')

#Uploading Solutions to Remote Server And Do Deployment Operation***************
        if self.startSSH(self.remote_ip, self.remote_uname, self.remote_pwd):
            if self.uploadSolution(self.solname_tde):
                if self.stopHPSA():
                    if self.undeploySolution(self.undeploySol_tde):
                        if self.deleteSolution(self.deleteSol_tde,self.tde_sol):
                            if self.importSolution(self.importSol_tde,self.tde_sol):
                                if self.deploySolution(self.deploySol_tde):
                                    if self.startHPSA():
                                        print('Solution should be UP and Running SuccessFully')
                                    else:print('Sorry Some Error Occured in startHPSA')
                                else:print('Sorry Some Error Occured in deploySolution')
                            else:print('Sorry Some Error Occured in importSolution')
                        else:print('Sorry Some Error Occured in deleteSolution')
                    else:print('Sorry Some Error Occured in undeploySolution')
                else:print('Sorry Some Error Occured in stopHPSA')
            else:print('Sorry Some Error Occured in uploadSolution')
        else:print('Sorry Some Error Occured in startSSH')

        self.closeSSH()

    def deployLegacySolution(self):
# Downloading Solutions From FTP Server***************
        if self.startSSH(self.ftp_ip,self.ftp_uname,self.ftp_pwd):
            if self.downloadSolution(self.solname_leg):
                self.closeSSH()
            else:print('Sorry Some Error Occured in downloadSolution')
        else:print('Sorry Some Error Occured in startSSH')

#Uploading Solutions to Remote Server And Do Deployment Operation***************
        if self.startSSH(self.remote_ip, self.remote_uname, self.remote_pwd):
            if self.uploadSolution(self.solname_leg):
                if self.stopHPSA():
                    if self.undeploySolution(self.undeploySol_leg):
                        if self.deleteSolution(self.deleteSol_leg,self.leg_sol):
                            if self.importSolution(self.importSol_leg,self.leg_sol):
                                if self.deploySolution(self.deploySol_leg):
                                    if self.startHPSA():
                                        print('Solution should be UP and Running SuccessFully')
                                    else:print('Sorry Some Error Occured in startHPSA')
                                else:print('Sorry Some Error Occured in deploySolution')
                            else:print('Sorry Some Error Occured in importSolution')
                        else:print('Sorry Some Error Occured in deleteSolution')
                    else:print('Sorry Some Error Occured in undeploySolution')
                else:print('Sorry Some Error Occured in stopHPSA')
            else:print('Sorry Some Error Occured in uploadSolution')
        else:print('Sorry Some Error Occured in startSSH')

        self.closeSSH()
obj=DeployTDESolution()
#obj.deployTDESolution()
# obj.deployLegacySolution()

#obj.downloadSolution(obj.solname_leg)
#obj.uploadSolution(obj.solname_tde)

