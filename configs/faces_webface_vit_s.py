from easydict import EasyDict as edict

config = edict()
config.margin_list = (1.0, 0.0, 0.4)
config.network = "vit_s"
config.resume = False
config.output = None
config.embedding_size = 512
config.sample_rate = 1.0
config.fp16 = True
config.momentum = 0.9
config.weight_decay = 1e-4
config.batch_size = 128
config.lr = 0.1
config.verbose = 2000
config.dali = False

config.rec = "./data/faces_webface_112x112"
config.num_classes = 10572
config.num_image = 490623
config.num_epoch = 20
config.warmup_epoch = 0
config.val_targets = ['lfw']
