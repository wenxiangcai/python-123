#encoding=UTF-8

class struct(object):
    def __init__(self,value):
        self.old = 0
        self.value = value

def updateold(list):
    for i in list:
            i.old+=1

def max_old(list):
    max_old = 0
    for i in range(1,len(list)):
        if list[i].old > list[max_old].old:
           max_old=i
    return max_old

if __name__=='__main__':
    page_list = []
    list1 = [1,2,3,1,2,4,5,2]
    Max_len=3
    print "[-]页置换队列:",list1
    for i in list1:
        i = struct(i)
        #第一种情况
        value_list=[j.value for j in page_list]
        if i.value not in value_list and len(page_list)<Max_len:
            #page_list中的old值+1
            updateold(page_list)
            page_list.append(i)
            print "[-]添加页:",[i.value for i in page_list]
        #第二种情况
        elif i.value in value_list:
            for j in page_list:
                if j.value == i.value:
                    j.old = 0
                else:
                    j.old+=1
            print "[-]发现已有页,更新:",[i.value for i in page_list]
        #第三种情况
        elif i.value not in value_list and len(page_list)==Max_len:
            #old值+1
            for j in page_list:
                j.old+=1
            #替换最老的
            page_list[max_old(page_list)] = i
            print "[-]缺页，进行替换:",[i.value for i in page_list]
