
Q. Assume we have a classifier that produces a score between 0 and 1 for the probability of a particular loan application being fraudulent. In this scenario: a) what are false positives, b) what are false negatives, and c) what are the trade-offs between them in terms of dollars and how should the model be weighted accordingly?

A. FP: False predicted fraudulent
FN: Falsely predicted Non-fraud
Here, Recall is very important metric here. So model should be weighted for FN. FN are the cases where fraud actually happened but model didn't detect and Bank ended up losing money. So we should choose a model where we can minimise FN at the expense of FP.

---
Q. Assume we have some credit model, which has accurately calibrated (up to some error) score of how credit-worthy any individual person is. For example, if the model’s estimate is 92% then we can assume the actual score is between 91 and 93. If we take 92 as a score cutoff and deem everyone above that score as credit-worthy, are we over-estimating or underestimating the actual population’s credit score?

A. 

---
Q. What is user churn and how can you build a model to predict whether a user will churn? What features would you include in the model and how do you assess importance?

---
Q. Assume we have a classifier that produces a score between 0 and 1 for the probability of a particular loan application behind a fraud. Say that for each application’s score, we take the square root of that score. How would the ROC curve change? If it doesn’t change, what kinds of functions would change the curve?

A. ROC is a ranking metrics so it wont change if you make same transformation for every score.

---

