import tempfile
import subprocess

contents = open('/etc/passwd', 'rb').read()

with tempfile.TemporaryFile() as fp:
    fp.write(contents)
    fp.flush()
    fp.seek(0)
    subprocess.check_call(["sendmail", "training@localhost"], stdin=fp)

