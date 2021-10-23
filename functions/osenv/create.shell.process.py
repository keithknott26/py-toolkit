from subprocess import Popen, PIPE
import subprocess as sp
import re
import socket

def run_proc(cmd, mode='default'):
    if mode == 'read':
        p = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE).stdout.read()
    if mode == 'readlines':
        p = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE).stdout.readlines()
    else:
        p = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)
    return p