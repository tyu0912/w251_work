Question/Answers:

1. The time it took you to train the model.

It took 37630.272 seconds, which is about 10.45 hours.

2. The final accuracy top1/top5 that you were able to achieve.

Acc@1 58.062 Acc@5 87.225

3. Could you increase the batch size? Why? How long did the training take you? 

The batch size as increased to 16. The batch size represents the total batch size of all GPUs on the current node. It seems you cannot go higher. The below is the error I received after 47 iterations.

```
Traceback (most recent call last):
  File "train.py", line 506, in <module>
    main()
  File "train.py", line 135, in main
    main_worker(args.gpu, ngpus_per_node, args)
  File "train.py", line 277, in main_worker
    train(train_loader, model, criterion, optimizer, epoch, num_classes, args)
  File "train.py", line 321, in train
    for i, (images, target) in enumerate(train_loader):
  File "/usr/local/lib/python3.6/dist-packages/torch/utils/data/dataloader.py", line 582, in __next__
  File "/usr/local/lib/python3.6/dist-packages/torch/utils/data/dataloader.py", line 608, in _process_next_batch
OSError: Traceback (most recent call last):
  File "/usr/local/lib/python3.6/dist-packages/torch/utils/data/_utils/worker.py", line 99, in _worker_loop
  File "/usr/local/lib/python3.6/dist-packages/torch/utils/data/_utils/worker.py", line 99, in <listcomp>
  File "/usr/local/lib/python3.6/dist-packages/torchvision-0.3.0-py3.6-linux-aarch64.egg/torchvision/datasets/folder.py", line 138, in __getitem__
    sample = self.loader(path)
  File "/usr/local/lib/python3.6/dist-packages/torchvision-0.3.0-py3.6-linux-aarch64.egg/torchvision/datasets/folder.py", line 174, in default_loader
    return pil_loader(path)
  File "/usr/local/lib/python3.6/dist-packages/torchvision-0.3.0-py3.6-linux-aarch64.egg/torchvision/datasets/folder.py", line 156, in pil_loader
    img = Image.open(f)
  File "/usr/local/lib/python3.6/dist-packages/Pillow-6.2.1-py3.6-linux-aarch64.egg/PIL/Image.py", line 2775, in open
    prefix = fp.read(16)
OSError: [Errno 5] Input/output error

Bus error (core dumped)

```

4. Please save your trained model.

Models are saved on the Jetson.

Commands Used:
root@tennisonyu-desktop:/jetson-inference/python/training/classification# python3 train.py --model-dir=plants --epochs=100 /data/PlantCLEF_Subset


