from subprocess import Popen, PIPE

proc = Popen(["python", "psdemo.py"], stdin=PIPE)
out, err = proc.communicate(b'12' + b"\n")