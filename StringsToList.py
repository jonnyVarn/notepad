from msvcrt import getwch as getwch


class StringsToList:

    def __init__(self):
        pass
    
    def editor(self, file_str, os_version):
        if os_version=="nt" or os_version=="linux":

            counter=0
            counter_append=0
            my_list=[]
            stop=False
            for i in file_str:
                    my_list.append(file_str[counter_append])
                    if counter_append<len(my_list): 
                        counter_append+=1
            while stop!=True:
                print(my_list)
                print(counter)
                print(my_list[counter])
                choice=getwch()
                if choice == "q":
                    stop=True 
                print(my_list[counter])
                if choice=="b" and counter>=0:
                    print(my_list[counter])
                    if counter==0:
                        print("min")
                    else:
                        counter-=1
                    continue
                if choice=="f" and counter<(len(my_list)-1):
                    print(my_list[counter])
                    print(counter)
                    if counter==len(my_list)-1:
                        print("max")
                    if counter!=len(my_list):
                        counter +=1
                if choice=="d":
                    if (len(my_list))==1:
                        my_list[0]=""
                        break
                    else:
                        my_list.pop(counter)
                    print(counter)
                    continue    
                if test=="q":
                    break
                else:
                    my_list[counter]=choice   
                    print(my_list[counter])
                    continue
            file_str=""
            for i in my_list:
                file_str+=i
                
        return file_str
    

#test=StringsToList()
#string1=test.editor("hej", "nt")
#print("-------------------------")
#print (string1)
