import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

vi_data_df = pd.read_csv("./data/vi_text_retrieval.csv")


def tfidf_search(question, tfidf_vectorizer, top_d=5):
    # Lowercasing before encoding
    query_embedded = tfidf_vectorizer.transform([question.lower()])
    cosine_scores = cosine_similarity(query_embedded, context_embedded).flatten()

    # Get top k cosine scores and index them
    results = []
    for idx in cosine_scores.argsort()[-top_d:][::-1]:
        doc_score = {
            'id': idx,
            'cosine_score': cosine_scores[idx]
        }
        results.append(doc_score)
    return results


def corr_search(question, tfidf_vectorizer, top_d=5):
    # Lowercasing before encoding
    query_embedded = tfidf_vectorizer.transform([question.lower()])
    corr_scores = cosine_similarity(query_embedded, context_embedded).flatten()

    # Get top k correlation scores and index them
    results = []
    for idx in corr_scores.argsort()[-top_d:][::-1]:
        doc = {
            'id': idx,
            'corr_score': corr_scores[idx]
        }
        results.append(doc)
    return results


# Question 10
print("Question 10")
context = vi_data_df['text']
context = [doc.lower() for doc in context]
tfidf_vectorizer = TfidfVectorizer()
context_embedded = tfidf_vectorizer.fit_transform(context)
print(context_embedded.toarray()[7][0])
print()


# Question 11
print("Question 11")
question = vi_data_df.iloc[0]['question']
results = tfidf_search(question, tfidf_vectorizer, top_d=5)
print(results[0]['cosine_score'])
print()


# Question 12
print("Question 12")
question = vi_data_df.iloc[0]['question']
results = corr_search(question, tfidf_vectorizer, top_d=5)
print(results[1]['corr_score'])
print()
