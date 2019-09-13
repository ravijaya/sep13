import io
import tarfile
import docker

import docker
client = docker.from_env()

fpout = io.BytesIO()
tfout = tarfile.open(fileobj=fpout, mode="w|")

info = tarfile.TarInfo(name="Dockerfile")

dockerfile = io.BytesIO("FROM scratch\nCOPY hello /hello".encode("ascii"))
# print(dockerfile.read())
# exit(1)
tfout.addfile(tarinfo=info, fileobj=dockerfile)

hello = io.BytesIO("This is a file saying 'hello'".encode("ascii"))

info = tarfile.TarInfo(name="hello")
tfout.addfile(tarinfo=info, fileobj=hello)

#tfout.seek(0)
cli = docker.APIClient()
cli.build(fileobj=fpout, tag="hello")
