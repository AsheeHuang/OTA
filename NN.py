import tensorflow as tf
import pandas
from random import sample

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
def next_batch(data ,n = 100) :
    sel = sample([i for i in range(len(data))],n)

    x = []
    y_ = []
    for s in sel :
        # print(s)
        x.append(data_features(data['data'][s]))
        y_.append(data.iloc[s,1:5])
    return x,y_


if __name__ == "__main__" :
    data = pandas.read_csv("labeled_data.csv")
    paths = data['data']
    train_data = data[0:200]
    test_data = data[200:301].reset_index(drop=True)



    # features = data_features(paths[0])
    # num_feature = len(features)
    # print(num_feature)
    x = tf.placeholder(tf.float32,[None,36]) #36 is number of features

    W = tf.Variable(tf.zeros([36,4]))
    b = tf.Variable(tf.zeros([4]))

    y = tf.nn.softmax(tf.matmul(x, W) + b)  # prediction
    y_ = tf.placeholder(tf.float32, [None, 4])  # actual

    entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y_,logits=y))

    train_step = tf.train.GradientDescentOptimizer(0.5).minimize(entropy)

    sess = tf.InteractiveSession()
    tf.global_variables_initializer().run()



    for i in range(20) :
        batch_x,batch_y = next_batch(train_data,1)
        sess.run(train_step, feed_dict={x: batch_x, y_: batch_y})
        print(b.eval())
        # print(W.value(), b.value())
        # correct_prediction = tf.equal(tf.argmax(y, 1),tf.argmax(y_, 1))
        # print(type(correct_prediction))

        mse = tf.losses.softmax_cross_entropy(y,y_)
        mse_loss = tf.reduce_sum(mse)
        # correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
        # accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
        test_data_x , test_data_y = next_batch(test_data,50)



        print("Step " + str(i)  , sess.run(mse_loss, feed_dict={x: test_data_x, y_: test_data_y}))



