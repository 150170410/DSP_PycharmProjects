import os
import paramiko
from stat import S_ISDIR


class BaseDeployment():

    def __init__(self):
        self.ssh=None
        self.sftp=None

    def startSSH(self,ip,uname,pwd):
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        #ssh.connect('15.213.54.219',username="root",password="hwroot")
        self.ssh.connect(ip, username=uname, password=pwd)
        print('SSH Connection Started for %s************'%ip)
        self.sftp = self.ssh.open_sftp()
        print('SFTP Connection Opened************')
        if(self.ssh):
            return True
        else:return False

    def closeSSH(self):
        self.sftp.close()
        print('SFTP Connection Closed#############')
        self.ssh.close()
        print('SSH Connection Closed##############')

    def sftpGet_data(self,remote_dir,local_dir):
        os.path.exists(local_dir) or os.makedirs(local_dir)

        for item in self.sftp.listdir_attr(remote_dir):
            remote_path = remote_dir + '/' + item.filename
            local_path = os.path.join(local_dir, item.filename)
            print (item)
            if S_ISDIR(item.st_mode):
                self.sftpGet_data(remote_path, local_path)
            else:
                self.sftp.get(remote_path, local_path)

        print('******Solution Downloading to Local Server***********')

    def sftpPut_data(self,local_dir, remote_dir):
        try:
            self.sftp.chdir(remote_dir)
        except IOError:
            self.sftp.mkdir(remote_dir)

        for item in os.listdir(local_dir):
            print (item)
            local_path = os.path.join(local_dir, item)
            remote_path = remote_dir + '/' + item

            if os.path.isdir(local_path):
                self.sftpPut_data(local_path,remote_path)
            else:
                self.sftp.put(local_path,remote_path)

        print('******File Upload to Test Server in Progress ***********')

    def sendCommand(self, command):

        # Check if connection is made previously
        if (self.ssh):
            stdin, stdout, stderr = self.ssh.exec_command(command)
            return stdout.read()

            # while not stdout.channel.exit_status_ready():
            #     # Print stdout data when available
            #     if stdout.channel.recv_ready():
            #         # Retrieve the first 1024 bytes
            #         alldata = stdout.channel.recv(1024)
            #         while stdout.channel.recv_ready():
            #             # Retrieve the next 1024 bytes
            #             alldata += stdout.channel.recv(1024)
            #
            #         # Print as string with utf8 encoding
            #         # print(str(alldata))
            #         return str(alldata)
        else:
            print("Connection not opened.")
            return None

