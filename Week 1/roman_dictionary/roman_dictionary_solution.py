"""
Roman Dictionary
----------------

Mark Antony keeps a list of the people he knows in several dictionaries
based on their relationship to him::

    friends = {'julius': '100 via apian', 'cleopatra': '000 pyramid parkway'}
    romans = dict(brutus='234 via tratorium', cassius='111 aqueduct lane')
    countrymen = dict([('plebius','786 via bunius'),
                       ('plebia', '786 via bunius')])


1. Print out the names for all of Antony's friends.
2. Now all of their addresses.
3. Now print them as "pairs".
4. Hmmm.  Something unfortunate befell Julius.  Remove him from the
   friends list.
5. Antony needs to mail everyone for his second-triumvirate party.  Make
   a single dictionary containing everyone.
6. Antony's stopping over in Egypt and wants to swing by Cleopatra's
   place while he is there. Get her address.
7. The barbarian hordes have invaded and destroyed all of Rome.
   Clear out everyone from the dictionary.
"""

friends = {'julius': '100 via apian', 'cleopatra': '000 pyramid parkway'}
romans = dict(brutus='234 via tratorium', cassius='111 aqueduct lane')
countrymen = dict([('plebius','786 via bunius'), ('plebia', '786 via bunius')])

print friends.keys()

print friends.values()

print friends.items()

del friends['julius']

#everyone = {}
#everyone.update(friends)
#everyone.update(romans)
#everyone.update(countrymen)
#[everyone.update(d) for d in (friends, romans, countrymen)]

everyone = dict(friends.items()+romans.items()+countrymen.items())

print everyone

print everyone['cleopatra']

everyone.clear()

