
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

Q.Difference between convex and non-convex cost function; what does it mean when a cost function is non-convex?(Amazon)  

Q. Describe the criterion for a particular model selection. Why is dimension reduction important?

Q.What are the assumptions for logistic and linear regression?

Q.If you can build a perfect (100% accuracy) classification model to predict some customer behaviour, what will be the problem in application?  
A. There can be multiple scenarios  
1. target-rate < 1% : If its fraud application. Then model might of no use.
2. Overfitting: It's highly difficult to build such model. So if its not validated well then it might not do well on test data

Q. Compare Lasso and Ridge Regression. (Amazon) 
Q. What’s the difference between MLE and MAP inference?(Amazon)  
Q. When users are navigating through the Amazon website, they are performing several actions. What is the best way to model if their next action would be a purchase?  
Q.How does K-means work? What kind of distance metric would you choose? What if different features have different dynamic range?
Q. What are some benefits and drawbacks of discriminative and generative models?  
Q. Difference between convex and non-convex cost function ; what does it mean when a cost function is non-convex?  
A. Convex: global optimum no local optimum

Q. why should we retrain the model after model selection / model evaluation?   
In a learning curve, the performance of a model both on the training and validation set is plotted as a function of the training set size. Fig. 1 shows a typical learning curve: The training score (performance on the training set) decreases with increasing training set size while the validation score increases at the same time. High training score and low validation score at the same time indicates that the model has overfit the data, i.e., has adapted too well to the specific training set samples. As the training set increases, overfitting decreases, and the validation score increases.
Especially for data-hungry machine learning models, the learning curve might not yet have reached a plateau at the given training set size, which means the generalization error might still decrease when providing more data to the model. Hence, it seems reasonable to increase the training set (by adding the validation set) before estimating the generalization error on the test set, and to further take advantage of the test set data for model fitting before shipping the model. Whether or not this strategy is needed depends strongly on the slope of the learning curve at the initial training set size.

Q. Bias Variance in Learning Curve  
A. Learning curves further allow to easily illustrate the concept of (statistical) bias and variance. Bias in this context refers to erroneous (e.g. simplifying) model assumptions, which can cause the model to underfit the data. A high-bias model does not adequately capture the structure present in the data. Variance on the other hand quantifies how much the model varies as we change the training data. A high-variance model is very sensitive to small fluctuations in the training data, which can cause the model to overfit. The amount of bias and variance can be estimated using learning curves: A model exhibits high variance, but low bias if the training score plateaus at a high level while the validation score at a low level, i.e., if there is a large gap between training and validation score. A model with low variance but high bias, in contrast, is a model where both training and validation score are low, but similar. Very simple models are high-bias, low-variance while with increasing model complexity they become low-bias, high-variance.

Q. Why is logistic regression considered a linear model?  
A. Logistic regression is considered linear because the decision boundary of a logistic model is linear in the feature space. Logistic regression is considered a generalized linear model because the outcome always depends on the sum of the inputs and parameters. Or in other words, the output cannot depend on the product (or quotient, etc.) of its parameters!  
Logistic regression is a *generalized linear model*. Generalized linear models are, despite their name, not generally considered linear models. They have a linear component, but the model itself is nonlinear due to the nonlinearity introduced by the link function.

Q. You have a dataset of a million example digits, what are some desirable qualities due to which you would pick a KNN classifier for digit recognition ?  
A. Lavanya.The following are some features of the KNN classifier The KNN classifier is simple to implement. Prediction could be relatively inefficient with the KNN classifier. While there is no training effort with the KNN algorithm, prediction involves scanning the entire training data to find the K-nearest neighbours to aggregate their value. With efficient implementation, such as a KD-tree the prediction time could be improved. With a high value of K, the decision boundary becomes smoother while the decision boundary is more noisy with a low value of K. The KNN-algorithm is non-parametric and can fit highly non-linear decision boundaries.


