#!/bin/python3.6

a='Case-1023232'
b='Case-1023234'
c='Case-1023221'
d='Case-1023678'
e='Case-1023789'

ans_a = a.split('-')
ans_b = b.split('-')
ans_c = c.split('-')
ans_d = d.split('-')
ans_e = e.split('-')

f1=open('codes1.txt','w')
f1.write(ans_a[-1]+'\n')
f1.write(ans_b[-1]+'\n')
f1.write(ans_c[-1]+'\n')
f1.write(ans_d[-1]+'\n')
f1.write(ans_e[-1]+'\n')

f1=open('codes2.txt','w')
f1.write("Code-"+ans_a[-1]+'\n')
f1.write("Code-"+ans_b[-1]+'\n')
f1.write("Code-"+ans_c[-1]+'\n')
f1.write("Code-"+ans_d[-1]+'\n')
f1.write("Code-"+ans_e[-1]+'\n')


f1=open('codes3.txt','w')
f1.write(ans_a[0]+ans_a[-1]+'\n')
f1.write(ans_b[0]+ans_b[-1]+'\n')
f1.write(ans_c[0]+ans_c[-1]+'\n')
f1.write(ans_d[0]+ans_d[-1]+'\n')
f1.write(ans_e[0]+ans_e[-1]+'\n')




