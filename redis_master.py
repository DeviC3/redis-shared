#!/usr/bin/python

import os
import sys
import shutil
import pwd
from redis_user import kill_proc
from pathlib import Path

sys.dont_write_bytecode = True

redis_main_config = '/etc/redis/redis.conf'
redis_opt_config = '/opt/redis/redis.conf'
mandatory_master_dirs = ['/opt/redis']


def install_services():
    try:
        for dir in mandatory_master_dirs:
            if not os.path.exists(dir):
                print(f'Creating {dir} directory')
                os.makedirs(dir)
            else:
                print(f'Directory /opt/{dir} exists')
        
        if not os.path.exists(redis_opt_config):
            print('Copy config file from default redis localization and setting chmod')
            shutil.copy(redis_main_config, redis_opt_config)
            Path(redis_opt_config).chmod(0o755)
        else:
            print('redis.conf exists in opt')

    except Exception as e:
        print(e)


def check_is_root():
    try:
        if os.getuid() != 0:
            print('Permission denied')
            sys.exit(1)
        else:
            print('Passed')
    except Exception as e:
        print(e)


def copy_default_config():
    try:
        shutil.copy(redis_main_config, redis_opt_config)
        Path(redis_opt_config).chmod(0o755)
        print('Default config copied to opt directory')
    except Exception as e:
        print(e)


def delete_user_instance(username):
    try:
        user_path = pwd.getpwnam(username).pw_dir
        shutil.rmtree(f'{user_path}/redis')
        kill_proc('redis-server', username)
    except Exception as e:
        print(e)
