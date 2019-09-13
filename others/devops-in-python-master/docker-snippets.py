import docker
client = docker.from_env()

client.containers.run("ubuntu", "echo hello world")
'hello world\n'
You can run containers in the background:

>>> client.containers.run("bfirsh/reticulate-splines", detach=True)
<Container '45e6d2de7c54'>
You can manage containers:

>>> client.containers.list()
[<Container '45e6d2de7c54'>, <Container 'db18e4f20eaa'>, ...]

>>> container = client.containers.get('45e6d2de7c54')

>>> container.attrs['Config']['Image']
"bfirsh/reticulate-splines"

>>> container.logs()
"Reticulating spline 1...\n"

>>> container.stop()
You can stream logs:

>>> for line in container.logs(stream=True):
...   print line.strip()
Reticulating spline 2...
Reticulating spline 3...
...
You can manage images:

>>> client.images.pull('nginx')
<Image 'nginx'>

>>> client.images.list()
[<Image 'ubuntu'>, <Image 'nginx'>, ...]x
