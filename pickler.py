from os import read
import pickle
with open('classes_convertor.txt') as f:
    dict = f.readlines()

file = open('classes.pkl', 'wb')
pickle.dump(dict, file)
file.close()

#and to read it again
file = open('classes.pkl', 'rb')
dict = pickle.load(file)