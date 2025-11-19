#PS 1st square numbers
#data being used
data=[1,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192,16384,32768,65536,131072,262144,524288]
#lambda function for sqring data
squarer=list(map(lambda num:num**2,data))
#display data for each on individually
for num in squarer:print(f"Original number:{data[squarer.index(num)]} Squared Number: {num}")