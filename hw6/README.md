## Homework 6: BERT Toxicity Classification

The goal of this project was to study the performance of two types of GPUs: V100 vs P100 by applying both to the problem of statement toxicity classification using BERT, a relatively new NLP algorithm.

Per instruction, much of the work here is based on yuval r, https://www.kaggle.com/yuval6967/toxic-bert-plain-vanilah and the infrastructure setup was done by following course instruction as seen here https://github.com/MIDS-scaling-up/v2/tree/master/week06/hw .

The main conclusions of this work is that V100 is far superior to the P100. In the training step, the V100 was 4X faster than the P100. For the final question, choice A, running an extra epoch was chosen. By running this extra epoch we saw a massive improvement in the classification of toxicity. Interestingly, the AUC decreased a little bit but this seems to imply that training more epochs could lead to even better results. 

Examples of resulting sentences and the training times can be found inside the final notebook seen in the main directory. The other notebooks in the "checkpoint" folder are intermediary notebooks saved throughout the process to prevent loss of work. 
