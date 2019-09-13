from paramiko import SSHClient
import paramiko
from scp import SCPClient

ssh = SSHClient()
ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect('localhost', 22, 'training', 'training')
"""https://pastebin.com/6VwUQr67"""
# SCPCLient takes a paramiko transport as an argument
scp = SCPClient(ssh.get_transport())

scp.put('/etc/passwd', 'passwd')
scp.get('passwd')

# Uploading the 'test' directory with its content in the
# # '/home/user/dump' remote directory
# scp.put('test', recursive=True, remote_path='/home/user/dump')

scp.close()
