from fbchat import  Client
from fbchat.models import *
import getpass

def partition(arr,arr2,low,high): 
    i = ( low-1 ) 
    pivot = arr[high] 
    for j in range(low , high):
        if arr[j] <= pivot:
            i=i+1
            arr[i],arr[j] = arr[j],arr[i]
            arr2[i],arr2[j] = arr2[j],arr2[i]
    arr[i+1],arr[high] = arr[high],arr[i+1]
    arr2[i+1],arr2[high] = arr2[high],arr2[i+1]
    return ( i+1 ) 
def quickSort(arr,arr2,low,high): 
	if low < high: 
		pi = partition(arr,arr2,low,high) 
		quickSort(arr,arr2, low, pi-1) 
		quickSort(arr,arr2, pi+1, high)  

login = input('Email: ')
passwd = getpass.getpass('Password: ')
client = Client(login,passwd)

Users = client.fetchAllUsers()
messages = []
names = []
numOfUsers = len(Users)
for x in range(0,numOfUsers):
    thread = client.fetchThreadInfo(Users[x].uid)
    names.append(Users[x].name)
    if thread[Users[x].uid].message_count == None:
        messages.append(0)
    else:
        messages.append(thread[Users[x].uid].message_count)
    print(str(100*(x+1)/numOfUsers)+'%')
quickSort(messages,names,0,numOfUsers-1)
print()
print('######')
print()
for x in range(numOfUsers-1,0,-1):
    print(str(numOfUsers-x)+'. '+names[x]+' | '+str(messages[x]))
client.logout()