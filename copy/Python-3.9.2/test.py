import subprocess

proc = subprocess.run(["mkdir","test"],stdout = subprocess.PIPE, stderr = subprocess.PIPE)
print(proc.stdout.decode("utf8"))
