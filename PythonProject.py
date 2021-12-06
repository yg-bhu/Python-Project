import datetime
import time

x=datetime.datetime.now()
y=x.strftime("%d")
z=x.strftime("%m")

def adddetails(a):
    if a==1:
        li.append(1)
    elif a==2:
        li.append(2)
    else:
        li.append(3)

class City:
  pass
class Movie:
  def infoAboutMovie(self):
    pass
  def date(self):
    print("Select The Date")
    print("1."+y+"/"+z)
    print("2."+str(int(y)+1)+"/"+z)
    print("3."+str(int(y)+2)+"/"+z)
  def time(self):
      print("1.9:00 AM\n2.12.00 PM\n3.3.00 PM")
    
  def cinemaHall(self):
      print("1.PVP\n2.PVR\n3.INOX")

class Initiatepaymet:
    a=0
    def UPI(self):
        print("Select your Upi app:\n1.Phonepe\n2.paytm\n3.gpay")
        a=int(input())
        print("Your payment is redirected respective gateway\n")
        print("......")
        print("Payment Successful\n")
    def internetBanking(self):
        print("Select your Bank:\n1.SBI\n2.HDFC\n3.ICICI")
        a=int(input())
        print("Your payment is redirected respective gateway\n")
        print("......")
        time.sleep(5)
        print("Payment Successful\n")
    

class Akhanda(Movie):
  name="Akhanda"
  def infoAboutMovie(self):
    print("Hero:NBK\nVillan:Srikanth\nHeroine:Pragya Jaiswal\nIMDB:8.1")

class Skylab(Movie):
  name="Skylab"
  def infoAboutMovie(self):
    print("Hero:Satyadev\nVillan:skylab\nHeroine:Nithya Menon\nIMDB:8.5")

class Marakkar(Movie):
  name="Marakkar"
  def infoAboutMovie(self):
    print("Hero:Mohan Lal\nVillan:daniel craig\nHeroine:Keerthy Suresh\nIMDB:6.5")




class Hyderabad(City):
  def _init_(self):
    pass
  def displayMovies(self):
    print("1.Akhanda\n2.Skylab\n3.Marakkar")

class Vizag(City):
  def _init_(self):
    pass
  def displayMovies(self):
    print("1.Akhanda\n2.Skylab\n3.Marakkar")

class Chennai(City):
  def _init_(self):
    pass
  def displayMovies(self):
    print("1.Akhanda\n2.Skylab\n3.Marakkar")
    
print("Welcome to BookMyMovie")
print("Select your City:")
print("1.Hyderabad\n2.Vizag\n3.Chennai")
city=input()
li=[]
print("Select your Movie:")
if int(city)==1:
  obj=Hyderabad()
  obj.displayMovies()
elif city==2:
  obj=Vizag()
  obj.displayMovies()
else:
  obj=Chennai()
  obj.displayMovies()
  
movie = int(input())

if movie==1:
  obj2=Akhanda()
  obj2.infoAboutMovie()
  obj2.date()
  d=int(input())
  adddetails(d)
  obj2.time()
  t=int(input())
  adddetails(t)
  obj2.cinemaHall()
  c=int(input())
  adddetails(c)
elif movie==2:
  obj2=Skylab()
  obj2.infoAboutMovie()
  obj2.date()
  d=int(input())
  adddetails(d)
  obj2.time()
  t=int(input())
  adddetails(t)
  obj2.cinemaHall()
  c=int(input())
  adddetails(c)
else:
  obj2=Marakkar()
  obj2.infoAboutMovie()
  obj2.date()
  d=int(input())
  adddetails(d)
  obj2.time()
  t=int(input())
  adddetails(t)
  obj2.cinemaHall()
  c=int(input())
  adddetails(c)

print("Enter the row and Seat Number:")
rowno=input()
seatno=int(input())
print("Enter your e-mail id:")
email=input()
print("The total amount to be paid is:",150,"\n")
obj1=Initiatepaymet()
print("Select your payment method:\n1.UPI\n2.Internet Banking")
pm=int(input())
if pm==1:
    obj1.UPI()
else:
    obj1.internetBanking()
print("Your ticket details:")
print("Movie:",obj2.name)
print("Seat:",rowno,seatno)
print("date:")
if li[0] == 1:
    print(y+"/"+z)
elif li[0] == 2:
    print(str(int(y)+1)+"/"+z)
else:
    print(str(int(y)+2)+"/"+z)
  
print("Time:")
if li[1] == 1:
    print("9.00 AM")
elif li[1] == 2:
    print("12.00 PM")
else:
    print("3.00 PM")
    
print("Cinema Hall:")
if li[1] == 1:
    print("PVP")
elif li[1] == 2:
    print("PVR")
else:
    print("INOX")
    
print("\n")
print("Thanks for using the BOOKMYMOVIE")





