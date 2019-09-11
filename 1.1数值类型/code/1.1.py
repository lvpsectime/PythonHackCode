# _*_ coding:utf-8 _*_

a = 0o101
print("a="+str(a))

b = 64
print("b="+str(b))

c = -127
print("c="+str(c))

d = 0x80
print("d="+str(d))

e = -0x92
print("e="+str(e))

print(bool(1))
print(bool(True))
print(bool('e'))
print(bool([]))
print(bool((1,)))

# 使用bool数
foo = 20
bar = foo<20

print(bar)
print(bar+10)
print('%s' % bar)
print('%d' % bar)

# 无_nozero_()
class C(object):
	pass

c = C()
print(bool(c))

# 双精度浮点型
print(0.0)
print(-777.)
print(-5.384739)
print(96e3 * 1.0)
print(-1.609E-19)

# 复数
print(complex(2, 4))
print(1.23e-045+6.7e+089j)

# 十进制浮点型
from decimal import *

dec = Decimal('.1')
print(dec)
print(Decimal(.1))
print(dec + Decimal(.1))

# 转换工厂
print(int(4.22222222))
print(float(4))
print(complex(4))

# 进制转换
print(hex(255))
print(oct(255))
print(oct(0x111

# ASCII转换
# print(chr(76))
print(ord('L'))