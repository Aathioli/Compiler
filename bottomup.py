#Variable Dcelaration
ip_ptr=0
st_ptr=0
temp2=[]
stack=""
input_list=[]
index=0

def check(stack,st_ptr,ip_sym,length):
    flag=0
    #global stack
    #global st_ptr
    if(index==4):
        temp2 = '+'
    else :
        temp2=stack[st_ptr]

    if(temp2=="a" or temp2=="b"):

        input_list=list(stack)
        input_list[st_ptr]='E'
        stack = "".join(input_list)

        if(temp2=="a"):
            print("\n $" + stack + "\t\t" + ip_sym + "$\t\t\tE->a")
        else:
            print("\n $" + stack + "\t\t" + ip_sym + "$\t\t\tE->b")
        flag=1

    if(temp2=="+" or temp2=="*" or temp2=="/"):
        flag=1

    if(stack=="E+E" or stack=="E\E" or stack=="E*E"):
        stack="E"
        st_ptr=0

        if(stack=="E+E"):
            print("\n $" + stack + "\t\t" + ip_sym + "$\t\t\tE->E+E")
        elif(stack=="E\E"):
            print("\n $" + stack + "\t\t " + ip_sym+ "$\t\t\tE->E\E")

        else:
            print("\n $" + stack + "\t\t " + ip_sym+ "$\t\t\tE->E*E")

        flag=1

    if(stack=="E" and ip_ptr==length):
        print("\n $" + stack +"\t\t" + ip_sym + "$\t\t\tACCEPT")
        exit(1)

    if (flag==0):
        print("\n " + stack +"\t\t\t " + ip_sym + "$\t\t\Reject")
        exit(1)

    return stack,st_ptr,ip_sym,length

print("\n\t\t SHIFT REDUCE PARSER\n");
print("\n GRAMMAR\n");
print("\n E->E+E\n E->E/E");
print("\n E->E*E\n E->a/b");
print("\n enter the input symbol:\t");
ip_sym= input()
print("\n\t stack implementation table");
print("\n stack\t\t input symbol\t\t action");
print("\n___\t\t ____\t\t ___\n");
print("\n $\t\t"+ ip_sym +"$\t\t\t--")
act="shift "
temp=ip_sym[ip_ptr]
act = act+temp
length=len(ip_sym)
for i in range(0,length):

#global stack
    stack = stack[:] + ip_sym[ip_ptr]
    input_list=list(ip_sym)
    input_list[ip_ptr]=' '
    #input_list.remove(ip_sym[ip_ptr])
    ip_sym = "".join(input_list)
    ip_ptr = ip_ptr + 1
    print("\n $" + stack + "\t\t" + ip_sym + "$\t\t\t" + act)
    act="shift "
    if (ip_ptr==length) :
        temp=ip_sym[ip_ptr-1]
    else :
        temp=ip_sym[ip_ptr]

    act= act + temp
    stack,st_ptr,ip_sym,length = check(stack,st_ptr,ip_sym,length)
    st_ptr=st_ptr+1
    index = index+1
#global st_ptr
st_ptr = st_ptr+1
index=index+1
stack,st_ptr,ip_sym,length = check(stack,st_ptr,ip_sym,length)