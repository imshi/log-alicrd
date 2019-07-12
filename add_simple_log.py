#!/usr/bin/python
# coding=utf-8

# import yaml
from jinja2 import Environment, FileSystemLoader
import sys
import os


class MakeLog(object):
    def __init__(self, prj_name, prj_level):
        self.tmplate_dir = os.getcwd()
        self.config_dir = os.getcwd() + "/testing-config/"
        self.j2_tempalte = "log-file-template.j2"
        self.prj_name = prj_name
        self.prj_level = prj_level

    def ecarx_log(self):
        configration_file = self.config_dir + self.prj_name + '-' + self.prj_level + '.yaml'
        env = Environment(loader=FileSystemLoader(self.tmplate_dir, 'utf-8'))
        template = env.get_template(self.j2_tempalte)
        deployment = template.render(name=self.prj_name, level=self.prj_level)
        with open(configration_file, 'w') as f:
            f.write(deployment)
        return configration_file


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print "Usage: python copy_k8s_dpm_yaml.py prj_name prj_level"
        sys.exit()
    else:
        pass
#    try:
#        prj_name = sys.argv[1]
#        prj_level = sys.argv[2]
#        app = MakeLog(prj_name, prj_level)
#        app.ecarx_log()
#    except Exception as e:
#        raise e
    prj_name = sys.argv[1]
    prj_level = sys.argv[2]
    app = MakeLog(prj_name, prj_level)
    app.ecarx_log()
