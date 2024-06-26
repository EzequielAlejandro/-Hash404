#!/usr/bin/env python 
#_*_ coding: utf8 _*_

import hashlib

def main():
    hashpass = str(raw_input("HASH: "))
    passfile = open("dictionary.txt",'r')
    for p in passfile.readlines():
        n = p.strip("\n")
        n = hashlib.sha256(n).hexdigest()

        if n == hashpass:
            print("Password: {}            HASH: {}".format(p,n))
            break
if __name__ == '__main__':
    main()

