apilepsy
========

apilepsy is my shorthand api requester so I dont have to use curl all the time. It uses py's requests.

why?
========

because I use PHP all day and I forgot how to Python?

how?
========
just clone the script, make sure you ```pip install requests```, edit the API URL of the file on line 19, and give it a go like this:
```python
script.py METHOD RESOURCE BODY
```

where:
* METHOD is one of POST PUT GET DELETE
* RESOURCE is /whatever
* BODY is your JSON formated payload, if you use GET set body to 0 for lulz

credits
=========
Myself, really, if you want to add more functionalities you can do whatever you want with this code!
