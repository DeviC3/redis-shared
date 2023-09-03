#!/bin/bash

set -e

destination=/usr/bin/redis-shared
wget -O $destination https://raw.githubusercontent.com/DeviC3/redis-shared/main/redis-shared
chmod 755 $destination
echo "Redis-shared ready to use"
echo "Version of application: $(redis-shared -v)"

