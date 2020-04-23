PATH='C:/Users/Sangwoo Kim/cr_data/'
Label_list=('attachment','elastic','excitation','ionization')
x_num=1024# interpol number
num_pair=x_num+1# +1= threshold energy
datanum=tot_num
num_group=np.zeros(4)
train_data=np.zeros((datanum,num_pair))
train_Label=np.zeros((datanum,1),dtype=str)
x_min=list()
x_max=list()
y_min=list()
y_max=list()
length_a=list()
def nor_interpol(PATH):
    a=0
    def min_exclude0(x):
        min=10000
        for i in x:
            if min>=i and i>0:
                min=i
        return min
    ind=0
    xvalues=list()
    for Label in Label_list:
        if Label=='attachment':
            Label2=0
        elif Label=='elastic':
            Label2=1
        elif Label=='excitation':
            Label2=2
        elif Label=='ionization':
            Label2=3
        dir_PATH_open=PATH+Label
        filenames=os.listdir(dir_PATH_open)
        num_group[a]=len(os.listdir(dir_PATH_open))
        for filename in filenames:
            full_filename=os.path.join(dir_PATH_open,filename)
            A1=np.loadtxt(full_filename,delimiter=',',dtype=np.float32)
            length=len(A1[:,1])
            length_a.append(length)
            max_ind=np.argmax(A1[:,1])
            max_x=A1[:,0][max_ind]
            x_min.append(min(A1[:,0]))
            x_max.append(max(A1[:,0]))
            y_min.append(min(A1[:,1]))
            y_max.append(max(A1[:,1]))
            for i in range(length):
                if A1[i,1]!=0 and A1[i,0]!=0:
                    threshold=A1[i,0]
                    break
            """
            scaler=MinMaxScaler()
            scaler.fit(A1)
            A2=scaler.transform(A1)
            """
            A2=sorted(A1,key=lambda A:A[0])
            A1=np.array(A2)
            x1=A1[:,0]
            xl=min(x1)
            xr=max(x1)
            y1=A1[:,1]
            interpol=interpolate.splrep(x1,y1,k=1)
            #print(interpol)
            x2=np.logspace(math.log10(min_exclude0(A1[:,0])),math.log10(max(A1[:,0])),x_num-1)

            x2=np.append(x2,max_x)
            x2=np.sort(x2)
            y2=spi.splev(x2,interpol)
            A2=np.array([x2,y2])
            A2=np.nan_to_num(A2,copy=False)
            A2=np.transpose(A2)
            scaler=MinMaxScaler()
            scaler.fit(A2)
            A2=scaler.transform(A2)
            Ath=np.zeros((2,1))
            print(np.shape(A2.T))
            Ath[0,0]=1.1
            Ath[1,0]=threshold
            A2=np.hstack((A2.T,Ath))
            print(np.shape(A2))
            train_data[ind]=A2[1]
            train_Label[ind]=Label2
            ind+=1
            
nor_interpol(PATH)