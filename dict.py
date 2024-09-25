#Dictionary:

#syntax:dictionary={key1:value1,key2:value2,key3:value3,-----}

# EXAMPLE:-
#d={"name":"vamsi","age":21,"gender":"male","stream":"cse"}
# print(d)   
# print(len(d))                                                             # 4 
# # print(type(d))                                                          # <class 'dict'>
# d["name"]="karthick"
# print(d)                                                                  # {'name': 'karthick', 'age': 25, 'gender': 'male', 'stream': 'cse'}
#print(d["name"]) # searchung the particulatr value                         # vamsi
#print(d["age"])                                                            # 21

# creating empty dict:
# d={ }
# d1=["age"]="21"           ------------------>>>>>>>>> doubt
# print(d1)

#Built in functions:
#d={1:10,2:20,3:30,4:40,5:50,6:60,7:70}

#1.keys():-
#syntax:dict.keys()----list
# print(d)
# res=d.keys()                                  #dict_keys([1, 2, 3, 4, 5, 6, 7])
# print(res)


#2.values():-
# syntax:dict.values()
# print(d)
# res=d.values()                                #dict_values([10, 20, 30, 40, 50, 60, 70])
# print(res)

#3.items():-
# syntax:dict.items()
# print(d)
# res=d.items()                                   #dict_items([(1, 10), (2, 20), (3, 30), (4, 40), (5, 50), (6, 60), (7, 70)])
# print(res)

#4.copy():-
#syntax:dict.copy()
#print(d)
# res=d.copy()                                    # {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60, 7: 70}
#print(res)

#5.clear():-
#syntax:dict.clear()
# print(d)
# d.clear()                                       #{}
# print(d)

#6.pop():-
#syntax:dict.pop(key)-->any
#print(d)
#res=d.pop(2)                                 
#print(res)                                     #20
#res1=d.pop(4)                                 
# print(res1)                                   #40
#print(d)                                       #{1: 10, 3: 30, 5: 50, 6: 60, 7: 70}

#d={}
#res4=d.pop(2)
# print(res4)   #KeyError: 2

#7.popitem():-
#syntax:dict.popitem()--->tuple
# print(d)
# res=d.popitem()    # removes last value  like List
# print(res)                                    #(7, 70)
# print(d)                                      #{1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}


#8.get():-
#syntax:dict.get(key)-------->Any
# print(d)
# res=d.get(2)
# print(res)                                     #20
# print(d) 
# res1=d.get(8)                                  #None
# print(res1)
# res2=d.get(8,"love you")
# print(res2)                                  #love you

#9.update():-
#syntax=dict.update(dict)
# print(d)                                       #{1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60, 7: 70}
# d.update({1:1000,2:2000})
# print(d)                                       #{1: 1000, 2: 2000, 3: 30, 4: 40, 5: 50, 6: 60, 7: 70}

#10.set default():-
#syntax=dict.set default(key,value)
# print(d)
# res=d.setdefault(1,200)                          
# res1=d.setdefault(10,100)                        
# print(res)                                       #10
# print(res1)                                      #100
# print(d)                                         #{1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60, 7: 70, 10: 100}


#11.fromkey():-
#syntax=dict.from keys(literable,value)----->dict
l=[1,2,3,4,5,6,7]
# res={}.fromkeys(l)
# print(res)                                  #{1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None}
# res1={}.fromkeys(l,"krishna")
# print(res1)                                 #{1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None}
# res2={}.fromkeys("abcd")
# # print(res2)                               #{'a': None, 'b': None, 'c': None, 'd': None}
# res3={}.fromkeys(l,{100,200})
# print(res3)                                 # {1: {200, 100}, 2: {200, 100}, 3: {200, 100}, 4: {200, 100}, 5: {200, 100}, 6: {200, 100}, 7: {200, 100}}
# res4={}.fromkeys(l,[10,20,30])
# print(res4)                                 #{1: [10, 20, 30], 2: [10, 20, 30], 3: [10, 20, 30], 4: [10, 20, 30], 5: [10, 20, 30], 6: [10, 20, 30], 7: [10, 20, 30]}
# res5={}.fromkeys(l,(1,2,3))
# print(res5)                                 #{1: (1, 2, 3), 2: (1, 2, 3), 3: (1, 2, 3), 4: (1, 2, 3), 5: (1, 2, 3), 6: (1, 2, 3), 7: (1, 2, 3)}


# Dictionary concatenation and dictionary repation not possiblemit became type error::::
