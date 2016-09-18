import re, subprocess
from two1.wallet import Wallet
from two1.bitrequests import BitTransferRequests


wallet = Wallet()
requests = BitTransferRequests(wallet)

srv = "http://10.244.174.124:4242/madlib"

print('''Choose a Category:
1 - Movies
2 - Games
3 - Books
4 - History
5 - Random\n''')
cat = int(input('Your choice: '))

if cat == 1: srv += "?category=movies"
if cat == 2: srv += "?category=games"
if cat == 3: srv += "?category=books"
if cat == 4: srv += "?category=history"

response = requests.get(url=srv)
story = response.text

l1 = re.findall('\(([^()]*)\)',story)
l2 = []
for i in l1:
 if i not in l2:
  l2.append(i)
for i in l2:
 substr = '({})'.format(i)
 word = input('{}: '.format(i))
 story = story.replace(substr,word)


print(story)
