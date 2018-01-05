import matplotlib.pyplot as plt

x1 = []
y1 = []
x2 = []
y2 = []

f1 = open('hmwk5c_problem1a.dat','r')
for line in f1.readlines():
	number1 = map(float, line.split())
        x1.append(number1[0])
        y1.append(number1[1])
        
f1.close

f2 = open('hmwk5c_problem1b.dat','r')
for line in f2.readlines():
	number2 = map(float, line.split())
        x2.append(number2[0])
        y2.append(number2[1])
        
f2.close


plt.plot(x1,y1)
plt.xlabel('reflected angle(theta)')
plt.ylabel('distribution')
plt.title('incident angle=30')
plt.show()
plt.savefig("hmwk6_poblem1a.jpg")

plt.plot(x2,y2)
plt.xlabel('reflected angle(theta)')
plt.ylabel('distribution')
plt.title('incident angle=45&180')
plt.show()
plt.savefig("hmwk6_poblem1b.jpg")
