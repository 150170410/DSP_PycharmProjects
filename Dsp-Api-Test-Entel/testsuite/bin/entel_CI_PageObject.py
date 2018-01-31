from testsuite.bin.entel_CI_Base import *
import ConfigParser
from subprocess import call
import time

config = ConfigParser.RawConfigParser()
filepath = '..\deployData.txt'
config.read(filepath)

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

HPSAcheck = '/etc/init.d/activator check'
HPSAstart = '/etc/init.d/activator start'
HPSAstop = '/etc/init.d/activator stop'
importSol = "/opt/OV/ServiceActivator/bin/deploymentmanager  ImportSolution -file /releases/Release_4.6/29012018/TDE/DSP_TDE.zip"
deleteSol = "/opt/OV/ServiceActivator/bin/deploymentmanager DeleteSolution -solutionName DSP_TDE"
deploySol = "/opt/OV/ServiceActivator/bin/deploymentmanager DeploySolution -solutionName DSP_TDE -deploymentFile  /opt/OV/ServiceActivator/solutions/DSP_TDE/deploy.xml -dbUser hpsa -dbPassword password"
undeploySol = "/opt/OV/ServiceActivator/bin/deploymentmanager  UndeploySolution -solutionName DSP_TDE -dbUser hpsa -dbPassword password -dbHost 15.213.50.68 -db ENTELDSP -dbPort 1521"
startMock = "/home/dspadmin/scripts/checkSaopProcess.sh"
hpsabinPath = '/opt/OV/ServiceActivator/bin/'
soldir='/opt/OV/ServiceActivator/solutions/'


class CIPageObject(BaseDeployment):

    def downloadSolution(self):
       self.startSSH(ftp_ip,ftp_uname, ftp_pwd)
       self.sftpGet_data(remoteFtp_dir,local_dir)
       self.closeSSH()

    def uploadSolution(self):
        self.startSSH(remote_ip,remote_uname,remote_pwd)
        self.sftpPut_data(local_dir,remoteSol_dir)
        self.closeSSH()

    def checkHPSA(self):
        print(self.sendCommand(HPSAcheck))
        return self.sendCommand(HPSAcheck)

    def startHPSA(self):
        status = self.checkHPSA()
        if (status.split(' ')[6] == 'not'):
            print('Starting HPSA$$$$$$$$$$$$$')
            self.sendCommand(HPSAstart)
            return True
        else: return False
    def stopHPSA(self):
        status = self.checkHPSA()
        if "running" in status.split(' ')[6]:
            print('Stopping HPSA$$$$$$$$$$$$$')
            print(self.sendCommand(HPSAstop))
            time.sleep(10)
            status = self.checkHPSA()
            if "running" in status.split(' ')[6]:
                print('Stopping HPSA$$$$$$$$$$$$$ Second Time')
                print(self.sendCommand(HPSAstop))
                time.sleep(10)
            return True
        elif "not" in status.split(' ')[6]:
            print('HPSA is not running , thus exiting**')
            return True
        else:return False

    def importSolution(self):
        print (self.sendCommand(importSol))
        time.sleep(5)
        try:
            stat= self.sftp.stat(soldir+'DSP_TDE') or self.sftp.stat(soldir+'DSP')
            print('Solution Imported and st_size = ',stat.st_size)
            print('True')
            return True

        except IOError,e:
            print(e)
            print('False')
            return False

    def deleteSolution(self):
        print(self.sendCommand(deleteSol))
        time.sleep(5)
        try:
            stat = self.sftp.stat(soldir + 'DSP_TDE') or self.sftp.stat(soldir + 'DSP')
            return False

        except IOError,e:
            print(e)
            return True

    def deploySolution(self):
            print(self.sendCommand(deploySol))
            time.sleep(5)
            return True

    def undeploySolution(self):
            print(self.sendCommand(undeploySol))
            time.sleep(5)
            return True

    def startMockservices(self):
        print(self.sendCommand(startMock))
        return True

# obj= CIPageObject()
# obj.startSSH(remote_ip,remote_uname,remote_pwd)
# obj.importSolution()