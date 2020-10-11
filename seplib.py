def separar(path,number):
    file = open(path,'rb').read()

    for i in range(number):
        #newfile = file 
        #print(file[int(i*len(file)/number):int(((i+1)*len(file)/number))])
        newfile = file[int(i*len(file)/number):int(((i+1)*len(file)/number))]
        newPath = path+'P'+str(i)
        open(newPath,'wb').write(newfile)

def juntar(path):
    NewPath = path[:-2]
    i=0
    found  = 1
    newfile = ''
    while (found == 1):
        try:
            fileObj = open(NewPath+'P'+str(i),'rb')
            file = fileObj.read()
            fileObj.close()
            if newfile == '':
                newfile = file
            else:
                newfile = bytes(list(newfile) + list(file))

        except:
            found=0
            break
        
        i+=1

   # print(newfile)
    open(NewPath,'wb').write(bytes(newfile))
    
