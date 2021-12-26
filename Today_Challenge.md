
Q.1 ABC is an e-commerce company. It gives expected delivery date for products you shop. It is found that if delivery date is long then there is some drop in conversion and RTO also starts to happen and if its too short then conversion rate increases but you miss the product delivery date more often. Now you want to increase the conversion rate and you are data scientist, how would you approach it? Which metric should i use for this task?

Q.2 ABC is an airline/hotel company. Conversion depends ranking of hotels you show to the customer. So how would you rank the hotels? How to remove ranking bias as well?
 

Q.3 How to reduce cancellation in ecommerce/airline/grocery etc?

Q.4 How to reduce RTO ?

Q.5 How to reduce total loss occurred on RTO ?

Q.6 Conv rate 30% and Revenue per conversion is 2 dollars, cost per click is 2 cents. Should I run the campaign, if yes whats my profit? At what cost we can keep running the campaign ?

Q.7 ABC is an airline company. There are psuedo companies which continuosly hit your website to get the fare using bots. This results into bad customer experience as there will be false traffic and actual user will suffer. We also set dynamic price on the basis of traffic so its important to detect bot on the website. How would you detect a bot?

Q.8 ABC is a OEM company. Their customers are other companies that distribute OEMs to the end users. These customer companies make their OEms purchases on basis of their demand. So some customers purchases once every month and some purchases once or twice a year. So now the problem is ABC OEMs wants to know if churn is happening and if so how they can prevent it? How would you predict churn?

<<<<<<< HEAD
Q. Design a parking system for airport, there are fixed no of slots for each type of vehicle and each # vehicle has a type and number. The amount charged is based on price per type per min. So when a # vehicle enters, it plate number is noted and if there is an available slot for that vehicle its # allowed to be parked.?
=======
>>>>>>> 85a5dac2ea4b513610a757191753022a50118e93





<<<<<<< HEAD
# print(random.randint(1,200))
l = {}
last_end = 0
loop = 0

num_list=list(range(0,200))

print(random.choices(num_list,k=2))

last_end,last_str = 0,0
m =0
for i in range(1,101):
  # endp=random.randint(1,200)
  # strp=random.randint(1,200)
  ends=random.sample(num_list,k=2)
  

  print(ends)
  num_list.remove(ends[0])
  num_list.remove(ends[1])

  if last_str in ends and last_end in ends:
    print('was here')
    loop = loop+1

  elif last_str in ends or last_end in ends:
    if   last_str in ends:
      l[m]=[last_str,last_end]





  if ends[0] % 2 == 0:
    last_str = ends[0]-1
  else:
    last_str = ends[0]+1


  if ends[1] % 2 == 0:
    last_end = ends[1]-1
  else:
    last_end = ends[1]+1


  l[m]=[last_str,last_end]
  m= m+1
    
    

  # last_str = ends[0]
  # last_end = ends[1]

print(loop)

```


Q. 


Q. Check permutation of string can become a palindrome?  
Q. 

'''
Given a sorted integer array nums, where the range of elements are in the inclusive range [lower, upper]
 return its missing ranges.

    Example:

    Input: nums = [0, 1, 3, 50, 75], lower = 0 and upper = 99,
    Output: ["2", "4->49", "51->74", "76->99"]
'''



def append_elem(lst, out):
  # print(lst)
  if len(lst) == 0:
    pass
  elif len(lst) == 1:
      out.append(lst[0])
  else:
    out.append('{0}->{1}'.format(min(lst), max(lst)))
    
  # print(out)
  return out


def missing_num_2(a, l, u):
  output = []
  tmp_lst = []
  
  for i in range(l, u+1):
    # print(i)
    if i not in a:
      # print(i)
      tmp_lst.append(i)
    else:
      # print(tmp_lst)
      output = append_elem(tmp_lst, output)
      tmp_lst = []
        
  if len(tmp_lst) != 0:
    output = append_elem(tmp_lst, output)
    
  return output



print(missing_num_2([0, 1, 3, 50, 75],0,99) )   

'''
def missing_num(a,l,u):
  b = []
  for i in range(l,len(a)):
    if a[i] == l:
      l=l+1
      continue
    else:
      
          #     if i+1 == len(a):
          # r='{}->{}'.format(l,a[i+1]-1)
          # # print(r)
          # b.append(r)
          
          # return b
      
      if a[i+1] != (l+1):
        r='{}->{}'.format(l,a[i+1]-1)
        # print(r)
        b.append(r)
        
      else:  
        b.append(str(l))
      l = l+1
  
  return b
       

print(missing_num([0, 1, 3, 50, 75],0,99) )      '''
=======
>>>>>>> 85a5dac2ea4b513610a757191753022a50118e93



### Solutions

A.1 There are two parts of the problem. 1. Optimizing the delivery time 2. Provide accurate estimate of delivery time. 3rd thing to do predicting shipping time and delivery date separately.
1. We can leverage ML to predict future orders of items so we can make them avaliable to the nearest hubs. We can also do inventory predictions as well.
2. Predict delivery date. Usually product decideds delivery date on the basis of some rules or based on intution. In Reality, it is pretty dynamic in nature and it also depends load and item availability in nearest hub . i.e. In sale there are huge orders to be delivered so to get better estimate ML based approach is needed.  
It requires the consideration of several factors such as inventory levels, region, holidays, expected future demand, etc. These factors along with ample historical data make this problem a perfect use case for applying machine learning. 
The vast majority of machine learning algorithms are constructed with a symmetric cost function optimization. In this case, the cost of either direction of the error is the same- an error of being X days late or X days early is the same. In our case, there is an error perceived to be costlier: we would rather deliver the order early than be late. We encoded this business logic in the machine learning models by creating a custom asymmetric cost function that penalizes late orders more than early orders.



A.4 Predict RTO at the time of placing a request and can depriortize. 

