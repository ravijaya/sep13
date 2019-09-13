import threading
import paramiko
from csv import reader

target_file = 'sshresponse.log'


def ssh_client(host, port, user, pwd, job):
    t_name = threading.current_thread().name
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, port, user, pwd)

    stdin, stdout, stderr = ssh.exec_command(job)
    output = stdout.read()

    payload = output if output else stderr.read()
    payload = payload.decode()

    caption = f'{t_name} ran {job} @ {host}'

    with open(target_file, 'a') as fw:
        fw.write(caption.center(80, '-') + '\n')
        fw.write(payload + '\n')


def main():
    for ssh_host in reader(open('hosts.csv')):
        ssh_host[1] = int(ssh_host[1])
        # print(ssh_host)

        t = threading.Thread(target=ssh_client, args=ssh_host)
        t.start()


if __name__ == '__main__':
    # op = ssh_client('localhost', 22, 'training', 'training', 'uname -a')
    # print(op)
    main()
