import pickle
import sys

infile = open("words.pkl",'rb')
new_dict = pickle.load(infile)
infile.close()
print(new_dict)
print(type(new_dict))

sys.stdout = open("words_convertor.txt", "w")

print(new_dict)

sys.stdout.close()