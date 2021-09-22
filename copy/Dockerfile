FROM python:3.6

ARG project_dir=/projects/

ADD src/ $project_dir

COPY ./.kube/client.config /root/.kube/

#COPY /var/snap/microk8s/current/credentials/client.config /root/.kube/

WORKDIR $project_dir

RUN pip install -r requirements.txt

RUN curl -LO "https://storage.googleapis.com/kubernetes-release/release/$(curl -s https://storage.googleapis.com/kubernetes-release/release/stable.txt)/bin/linux/amd64/kubectl"

RUN chmod +x ./kubectl

RUN mv ./kubectl /usr/local/bin/kubectl

RUN kubectl version --client

WORKDIR ./app

COPY kubectl-cp1.py ./

RUN python3 kubectl-cp1.py
