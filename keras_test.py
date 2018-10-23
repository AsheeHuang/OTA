from keras.models import Sequential
from keras.layers import Dense, Activation
import  matplotlib.pyplot as plt
import pandas
from random import sample,randint
from sklearn.model_selection import train_test_split
def data_features(path) :
    features = []

    data = pandas.read_csv(path+'.csv')

    features.append(len(data))
    des = data.describe()
    for attr in des :
        features.append(des[attr]['mean'])
        features.append(des[attr]['std'])
        features.append(des[attr]['min'])
        features.append(des[attr]['25%'])
        features.append(des[attr]['50%'])
        features.append(des[attr]['75%'])
        features.append(des[attr]['max'])
    return features

def get_metadata(data) :
    x = []
    for i in range(len(data)) :
        # x.append(data_features(data['data'][i]))
        x.append(data_features(data['data'].iloc[i]))
    x = pandas.DataFrame(x)
    return x
if __name__ == "__main__" :
    data = pandas.read_csv("labeled_data.csv")
    paths = data['data']

    train_y,test_y = train_test_split(data,test_size=0.3)
    train_x = get_metadata(train_y)
    test_x = get_metadata(test_y)

    train_y = train_y.iloc[:,1:5]
    test_y = test_y.iloc[:,1:5]
    # print(test_x,test_y)
    # print(train_y)

    model = Sequential()

    model.add(Dense(36,activation = 'relu'))
    model.add(Dense(50,activation = 'relu'))
    model.add(Dense(4))

    model.compile(optimizer = "adam", loss = "mean_absolute_error")
    # print(model.summary())
    results = model.fit(train_x.values,train_y.values,
                        epochs = 2000,
                        batch_size = 10,
                        validation_data=(test_x.values,test_y.values))
    plt.plot(results.history['val_loss'][5:])
    plt.plot(results.history['loss'][5:])
    # print(results.history)
    plt.show()

    for i in range(20) :
        s = randint(0,len(test_x))
        print(model.predict(test_x[s:s+1]),"  ",test_y[s:s+1].values)