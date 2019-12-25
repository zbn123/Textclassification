import torch
import torch.nn as nn
import torch.nn.functional as F
import numpy as np
import copy


class Config(object):

    """配置参数"""
    def __init__(self, embedding):
        self.model_name = 'Transformer'
        self.train_path = './Datas/train.txt'
        self.dev_path ='./Datas/dev.txt'
        self.test_path ='./Datas/test.txt'
        self.pred_path = './PRED/pred.txt'
        self.class_list = [x.strip() for x in open('./Datas/class.txt').readlines()]
        self.vocab_path ='./Datas/vocab.pkl'
        self.save_path = './Save_path/' + self.model_name + '.ckpt'
        self.log_path = './Log/' + self.model_name
        self.embedding_pretrained = torch.tensor(
            np.load('./Datas/' + embedding)["embeddings"].astype('float32'))\
            if embedding != 'random' else None
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

        self.dropout = 0.5
        self.require_improvement = 2000
        self.num_classes = len(self.class_list)
        self.n_vocab = 0
        self.num_epochs = 20
        self.batch_size = 128
        self.pad_size = 32
        self.learning_rate = 5e-4
        self.embed = self.embedding_pretrained.size(1)\
            if self.embedding_pretrained is not None else 300
        self.dim_model = 300
        self.hidden = 1024
        self.last_hidden = 512
        self.num_head = 5
        self.num_encoder = 2

