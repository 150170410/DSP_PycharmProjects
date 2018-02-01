from testsuite.bin.entel_CI_Base import *
import ConfigParser
from subprocess import call
import time

config = ConfigParser.RawConfigParser()
filepath = '..\deployData.txt'
config.read(filepath)


class CIPageObject(BaseDeployment):
    ftp_ip = config.get('StaticData', 'ftp_ip')
    ftp_uname = config.get('StaticData', 'ftp_uname')
    ftp_pwd = config.get('StaticData', 'ftp_pwd')
    remoteFtp_dir = config.get('StaticData', 'remoteFtp_dir')

    local_dir = config.get('StaticData', 'local_dir')

    remote_ip = config.get('StaticData', 'remote_ip')
    remote_uname = config.get('StaticData', 'remote_uname')
    remote_pwd = config.get('StaticData', 'remote_pwd')
    remoteSol_dir = config.get('StaticData', 'remoteSol_dir')

    imp_sol_path = config.get('StaticData', 'imp_sol_path')

    HPSAcheck = config.get('StaticData', 'HPSAcheck')
    HPSAstart = config.get('StaticData', 'HPSAstart')
    HPSAstop = config.get('StaticData', 'HPSAstop')

    startMock = config.get('StaticData', 'startMock')
    hpsabinPath = config.get('StaticData', 'hpsabinPath')
    soldir = config.get('StaticData', 'soldir')
    importSol_tde = config.get('StaticData', 'importSol_tde')
    deleteSol_tde = config.get('StaticData', 'deleteSol_tde')
    deploySol_tde = config.get('StaticData', 'deploySol_tde')
    undeploySol_tde = config.get('StaticData', 'undeploySol_tde')

    importSol_leg = config.get('StaticData', 'importSol_leg')
    deleteSol_leg = config.get('StaticData', 'deleteSol_leg')
    deploySol_leg = config.get('StaticData', 'deploySol_leg')
    undeploySol_leg = config.get('StaticData', 'undeploySol_leg')

    tde_sol = config.get('StaticData', 'tde_sol')
    leg_sol = config.get('StaticData', 'leg_sol')

    def downloadSolution(self):
       self.startSSH(self.ftp_ip,self.ftp_uname, self.ftp_pwd)
       self.sftpGet_data(self.remoteFtp_dir,self.local_dir)
       self.closeSSH()

    def uploadSolution(self):
        self.startSSH(self.remote_ip,self.remote_uname,self.remote_pwd)
        self.sftpPut_data(self.local_dir,self.remoteSol_dir)
        self.closeSSH()

    def checkHPSA(self):
        print(self.sendCommand(self.HPSAcheck))
        return self.sendCommand(self.HPSAcheck)

    def startHPSA(self):
        status = self.checkHPSA()
        try:
            if (status.split(' ')[6] == 'not'):
                print('Starting HPSA$$$$$$$$$$$$$')
                self.sendCommand(self.HPSAstart)
                time.sleep(20)
                status = self.checkHPSA()
                if "running" in status.split(' ')[6]:
                    return True
            else: return False
        except AttributeError as e:
            print(e)
            return False
    def stopHPSA(self):
        status = self.checkHPSA()
        try:
            if "running" in status.split(' ')[6]:
                print('Stopping HPSA$$$$$$$$$$$$$')
                print(self.sendCommand(self.HPSAstop))
                time.sleep(10)
                status = self.checkHPSA()
                if "running" in status.split(' ')[6]:
                    print('Stopping HPSA$$$$$$$$$$$$$ Second Time')
                    print(self.sendCommand(self.HPSAstop))
                    time.sleep(10)
                return True
            elif "not" in status.split(' ')[6]:
                print('HPSA is not running , thus exiting**')
                return True
            else:return False
        except AttributeError as e:
            print(e)
            return False
    def importSolution(self,importSol,soln):
        print (self.sendCommand(importSol))
        time.sleep(5)
        try:
            stat= self.sftp.stat(self.soldir+soln)
            print('Solution Imported and st_size = ',stat.st_size)
            print('True')
            return True

        except IOError as e:
            print(e)
            print('False')
            return False

    def deleteSolution(self,deleteSol,soln):
        print(self.sendCommand(deleteSol))
        time.sleep(5)
        try:
            stat = self.sftp.stat(self.soldir + soln)
            print(deleteSol)
            print('True')
            return False

        except IOError as e:
            print(e)
            print('False')
            return True

    def deploySolution(self,deploySol):
            print(self.sendCommand(deploySol))
            time.sleep(5)
            return True

    def undeploySolution(self,undeploySol):
            print(self.sendCommand(undeploySol))
            time.sleep(5)
            return True

    def startMockservices(self):
        print(self.sendCommand(self.startMock))
        return True

