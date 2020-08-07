from collections import Counter
# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    a=Counter(magazine)
    b=Counter(note)
    if((b-a)=={}):
        print('Yes')
    else:
        print('No')
    
