# redis-shared

Application used for create and manage redis instances by Unix users.

## Installation

curl/wget

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

## License

GPL