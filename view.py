import pickle

file = "classes.pkl"
fileobj = open(file, 'rb')
words = pickle.load(fileobj)
print(words)