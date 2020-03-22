Question/Answers:

1. The time it took you to train the model.

It took 37630.272 seconds, which is about 10.45 hours.

2. The final accuracy top1/top5 that you were able to achieve.

Acc@1 58.062 Acc@5 87.225

3. Could you increase the batch size? Why? How long did the training take you? 

The batch size as increased to 16. The batch size represents the total batch size of all GPUs on the current node when using parallelization settings so it seems like I am able to increase because this is a parallelizable process. The training took 

4. Please save your trained model.

Models are saved on the Jetson.

Commands Used:
root@tennisonyu-desktop:/jetson-inference/python/training/classification# python3 train.py --model-dir=plants --epochs=100 /data/PlantCLEF_Subset


