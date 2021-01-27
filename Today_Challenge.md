

1. Let the sample space be the set of all positive integers. Is it possible to have a “uniform" probability law, that is, a probability law that assigns the same probability  𝑐  to each positive integer?
2. Let the sample space be the two-dimensional plane. For any real number  𝑥 , let  𝐴𝑥  be the subset of the plane that consists of all points of the vertical line through the point  (𝑥,0) , i.e.,  𝐴𝑥={(𝑥,𝑦):𝑦∈Re} .

a) Do the axioms of probability theory imply that the probability of the union of the sets  𝐴𝑥  (which is the whole plane) is equal to the sum of the probabilities  𝐏(𝐴𝑥) ?
b)  Do the axioms of probability theory imply that

𝐏(𝐴1∪𝐴2∪⋯)=∑𝑥=1∞𝐏(𝐴𝑥)?
(In other words, we consider only those lines for which the  𝑥  coordinate is a positive integer.)
 
3. Mary and Tom park their cars in an empty parking lot with  n≥2  consecutive parking spaces (i.e,  n  spaces in a row, where only one car fits in each space). Mary and Tom pick parking spaces at random; of course, they must each choose a different space. (All pairs of distinct parking spaces are equally likely.) What is the probability that there is at most one empty parking space between them? 
4. Romeo and Juliet have a date at a given time, and each will arrive at the meeting place with a delay between 0 and 1 hour, with all pairs of delays being “equally likely," that is, according to a uniform probability law on the unit square. The first to arrive will wait for 15 minutes and will leave if the other has not arrived. What is the probability that they will meet? Instead of calculating given that they arrive within
15 minutes of each other, what is the probability that
they'll meet, let's say that Romeo really wants to meet up
with Juliet, and he wants to assure himself a least, say, a
90% chance of meeting Juliet.
Then you can ask, if he wants to have at least a 90% chance
of meeting her, how long should he be willing to wait?
5. Alice and Bob each choose at random a real number between zero and one. We assume that the pair of numbers is chosen according to the uniform probability law on the unit square, so that the probability of an event is equal to its area.
We define the following events:

 	 A 	 = 	 {The magnitude of the difference (for any two real numbers x and y, the value |x−y|) of the two numbers is greater than 1/3} 	 	 
 	 B 	 = 	 {At least one of the numbers is greater than 1/4} 	 	 
 	 C 	 = 	 {The sum of the two numbers is 1} 	 	 
 	 D 	 = 	 {Alice's number is greater than 1/4}





### Solutions
1. Suppose that  𝑐=0 . Then, by countable additivity,
1=𝐏(Ω)=𝐏({1}∪{2}∪{3}⋯)=𝐏({1})+𝐏({2})+𝐏({3})+⋯=0+0+0+⋯=0, 
which is a contradiction.
Suppose that  𝑐>0 . Then, there exists an integer  𝑘  such that  𝑘𝑐>1 . By additivity,
𝐏({1,2,…,𝑘})=𝑘𝑐>1, 
which contradicts the normalization axiom.

2. a) The collection of sets  𝐴𝑥  is not countable because the set of real numbers is not countable (i.e., cannot be arranged in a sequence), and so the additivity axiom does not apply.

b) The countable additivity axiom applies because we are dealing with a sequence (in particular, a countable collection) of disjoint events.

3. Part of EDX probability problems unit 1. The sample space is  Ω={(i,j):i≠j,1≤i,j≤n} , where outcome  (i,j)  indicates that Mary and Tom parked in slots  i  and  j , respectively. We apply the discrete uniform probability law to find the required probability. We are interested in the probability of the event

A={(i,j)∈Ω:|i−j|≤2}. 
 
We first find the cardinality of  Ω . There are  n2  pairs  (i,j) , but since the set  Ω  excludes outcomes of the form  (i,i) , the cardinality of  Ω  is  n2−n=n(n−1) .
If n≥3, event A consists of the four lines indicated in the figure above and contains 2(n−1)+2(n−2)=4n−6 elements. If n=2, event A contains exactly 2 elements, namely, (1,2) and (2,1), which agrees with the formula 4(2)−6=2. Therefore,

P(A)=4n−6/n(n−1).

4. Discrete = 13/25 Continuous Case = 7/16
5. P(A)=2⋅(2/3)22=4/9.
6. 