from deepspeech import Model
from globals import config

# These constants control the beam search decoder

# Beam width used in the CTC decoder when building candidate transcriptions
BEAM_WIDTH = 500

# The alpha hyperparameter of the CTC decoder. Language Model weight
LM_ALPHA = 0.75

# The beta hyperparameter of the CTC decoder. Word insertion bonus.
LM_BETA = 1.85


# These constants are tied to the shape of the graph used (changing them changes
# the geometry of the first layer), so make sure you use the same constants that
# were used during training

# Number of MFCC features to use
# N_FEATURES = 26

# Size of the context window used for producing timesteps in the input vector
# N_CONTEXT = 9


class SpeechToTextService:
    def transcribe(self, audio):

        name = 'speech_server_main'
        conf = config.ConfigDeepSpeech()
        model = conf.get_config('model')
        print(model)
        # alphabet = conf.get_config('alphabet')
        # print(alphabet)
        lm = conf.get_config('lm')
        trie = conf.get_config('trie')
        print(trie)
        ds = Model(model, BEAM_WIDTH)
        if lm and trie:
            ds.enableDecoderWithLM(lm, trie, LM_ALPHA, LM_BETA)
        text = ds.stt(audio)
        return text

    def ready(self):
        print("Deepspeech Server Initialization")