#!/usr/bin/python

import redis
import os
import shutil
import subprocess
import logging
import psutil
import sys
from pathlib import Path

sys.dont_write_bytecode = True

user_home = Path.home()
logging.basicConfig(filename=f'{user_home}/redis_error.log', format='%(asctime)s - %(message)s - %(levelname)s', level=logging.ERROR)

redis_config_path = '/opt/redis/redis.conf'
redis_config_run_path = f'{user_home}/redis/redis.conf'
mandatory_dirs = ['redis/run', 'redis/log']

change_bind_ip = 'bind 127.0.0.1\n'
change_port = 'port 0\n'
change_unix_socket = f'unixsocket {user_home}/redis/run/redis.sock\n'
change_socket_permissions = 'unixsocketperm 775\n'
change_daemonize = 'daemonize yes\n'
change_pidfile = f'pidfile {user_home}/redis/run/redis_6379.pid\n'
change_logfile = f'logfile {user_home}/redis/log/redis.log\n'
change_maxmem_policy = 'maxmemory-policy allkeys-lru\n'
change_dir = f"dir {user_home}/redis"


def kill_proc(pname, username):
    try:
        for process in psutil.process_iter(attrs=['pid', 'name', 'username']):
            if process.info['name'] == pname and process.info['username'] == username:
                process_result = psutil.Process(process.info['pid'])
                process_result.kill()
                print(f"Process {pname} - PID {process.info['pid']} handled by {username} terminated")
    except Exception as e:
        logging.error(e)
        print(e)


def create_mandatory_dirs():
    try:
        Path(f'{user_home}/redis_error.log').touch()
        for dir in mandatory_dirs:
            if not os.path.exists(f'{user_home}/{dir}'):
                os.makedirs(dir)
            else:
                print(f'Directory {user_home}/{dir} exists')

    except Exception as e:
        print(f'{e}')
        logging.error(e)


def create_process_from_file():
    try:
        shutil.copyfile(redis_config_path, redis_config_run_path, follow_symlinks=False)

        values_to_replace = {
            "bind 127.0.0.1": change_bind_ip,
            "port 6379": change_port,
            "# unixsocketperm": change_socket_permissions,
            "# unixsocket": change_unix_socket,
            "daemonize no": change_daemonize,
            "pidfile /var": change_pidfile,
            "logfile": change_logfile,
            "# maxmemory-policy": change_maxmem_policy,
            "dir /var": change_dir
        }

        with open(redis_config_run_path, 'r') as file:
            lines = file.readlines()

        with open(redis_config_run_path, 'w') as file:
            for line in lines:
                found_result = False
                for old_line, new_line in values_to_replace.items():
                    if old_line in line:
                        file.write(new_line)
                        found_result = True
                        break
                if not found_result:
                    file.write(line)

        subprocess.run(f'redis-server {redis_config_run_path}', shell=True, capture_output=True)

    except Exception as e:
        print(f'{e}')
        logging.error(e)


def check_is_running():
    try:
        unix_socket_addr = f'{user_home}/redis/run/redis.sock'
        r = redis.Redis(unix_socket_path=unix_socket_addr)

        if r.ping() == True:
            print(f'''
                Redis server running on address: {unix_socket_addr}
                Enter from cli: redis-cli -s {unix_socket_addr}
                ''')
        else:
            print(f'Something went wrong, check logs at {user_home}/redis/log/redis.log')
    except Exception as e:
        print(f'{e}')
        logging.error(e)


def start_service():
    try:        
        subprocess.run(f'redis-server {redis_config_run_path}', shell=True, capture_output=True)

    except Exception as e:
        print(f'{e}')
        logging.error(e)


def flush_files():
    try:
        shutil.rmtree(f'{user_home}/redis')
    except Exception as e:
        print(f'{e}')
        logging.error(e)