filepath_save=''
filepath_load=''
f=open("%s" % (filepath_load+fileName_load+fileExe),'r')
while True:
    line=f.readline()
    if not line:break    
    print(line)
    if line=='EXCITATION,\n':
        nPathIdx='excitation/'
        fDivName=open("%s%05d%s"%(filepath_save+nPathIdx+fileName_save,nFileIdx,fileExe),'w')
    elif line=='ELASTIC,\n':
        nPathIdx='elastic/'
        fDivName=open("%s%05d%s"%(filepath_save+nPathIdx+fileName_save,nFileIdx,fileExe),'w')
    elif line=='ATTACHMENT,\n':
        nPathIdx='attachment/'
        fDivName=open("%s%05d%s"%(filepath_save+nPathIdx+fileName_save,nFileIdx,fileExe),'w')
    elif line=='IONIZATION,\n':
        nPathIdx='ionization/'
        fDivName=open("%s%05d%s"%(filepath_save+nPathIdx+fileName_save,nFileIdx,fileExe),'w')
    
    if line=='-----------------------------,\n': 
        a=0
        while True:
            line2=f.readline()
            if line2=='-----------------------------,\n'and a!=0:
                print("break")
                break
            a+=1
            print(a)
            fDivName.write(line2)
        fDivName.close()
        print("Closed file")
        nFileIdx+=1
f.close()
fDivName.close()