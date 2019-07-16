class C:
    dangerous = 2
c1 = C()
c2 = C()
print c1.dangerous
c1.dangerous = 3
print c1.dangerous
print c2.dangerous
del c1.dangerous
print "after del -"+str(c1.dangerous)
C.dangerous = 3
print c2.dangerous
c3 = C()
print c1.dangerous
print c3.dangerous
