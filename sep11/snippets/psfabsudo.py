import logging
from getpass import getpass
from fabric import Connection, Config

# logging.basicConfig(level=logging.DEBUG)

sudo_pass = 'fearsome' # getpass("What's your sudo password?")
config = Config(overrides={'sudo': {'password': sudo_pass}})

c = Connection('ravi@localhost', config=config,
               connect_kwargs={"password": sudo_pass})

# op = c.sudo('su - training -c whoami', hide=True)
c.sudo('whoami')
c.run('cd /tmp')
c.run('pwd')
# op.stdin.write("cat /etc/passwd | tr 'a-z' 'A-Z'")
# op = c.run('whoami', hide=True)
# print(op.stdout)

