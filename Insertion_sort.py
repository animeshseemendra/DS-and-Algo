array=list(map(int,input().split()))
print('Your Array :',array)
for i in range(0,len(array)-1):
    if(array[i+1]<array[i]):
        temp=array[i+1]
        j=i
        while(temp<array[j] and j>=0):
            array[j+1]=array[j]
            j-=1 
        array[j+1]=temp
print('Sorted Array : ',array)