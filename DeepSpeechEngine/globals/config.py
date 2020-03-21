import os
import json
from functools import lru_cache


class ConfigDeepSpeech:

    @lru_cache(maxsize=32)
    def get_config(self, key):
        print('inside module')
        module_dir = os.path.dirname(__file__)  # get current directory
        file_path = os.path.join(module_dir, 'config.json')

        with open(file_path, 'r') as f:
            config = json.load(f)

        ds_config = config['deepspeech']
        model = ds_config['model']
        # alphabet = ds_config['alphabet']
        lm = ds_config['lm']
        trie = ds_config['trie']
        audio_folder = ds_config['audio_folder']
        frequency = ds_config['frequency']
        if key == 'model':
            return model
        elif key == 'lm':
            return lm
        elif key == 'trie':
            return trie
        elif key == 'audio_folder':
            return audio_folder
        elif key == 'frequency':
            return frequency
        else:
            raise Exception('Invalid key value.')
