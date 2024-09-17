from ctypes import CDLL, c_int

dll = CDLL("./sum_sub.dll")
resultado = dll.sum(5,3)
resultado1 = dll.sub(5,3)

print('resultado da soma: {}' .format(resultado))
print('resultado da subtracao: {}' .format(resultado1))