import pandas as pd
import glob
import csv

# convert all tsv files into csv file
path = '/home/nauxiy/Workspace/reproNLP/ReproductionProject/Using_LIAR'

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

# add a new column to indicate if the text is fake or not (label each row as 1 or 0)
destpath = '/home/nauxiy/Workspace/reproNLP/ReproductionProject/Using_LIAR/modified'
destfiles = glob.glob(destpath + "/*.csv")
falselist = ['half-true', 'false', 'barely-true', 'pants-fire' ]
for c,d in zip(csvfiles, destfiles):
    print(c,d)
    with open(c, "rb") as source, open(d, "wb") as dest:
        # XXX are you sure you want this as quotechar ???
        reader = csv.reader(source)
        writer = csv.writer(dest)

        # first copy the (augmented) headers
        headers = reader.next()
        headers.append("list")
        writer.writerow(headers)

        # then loop on the content
        for rownum, row in enumerate(reader):
        
            if row[1] in falselist:
                result = ["[0, 1]"]
            else:
                result =["[1, 0]"]

            row.append(result)
            writer.writerow(row)
