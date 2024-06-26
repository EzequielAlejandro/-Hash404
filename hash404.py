#!/usr/bin/env python 
#_*_ coding: utf8 _*_

import hashlib

def main():
    password = str(raw_input("Palabra: "))
    print("\n")
    md5pass = hashlib.md5(password).hexdigest()
    print("MD5: " + md5pass)
    print("\n")
    sha1pass = hashlib.sha1(password).hexdigest()
    print("SHA1: " + sha1pass)
    print("\n")
    sha224pass = hashlib.sha224(password).hexdigest()
    print("SHA224: " + sha224pass)
    print("\n")
    sha256pass = hashlib.sha256(password).hexdigest()
    print("SHA256: " + sha256pass)
    print("\n")
    sha384pass = hashlib.sha384(password).hexdigest()
    print("SHA384: " + sha384pass)
    print("\n")
    sha512pass = hashlib.sha512(password).hexdigest()
    print("SHA512: " + sha512pass)
    print("\n")
if __name__ == '__main__':
    main()
