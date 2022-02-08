#%%

 from itertools import count
from operator import index


print("Hello world!")


#%%
# Question 1: Create a Markdown cell with the followings:
# Two paragraphs about yourself. In one of the paragraphs, give a hyperlink of a website 
# that you want us to see. Can be about yourself, or something you like.

#%%
# My name is Emily, I am 28 years old, my pronouns are she/her, and I'm studying bioinformatics amd molecular medicine at GWU. 
# I received two Bachelor of Science degrees at Virginia Commonwealth University; one in Biology with a minor in chemistry, and the other in Forensic Science.
# I have two big labradors that I love very much. They're my entire heart. They are the best of friends and the funniest looking pair when they stand next to eachother, because despite the fact that they're the same weight and breed, one is tall, muscular and lean, and the other is all belly rolls and stubby little legs.  
# They both came into my life very serendipitously. I never intended to get a dog in college, especially not two 60 pound, high-energy dogs in a small studio apartment in downtown Richmond Virginia, but I feel so lucky to have them.
# I actually have their names tattooed on my arm because that is how much they mean to me. The tattoo is in Tengwar which is the colloquial elvish language used in Lord of the Rings, which I translated using http://tecendil.com  
# 
# I also love to travel and enjoy the outdoors whenever possible. I love snowboarding, surfing, swimming, wakeboarding, and kayaking.
# To relax, I like to read and paint. My little sister and I love to watch Law and Order and keep up with the newest season of RuPaul's drag race together. 
# I listen to audiobooks on my commute, while doing little tasks in the lab, and completing chores at home to make everything a little more interesting. 
# My audble account is full of non-fiction autobiographies, and journalist accounts of their undercover cult investigations. Currently, I'm listening to an autobiography of a woman who spent her life as a texas hold 'em dealer in the most exclusive, undergound celebrity gambling rings who found herself in the middle of an FBI mafia investigation.
# Like I said, this is a true story which I think makes it even cooler. Let me know if you guys wanna talk about conspiracies, dark celebrity gossip, or just trade dog pictures because I'm available. 



#%%
# Question 2: Create
# a list of all the class titles that you are planning to take in the data science program. 
# Have at least 6 classes, even if you are not a DS major
# Then print out the last entry in your list.

myclasslist = ["DATS6103", "BIOC6222", "BIOC6237", "GENO8232", 'BISC6210', "BIOC6998"]
print(myclasslist[5])

#%%
# Question 3: After you completed question 2, you feel Intro to data mining is too stupid, so you are going 
# to replace it with Intro to Coal mining. Do that in python here.
myclasslist = ["DATS6103", "BIOC6222", "BIOC6237", "GENO8232", 'BISC6210', "BIOC6998"]
myclasslist.remove("DATS6103")
myclasslist.append("Intro to coal mining")
print(myclasslist)

#%%
# Question 4: Before you go see your acadmic advisor, you are 
# asked to create a python dictionary of the classes you plan to take, 
# with the course number as key. Please do that. Don't forget that your advisor 
# probably doesn't like coal. And that coal mining class doesn't even have a 
# course number.

classdictionary = {6103:"intro to data science", 6222:"Proteomics and medicine", 6237:"proteomics and biomarkers", 8232:"computational biology and genomics", 6210:"methods of study of evolution", 6998:"thesis"}

#%%
# Question 5: print out and show your advisor how many 
# classes (print out the number, not the list/dictionary) you plan 
# to take.
classdictionary = {6103:"intro to data science", 6222:"Proteomics and medicine", 6237:"proteomics and biomarkers", 8232:"computational biology and genomics", 6210:"methods of study of evolution", 6998:"thesis"}
print(len(classdictionary))

#%%
# Question 6: Using loops 
# Goal: print out the list of days (31) in Jan 2021 like this
# Sat - 2022/1/1
# Sun - 2022/1/2
# Mon - 2022/1/3
# Tue - 2022/1/4
# Wed - 2022/1/5
# Thu - 2022/1/6
# Fri - 2022/1/7
# Sat - 2022/1/8
# Sun - 2022/1/9
# Mon - 2022/1/10
# Tue - 2022/1/11
# Wed - 2022/1/12
# Thu - 2022/1/13
# ...
# You might find something like this useful, especially if you use the remainder property x%7

listweekdays = ['Sat','Sun','Mon','Tue','Wed','Thu','Fri']
month = listweekdays*4 + listweekdays[0:3]

days = [] #list from 1 to 31 as integers
for i in range(1,32):
  days.append(i)

for val in range(len(month)):
  print(month[val] + " - 2022/1/" + str(days[val]))
  

#%%
# or try this for dictionary, using .items() to get the pairs
print("\nalternative method to loop thru key, val in dictionary:")
# adictionary.items() # creates a object type of dict_items, which can be looped thru as key/value pairs   

calendar = {'Sat':[1,8,15,22,29],'Sun':[2,9,16,23,30],'Mon':[3,10,17,24,31],'Tue':[4,11,18,25],'Wed':[5,12,19,26],'Thu':[6,13,20,27],'Fri':[7,14,21,28]}
for key, val in calendar.items():
  print(key,val)


# %%[markdown]
# # Additional Exercise: 
# Choose three of the five exercises below to complete.
#%%
# =================================================================
# Class_Ex1: 
# Write python codes that converts seconds, say 257364 seconds,  to 
# (x Hour, x min, x seconds)
# ----------------------------------------------------------------
total_seconds = 257364
seconds = int(total_seconds)
mins = int(seconds/60)
hours = int(mins)/60

print(str(int(hours)) + " Hours", str(int(mins))+ " minutes", str(int(seconds)) + " seconds")





#%%
# =================================================================
# Class_Ex2: 
# Write a python codes to print all the different arrangements of the
# letters A, B, and C. Each string printed is a permutation of ABC.
# Hint: one way is to create three nested loops.
# ----------------------------------------------------------------






#%%
# =================================================================
# Class_Ex3: 
# Write a python codes to print all the different arrangements of the
# letters A, B, C and D. Each string printed is a permutation of ABCD.
# ----------------------------------------------------------------





#%%
# =================================================================
# Class_Ex4: 
# Suppose we wish to draw a triangular tree, and its height is provided 
# by the user, like this, for a height of 5:
#      *
#     ***
#    *****
#   *******
#  *********
# ----------------------------------------------------------------



#%%
# =================================================================
# Class_Ex5: 
# Write python codes to print prime numbers up to a specified 
# values, say up to 200.
# ----------------------------------------------------------------
lower= 0
upper =200
# only divisible by itself and 1
# if results have remainder its not prime 

for g in range(lower,upper+1):
  if g>1:
    for f in range(2,g):
      # another range for loop from value of 2 to to value from the first loop g 
      # creates a second range of numbers to divide g by possible factors (possible factors = positive integers within range f starting from 2 as identified)      
      # we are skipping 1 and 0 in this case
      if(g % f)==0:
        # if g divided by f has no remainder then it is NOT prime
        break
    else:
      print(g)
      # if nothing is divisible in range f produces remainder of zero then g is prime 

  
#%%
print(11/0)

