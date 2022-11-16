import pickle

listexample = ["pineapple", "Atlas", ("shaft", "blade"), 1150]
pickle_open = open("saveme.dat", "wb")
print(listexample)
print(pickle_open)
pickle.dump(listexample, pickle_open)

pickle_open.close()

# Never, ever manually edit any file which is written in the bitmode "bw".
# This breaks the file completely beyond any hope for repairing it.

pickle_open2 =open("saveme.dat","rb")
justread=pickle.load(pickle_open2)
print("Read as:",justread)
print(justread[2])
print(justread[3])
pickle_open2.close()

# basically pickle is to make normal things into .dat file
# and can only read them using pickle load
