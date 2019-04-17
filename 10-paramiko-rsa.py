#!/usr/bin/python3

## standard library imports
import os
import warnings

## 3rd party import
import paramiko

## excel data or csv data
excellist = [{"un": "bender", "ip": "10.10.2.3"}, {"un": "fry", "ip": "10.10.2.4"}, {"un": "zoidberg", "ip": "10.10.2.5"}]

## filter out any warnings the paramiko library creates
warnings.filterwarnings(action="ignore", module=".*paramiko.*")

## THINK! We created an empty PuTTY session
sshsession = paramiko.SSHClient()

## go grab an SSH key
mykey = paramiko.RSAKey.from_private_key_file("/home/student/.ssh/id_rsa")

## Skips the warning that says "THIS FINGERPRINT LOOKS NEW!" (authorized_hosts)
sshsession.set_missing_host_key_policy(paramiko.AutoAddPolicy())

for fc in excellist:
    ## cool window dressing
    print("\nConnecting to ...", fc['un'], "@", fc['ip'])
    
    ## press the CONNECT button in our Putty session
    sshsession.connect(hostname=fc['ip'], username=fc['un'], pkey=mykey)

    ## capture 3 responses from exec_command
    ssh_in, ssh_out, ssh_err = sshsession.exec_command ('ls /var/')

    ## display the results of our command
    print(ssh_out.read().decode('utf-8'))
    ## ssh is not a barn
    sshsession.close()




