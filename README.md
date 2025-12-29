# proxychains-conf

Configure and run proxychains inline


socks4 127.0.0.1 1080
strict_chain
```
proxychains-conf curl https://example.com
```

http 127.0.0.1 8080
strict_chain
```
proxychains-conf -t http -p 8080 curl https://example.com
```

socks5 127.0.0.1 8080
dynamic_chain
```
proxychains-conf -t socks5 -p 8080 -c dynamic curl https://example.com
```

## Install
```
wget https://github.com/nathrema/proxychains-conf/refs/heads/main/install.sh | sh
```

## Uninstall
```
wget https://github.com/nathrema/proxychains-conf/refs/heads/main/uninstall.sh | sh

```

## Help
```
usage: proxychains-conf [-h] [-t {http,socks4,socks5}] [-p PORT] [-i IP] [-c {strict,dynamic,random}]
             [-nq | --no-quiet | --no-no-quiet]

Configure and run proxychains inline

positional arguments:
  command

options:
  -h, --help            show this help message and exit
  -t, --type {http,socks4,socks5}
  -p, --port PORT
  -i, --ip IP
  -c, --chain {strict,dynamic,random}
  -nq, --no-quiet
```
