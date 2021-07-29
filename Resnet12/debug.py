import pickle


def load_data(file):
    try:
        with open(file, 'rb') as fo:
            data = pickle.load(fo)
        return data
    except:
        with open(file, 'rb') as f:
            u = pickle._Unpickler(f)
            u.encoding = 'latin1'
            data = u.load()
        return data


train = load_data('cifar/CIFAR-FS/CIFAR_FS_train.pickle')['data']
test = load_data('cifar/CIFAR-FS/CIFAR_FS_test.pickle')['data']
val = load_data('cifar/CIFAR-FS/CIFAR_FS_val.pickle')['data']
