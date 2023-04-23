import numpy as np
import pandas as pd
import os

from transformers import BertTokenizer, BertForSequenceClassification

finbert = BertForSequenceClassification.from_pretrained('yiyanghkust/finbert-tone', num_labels=3)
tokenizer = BertTokenizer.from_pretrained('yiyanghkust/finbert-tone')
directory = "10K-10Q_dataset/10K-10Q_dataset/"


def analyze(selection):
    inputs = tokenizer(selection, return_tensors="pt", padding=True, truncation=True, max_length=512)
    outputs = finbert(**inputs)[0]

    labels = {0: 'neutral', 1: 'positive', 2: 'negative'}
    val = np.argmax(outputs.detach().numpy(), axis=1)
    res = np.unique(val, return_counts=True)

    return res

results = pd.DataFrame(columns=['ticker', 'total', 'positive', 'negative'])
for filename in os.listdir(directory):
    if filename <= "cdk.csv":
        continue
    ticker = filename[0:-4]
    f = os.path.join(directory, filename)
    # checking if it is a file
    if os.path.isfile(f):
        print(f)

    data = pd.read_csv(f)

    x = data.loc[:, "paragraph"].tolist()
    ndata = len(x)
    pos = 0
    neg = 0
    step = 10
    for row in range(0, ndata, step):
        if row < ndata:
            selection = x[row:row + step]
        if len(selection) > 0:
            try:
                res = analyze(selection)
                if 1 in res[0]:
                    ind = np.where(res[0] == 1)[0][0]
                    pos += res[1][ind]
                if 2 in res[0]:
                    ind = np.where(res[0] == 2)[0][0]
                    neg += res[1][ind]
            except Exception as e:
                print(e)
        if row % 500 == 0:
            print(row)
    row_to_append = pd.DataFrame([{'ticker': ticker, 'total': ndata, 'positive': pos, 'negative': neg }])
    print(row_to_append)
    results = pd.concat([results, row_to_append])
    results.to_csv("results.csv")