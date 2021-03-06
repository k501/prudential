"""
This module tests stacked_autoencoders.ipynb
"""
import os

from pylearn2.testing import skip
from pylearn2.testing import no_debug_mode
from pylearn2.config import yaml_parse


@no_debug_mode
def train_yaml(yaml_file):

    train = yaml_parse.load(yaml_file)
    train.main_loop()

def train_maxout_2layer(yaml_file_path, save_path, train_data, valid_data, model_name):

    print 'MAXOUT-DROPOUT 2 LAYERS'
    yaml = open("{0}/maxout-2layer.yaml".format(yaml_file_path), 'r').read()
    hyper_params = {'batch_size'          : 1000,
                    'monitoring_batches'  : 1,
                    'nvis'                : 1077,
                    'train_data'          : train_data,
                    'valid_data'          : valid_data,
                    'save_path'           : save_path,
                    'model_name'          : model_name }
    yaml = yaml % (hyper_params)
    train_yaml(yaml)

def train_maxout_3layer(yaml_file_path, save_path, train_data, valid_data, model_name):

    print 'MAXOUT-DROPOUT 3 LAYERS'
    yaml = open("{0}/maxout-3layer.yaml".format(yaml_file_path), 'r').read()
    hyper_params = {'batch_size'          : 1000,
                    'monitoring_batches'  : 1,
                    'nvis'                : 1077,
                    'train_data'          : train_data,
                    'valid_data'          : valid_data,
                    'save_path'           : save_path,
                    'model_name'          : model_name }
    yaml = yaml % (hyper_params)
    train_yaml(yaml)

def test_sda():

    skip.skip_if_no_data()

    # set common parameter
    yaml_file_path = '.';
    save_path = '.';
    train_data = '../data/train.pkl';
    valid_data = '../data/valid.pkl';
    model_name = 'model.pkl';

    #train_maxout_2layer(yaml_file_path, save_path, train_data, valid_data, model_name)
    train_maxout_3layer(yaml_file_path, save_path, train_data, valid_data, model_name)

    '''
    try:
        os.remove("{}/dae_l1.pkl".format(save_path))
        os.remove("{}/dae_l2.pkl".format(save_path))
    except OSError:
        pass
    '''

if __name__ == '__main__':
    test_sda()
