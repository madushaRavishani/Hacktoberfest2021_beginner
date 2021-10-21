a1 = input()
a2 = input()
out1 = {x : a1.count(x) for x in set(a1)}  
out2 = {x : a2.count(x) for x in set(a2)} 

print(''.join(sorted(a1)))
print(''.join(sorted(a2)))    
print ("Occurrence of all characters in first input is :\n "+ str(out1)) 
print ("Occurrence of all characters in second input is :\n "+ str(out2)) 
