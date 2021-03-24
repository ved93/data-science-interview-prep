


### Fraud Prediction
There are many approaches to determining whether a particular transaction is fraudulent. From rule based systems to machine learning models — each method tends to work best under certain conditions. Successful anti-fraud systems should reap the benefits of all the approaches and utilize them where they fit the problem best.  
We can start with connection analysis using txn analysis. Each transaction can be described by a set of attributes.The processed txn shares an IP address, email address and some cookies with several other successfull txn.In short, it’s all about connecting transactions using some attribute as a matching key. This approach, although simple in principle, provides valuable context. After extracting the network’s features, we can then feed them to rule based systems or ML models  
it’s quite rare for people to possess a great number of credit cards, this type of network might be an example of carding fraud. In such attacks, fraudsters use stolen credit card credentials to perform numerous transactions. We can distinguish between normal traffic and carding patterns (few people, numerous cards and transactions) easily when having data structured as a network. After querying our graph and encountering a risky pattern, we can add suspicious attribute values to blacklists.   
there are no hard rules about what is and what is not fraudulent behavior. If we can see multiple transactions coming out of a common IP address it can mean a fraud attack, but it can also mean employees using their corporate, proxied network to make purchases. It’s important to take as many factors in as possible — missing out on some may cause serious distortions in the way we perceive the data through our networks. A good example of a crucial factor is time — someone making a 10th transaction on the same day and cleaning browser cookies after each one will look exactly the same as a legitimate user making a 10th purchase in the same year, whose cookies naturally expire between consequent transactions. Context is everything.
Summary:
how connection analysis is used in fraud detection and what are the associated benefits & challenges
how to interpret networks in the context of catching fraud
how transactions’ attributes are used to organize data into networks
how to implement attribute matching in Python’s Networkx library

   


### Malicious/Fishing Prediction    