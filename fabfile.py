import os
import re
import logging
import logging.config
import yaml

from fabric.api import cd, run, sudo
from fabric.api import settings, abort, env, prefix
from contextlib import contextmanager as _contextmanager


env.BASE = '/root/Desktop'
env.VIR_PATH = '/root/Desktop/django/takeout_env/bin/activate'
env.PRO_PATH = os.path.join(env.BASE, 'project')
env.VENDOR_PATH = os.path.join(env.BASE, 'vendor')
env.LOG = os.path.join(env.PRO_PATH, 'logs')

env.hosts = ['127.0.0.1']


##############################
# log
##############################
with open("config/yaml.conf", 'r') as stream:
    try:
        dict_conf = yaml.load(stream)
    except yaml.YAMLError, exc:
        print exc
logging.config.dictConfig(dict_conf)
pip_logger = logging.getLogger("pip_log")
yum_logger = logging.getLogger("yum_log")


def get_require_list():
    require_path = os.path.join(env.PRO_PATH, 'requirements.txt')
    require_file = open(require_path,"r")

    re_com = re.compile('(.*[^\n])')
    require_list = list()
    line = '--'
    while line != '':
        line = require_file.readline()
        if line != '':
            line = re_com.findall(line)
            require_list.append(line[0])

    require_file.close()
    return require_list

def yum_log(str):
    u'''
    log yum error
    '''
    yum_logger.info(str)


def pip_log(str):
    u'''
    log pip error
    '''
    pip_logger.info(str)


class FabricException(Exception):
    def __init__(self, result):
        self.result = result


u'''
    env-virtual
'''
@_contextmanager
def virtualenv():
    with prefix("source %s" %env.VIR_PATH):
        with cd(env.PRO_PATH):
            yield


@_contextmanager
def fabric_exception():
    with settings(abort_exception=FabricException):
        yield


def install_prerequisites():
    packages = [
        'python-devel',
        'mysql-devel',
        'readline-devel',
        'zlib-devel',
        'libjpeg-turbo-devel',
    ]

    with fabric_exception():
        for item in packages:
            try:
                run_command = "yum install -y %s" %item
                sudo(run_command)
            except FabricException, e:
                yum_log(run_command)


def install_pyp():
    with virtualenv():
        with fabric_exception():
            require_list = get_require_list()
            for item in require_list:
                try:
                    run_command = "pip install %s" %item
                    print '---------------============= %r' % run_command
                    sudo(run_command)
                except FabricException, e:
                    pip_log(run_command)

