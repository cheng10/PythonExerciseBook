from sklearn.feature_extraction.text import TfidfVectorizer
import os


DIR = 'txt/'

score_kv = {}
index2id = {}
corpus = []
docs = []

for txt in os.listdir(DIR):
    with open(DIR+txt) as f:
        doc = ''
        for line in f:
            doc += line
        docs.append(doc)

for doc in docs:
    corpus.append(doc)

# print(docs)
# print(len(docs))

tf = TfidfVectorizer(analyzer='word', ngram_range=(1, 1), min_df=0, stop_words='english')
tfidf_matrix = tf.fit_transform(corpus)
feature_names = tf.get_feature_names()
dense = tfidf_matrix.todense()

for i in range(len(dense)):
    print(i)
    doc = dense[i].tolist()[0]
    phrase_scores = [pair for pair in zip(range(0, len(doc)), doc)if pair[1] > 0]
    # print len(phrase_scores)
    # print sorted(phrase_scores, key=lambda t: t[1] * -1)[:5]
    sorted_phrase_scores = sorted(phrase_scores, key=lambda t: t[1] * -1)
    sps = sorted_phrase_scores
    for phrase, score in [(feature_names[word_id], score) for (word_id, score) in sps][:5]:
        print('{0: <20} {1}'.format(phrase, score))
    print('--------')
