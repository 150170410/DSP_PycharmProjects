import os
import paramiko
import ConfigParser
from stat import S_ISDIR
#from testsuite.bin.entel_PageObject import *


#---Reading data from .proporties file
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

class pullSolution():

    def __init__(self):
        #-----FTP Connection Started------------
        self.ssh=None
        self.sftp=None
        # self.ssh=paramiko.SSHClient()
        # self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # #ssh.connect('15.213.54.219',username="root",password="hwroot")
        # self.ssh.connect(ftp_ip, username=ftp_uname, password=ftp_pwd)
        # self.sftp = self.ssh.open_sftp()
        # print('SFTP connection started for Solution Download************')

    def startSSH(self,ip,uname,pwd):
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        #ssh.connect('15.213.54.219',username="root",password="hwroot")
        self.ssh.connect(ip, username=uname, password=pwd)
        self.sftp = self.ssh.open_sftp()
        print('SFTP connection started for Solution Download************')

    def closeSSH(self):
        self.sftp.close()
        print('sftp connection closed#############3')
        self.ssh.close()
        print('ssh connection closed#############3')

    def sftpGet_data(self,remote_dir,local_dir):
        os.path.exists(local_dir) or os.makedirs(local_dir)

        for item in self.sftp.listdir_attr(remote_dir):
            remote_path = remote_dir + '/' + item.filename
            local_path = os.path.join(local_dir, item.filename)
            print item
            if S_ISDIR(item.st_mode):
                self.sftpGet_data(remote_path, local_path)
            else:
                self.sftp.get(remote_path, local_path)

        print'******Solution Downloading to Local Server Completed Successfully***********'

    def sftpPut_data(self,local_dir, remote_dir):
        try:
            self.sftp.chdir(remote_dir)
        except IOError:
            self.sftp.mkdir(remote_dir)

        for item in os.listdir(local_dir):
            print item
            local_path = os.path.join(local_dir, item)
            remote_path = remote_dir + '/' + item

            if os.path.isdir(local_path):
                self.sftpPut_data(local_path,remote_path)
            else:
                print(local_path)
                print remote_path
                self.sftp.put(local_path,remote_path)

        print'******Solution Upload to Test Server Completed Successfully***********'

    def sendCommand(self, command):

        # Check if connection is made previously
        if (self.ssh):
            stdin, stdout, stderr = self.ssh.exec_command(command)

            while not stdout.channel.exit_status_ready():
                # Print stdout data when available
                if stdout.channel.recv_ready():
                    # Retrieve the first 1024 bytes
                    alldata = stdout.channel.recv(1024)
                    while stdout.channel.recv_ready():
                        # Retrieve the next 1024 bytes
                        alldata += stdout.channel.recv(1024)

                    # Print as string with utf8 encoding
                    # print(str(alldata))
                    return str(alldata)
        else:
            print("Connection not opened.")
            return None

    def checkAppStatus(self):
        command='/etc/init.d/activator check'
        return self.sendCommand(command)


pull =pullSolution()
pull.startSSH(remote_ip,remote_uname,remote_pwd)
# pull.startSSH(ftp_ip,ftp_uname,ftp_pwd)
# pull.sftpGet_data(remoteFtp_dir,local_dir)
#pull.sftpPut_data(local_dir,remoteSol_dir)
#pull.checkAppStatus()
pull.closeSSH()
