Python 3.10.7 (tags/v3.10.7:6cc6b13, Sep  5 2022, 14:08:36) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> pt_eng = {'Cachorro': 'dog', 'Agua': 'Water'}
>>> pt_eng
{'Cachorro': 'dog', 'Agua': 'Water'}
>>> pt_eng["Cachorro"]
'dog'
>>> pt_eng.get("Agua")
'Water'
>>> pt_eng.get("Aguaa")
>>> pt_eng["Cachorroa"]
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    pt_eng["Cachorroa"]
KeyError: 'Cachorroa'
>>> pt_eng['Cachorro'] = 'Puppy'
>>> pt_eng
{'Cachorro': 'Puppy', 'Agua': 'Water'}
>>> pt_eng['Cacharro'] = 'Puppy'
>>> pt_eng["Cachorro"]
'Puppy'
>>> pt_eng["Cacharro"]
'Puppy'
>>> pt_eng
{'Cachorro': 'Puppy', 'Agua': 'Water', 'Cacharro': 'Puppy'}
