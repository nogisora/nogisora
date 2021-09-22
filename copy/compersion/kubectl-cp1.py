import csv
import subprocess
pod_name1= "pdf-test"
pod_name2= "upload-test"
subprocess.run('microk8s kubectl cp '+pod_name1+':/app/List1.csv ./List1.csv', shell=True)
subprocess.run('microk8s kubectl cp '+pod_name2+':/app/List2.csv ./List2.csv', shell=True)

with open('List1.csv', 'r') as f1:
    reader1 = csv.reader(f1)
    d1 = dict(map(reversed, reader1))
    k1 = d1.keys()
with open('List2.csv', 'r') as f2:
    reader2 = csv.reader(f2)
    d2 = dict(map(reversed, reader2))
    k2 = d2.keys()


result = k1 - k2


result = map(lambda t: d1[t][2:], result)
#for a in result:
    #print(a)

#with open("hashlist.csv", 'w', newline="") as file:
    #spawriter = csv.writer(file)
    #spawriter.writerows(result)





for i in result:
  subprocess.run(f'microk8s kubectl cp {pod_name1}:/app/{i} {i}', shell=True)
  subprocess.run(f'microk8s kubectl cp {i} {pod_name2}:/app/{i}', shell=True)
