import sys
import requests
import json


def main():
   # print met, res, data, len(sys.argv)
   #
    if len(sys.argv) != 4:
        print '<<<<ERROR>>>>\n Usage is: method resource data \n Ex: thisscript.py POST contacts {\"name\":\"bob\""}'
        return

    #Define the vars
    met = sys.argv[1].upper()
    res = sys.argv[2].lower()
    data = str(sys.argv[3])
    head = {'content-type': 'application/json'}

    url = ""
    #print met, res, data

    if met == 'POST':
        furl = url+res
        resp = requests.post(furl, data=data, headers=head)
        print data
        print resp.text
        return 0

    if met == 'GET':
        furl = url+res
        resp = requests.get(furl, data=0)
        print resp.text
        return 0

    if met == 'PUT':
        furl = url+res
        resp = requests.put(furl, data=data, headers=head)
        print resp.text
        return 0

    if met == 'DELETE':
        furl = url+res
        resp = requests.delete(furl, data=data)
        print resp.text
        return 0

if __name__ == '__main__':
    main()
