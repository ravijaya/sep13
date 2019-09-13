"""ssh client"""

import paramiko


# http://collabedit.com/ssfen

def sftp_upload(ssh, src_file, dest_file=None):
    ftp = ssh.open_sftp()

    if not dest_file:
        dest_file = src_file

    ftp.put(src_file, dest_file)  # use ftp method get to download
    ftp.close()


def get_ssh_connection(host, port, user, pwd):
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, port, user, pwd)
    return ssh


def task_runner(ssh_object, job):
    stdin, stdout, stderr = ssh_object.exec_command(job)
    output = stdout.read()

    if output:
        return output.decode()
    else:
        return stderr.read().decode()


def close_ssh_connection(ssh):
    ssh.close()


if __name__ == '__main__':
    ssh = get_ssh_connection('localhost', 22, 'training', 'training')
    sftp_upload(ssh, 'sysinfo.sh', 'systeminfo.sh')
    print(task_runner(ssh, 'stat systeminfo.sh'))
    print()
    print('-' * 60)
    print(task_runner(ssh, 'bash systeminfo.sh'))
    close_ssh_connection(ssh)
