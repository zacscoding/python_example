import os
import pickle


def delete_file(name):
    if os.path.exists(name):
        os.remove(name)


# remove file if exist
file_name = 'test.txt'

delete_file(file_name)

# serialize data dictionary
f = open(file_name, 'wb')
data = {1: 'python', 'key2': 'you need'}
pickle.dump(data, f)
f.close()

# deserialize data dictionary
f = open(file_name, 'rb')
read_data = pickle.load(f)
print(data)
print(data[1])
print(data['key2'])
f.close()

delete_file(file_name)
