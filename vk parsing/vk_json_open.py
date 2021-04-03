# -*- coding: utf-8 -*-
import requests
import os, time, json

vk_id = "67267231" # skynet
#vk_id = "47376425" #цифровая копия
F = json.load(open(f"{vk_id}_wall.json","r"))
print (len(F))
for i in F:
    print (i)
