import subprocess
pod_name1= input("comparison pod name? ")
pod_name2= input("comparison pod name? ")
subprocess.run('microk8s kubectl cp '+pod_name1+':/app ./copy_test', shell=True)
subprocess.run('microk8s kubectl cp '+pod_name2+':/app ./copy_test', shell=True)
