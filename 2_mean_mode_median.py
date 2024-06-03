array=[2,1,8,6,3,4,7,2,9,6,3,4,7,1,5,9,7,4]
#to find mean ,median, and mode of the array
mean=sum(array)/len(array)
mode=max(set(array),key=array.count)
median=sorted(array)[len(array)//2]

print(f"mean:{mean} \nmode:{mode} \nmedian: {median}")
