#!/usr/bin/python
# coding=utf-8
# ###############
# some public function and parameters
# ###############
import subprocess
import os

# import time


# pubilc fun
def dir_verify(path_name):
    if not os.path.exists(path_name):
        os.makedirs(path_name, mode=0755)


def change_k8s(cluster_name):
    if cluster_name == "ecarx-testing-k8s":
        subprocess.check_call(
            'gcloud container clusters get-credentials ecarx-testing-k8s',
            shell=True)
    elif cluster_name == "ecarx-api-k8s":
        subprocess.check_call(
            'gcloud container clusters get-credentials ecarx-api-k8s',
            shell=True)
    else:
        print "Error: [K8s] Cluster name does not exist!"


# public parameters
project_name = "malaysia-project-201206"
project_zone = "asia-southeast1-a"
