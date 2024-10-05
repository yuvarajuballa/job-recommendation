import streamlit as st
import pandas as pd
import pickle
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

df=pickle.load(open('data.pkl','rb'))
tfidf_matrix=pickle.load(open('tfi.pkl','rb'))



def jobs_recommendation(Title):
    idx=df[df['skills']==Title].index[0]
    idx=df.index.get_loc(idx)
    similarity_scores = sorted(list(enumerate(tfidf_matrix[idx])), key=lambda x: x[1], reverse=True)
    newsindices = [i[0] for i in similarity_scores]
    return df[['company','jobtitle', 'skills','joblocation_address', 'payrate']].iloc[newsindices][0:5]





#web app
if __name__=="__main__":


    st.title('Job Recommendation System')
    Title=st.selectbox('search job',df['skills'])

    if st.button('Get Recommendation'):
        st.subheader('Recommended Jobs')

        jobs=jobs_recommendation(Title)


        st.write(jobs)


