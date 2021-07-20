import subprocess

proc = subprocess.run(["microk8s","kubectl","get","svc"],stdout = subprocess.PIPE, stderr = subprocess.PIPE)
print(proc.stdout.decode("utf8"))
