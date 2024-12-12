#def binary_search(arr, target): 
    #low = 0 
    #high = len(arr) - 1 
     
    #while low <= high: 
        #mid = (low + high) // 2 
        #if arr[mid] == target: 
            #return mid   
        #elif arr[mid] < target: 
            #low = mid + 1   
        #else: 
            #high = mid - 1  
     
    #return -1   
 
#def search_element(arr, target): 
     
    #arr.sort()  
    #print("List setelah diurutkan:", arr) 
     
    #result = binary_search(arr, target) 
     
    #if result != -1: 
        #print(f"Elemen {target} ditemukan pada indeks {result}.") 
    #else: 
        # print(f"Elemen {target} tidak ditemukan dalam list.") 
 
#arr = [2, 15, 23, 28, 31, 34, 56, 87, 89, 200] 
#target = 23 
#search_element(arr, target)

#NO 2

def sort_data(data, n=None):
    if n is None:
        n = len(data)
    if n == 1:
        return
    for i in range(n - 1):
        if data[i] > data[i + 1]:
            data[1], data[i + 1] = data[i + 1], data[i]
    sort_data(data, n - 1)

def search_data(data, target, start, end):
    if start > end:
        return -1
    mid = (start + end) // 2
    if data[mid] == target:
        return mid
    elif data[mid] > target:
        return search_data(data, target, start, mid -1)
    else:
        return search_data(data, target, mid + 1, end) 

data = [87, 56, 34, 23, 89, 15, 2, 200, 28, 31]
target = int(input("masukan angka yang dicari:"))
print("data sebelum diurutkan:", data)

sort_data(data)
print("data setelah diurutkan:", data)

result = search_data(data, target, 0, len(data) - 1)
if result != -1:
    print(f"angka ditemukan pada urutan ke-{result + 1}")
else:
    print("angka tidak ditemukan.")