#!/usr/bin/python
# coding=utf-8

from jinja2 import Environment, FileSystemLoader
import sys
import os
from tool import *
# from kubernetes import client, config
import yaml
import subprocess


class MakeConfig(object):
    def __init__(self, prj_name, prj_level):
        self.tmplate_dir = os.getcwd()
        self.config_dir = os.getcwd() + "/testing-config/"
        self.j2_tempalte = "java-regular-template.j2"
        self.prj_name = prj_name
        self.prj_level = prj_level
        self.config_file = self.config_dir + self.prj_name + '-' + self.prj_level + '.yaml'

    def ecarx_log(self):
        env = Environment(loader=FileSystemLoader(self.tmplate_dir, 'utf-8'))
        template = env.get_template(self.j2_tempalte)
        deployment = template.render(name=self.prj_name, level=self.prj_level)
        with open(self.config_file, 'w') as f:
            f.write(deployment)
        return self.config_file


class ApplyConfig(object):
    def __init__(self, prj_name):
        self.prj_name = prj_name

    def cluster_init(self):
        api_prj = ['configserver', 'primary-gateway']
        if self.prj_name in api_prj:
            change_k8s('ecarx-api-k8s')
        else:
            change_k8s('ecarx-testing-k8s')

    def deployment_create(self, api_instance, yaml_file):
        # config.load_kube_config()
        # k8s_beta = client.ExtensionsV1beta1Api()
        with open(yaml_file, 'r') as f:
            dep = yaml.load(f)
            api_response = api_instance.create_namespaced_deployment(
                body=dep, namespace="default")
            print("Deployment created. status='%s'" % str(api_response.status))

    def log_apply(self, yaml_file):
        yaml_l = []
        yaml_l.append(yaml_file)
        subprocess.check_call(['kubectl', 'apply', '-f'] + yaml_l)


def main():
    if len(sys.argv) != 3:
        print "Usage: python copy_k8s_dpm_yaml.py prj_name prj_level"
        sys.exit()
    else:
        pass
    prj_name = sys.argv[1]
    prj_level = sys.argv[2]
    mlog = MakeConfig(prj_name, prj_level)
    myaml = mlog.ecarx_log()

    # try:
    #     config.load_kube_config()
    #     k8s_beta = client.ExtensionsV1beta1Api()
    #     a_log = ApplyConfig(prj_name)
    #     a_log.cluster_init()
    #     a_log.log_apply(k8s_beta, myaml)
    # except Exception as e:
    #     raise e

    try:
        # config.load_kube_config()
        # k8s_beta = client.ExtensionsV1beta1Api()
        a_log = ApplyConfig(prj_name)
        a_log.cluster_init()
        print "==YAML: %s" % (myaml)
        a_log.log_apply(myaml)
    except Exception as e:
        print e


if __name__ == '__main__':
    main()
