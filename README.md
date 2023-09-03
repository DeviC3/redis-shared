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

```redis-shared --master install```<br>
Install mandatory files

```redis-shared --master copyconfig```<br>
Copy config from default redis location (in case something wen wrong in /opt/redis location)

```redis-shared --master stop username```<br>
Force to stop redis-server processes by Unix username

```redis-shared --master delete username```<br>
Delete processes and files from user directory


### As Unix user

```redis-shared --server install```<br>
Create mandatory files and start redis server based on unix socket

```redis-shared --server start```<br>
Start redis-server service

```redis-shared --server stop```<br>
Stop redis-server service

```redis-shared --server flush```<br>
Delete all files and running processes


> Note: Script already tested under Ubunt 20+ environment
> In next releases it will be tested under Red Hat and derivatives

## License

[GPLv3](https://github.com/DeviC3/redis-shared/blob/main/LICENSE)