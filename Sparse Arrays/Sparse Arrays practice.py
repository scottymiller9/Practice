N=int(input())
strings=[]
for i in range(0,N):
    strings.append(input())
Q=int(input())
queries={}
for a in range(0,Q):
    queries[input()]=0
print(queries)
for b in strings:
    if b in queries:
        queries[b]+=1
queries=map(str,queries.values())
print('\n'.join(queries))