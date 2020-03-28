file=open("garb.py","r",encoding="UTF-8")
info=file.readlines()
file.close()
print("-->>READ FILE: DONE")
update=", 'TRYNDEC HAPPENS! YOU HAVE BEEN VZLOMAN'"
final=[]
for i in info:
 if "print" not in i:
  final.append(i)
 else:
  line=""
  for j in i:
   if j!=")":
    line +=j
   else:
    line+=update + ")"
  final.append(line)
print("-->> INFO MODIFIED")
file=open("garb.py", "w", encoding="UTF-8")
for i in final:
 file.write(i)
file.close()