# module math from scratch
''' i am coder 8  made the class myth from scratch by using python and some collected data from basic math 
with the help of these and stack data structure i made the class myth algorithm complete implimented from scratch 
i am going to write a paper about it i had noticed some keypoints about this program i think that should be 
discusse  with the world

i hope i did correct  '''



class myth(object):
    '''it is a class perform basic math operations such as ["Addition","Substraction","Multipication","Divison"]'''
    
    def __init__(self):
        
        self.num1 = [] #addition var
        self.num2 = []
        self.remainder = []
        self.result =  []
        self.value = ""

        self.subrem = [] #substract var
        self.subres = []
        self.sub1 = []
        self.sub2 = []
        self.subval = ""

        self.table_add = { "0 + 0":0,"0 + 1":1,"0 + 2":2,"0 + 3":3,"0 + 4":4,"0 + 5":5,"0 + 6":6,"0 + 7":7,"0 + 8":8,"0 + 9":9,
        "1 + 0":1,"1 + 1":2,"1 + 2":3,"1 + 3":4,"1 + 4":5,"1 + 5":6,"1 + 6":7,"1 + 7":8,"1 + 8":9,"1 + 9":10,"2 + 0":2,
        "2 + 1":3,"2 + 2":4,"2 + 3":5,"2 + 4":6,"2 + 5":7,"2 + 6":8,"2 + 7":9,"2 + 8":10,"2 + 9":11,
        "3 + 0":3,"3 + 1":4,"3 + 2":5,"3 + 3":6,"3 + 4":7,"3 + 5":8,"3 + 6":9,"3 + 7":10,"3 + 8":11,"3 + 9":12,"4 + 0":4,"4 + 1":5,"4 + 2":6,"4 + 3":7,"4 + 4":8,"4 + 5":9,"4 + 6":10,"4 + 7":11,"4 + 8":12,"4 + 9":13,"5 + 0":5,"5 + 1":6,
        "5 + 2":7,"5 + 3":8,"5 + 4":9,"5 + 5":10,"5 + 6":11,"5 + 7":12,"5 + 8":13,"5 + 9":14,"6 + 0":6,"6 + 1":7,"6 + 2":8,"6 + 3":9,"6 + 4":10,"6 + 5":11,
        "6 + 6":12,"6 + 7":13,"6 + 8":14,"6 + 9":15,"7 + 0":7,"7 + 1":8,"7 + 2":9,"7 + 3":10,"7 + 4":11,"7 + 5":12,"7 + 6":13,"7 + 7":14,"7 + 8":15,"7 + 9":16,
        "8 + 0":8,"8 + 1":9,"8 + 2":10,"8 + 3":11,"8 + 4":12,"8 + 5":13,"8 + 6":14,"8 + 7":15,"8 + 8":16,"8 + 9":17,"9 + 0":9,"9 + 1":10,"9 + 2":11,
        "9 + 3":13,"9 + 4":13,"9 + 5":14,"9 + 6":15,"9 + 7":16,"9 + 8":17,"9 + 9":18,
        } # addition data
        self.sub_table = {"0 - 0":0,
        "0 - 1":-1,"0 - 2":-2,"0 - 3":-3,"0 - 4":-4,"0 - 5":-5,"0 - 6":-6,"0 - 7":-7,"0 - 8":-8,"0 - 9":-9,"1 - 0":1,"1 - 1":0,"1 - 2":-1,"1 - 3":-2,"1 - 4":-3,"1 - 5":-4,"1 - 6":-5,"1 - 7":-6,"1 - 8":-7,"1 - 9":-8,"2 - 0":2,"2 - 1":1,
        "2 - 2":0,"2 - 3":-1,"2 - 4":-2,"2 - 5":-3,"2 - 6":-4,"2 - 7":-5,"2 - 8":-6,"2 - 9":-7,"3 - 0":3,"3 - 1":2,"3 - 2":1,
        "3 - 3":0,"3 - 4":-1,"3 - 5":-2,"3 - 6":-3,"3 - 7":-4,"3 - 8":-5,"3 - 9":-6,"4 - 0":4,"4 - 1":3,"4 - 2":2,"4 - 3":1,"4 - 4":0,"4 - 5":-1,"4 - 6":-2,"4 - 7":-3,"4 - 8":-4,"4 - 9":-5,"5 - 0":5,"5 - 1":4,"5 - 2":3,"5 - 3":2,
        "5 - 4":1,"5 - 5":0,"5 - 6":-1,"5 - 7":-2,"5 - 8":-3,"5 - 9":-4,"6 - 0":6,"6 - 1":5,"6 - 2":4,"6 - 3":3,"6 - 4":2,"6 - 5":1,"6 - 6":0,"6 - 7":-1,"6 - 8":-2,"6 - 9":-3,"7 - 0":7,"7 - 1":6,"7 - 2":5,"7 - 3":4,"7 - 4":3,"7 - 5":2,"7 - 6":1,"7 - 7":0,"7 - 8":-1,
        "7 - 9":-2,"8 - 0":8,"8 - 1":7,"8 - 2":6,"8 - 3":5,"8 - 4":4,"8 - 5":3,"8 - 6":2,"8 - 7":1,"8 - 8":0,"8 - 9":-1,"9 - 0":9,"9 - 1":8,"9 - 2":7,"9 - 3":6,"9 - 4":5,"9 - 5":4,"9 - 6":3,"9 - 7":2,"9 - 8":1,"9 - 9":0,}
        # substract data

    # methods defining start here
    
    def add(self,num1,num2):  # addition function
        self.lenght = len(str(num1)) # lenght of num1 and num2
        self.lenght2 = len(str(num2))
        num1 = str(num1) # converting as string
        num2 = str(num2)
        
        for i in num1:  
            self.num1.append(i) # pushing data to stack
        for j in num2:
            
            self.num2.append(j)
        if self.lenght > self.lenght2:  # checking lenght > or not
            for i in range(1,self.lenght-self.lenght2+1):
                self.num2.insert(0,"0")

        if self.lenght >= self.lenght2:  # > = or not
           
                    for i in range(self.lenght):
                        
                        b,v = str(self.num1.pop()),str(self.num2.pop()) # pop data from stack
                       
                        self.expression_ = "{} + {}".format(b,v) # creating expression
                       
                    
                        
                        self.keys = self.table_add.keys()
                        for i in self.keys:
                            if i == self.expression_:   # matching expression
                                self.value = str(self.table_add[str(i)])
                              
                                if len(self.value) == 1: # checking lenght of result
                                        self.result.append(self.value)
                                        self.s = []  
                                        for i in self.result:
                                            self.s.append(i)

                                        for i in range(1,len(self.remainder)+1):

                                            data_ = str(self.result[-i])
                                            if len(str(data_)) == 2:

                                                    expression = "{} + {}".format(data_[1],self.remainder[-1])
                                                    self.keys = self.table_add.keys()
                                                    for j in self.keys:
                                                        if j == expression:
                                                            data_ = data_.replace(data_[1],str(self.table_add[j]))
                                                            self.result.pop()
                                                            self.result.append(data_)
                                                            self.remainder.pop()
                                                            print(self.result [::-1])


                                            elif len(str(data_)) == 1:

                                                expression = "{} + {}".format(data_,self.remainder[-1])
                                                self.keys = self.table_add.keys()
                                                for j in self.keys:
                                                    if j == expression:
                                                        self.result.insert(-i,self.table_add[j])
                                                        self.remainder.pop()
                                                        for g in self.result:
                                                            if g == data_:
                                                                self.result.pop()
                                                                





                                            else:
                                                pass            
                                            
                                if len(self.value) == 2:
                                        if len(self.num1) == 0:
                                            self.result.append(self.value)

                                        else:

                                            self.result.append(self.value[1])
                                            self.remainder.append(self.value[0])
                                
                                        self.s = []  
                                        for i in self.result:
                                            self.s.append(i)

                                        for i in range(1,len(self.remainder)):

                                            data_ = str(self.result[-i])
                                            if len(str(data_)) == 2:

                                                    expression = "{} + {}".format(data_[1],self.remainder[-1])
                                                    self.keys = self.table_add.keys()
                                                    for j in self.keys:
                                                        if j == expression:
                                                            data_ = data_.replace(data_[1],str(self.table_add[j]))
                                                            self.result.pop()
                                                            self.result.append(data_)
                                                            self.remainder.pop()
                                                            print(self.result [::-1])


                                            elif len(str(data_)) == 1:

                                                expression = "{} + {}".format(data_,self.remainder[-1])
                                                self.keys = self.table_add.keys()
                                                for j in self.keys:
                                                    if j == expression:
                                                        self.result.insert(-i,self.table_add[j])
                                                        self.remainder.pop()
                                                        for g in self.result:
                                                            if g == data_:
                                                                self.result.pop()
                                                                





                                            else:
                                                pass
       
        
                                             
        

        if len(self.remainder) == 1 or len(self.remainder) == 0: #remainder part
                            
                            if len(self.remainder) != 0:
                                expression = str(self.result[-1])
                                new = ""
                                for i in expression:
                                    new = new + i

                                sub_ex = "{} + {}".format(expression[1],self.remainder[0])
                                self.keys = self.table_add.keys()
                                for j in self.keys:
                                    if j == sub_ex:
                                        new = new.replace(new[1],str(self.table_add[j]))
                                        
                                        self.result.pop()
                                        self.result.append(new)
                            string_ = ""
                            for i in self.result[::-1]:          
                                       string_ = string_ + str(i)
                            return int(string_)             # addition of same lenght digit end here         
                                          
                        
        
    def sub(self,num1,num2): #substraction part
        if len(str(num1)) > len(str(num2)):
            
            for i in range(len(str(num1))+1):
                self.sub2.extend("0")
        self.num11 = str(num1)
        self.num22 = str(num2)


        for j in range(len(self.num11)):

            self.sub1.append(self.num11[j])

        for k in range(len(self.num22)):
            self.sub2.append(self.num22[k])

        
        for i in range(0,len(self.sub1)):
            a = self.sub1.pop()
            b = self.sub2.pop()
            
            if a < b:
                expression = "{} - {}".format(a,b)
                self.key = self.table_add.keys()
                for i in self.key:
                    if i[0] == b:
                        self.subval = str(self.table_add[i])
                        if len(self.subval) == 2:
                            if self.subval[1] == a:
                                    self.subres.append(i[-1])
                                    self.subrem.append(1)
                        
                if len(self.subrem) == 1:
                    ans = str(self.add(self.sub2.pop(),self.subrem.pop()))
                    if len(self.result) == 2:
                        if ans[1] == 0:
                            self.sub2.append(0)
                            ans2 = self.add(self.sub2[-1-1],1)
                            self.sub2.pop()
                            self.sub2.pop()
                            self.sub2.append(ans2)
                            self.sub2.append(0)

                    if len(str(self.result[-1])) == 1:
                        self.sub2.append(self.result[-1])
            if a >= b:
                
                    expression = "{} - {}".format(a,b)
                    self.key = self.sub_table.keys()
                    for i in self.key:
                        if i == expression:
                            self.subval = self.sub_table[i]
                            self.subres.append(self.subval)
        string_ = ""
        for i in self.subres[::-1]:          
             string_ = string_ + str(i)
        return int(string_)   # end of substraction

    def multiply(self,num1,num2):
        pass
    
    def div(self,num1,num2):
        if num2 == 0:
            return "invalid operation"

       


        

        
        
       



        




                                
                                    
                                        

if __name__ == "__main__":    
      
        m = myth()
        
        print(m.sub(9999999999998787665434677543456677,99999999976545342342177979797977434234234234242343414325435))
        