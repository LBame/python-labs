#var 8, islamov,lab 8.2
with open('8.txt', 'r') as f:
    s = f.readline()
count, max = 0, 0
for i in range(1,len(s)-1):
    if (int(s[i])+int(s[i+1]))>10 and (int(s[i])+int(s[i-1]))>10 :
        count+=1
        if count > max:
            max=count
    else: count=0
print(f'Максимальная длина цепочки : {max}')