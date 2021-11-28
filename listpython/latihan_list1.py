list1 = [2,3,5,6,8]

print(list1)
print('List elemen ke 3:',list1[2])
print('List elemen ke 2 sampai elemen ke 4:',list1[1:4])
print('List elemen terakhir:',list1[-1]) 

list1[3] = 10

print('Perubahan elemen ke 4:',list1)

list1[3:] = 10,14

print('Perubahan elemen ke 4 dengan elemen terakhir:',list1)

list2 = [20,30,40,50,55]

list2.append(list1[0:2])
print('2 Bagian list pertama yang dijadikan bagian dalam list ke 2:',list2)

list2.append('halo kamu')
print('Penambahan elemen list pada list2:', list2)

list2.extend([80,90,102])
print('Penambahan 3 nilai pada list ke dua:',list2)

x = list1+list2
print('Gabungan list satu dengan list dua:',x) 