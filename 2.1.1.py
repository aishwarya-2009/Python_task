n=input()
freq={}
count=0
for i in n:
    freq[i]=freq.get(i,0)+1
for i in n:
    if freq[i]==1:
       count+=1
print(count)
