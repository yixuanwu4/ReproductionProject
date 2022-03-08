import pandas as pd
import glob

# convert all tsv files into csv file
path = '/home/nauxiy/Workspace/reproNLP/SentimentalLIAR/Using_LIAR'

tsvfiles = glob.glob(path + "/*.tsv") 
for t in tsvfiles:
    tsv = pd.read_table(t, sep='\t')
    tsv.to_csv(t[:-4] + '.csv', index=False)

# add header to the csv files
csvfiles = glob.glob(path + "/*.csv")
headerList = ['speaker_id', 'label', 'statement', 'subject', 'speaker', 'speaker_job', 'state_info', 'party_affiliation', 'barely_true_counts', 'false_counts', 'half_true_counts', 'mostly_true_counts', 'pants_on_fire_counts', 'context']
for c in csvfiles:
    file = pd.read_csv(c)
    # converting data frame to csv
    file.to_csv(c, header=headerList, index=False)

