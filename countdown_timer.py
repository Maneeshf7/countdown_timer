import time
mytime=int(input("enter your time :"))
for i  in reversed(range(0,mytime)):
    sec=i%60
    mins=(i%3600)//60
    hr=i//3600
    print (f"{hr:02d}:{mins:02d}:{sec:02d}")
    time.sleep(1)
print("Times up")
 
      
