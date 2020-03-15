# Homework 11:

The goal of this homework is to land the lunar lander between the pictured goal post using reinforcement style learning. In `old_files/README.md`, we can see the run instructions and recommendations on how to potentially achieve our goal better.  Below are the answers to the questions that are also specified and serves as a guide to the changes that were made.

** To see videos of the latest change, please go to http://s3.us-east.cloud-object-storage.appdomain.cloud/tennisonyu-w251-hw11 **

## 1. What parameters did you change?

**Change 1:**
I changed the inference and update process.

**Change 2:**
I changed the optimizer.

**Change 3:**
I changed the overall neural network architecture. More specifically the number of layers and nodes.

**Change 4:**
I changed the number of iterations and threshold.


## 2. What values did you try?

**Change 1:**

```
### Old
maxr = -1000
maxa = None
for i in range(100):
    a1 = np.random.randint(-1000,1000)/1000
    a2 = np.random.randint(-1000,1000)/1000
    testa = [a1,a2]
    r_pred = model.predict(np.array(list(new_s)+list(testa)).reshape(1,len(list(new_s)+list(testa))))
    if r_pred > maxr:
        maxr = r_pred
        maxa = testa
a = np.array(maxa)

### New
a_candidates = np.random.uniform(low=-1, high=1, size=(batch_size, 2))
s_expanded = np.broadcast_to(new_s, (batch_size, 8))
all_candidates = np.concatenate([s_expanded, a_candidates], axis=1)
r_pred = model.predict(all_candidates)
max_idx = np.argmax(r_pred)
a = a_candidates[max_idx]
```

**Change 2:**
Adam was replaced with Adamax. Adamax is supposed to work better with sparse parameter updates. The gradient term is essentially ignored when it’s small therefore parameters are less susceptible to gradient noise.

**Change 3:**
The below is the new neural network architecture:
```
model = Sequential()
model.add(Dense(64, input_dim=input_dim, activation='relu'))
model.add(Dense(64, input_dim=input_dim, activation='relu'))
model.add(Dense(32, activation='sigmoid'))
model.add(Dense(1))
model.compile(loss='mean_squared_error', optimizer='adamax', metrics=['accuracy'])
```

**Change 4:**
```
training_thr = 3000
total_itrs = 300
```

## 3. Did you try any other changes that made things better or worse? Did they improve or degrade the model?

**Change 1:**
```
At step  50000
reward:  -4.262057550031028
total rewards  229.75075210891367
loss: 174.4578
```

**Change 2 - adam to adamax:**
```
At step  50000
reward:  -7.917616013448585
total rewards  174.91816134397675
loss: 158.1465
```

**Change 3 - change layers:**
```
At step  50000
reward:  -7.73850445549951
total rewards  -368.4289377267589
loss: 171.5462
```

The first three changes are detailed above. All are after 50000 steps. Overall, changing Adam to Adamax seems to be the thing that positively changed the lunar lander whereas increasing the number of layers and nodes did not seem to help. In fact, it seems a more complex model is detrimental. In this article, https://towardsdatascience.com/ai-learning-to-land-a-rocket-reinforcement-learning-84d61f97d055, Ashish Gupta points out that overtraining the model is potentially harmful. We rectify this below by changing the threshold and the number of iterations. Additionally, there is another article https://towardsdatascience.com/ai-learning-to-land-a-rocket-reinforcement-learning-84d61f97d055 which makes made couple good observations about potential variables to try and configure. If time permits, it would be worthwhile to try some of these.

**Change 4 - reduced training threshold and total iterations**
```
At step  50000
reward:  0.36437514063715937
total rewards  265.53854890961657
loss: 149.1106
```

## 4. Based on what you observed, what conclusions can you draw about the different parameters and their values?

Again, it seems like increasing the complexity of the model does not lead to a better result due to overtraining. Rather, it is the optimization and subtle tuning of hyperparameters during training that really dictates the results. Both shifting to adamax and lowering the threshold/training iterations lines up well with this.

** To see videos of the latest change, please go to http://s3.us-east.cloud-object-storage.appdomain.cloud/tennisonyu-w251-hw11 **
