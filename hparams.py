from dataset.texts import symbols

ngpu=1       # number of gpus ("0" uses cpu, otherwise use gpu)
nj=32        # numebr of parallel jobs
dumpdir='' # directory to dump full features
verbose=0    # verbose option (if set > 0, get more log)
N=0          # number of minibatches to be used (mainly for debugging). "0" uses all minibatches.
seed=1       # random seed number
resume=""    # the snapshot path to resume (if set empty, no effect)

# feature extraction related
sample_rate=22050      # sampling frequency
fmax=8000.0       # maximum frequency
fmin=0.0       # minimum frequency
n_mels=80     # number of mel basis
n_fft=1024    # number of fft points
hop_length=256   # number of shift points
win_length=1024 # window length
num_mels = 80
min_level_db = -100
ref_level_db = 20
bits = 9                            # bit depth of signal
mu_law = True                       # Recommended to suppress noise if using raw bits in hp.voc_mode below
peak_norm = False                   # Normalise to the peak of each wav file
eos=True
symbol_len = len(symbols)
batch_size = 16


# network architecture related
#model_module= espnet.nets.pytorch_backend.e2e_tts_transformer=Transformer
embed_dim= 0
eprenet_conv_layers= 0  # one more linear layer w/o non_linear will be added for 0_centor
eprenet_conv_filts= 0
eprenet_conv_chans= 0
dprenet_layers= 2  # one more linear layer w/o non_linear will be added for 0_centor
dprenet_units= 256
adim= 384
aheads= 4
elayers= 6
eunits= 1536
dlayers= 6
dunits= 1536
positionwise_layer_type = "linear" # conv1d
positionwise_conv_kernel_size = 1 # 3
postnet_layers= 5
postnet_filts= 5
postnet_chans= 256
use_masking= True
bce_pos_weight= 5.0
use_batch_norm= True
use_scaled_pos_enc= True
encoder_normalize_before= False
decoder_normalize_before= False
encoder_concat_after= False
decoder_concat_after= False
reduction_factor= 1
loss_type = "L1"
# minibatch related
batch_sort_key= input # shuffle or input or output
batch_bins= 910800    # 12 * (870 * 80 + 180 * 35)
                      # batch_size * (max_out * dim_out + max_in * dim_in)
                      # resuling in 11 ~ 66 samples (avg 15 samples) in batch (809 batches per epochs) for ljspeech

# training related
transformer_init= 'pytorch' # choices=["pytorch", "xavier_uniform", "xavier_normal", "kaiming_uniform", "kaiming_normal"]
transformer_warmup_steps= 4000
transformer_lr= 1.0
initial_encoder_alpha= 1.0
initial_decoder_alpha= 1.0
eprenet_dropout_rate= 0.0
dprenet_dropout_rate= 0.5
postnet_dropout_rate= 0.5
transformer_enc_dropout_rate= 0.1
transformer_enc_positional_dropout_rate= 0.1
transformer_enc_attn_dropout_rate= 0.1
transformer_dec_dropout_rate= 0.1
transformer_dec_positional_dropout_rate= 0.1
transformer_dec_attn_dropout_rate= 0.1
transformer_enc_dec_attn_dropout_rate= 0.1
use_guided_attn_loss= True
num_heads_applied_guided_attn= 2
num_layers_applied_guided_attn= 2
modules_applied_guided_attn= ["encoder_decoder"]
guided_attn_loss_sigma=0.4
guided_attn_loss_lambda=1.0

### FastSpeech
duration_predictor_layers = 2
duration_predictor_chans = 384
duration_predictor_kernel_size = 3
transfer_encoder_from_teacher = True
duration_predictor_dropout_rate = 0.1
teacher_model = "transformer_chkpt/checkpoint_430k_steps.pyt"
transferred_encoder_module = "all" # choices=["all", "embed"]



# optimization related
opt= 'noam'
accum_grad= 4
grad_clip= 1.0
weight_decay= 0.0
patience= 0
epochs= 1000  # 1,000 epochs * 809 batches / 5 accum_grad = 161,800 iters

# other
save_interval_epoch= 10

tts_cleaner_names = ['english_cleaners']
# other
save_interval = 5000
chkpt_dir = './checkpoints'
#fastspeech_chkpt = './fastspeech_checkpoints'
log_dir = './logs'
data_dir = './data/'
summary_interval = 1000
validation_step = 2000
tts_max_mel_len = 870              # if you have a couple of extremely long spectrograms you might want to use this
tts_bin_lengths = True              # bins the spectrogram lengths before sampling in data loader - speeds up training
