print ("I love you")

x=2
x=8+x
print (x)

x=-1
if x > 0:
	print ("shabi")
print ('sha')

n=5
while n>0:
	n=n-1
	print (n)
print ("la la land")

n=0
while n<10:
	print(n)
	n=n+1
print ('done')

name = raw_input ('what is your name?')
print ('welcome', name)

hour = 35
rate = 2.75
pay = hour * rate
print (pay)

a = raw_input ('working hours?')
H = float(a)
print H

b = raw_input ('Pay rate?')
P = float(b)
print P

input_h = raw_input("Enter Hours:")
hours = float (input_h)

input_r = raw_input("Enter Rates:")
rates = float (input_r)

def computepay(h,r):
    if h <= 40:
        pay = h*r
    else:
        pay = 40*r+(h-40)*1.5*r
       
    return pay

print computepay(hours,rates)

score = raw_input ('enter your score')
s = float(score)
if s>90:
    print ('A')
else if s>80:
    print ('B')
else if s>70:
    print ('C')
else:
    print ('F')
    
def score(s):
    if s>90

def lyrics():
    return "print"
print (lyrics())