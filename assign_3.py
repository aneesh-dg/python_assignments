numbers=[12, 34, 56, 78, 90, 23, 45, 67, 89, 10, 90, 67, 56]
seen=set()
res=[]
for num in numbers:
    if num not in seen:
        res.append(num)
        seen.add(num)

print(res)
