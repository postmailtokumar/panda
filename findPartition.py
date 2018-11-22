def k_subset(s, k):
    if k == len(s):
        return (tuple([(x,) for x in s]),)
    k_subs = []
    for i in range(len(s)):
        partials = k_subset(s[:i] + s[i + 1:], k)
        for partial in partials:
            for p in range(len(partial)):
                k_subs.append(partial[:p] + (partial[p] + (s[i],),) + partial[p + 1:])
    return k_subs

def uniq_subsets(s):
    u = set()
    for x in s:
        t = []
        for y in x:
            y = list(y)
            y.sort()
            t.append(tuple(y))
        t.sort()
        u.add(tuple(t))
    return u


#print(uniqueSets)  
def findPartitionSet(uniqueSets):
  for i in uniqueSets:
    if sum(i[0]) == sum(i[1]):
      print(sum(i[0]),sum(i[1]))
      return i
  return "No Partition Found!"

uniqueSets = uniq_subsets(k_subset([2,3,5], 2))
PartitionSet = findPartitionSet(uniqueSets) 
print(PartitionSet) 

  
