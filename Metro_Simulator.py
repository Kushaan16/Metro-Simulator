d={"blue1" : [
    "Dwarka Sector 21",
    "Dwarka Sector 8",
    "Dwarka Sector 9",
    "Dwarka Sector 10",
    "Dwarka Sector 11",
    "Dwarka Sector 12",
    "Dwarka Sector 13",
    "Dwarka Sector 14",
    "Dwarka",
    "Dwarka Mor",
    "Nawada",
    "Uttam Nagar West",
    "Uttam Nagar East",
    "Janakpuri West",
    "Janakpuri East",
    "Tilak Nagar",
    "Subhash Nagar",
    "Tagore Garden",
    "Rajouri Garden",
    "Ramesh Nagar",
    "Moti Nagar",
    "Kirti Nagar",
    "Shadipur",
    "Patel Nagar",
    "Rajendra Place",
    "Karol Bagh",
    "Jhandewalan",
    "Ramakrishna Ashram Marg",
    "Rajiv Chowk",
    "Barakhamba Road",
    "Mandi House",
    "Supreme Court",
    "Indraprastha",
    "Yamuna Bank",
    "Akshardham",
    "Mayur Vihar-1",
    "Mayur Vihar Extension",
    "New Ashok Nagar",
    "Noida Sector 15",
    "Noida Sector 16",
    "Noida Sector 18",
    "Botanical Garden",
    "Golf Course",
    "Noida City Centre",
    "Noida Sector 34",
    "Noida Sector 52",
    "Noida Sector 61",
    "Noida Sector 59",
    "Noida Sector 62",
    "Noida Electronic City"
]
,"blue2" : [
    "Dwarka Sector 21",
    "Dwarka Sector 8",
    "Dwarka Sector 9",
    "Dwarka Sector 10",
    "Dwarka Sector 11",
    "Dwarka Sector 12",
    "Dwarka Sector 13",
    "Dwarka Sector 14",
    "Dwarka",
    "Dwarka Mor",
    "Nawada",
    "Uttam Nagar West",
    "Uttam Nagar East",
    "Janakpuri West",
    "Janakpuri East",
    "Tilak Nagar",
    "Subhash Nagar",
    "Tagore Garden",
    "Rajouri Garden",
    "Ramesh Nagar",
    "Moti Nagar",
    "Kirti Nagar",
    "Shadipur",
    "Patel Nagar",
    "Rajendra Place",
    "Karol Bagh",
    "Jhandewalan",
    "Ramakrishna Ashram Marg",
    "Rajiv Chowk",
    "Barakhamba Road",
    "Mandi House",
    "Supreme Court",
    "Indraprastha",
    "Yamuna Bank",
    "Laxmi Nagar",
    "Nirman Vihar",
    "Preet Vihar",
    "Karkarduma",
    "Anand Vihar Isbt",
    "Kaushambi",
    "Vaishali"
],
'magenta': [
    "Janakpuri West",
    "Dabri Mor Janakpuri South",
    "Dashrathpuri",
    "Palam",
    "Sadar Bazaar Cantonment",
    "Terminal 1-igi Airport",
    "Shankar Vihar",
    "Vasant Vihar",
    "Munirka",
    "R.k. Puram",
    "Iit Delhi",
    "Hauz Khas",
    "Panchsheel Park",
    "Chirag Delhi",
    "Greater Kailash",
    "Nehru Enclave",
    "Kalkaji Mandir",
    "Okhla Nsic",
    "Sukhdev Vihar",
    "Jamia Millia Islamia",
    "Okhla Vihar",
    "Jasola Vihar Shaheen Bagh",
    "Kalindi Kunj",
    "Okhla Bird Sanctuary",
    "Botanical Garden"
],
'airport express line':[
'New Delhi',
'Shivaji Stadium',
'Dhaula Kuan',
'Delhi Aerocity',
'Igi Airport T3',
'Dwarka Sector 21'
]
}
totaldn=114
totaldv=89
totaljb=64
totalo=24
def htomin(s):
    s1=s[3]+s[4]
    s1=int(s1)
    s2=int(s[0]+s[1])
    s2=s2*60
    return s1+s2
def mintoh(x):
    hh=x//60
    mm=x%60
    s=f"{hh:02d}"+":"+f"{mm:02d}"  
    return s
def nextmet(t1,x,s):
    if(0<=t1<360):
        t1+=24*60
    if(t1>1380+s):
        return "no service available"
    while True:
         a=x+s
         if(a>=t1):
            t2=mintoh(a)
            return t2
         if(480<=x<600 or 1020<=x<1140):
             x+=4
         else:
             x+=8
def timetost(line,st):
    f=open("metro.txt","r")
    x=f.readlines()
    sum1=0
    for i in x:
        a=i.split(",")
        if(a[0]==line):
            if(a[1]==st):
                break
            else:
                sum1+=int(a[3])
    f.close()
    return sum1
def time(line,st,t,total):
    t1=htomin(t)
    s=timetost(line,st)
    
    e=total-s
  
    l=[]
    x=360 
    s1=nextmet(t1,x,s)
    e1=nextmet(t1,x,e)
    if(s1!="no service available"):
       if(s1>="24:00"):
          a=f"{int(s1[0]+s1[1])-24:02d}"
          b=s1[-2]+s1[-1]
          l.append(a+":"+b)
       else:
          l.append(s1)
    else:
        l.append("no service available")  
    if(e1!="no service available"):
       if(e1>="24:00"):
          a=f"{(int(e1[0]+e1[1])-24):02d}"
          b=e1[-2]+e1[-1]
          l.append(a+":"+b)
       else:
          l.append(e1)
    else:
        l.append("no service available")
    return l
def removenoserv(l):
    while True:
        if("no service available" in l):
            l.remove("no service available")
        else:
            break
    return l
def printr(l,l1=[]):
    #print(l,l1)
    l2=l+l1
    l2=list(set(l2))
    if(l2==[]):
        print("no service available")
    else:
        a1=min(l2)
        print("Next metro at",a1)
        l2.remove(a1)
        if("8:00"<=a1<"10:00" or "17:00"<=a1<"19:00"):
            l2.append(a1[0]+a1[1]+a1[2]+f"{int(a1[3]+a1[4])+4:02d}")
        else:
            l2.append(a1[0]+a1[1]+a1[2]+f"{int(a1[3]+a1[4])+8:02d}")
        a2=min(l2)
        l2.remove(a2)
        if("8:00"<=a2<"10:00" or "17:00"<=a2<"19:00"):
            l2.append(a2[0]+a2[1]+a2[2]+f"{int(a2[3]+a2[4])+4:02d}")
        else:
            l2.append(a2[0]+a2[1]+a2[2]+f"{int(a2[3]+a2[4])+8:02d}")
        a3=min(l2)
        print("Subsequent metros at",a2,a3,"...")

def sttime(l,j):
    with open("metro.txt","r") as f:
        x=f.readlines()
    for i1 in x:
        a=i1.split(",")
        if((a[1]==l[j-1] and a[2]==l[j]) or (a[2]==l[j-1] and a[1]==l[j])):
            return int(a[3])
def time2(l,l1):
    l2=l1.copy()
    l2.append(l[-1])
    j=1
    t=[]
    for i in l2:
        sum1=0
        while j<len(l):
            if(l[j]==i):
               sum1+=sttime(l,j)
               t.append(sum1)
               j+=1
               break
            sum1+=sttime(l,j)
            j+=1
    return t
def whichline(line,src,dest):
    a=d[line].index(src)
    b=d[line].index(dest)
    if(a<b):
        return 0
    elif(a>b):
        return -1
def nextmet1(curtime,t,route,interchange):
    inter=interchange.copy()
    inter.append(route[-1])
    inter.insert(0,route[0])
    j=1
    j1=0
    p=1
    lst=[]
    print("Journey Plan:")
    while j<len(inter):
        if(inter[j] in d["blue1"] and inter[j-1] in d['blue1']):
            line="blue1"
            line1="Blue"
            l=time('blue1',inter[j-1],curtime,totaldn)
        elif(inter[j] in d["blue2"] and inter[j-1] in d['blue2']):
            line="blue2"
            line1="Blue"
            l=time('blue2',inter[j-1],curtime,totaldv)
        elif(inter[j] in d["magenta"] and inter[j-1] in d['magenta']):
            line="magenta"
            line1="Magenta"
            l=time('magenta',inter[j-1],curtime,totaljb)
        elif(inter[j] in d["airport express line"] and inter[j-1] in d['airport express line']):
            line="airport express line"
            line1="Airport Express"
            l=time("airport express line",inter[j-1],curtime,totalo)
        index=whichline(line,inter[j-1],inter[j])
        if(j1==0):
            lst.append(l[index])
            print('Start at',inter[j-1],f"({line1} Line)")
        else:
            print("Transfer to",line1,"Line")
           
        if(l[index]=="no service available"):
            print("No service available for metro at this station to reach your destination")
            p=0
            break
        else:
            if(l[index]>="24:00"):
                q=l[index]
                print("Next",line1,"line metro departs at",f"{int(q[0]+q[1])-24:02d}:{q[3]+q[4]}")
            else:
                print("Next",line1,"line metro departs at",l[index])
        c1=htomin(l[index])
        c1+=t[j1]
        curtime=mintoh(c1)
        if(curtime>="24:00"):
                q=curtime
                print("Arrive at",inter[j],"at",f"{int(q[0]+q[1])-24:02d}:{q[3]+q[4]}")
        else:
                print("Arrive at",inter[j],"at",curtime)
      
        if(j==len(inter)-1):
            lst.append(curtime)
            break 
        if("08:00"<=curtime<"10:00" or "17:00"<=curtime<"19:00"):
            curtime=htomin(curtime)
            curtime+=10
            curtime=mintoh(curtime)
        else:
            curtime=htomin(curtime)
            curtime+=5
            curtime=mintoh(curtime)
        j1+=1
        j+=1
    if(p==0):
        pass
    else:
        a1=htomin(lst[0])
        b1=htomin(lst[1])
        c1=b1-a1
        c1=mintoh(c1)
        print("Total travel time:",c1[0]+c1[1],"hours",c1[3]+c1[4],"minutes")
def findst(source,dest):
    if(source in d['blue1'] and dest in d["blue1"]):
        a=d['blue1'].index(source)
        b=d['blue1'].index(dest)
        if a <= b:
            return (d['blue1'][a:b+1],[])
        else:
            return (d['blue1'][b:a+1][::-1],[])

    elif(source in d['blue2'] and dest in d["blue2"] ):
        a=d['blue2'].index(source)
        b=d['blue2'].index(dest)
        if a <= b:
            return d['blue2'][a:b+1],[]
        else:
            return d['blue2'][b:a+1][::-1],[]
    elif(source in d['magenta'] and dest in d["magenta"] ):
        a=d['magenta'].index(source)
        b=d['magenta'].index(dest)
        if a <= b:
            return  d['magenta'][a:b+1],[]
        else:
            return d['magenta'][b:a+1][::-1],[]
    
    elif(source in d['blue1'] and dest in d["blue2"] ):
        a = d['blue1'].index(source)
        b = d['blue1'].index("Yamuna Bank")
        if a <= b:
            part1 = d['blue1'][a:b+1]
        else:
            part1 = d['blue1'][b:a+1][::-1]
        c = d['blue2'].index("Yamuna Bank")
        d1 = d['blue2'].index(dest)
        if c <= d1:
            part2 = d['blue2'][c+1:d1+1]
        else:
            part2 = d['blue2'][d1:c][::-1]
        return part1+part2,["Yamuna Bank"]
    elif(source in d['blue2'] and dest in d["blue1"] ):
        a = d['blue2'].index(source)
        b = d['blue2'].index("Yamuna Bank")
        if a <= b:
            part1 = d['blue2'][a:b+1]
        else:
            part1 = d['blue2'][b:a+1][::-1]
        c = d['blue1'].index("Yamuna Bank")
        d1 = d['blue1'].index(dest)
        if c <= d1:
            part2 = d['blue1'][c+1:d1+1]
        else:
            part2 = d['blue1'][d1:c][::-1]
        return part1+part2,["Yamuna Bank"]
    elif(source in d["magenta"] and (dest in d["blue1"] or dest in d["blue2"])):
            if(dest in d["blue1"]):
                a = d['magenta'].index(source)
                b = d['magenta'].index("Janakpuri West")
                if a <= b:
                    part1 = d['magenta'][a:b+1]
                else:
                    part1 = d['magenta'][b:a+1][::-1]
                c = d['blue1'].index("Janakpuri West")
                d1 = d['blue1'].index(dest)
                if c <= d1:
                    part2 = d['blue1'][c+1:d1+1]
                else:
                    part2 = d['blue1'][d1:c][::-1]
                return part1+part2,["Janakpuri West"]
            elif(dest in d["blue2"]):
                a = d['magenta'].index(source)
                b = d['magenta'].index("Janakpuri West")
                if a <= b:
                    part1 = d['magenta'][a:b+1]
                else:
                    part1 = d['magenta'][b:a+1][::-1]
                c = d['blue2'].index("Janakpuri West")
                d1 = d['blue2'].index(dest)
                if c <= d1:
                    part2 = d['blue2'][c+1:d1+1]
                else:
                    part2 = d['blue2'][d1:c][::-1]
                return part1+part2,["Janakpuri West"]
    elif(dest in d["magenta"] and (source in d["blue1"] or source in d["blue2"])):
            if(source in d["blue1"]):
                a = d['blue1'].index(source)
                b = d['blue1'].index("Janakpuri West")
                if a <= b:
                    part1 = d['blue1'][a:b+1]
                else:
                    part1 = d['blue1'][b:a+1][::-1]
                c = d['magenta'].index("Janakpuri West")
                d1 = d['magenta'].index(dest)
                if c <= d1:
                    part2 = d['magenta'][c+1:d1+1]
                else:
                    part2 = d['magenta'][d1:c][::-1]
                return part1+part2,["Janakpuri West"]
            elif(source in d["blue2"]):
                a = d['blue2'].index(source)
                b = d['blue2'].index("Janakpuri West")
                if a <= b:
                    part1 = d['blue2'][a:b+1]
                else:
                    part1 = d['blue2'][b:a+1][::-1]
                c = d['magenta'].index("Janakpuri West")
                d1 = d['magenta'].index(dest)
                if c <= d1:
                    part2 = d['magenta'][c+1:d1+1]
                else:
                    part2 = d['magenta'][d1:c][::-1]
                return part1+part2,["Janakpuri West"]
    else:
        if(source in d["airport express line"] and destination in d["airport express line"]):
            a=d["airport express line"].index(source)
            b=d["airport express line"].index(dest)
            if a <= b:
                return  d["airport express line"][a:b+1],[]
            else:
                return d["airport express line"][b:a+1][::-1],[]
        elif(source in d["airport express line"]):
                a = d["airport express line"].index(source)
                b = d["airport express line"].index("Dwarka Sector 21")
                if a <= b:
                    part1 = d["airport express line"][a:b+1]
                else:
                    part1 = d["airport express line"][b:a+1][::-1]
                part2,changept=findst("Dwarka Sector 21",destination)
                part2.remove("Dwarka Sector 21")
                return part1+part2,["Dwarka Sector 21"]+changept
        elif(destination in d["airport express line"]):
                part1,changept=findst(source,"Dwarka Sector 21")
                a = d["airport express line"].index("Dwarka Sector 21")
                b = d["airport express line"].index(destination)
                if a <= b:
                    part2 = d["airport express line"][a:b+1]
                else:
                    part2 = d["airport express line"][b:a+1][::-1]
                part2.remove("Dwarka Sector 21")
                return part1+part2,changept+["Dwarka Sector 21"]

def getfandl(line):
    if(line=="blue"):
        print(d["blue1"][0],f"<--> {d['blue1'][-1]} / {d['blue2'][-1]}")
    elif(line=="magenta"):
        print(d["magenta"][0],"<-->",d["magenta"][-1])
    else:
        print(d["airport express line"][0],"<-->",d["airport express line"][-1])
def dist(l,j):
    with open("metro.txt","r") as f:
        x=f.readlines()
    #print(l[j-1],",",l[j])
    for i1 in x:
        i2=i1.splitlines()
        a=i2[0].split(",")
        if((a[1]==l[j-1] and a[2]==l[j]) or (a[2]==l[j-1] and a[1]==l[j])):
            return float(a[-1])
def tdist(l):
    j=1
    sum1=0
    while j<len(l):
        sum1+=dist(l,j)
        j+=1
    return sum1
def getfare(source,destination):
    route,interchange=findst(source,destination)
    dist=tdist(route)
    if(0<=dist<2):
        return 11
    elif(2<=dist<5):
        return 21
    elif(5<=dist<12):
        return 32
    elif(12<=dist<21):
        return 43
    elif(21<=dist<32):
        return 54
    else:
        return 64

while True:
    print("MENU:")
    print("1.Metro Timing")
    print("2.Ride Journey Planner")
    print("3.Get first and last station corresponding to any line")
    print("4.get fare")
    print("5.Exit")

    z=int(input("enter your choice: "))
    if(z==1):
        mline=input("Line = ").strip()
        station=input("Station = ").strip()
        station=station.title()
        currtime=input("Current time = ").strip()
        mline=mline.lower()
        try:
            assert mline=="airport express line" or mline=="blue" or mline=="magenta"
            if(mline=="blue"):
                assert station in d["blue1"] or station in d["blue2"]
            else:
                assert station in d[mline]
            assert len(currtime) == 5 and currtime[2] == ":" and currtime[:2].isdigit() and currtime[3:].isdigit() and 0 <= int(currtime[:2]) <= 23 and 0 <= int(currtime[3:]) <= 59
        except:
            print("invalid input!")
            continue
        if(mline=="blue"):
            if(station in d['blue1'] and station not in d['blue2']):
                l=time("blue1",station,currtime,totaldn)
                l=removenoserv(l)
                printr(l)
            elif(station in d['blue2'] and station not in d['blue1']):
                l=time("blue2",station,currtime,totaldv)
                l=removenoserv(l)
                printr(l)
            elif(station in d['blue2'] and station in d['blue1']):
                l=time("blue1",station,currtime,totaldn)
                l1=time("blue2",station,currtime,totaldv)
                l=removenoserv(l)
                l1=removenoserv(l1)
                printr(l,l1)
        elif(mline=="magenta"):
            l=time('magenta',station,currtime,totaljb)
            printr(l)
        elif(mline=="airport express line"):
             l=time("airport express line",station,currtime,totalo)
             printr(l)
        print()
    elif(z==2):
        source=input("Source: ").strip()
        destination=input("Destination: ").strip()
        currtime=input("Time of Travel: ").strip()
        source=source.title()
        destination=destination.title()
        try:
            assert source!=destination
            assert source in d["blue1"] or source in d["blue2"] or source in d["magenta"] or source in d["airport express line"]
            assert destination in d["blue1"] or destination in d["blue2"] or destination in d["magenta"] or destination in d["airport express line"]
            assert len(currtime) == 5 and currtime[2] == ":" and currtime[:2].isdigit() and currtime[3:].isdigit() and 0 <= int(currtime[:2]) <= 23 and 0 <= int(currtime[3:]) <= 59
        except:
            print("invalid input!")
            continue
        route,interchange=findst(source,destination)
        time1=time2(route,interchange)
        nextmet1(currtime,time1,route,interchange)
        print()
    elif(z==3):
        line=input("Line: ").strip()
        try:
            assert line=="airport express line" or line=="blue" or line=="magenta"
        except:
            print("invalid input!")
            continue
        getfandl(line)
        print()
    elif(z==4):
        source=input("Source: ").strip()
        destination=input("Destination: ").strip()
        source=source.title()
        destination=destination.title()
        try:
            assert source!=destination
            assert source in d["blue1"] or source in d["blue2"] or source in d["magenta"] or source in d["airport express line"]
            assert destination in d["blue1"] or destination in d["blue2"] or destination in d["magenta"] or destination in d["airport express line"]
        except:
            print("invalid input!")
            continue
        fare=getfare(source, destination)
        print(f"Fare to travel from {source} to {destination} is Rs.{fare}")
        print()
    elif(z==5):
        print("bye")
        break
    else:
        print("Invalid choice!")

