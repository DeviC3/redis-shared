# redis-shared

Application used for create and manage redis instances by Unix users.

## Installation

Use wget or curl to run script directly.
It is placing binary file directly under ```/usr/bin/``` directory and it should be ready to use.

```bash
wget -O - https://github.com/DeviC3/redis-shared/raw/main/install.sh | bash
```
```bash
curl -s https://github.com/DeviC3/redis-shared/raw/main/install.sh | bash
```

## Usage

### As root user:
Install mandatory files
```redis-shared --master install```

Copy config from default redis location (in case something wen wrong in /opt/redis location)
```redis-shared --master copyconfig```

Force to stop redis-server processes by Unix username
```redis-shared --master stop username```

Delete processes and files from user directory
```redis-shared --master delete username```

### As Unix user
Create mandatory files and start redis server based on unix socket
```redis-shared --server install```

Start redis-server service
```redis-shared --server start```

Stop redis-server service
```redis-shared --server stop```

Delete all files and running processes
```redis-shared --server flush```


> Note: Script already tested under Ubunt 20+ environment
> In next releases it will be tested under Red Hat and derivatives

## License

[GPLv3](https://github.com/DeviC3/redis-shared/blob/main/LICENSE)