import docker
import logging
logging.basicConfig(level=logging.DEBUG)


client = docker.from_env()
print(client.containers.run('ubuntu', 'echo hello world'))
print()
print(client.containers.list())