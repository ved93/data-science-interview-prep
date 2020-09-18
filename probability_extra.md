

1. Let the sample space be the set of all positive integers. Is it possible to have a “uniform" probability law, that is, a probability law that assigns the same probability  𝑐  to each positive integer?
2. Let the sample space be the two-dimensional plane. For any real number  𝑥 , let  𝐴𝑥  be the subset of the plane that consists of all points of the vertical line through the point  (𝑥,0) , i.e.,  𝐴𝑥={(𝑥,𝑦):𝑦∈Re} .

a) Do the axioms of probability theory imply that the probability of the union of the sets  𝐴𝑥  (which is the whole plane) is equal to the sum of the probabilities  𝐏(𝐴𝑥) ?
b)  Do the axioms of probability theory imply that

𝐏(𝐴1∪𝐴2∪⋯)=∑𝑥=1∞𝐏(𝐴𝑥)?
(In other words, we consider only those lines for which the  𝑥  coordinate is a positive integer.)















### Solutions
1. Suppose that  𝑐=0 . Then, by countable additivity,
1=𝐏(Ω)=𝐏({1}∪{2}∪{3}⋯)=𝐏({1})+𝐏({2})+𝐏({3})+⋯=0+0+0+⋯=0, 
which is a contradiction.
Suppose that  𝑐>0 . Then, there exists an integer  𝑘  such that  𝑘𝑐>1 . By additivity,
𝐏({1,2,…,𝑘})=𝑘𝑐>1, 
which contradicts the normalization axiom.

2. a) The collection of sets  𝐴𝑥  is not countable because the set of real numbers is not countable (i.e., cannot be arranged in a sequence), and so the additivity axiom does not apply.

b) The countable additivity axiom applies because we are dealing with a sequence (in particular, a countable collection) of disjoint events.