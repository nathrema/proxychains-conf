#!/bin/python
import os,argparse,sys,subprocess,hashlib

def get_hash(input):
    m = hashlib.md5()
    m.update(input.encode())
    return m.hexdigest()

parser=argparse.ArgumentParser(prog='chain',description='Configure and run proxychains inline')
parser.add_argument('-t','--type',choices=['http','socks4','socks5'],default='socks4')
parser.add_argument('-p','--port',default='1080')
parser.add_argument('-i','--ip',default='127.0.0.1')
parser.add_argument('-c','--chain',default='strict',choices=['strict','dynamic','random'])
parser.add_argument('-nq','--no-quiet',action=argparse.BooleanOptionalAction,default=False)
parser.add_argument('command',nargs=argparse.REMAINDER)
args=parser.parse_args()

quiet='-q'
if args.no_quiet is True:
    quiet=''

if args.port is None or not args.port.isdigit() or int(args.port) < 0 or int(args.port) > 65535:
    print("invalid port")
    exit(0)

if args.command is None or len(args.command) == 0:
    print("command is required")
    exit(0)

conf=f'''{args.chain}_chain
proxy_dns
tcp_read_time_out 15000
tcp_connect_time_out 8000

[ProxyList]
{args.type} {args.ip} {args.port}
'''

hash_id=get_hash(f'{args.type}{args.port}{args.ip}{args.chain}')
conf_path=f'/tmp/proxychains-{hash_id}.conf'

f=open(conf_path,'w')
f.write(conf)
f.close()

if args.no_quiet is True:
    print(f'proxychains -f {conf_path}{quiet} {' '.join(args.command)}')

command=["proxychains", '-f', conf_path]
if args.no_quiet is not True:
    command.append('-q')
command += args.command
subprocess.run(command)

try:
    os.remove(conf_path)
finally:
    pass
