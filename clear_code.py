# not for military use speed renge (0-100ms^-1)
def im_negetive(negative):
    xo=negative
    global yo
    global mark10
    if xo < 0:
        yo= -1*xo
        mark10="i"
        
    else:
        yo = xo
        mark10=" "
    return yo
print(im_negetive(9))
def A():
    import math
    global x2
    global u2
    global a
    x2=math.pow(x,2)
    u2=math.pow(u,2)
    a_up=g*x2
    a_down=2*u2
    a =a_up/a_down
    return a
def C():
    global c
    c_lef=A()
    c=c_lef-High
    return c
def fomula():
    def positwe():
        import math
        global mula
        global negative
        ac4 = 4*a*c
        in_mula=x2-ac4
        negative=float(im_negetive(in_mula))
        mula=math.sqrt(negative)
        #print("loading /////")
        return mula
    
    mula=positwe()
    global tan_c90
    global tan_c
    #tan c
    tan_c_up =-x+mula
    tan_c_down = 2*a
    tan_c = tan_c_up/tan_c_down
    #tan 90-c
    tan_c90_up =-x-mula
    tan_c90=tan_c90_up/tan_c_down
    return tan_c

def floati():
    global x
    global High
    global u
    global g
    x=float(x1)
    High=float(y1)
    u=float(u1)
    g=float(g1)

def tanatoa():
    import math
    global tana1
    global tana2
    global cone1
    global cone2
    global theta_in_radians1
    global theta_in_radians2
    # Example: Given tan(theta) , find theta
    tan_value1 = fomula()
    tana1=fomula()
    theta_in_radians1 = math.atan(tan_value1)
    # Convert radians to degrees if needed
    cone1 = math.degrees(theta_in_radians1)
    # Example: Given tan(theta) , find theta
    tan_value2 = tan_c90
    tana2=tan_c90
    theta_in_radians2 = math.atan(tan_value2)
    # Convert radians to degrees if needed
    cone2 = math.degrees(theta_in_radians2)


#avoide wrong dergrees
def null():
    global tana1
    global tana2
    global cone1
    global cone2
    if tana1 < 0 :
        cone1="null"
    if tana2 < 0 :
        cone2="null"
    
def history():
    global f
    global filedeta
    f=open("report.txt","a")
    print ("",x1,"\t",y1,"\t",u1,"\t",g1,file=f)

    return f
def reeed():
    for i in range(10):
        detaf=f.read()
        print(detaf)
def menusys():
    print("     /\             //|                              ")
    print("     |            //   |           tan@              ")
    print("     |          //      |            ballistic       ")
    print("hight|        //         |                 calculetor")
    print("     |      //            |                          ")
    print("     |    // ;             |                         ")
    print("     |  // @  ;            |                         ")
    print("     \/                                              ")
    print("     <--------------------->                         ")
    print("             lenth                             v1.5  ")

    
loop=True
while loop:
    menusys()
    x1 = input("enter lenth <m> :")
    y1=input("enter hight <m> :")
    u1= input("enter speed <m/s>:")
    g1 =9.87
    history()
    floati()
    #print("loading //")

    A()
    #print("loading ///")
    C()
    tanatoa()
    null()
    #runbreak()
    if mark10 == "i":
        print("wrong claculetion --------------------------------")
        do=str(input("did u wont to continue 'Y'  : "))
        if do != "Y":
            continue
    

    #print("loading ////")
    #sum time only one cone is correct
    print("total tan@ is :",tana1,mark10)
    print("or ")
    print ("total tan@ is :",tana2,mark10)
    import math
    print("_____________________________________________________")
    print("cone is  :",cone1,mark10)
    print("cone is  :",cone2,mark10)
    
    print("_________sum time only one cone is correct___________")
    print("_____________________________________________________")
    print("history  :-? ")
    print("redo     :-Yes\\y")
    loopC=str(input("\n:-"))
    if loopC=="Yes":
        loop=True
    elif loopC=="y":

            loop==True
    elif loopC=="?":
        print("\n done ----------------------------------------\n history:- \n hight\tlenth\tspeed\tg \n")
        f=open("report.txt","r")
        reeed()
        clear = input("clear history 'Y' \n:-")
        if clear == "Y":
            f=open("report.txt","w+")
            print ("",x1,"\t",y1,"\t",u1,"\t",g1,file=f)
            reeed()


            
        w= input("\n done ----------------------------------------")     
    else:
        loop=0
        print("\n done ----------------------------------------")



