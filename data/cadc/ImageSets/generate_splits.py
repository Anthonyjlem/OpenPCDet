import glob
import numpy

val_set = [
  ['2018_03_06', '0001'],
  ['2018_03_06', '0008'],
  ['2018_03_06', '0016'],
  ['2018_03_07', '0004'],
  ['2019_02_27', '0009'],
  ['2019_02_27', '0016'],
  ['2019_02_27', '0028'],
  ['2019_02_27', '0033'],
  ['2019_02_27', '0040'],
  ['2019_02_27', '0043'],
  ['2019_02_27', '0054'],
  ['2019_02_27', '0060'],
  ['2019_02_27', '0065'],
  ['2019_02_27', '0076'],
]

paths = glob.glob('../201*/**/*.bin', recursive=True)
samples = numpy.array([[x.split('/')[-6], x.split('/')[-5], x.split('/')[-1].rstrip('.bin')] for x in paths])

# This will create a random split instead of using the preselected train val split
CREATE_RANDOM = True

if CREATE_RANDOM:
  indices = numpy.random.permutation(samples.shape[0])
  train_split = int(samples.shape[0] * 0.70)
  val_split = int(samples.shape[0] * 0.85)
  training_idx, val_idx, test_idx = indices[:train_split], indices[train_split:val_split], indices[val_split:]
  training, val, test = samples[training_idx], samples[val_idx], samples[test_idx]

  with open("train.txt", "w") as f:
    for idx in training:
      f.write("%s %s %s\n" % (idx[0], idx[1], idx[2]))
  with open("val.txt", "w") as f:
    for idx in val:
      f.write("%s %s %s\n" % (idx[0], idx[1], idx[2]))
  with open("test.txt", "w") as f:
    for idx in test:
      f.write("%s %s %s\n" % (idx[0], idx[1], idx[2]))
else:
  with open("train.txt", "w") as f_train:
    with open("val.txt", "w") as f_val:
      for sample in samples:
        is_val = False
        # Check if sample is in val set
        for val in val_set:
          if val[0] == sample[0] and val[1] == sample[1]:
            is_val = True
            break
        # Output frame to corresponding file
        if is_val:
          f_val.write("%s %s %s\n" % (sample[0], sample[1], sample[2]))
        else:
          f_train.write("%s %s %s\n" % (sample[0], sample[1], sample[2]))
