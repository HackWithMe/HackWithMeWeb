
from main import SetInterests, MakeGroups


peoplefile = open("DemoPeopleInterests.txt", 'r')
personfile = open("DemoPersonInterests.txt", 'r')
    
interests = []


s = peoplefile.read()
s = s.split(',')

for i in range(len(s)):
    if s[i].strip() == '': continue
    interests.append(s[i].lower())

s = personfile.read()
s = s.split(',')

for i in range(len(s)):
    if s[i].strip() == '': continue
    interests.append(s[i].lower())


peoplefile.close()
personfile.close()


n = input('Number of groups: ')
SetInterests(interests)
groups = MakeGroups(n)

print
for i in range(len(groups)):
        print "GROUP " + str(i) + ": "
        for interest in groups[i]:
            print "    " + interest
            
        print

