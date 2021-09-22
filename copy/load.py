from kubernetes import client, config
import json

config.load_kube_config() #kubernetesのConfigファイルを読み込む
api = client.CustomObjectsApi()
#v1 = client.CoreV1Api()i
resource = api.list_namespaced_custom_object(group="metrics.k8s.io",version="v1", namespace="default", plural="pods")
#def load():
all_array = []

    #print(json.dumps(resource,ensure_ascii=False, indent=4, sort_keys=True, separators=(',', ': ')))
for pod in resource["items"]:
    s=pod["metadata"]["name"]
    all_array.append(s)
    print(s)

