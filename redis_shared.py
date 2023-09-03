#!/usr/bin/python
import argparse
import os
import redis_user
import redis_master
import sys
from time import sleep

__version__ = '0.1.0'
sys.dont_write_bytecode = True

parser = argparse.ArgumentParser()

parser.add_argument('-v', action='store_true')
parser.add_argument('--server', choices=['start', 'stop', 'flush', 'install', 'version'])
parser.add_argument('--master', choices=['install', 'copyconfig', 'delete', 'stop', 'version'])
parser.add_argument('username', nargs='?')

args = parser.parse_args()
    
if args.v:
    print(__version__)
if args.server == 'install':
    redis_user.create_mandatory_dirs()
    redis_user.create_process_from_file()
    sleep(0.5)
    redis_user.check_is_running()

if args.server == 'start':
    redis_user.start_service()

if args.server == 'stop':
    redis_user.kill_proc('redis-server', os.getenv('USER'))

if args.server == 'flush':
    q = input('Are you sure? y/n: ')
    if q.lower() == 'y':
        redis_user.flush_files()
        redis_user.kill_proc('redis-server', os.getenv('USER'))
    elif q.lower() == 'n':
        print('Nothing happens')
    else:
        print('Type y or n (yes/no)')

if args.master == 'install':
    redis_master.check_is_root()
    redis_master.install_services()
if args.master == 'copyconfig':
    redis_master.check_is_root()
    redis_master.copy_default_config()
if args.master == 'stop':
    redis_master.check_is_root()
    if args.username:
        redis_user.kill_proc('redis-server', args.username)
if args.master == 'delete':
    redis_master.check_is_root()
    if args.username:
        redis_master.delete_user_instance(args.username)
