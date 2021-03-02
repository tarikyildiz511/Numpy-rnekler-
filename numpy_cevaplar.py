import numpy as np
np_array = np.array([10,15,30,45,60])

# 5-15 arası dizi
np_array2 = np.arange(5,15)
print(np_array)
print(np_array2)
#(50,100) arasında 5'er 5'er artan dizi
np_array3 = np.arange(50,100,5)
print(np_array3)
#10 tane sıfır
np_array4 = np.zeros(10)
print(np_array4)
#10 tane 1
np_array5 = np.ones(10)
print(np_array5)
#0'dan 100 arasında 5-5 artıyor 
np_array6 =np.linspace(0,100,5)
print(np_array6)
# 10 ile 30 arasında 5 sayı üret
np_array7 = np.random.randint(10,30,5)
#-1 ile 1 arasında 10 adet sayı üretin
np_array8 = np.random.randint(-1,1,10)
print(np_array8)
