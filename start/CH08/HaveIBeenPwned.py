#!/usr/bin/env python3
# Script that checks passwords agains haveibeenpwned.com API
# https://haveibeenpwned.com/API/v3#PwnedPasswords
# By Melinda Henke

import hashlib
import requests
def SHA1(msg): 
    return hashlib.sha1(msg.encode()).hexdigest()
def text_password(prefix):
    url = "https://api.pwnedpasswords.com/range/"+ prefix
    payload={}
    headers={}
    response = requests.request ("GET", url, headers = headers, data=payload)
    # Save response to variable
    raw_text = response.text 
    #Split on CRLF
    raw_list = raw_text.split("\r\n")
    # Separate on :, save to dictionary
    raw_dict ={}
    for item in raw_list:
        split_result=item.split(":")
        raw_dict[split_result[0]]=split_result[1]
    # Return dictionary
    return raw_dict


#Ask user for password
password = input ("Password: ")

# Hash password
pass_hash =SHA1(password)
pass_hash=pass_hash.upper()

#Split password
hash_prefix =pass_hash [:5]
hash_suffix = pass_hash [5:]


#Call API
results=text_password(hash_prefix)

#Search results
if hash_suffix in results.keys():
    print(f"Password is bad, it has been found {results[hash_suffix]}times")
else:
    print ("Password is safe")