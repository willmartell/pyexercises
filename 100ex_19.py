def swap(a,b,c=None):
    if( c is not None ):
        #print "swap ",a[c],",",b[c],"\tto\t",b[c],", ",a[c]
        a[c],b[c]=b[c],a[c]
    else:
        #print "swap ",a,",",b,"\tto\t",b,", ",a
        a,b=b,a
    return a,b

def order_by(l,key):
    dirty = 0
    #print "length of list:",len(l),
    #print ". last element of list at position:",(len(l)-1)

    if(len(l)%2!=0):
        l.append([''])
        #print "length of list adjusted to length:",len(l) 

    #print "show values comparing"

    for i in range(0,len(l)-2):
        j = i + 1
        if(j>len(l)-1):
            j = len(l)-1

        #print "i is:",i,", j is:",j 
        #print l[i][key],' or ',l[j][key], ' : ',

        if(l[i][key]==l[j][key]):
            #print "they are equal ",l[i][key]
            continue
        else:
            if(l[i][key]>l[j][key]):
                #print l[i][key]
                l[i],l[j]=swap(l[i],l[j])
                dirty = dirty + 1
            #else:
                #print l[j][key]

    return dirty,l

def order_slice_by(l,key,start,end,debug):
    dirty = 0

    #print "start:",start,"\t","end:",end

    if(len(l)<2):
        raise Exception,"you passed a short list to order_slice_by"

    if(len(l)%2!=0):
        l.append([''])
    #print "show values comparing"

    for i in range(start,end):
        j = i + 1
        if(j>end):
            j = end

        #print "i is:",i,", j is:",j,"\t",l[i][key],' or ',l[j][key], ' : ',

        if(l[i][key]==l[j][key]):
            #print "they are equal ",l[i][key]
            continue
        else:
            if(l[i][key]>l[j][key]):
                #print l[i][key]
                l[i],l[j]=swap(l[i],l[j])
                dirty = dirty + 1
            #else:
                #print l[j][key]

    return dirty,l

def order_slice_by_two_keys(l,key1,key2,start,end,debug):
    #keys is a list instead of an string
    dirty = 0

    #print "start:",start,"\t","end:",end

    if(len(l)<2):
        raise Exception,"you passed a short list to order_slice_by"

    if(len(l)%2!=0):
        l.append([''])
    #print "show values comparing"

    for i in range(start,end):
        j = i + 1
        if(j>end):
            j = end

        #print "i is:",i,", j is:",j,"\t",l[i][key2],' or ',l[j][key2], ' : ',

        if(l[i][key2]==l[j][key2]):
            #print "they are equal ",l[i][key]
            continue
        else:
            if(l[i][key2]>l[j][key2] and l[i][key1]==l[j][key1]):
                #print l[i][key]
                l[i],l[j]=swap(l[i],l[j])
                dirty = dirty + 1
            #else:
                #print l[j][key]

    return dirty,l

def get_dict_vals(l,key):
    #given a list and a key, return the key values from the list
    vals = []
    for i in range(0,len(l)-1):
        vals.append(l[i][key])
    return vals

def get_dup_dict_val(l,key):
    #go thru list of dicts and determine what value for key is duplicated
    #return list of dup vals
    vals = get_dict_vals(l,key)
    #print "vals is :",vals
    #print type(vals)
    vals = sorted(vals) #make sure they are sorted otherwise last might not equal current

    last = ''
    dups = []
    locs = []
    for i in range(0,len(vals)):
        if(vals[i]==last):
            if(i-1 not in locs): #only add if not already there
                locs.append(i-1)
            if(i not in locs):
                locs.append(i)
            if(vals[i] not in dups):
                dups.append(vals[i])
        else:
            last = vals[i]
    return locs,dups

def print_list(l):
    #print "list length:",len(l)
    for i in range(0,len(l)):
        if(l[i]<>['']):
            print str(i+1)+").",l[i]


#print "verify swap with element"
#print swap('A','B')
#print

#print "verify swap with list"
list1 = ['A','B']
list2 = ['C','D']
#print swap(list1,list2)
#print 

#print "verify swap with list of dictionaries"
list3 = [{'name':'A'},{'name':'B'}]
list4 = [{'name':'C'},{'name':'D'}]
#print swap(list3,list4)
#print 

people = [
    {'name':'Tom','age':19,'score':80},
    {'name':'Jony','age':17,'score':93},
    {'name':'John','age':20,'score':90},
    {'name':'Jony','age':17,'score':91},
    {'name':'Jony','age':21,'score':91},
    {'name':'Json','age':21,'score':85}
]

print "original list"
print_list(people)
print 

loops = 0
done = 1
#print "sorted list by name"
while(done <> 0):
    done,sorted_people = order_by(people,'name')
    if(loops > len(people)):
        raise exception, "loop count exceeded"
        break
    loops = loops + 1

#print_list(sorted_people)
#print "loop count:",loops
#print 

dup_locations,dups = get_dup_dict_val(sorted_people,'name')
#print dup_locations
#print dups
#print

loops = 0
done = 1
print "sorted list by name and age"
while(done <> 0):
    done,sorted_age_people = order_slice_by(sorted_people,'age',dup_locations[0],dup_locations[len(dup_locations)-1],1)
    if(loops > len(sorted_people)):
        raise exception,"loop count exceeded"
        break
    loops = loops + 1

print_list(sorted_age_people)


#assuming that you need to also sort by score since there are duplicate ages and duplicate names
dup_indexs,dup_ages = get_dup_dict_val(sorted_age_people,'age')
#print dup_ages
if(len(dup_ages)>0):
    loops = 0
    done = 1
    print 
    print "sorted list by name and age and score"
    while(done <> 0):
        done,sorted_age_score_people = order_slice_by_two_keys(sorted_age_people,'age','score',dup_locations[0],dup_locations[len(dup_locations)-1],1)
        #print done
        #print_list(sorted_age_score_people)
        #print
        if(loops > len(sorted_age_people)):
            raise exception,"loop count exceeded"
            break
        loops = loops + 1

    print_list(sorted_age_score_people)




