"""
word meaning in an MLP

Instead of representing each word as a one-hot ID, map each word to a dense vector in a continuous 
space, where similar words can have similar vectors.
Then use those vectors to predict the next word.
This lets the model generalize across similar contexts

distributional hypothesis: words in similar contexts get similar vectors


king-man+woman=queen

Consistent offset directions: show that 
queen - king ≈ woman - man ≈ aunt - uncle. 
The “gender direction” as a single vector is a striking visual.

"""