
What are the differences between GloVe, word2vec and tf-idf?  
Glove and word2vec are models that learn from vectors of words by taking into consideration their occurrence and co-occurrence information. While word2vec can be seen as a model that improves its ability to predict [ (target word | context words), and GloVe is modeled to do dimensionality reduction. This reduction is on the co-occurrence counts matrix [minimizing a loss - the reconstruction loss]. Reconstruction loss tries to find the lower-dimensional representations.

TF-IDF is a way to judge the topic of an article. This is done by the kind of words it contains. Here words are given weight so it measures relevance, not frequency.

Wordcounts are replaced with TF-IDF scores throughout dataset.

Word2vec produces one vector per word, whereas tf-idf produces a score. Word2vec is great for going deeper into the documents we have and helps in identifying content and subsets of content. Its vectors represent each word’s context. (i.e the n-gram of which it is a part)   


Q. How is GloVe different from word2vec?
A. https://www.quora.com/How-is-GloVe-different-from-word2vec
