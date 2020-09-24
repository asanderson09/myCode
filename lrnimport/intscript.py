#!/usr/bin/env python3

from subprocess import call # we only want to import the call and check_ouput functions

call(["ip", "link", "show", "up"]) #actually issue ip link show up

print("This program will check your interfaces.")

interface = input("Enter an interface, like, ens3: ")

call(["ip", "addr", "show", "dev", interface])

call(["ip", "route", "show", "dev", interface])

