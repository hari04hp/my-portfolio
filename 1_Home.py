import base64
from pathlib import Path
from streamlit_lottie import st_lottie
import requests
import streamlit as st

st.set_page_config(page_title="Haripriya Rajendran", page_icon="🕵️‍♀️", layout="wide") #emoji taken from webfx 

st.markdown("""
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
            <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css" rel="stylesheet">
            """, unsafe_allow_html=True)
with open('assets/css/styles.css') as f:
        st.markdown(f"""<style>{f.read()}""", unsafe_allow_html=True)

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def img_to_bytes(img_path):
    img_bytes = Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded

python_lottie = load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_2znxgjyt.json")
my_sql_lottie = load_lottieurl("https://assets4.lottiefiles.com/private_files/lf30_w11f2rwn.json")
ml_lottie = load_lottieurl("https://lottie.host/30f7a673-5d1a-4a83-b694-0361c985b506/Ik5pQjtkjb.json")


with st.container():
    st.sidebar.image("images/my-image-2.jpg")
    st.sidebar.title("Haripriya Rajendran 🤓")
    st.sidebar.header("Data Scientist 👩‍💻")
    
    with st.sidebar:
        columns = st.columns(2)
        columns[i:=0].markdown("""
        <a href="https://github.com/hari04hp" class="text-decoration-none text-light"><i class="fab fa-github contact-icons1" style="font-size: 50px;"></i></a>""",unsafe_allow_html=True,)
        columns[i:=i+1].markdown("""
        <a href="https://www.linkedin.com/in/haripriyar" class="text-decoration-none text-light"><i class="fab fa-linkedin contact-icons1" style="font-size: 50px;"></i></a>""",unsafe_allow_html=True,)
    
    with st.sidebar:
        dict_of_lotties = {"python": python_lottie, "mysql": my_sql_lottie, "ml": ml_lottie}
        columns = st.columns(len(dict_of_lotties))
        for index,column in enumerate(columns):
            with column:
                st_lottie(dict_of_lotties[list(dict_of_lotties.keys())[index]], height=70,width=70, key=list(dict_of_lotties.keys())[index], speed=2.5)

with st.container():
    st.header("My AI Assistant 🤖")
    st.page_link("pages/2_My_Assistant.py", label="Click on this link to go to my Chatbot Assistant page.")

# ---- ABOUT SECTION ----
with st.container():
    st.write("----")
    st.header("About 🗒")
    # st.title("Data Scientist and AI enthusiast")
    st.write(
        "A passionate Data Scientist with 6 years of overall experience with 4.5 years of experience in Machine Learning, Data Analysis and Data Science in FinTech.  \n\nI have worked in Applied Data Finance as a Lead Data Scientist where I have worked on end-to-end model building pipeline in which I figured out the need for the model, performed feature engineering, built multiple models to predict risk/fraud of a customer after performing statistical analysis, compiled a scorecard that works the best for the current scenario, implemented and deployed models in production."
    )

with st.container():
    st.write("---")
    st.header("Area of Knowledge 🧠")
    left_column, right_column = st.columns(2)
    with left_column:
        st.write("""
            - Data Extraction
            - Feature Engineering
            - Exploratory Data Analysis
            - Model Building and logging
            - Model deployment
            - Scorecard creation
            - Swap in - swap out Analysis""")
    with right_column:
        st.write("""
            - Ray Parallel processing
            - Applying Statistical methods
            - Models Evaluation Framework
            - Optuna parameter tuning
            - OpenAI API using LangChain""")

with st.container():
    st.write("---")
    st.header("Professional Experience 👩‍💻")
    columns = st.columns([0.2,0.8])
    with columns[0]:
        st.image("images/ADF_logo.jpg", width=200, )
    with columns[1]:
        st.subheader("Applied Data Finance - Lead Data Scientist")
        st.caption("Sep 2019 - Feb 2024")
    st.write("""Applied Data Finance uses data science and technology to responsibly open up access to credit for underestimated American consumers. Traditional finance has underestimated tens of millions of Americans. Our platform offers them access to credit with fair and responsible terms.""")
    with st.expander("See experience"):
        tab1, tab2, tab3 = st.tabs(["Tab 1", "Tab 2", "Tab 3"])
        with tab1:
            st.write("""
                    - Developed the core production risk model with all the loans resulting a KS of about 35. This was implemented into production and was expected 10% increase in loans volume and 8% reduction in risk.
                    - Responsible for creating new features, building the risk/fraud models, performing statistical analysis, implementing and deploying models in production. Recently created a Model Evaluation framework.
                    - Worked on GenAI with LLM in generating automated NOAA (Notice of Adverse Action) decline translations. I framed the prompt to get the proper decline code and translations based on our independent variables and their predefined descriptions, and prompted OpenAI API with GPT-3.5 model using LangChain framework. The prompt was framed in a way to generate user friendly reasons for over 5000 variables  and we achieved 75% accuracy which avoided manual framing of the decline reasons. The entire flow was exposed as HTTP Endpoint using Flask internally.""")
        with tab2:
            st.write("""
                    - Created an automated model evaluation framework that evaluates the newly added models and also suggests how the newly added models perform well on top of the existing ones. It also suggests the retirement of existing models if necessary. 
                    - Responsible for maintaining the Underwriting and the production script logic and models.
                    - Can make data-driven decisions by monitoring credit risk, exploring, transforming and analyzing large loan data sets, their default rates(PD, SMM) and presenting, which results in changing the operational settings in Underwriting based on the current scenario.
                    - Performed significance test to see if the reduction in risk is significant if a new rule is added in Underwriting""")
        with tab3:
            st.write("""
                    - Work closely with the ML Engineering team, to give insights on ML algorithms and help in developing modules and development pipelines.
                    - Encoded the categorical variables, analysed their bad rates and created Bayesian Features.
                    - Actively participated in all hackathons and received second prize in Data Science hackathon (placed with the second top KS value) and received a special award in technology hackathon.""")
                    
    columns = st.columns([0.2,0.8])
    with columns[0]:
        st.image("images/mq.png", width=200, )
    with columns[1]:
        st.subheader("MQ Spectrum India Pvt. Ltd.")
        st.caption("Oct 2017 - Aug 2019")
    st.write("""MQ Spectrum provides eLearning solutions for corporates. Products include an MQ learning portal & My VCMS - classroom management solutions. They also provide consultancy & system integration services. Clients include HP, Changi Airport, DSTA, etc.""")
    with st.expander("See experience"):
        st.write("""
            - Worked in the fields of Liferay Platform, Apache Tomcat Web application with J2EE and in the development of REST Web Services, WPF in C# and Search Indexer in C# platforms. Also worked in the MVC framework of ASP.NET.
            - As an Assistant Technical Lead, I was guiding my team on Android and WPF projects. Environment: Moodle framework, SQL Server, Apache Tomcat Server, Liferay, C# and ASP.NET.""")

with st.container():
    st.write("---")
    st.header("Skills 💪")
    left_column, right_column = st.columns(2)
    with left_column:
        st.subheader("Programming Languages")
        st.write(
            """
            - Python
            - R
            - MySQL
            - RedShift's PostgreSQL
            - SQL
            - MongoDB (basics)
            - BigQuery (basics)""")
        st.subheader("Python Libraries")   
        st.write(""" 
            - Pandas
            - Numpy
            - Scikit-learn
            - XGBoost
            - Matplotlib, Seaborn, plotly
            - Tensor Flow and Keras
            - Optuna, Ray and MLFlow
            - langchain, streamlit, pinecone
            - OpenAI
            - joblib and pickle
            - joblib-Parallel-delayed
            - pycopg2, pymysql, pymongo, sqlalchemy
            - json, requests, flask""")
        st.subheader("Statistics")
        st.write("""
            - Descriptive, Predictive and Inferential Data Analytics
            - Linear Modeling
            - Probability distributions
            - Hypothesis Testing (z-test, ANOVA, t-test)
            - Bayesian Statistics
            - Accuracy Analysis
            - Cross-Validation
            - Correlation Matrix
            - Multicollinearity and VIF """)
    with right_column:
        st.subheader("Machine Learning Algorithms")
        st.write("""
            - Linear and Logistic Regression
            - XGBoost
            - Decision Trees
            - Random Forests
            - Stratified sampling
            - Propensity sample weighting
            - Optuna Parameter tuning
        """)
        st.subheader("Deep Learning and GenAI")
        st.write("""
                - OpenAI API using LangChain
                - Convolution Neural Network
                - Recurrent Neural Network (basics)""")
        st.subheader("Tools and Platform")
        st.write("""
                - Tableau Server and Desktop
                - MS Office Suite (Word, Excel, Powerpoint
                - Visual Studio Code
                - Streamlit
                - gunicorn/Flask
                - Bitbucket (Git) and github
                - DVC
                - JIRA
                - Jenkins
                - Windows
                - Linux
                - AWS S3,EC2,RDS,RedShift""")

with st.container():
        st.write("---")
        st.header("Projects 📈")
        st.markdown("""<div class="project-container mt-5">
        <div class="container">
            <div class="row">
                <div class="col-md-4 mb-4">
                    <a href="3_About_My_Assistant" target='_self'
                        class="text-decoration-none">
                        <div class="card project-card position-relative">
                            <img src='data:image/png;base64,{2}'
                                class="card-img-top" alt="Project 1 Image" >
                            <div class="project-name">Chat Application Project using RAG with LangChain and OpenAI</div>
                            <div class="card-body">
                                <h5 class="card-title d-none">Chat Application Project using RAG with LangChain and OpenAI</h5>
                                <p class="card-text text-light">
                                    For my personal project, I developed a chat assistant application using Retrieval Augmentaion with Langchain which learns about me with my resume and will try to answer the relevant questions that are raised.</p>
                            </div>
                        </div>
                    </a>
                </div>
                <div class="col-md-4 mb-4">
                    <a href="https://github.com/hari04hp/google-advanced-capstone"
                        class="text-decoration-none">
                        <div class="card project-card position-relative">
                            <img src='data:image/png;base64,{0}'
                                class="card-img-top" alt="Project 1 Image">
                            <div class="project-name">Case study - employee retention model
                            </div>
                            <div class="card-body">
                                <h5 class="card-title d-none">Case study - employee retention model</h5>
                                <p class="card-text text-light">
                                    For Google Advanced Data Analytics Course, I have completed the case study on a fictional company Salifort Motors to increase employee retention. I have completed an exploratory data analysis on all the features given and a classification model is built on the same. The Case Study is published in github.</p>
                            </div>
                        </div>
                    </a>
                </div>
                <div class="col-md-4 mb-4">
                    <a href="https://rpubs.com/haripriya_rhp/cyclistic-case-study"
                        class="text-decoration-none">
                        <div class="card project-card position-relative">
                            <img src='data:image/png;base64,{1}'
                                class="card-img-top" alt="Project 1 Image">
                            <div class="project-name">Case study - cyclistic bike
                                share analysis</div>
                            <div class="card-body">
                                <h5 class="card-title d-none">Case study - cyclistic
                                    bike share analysis</h5>
                                <p class="card-text text-light">
                                    For Google Data Analytics Course, I have
                                    completed the case study on a fictional company
                                    Cyclistic on maximizing the number of annual
                                    memberships. The Case Study is published in
                                    RPubs, Kaggle and github.</p>
                            </div>
                        </div>
                    </a>
                </div>
            </div>
        </div>
    </div>
                            
                        """.format(
        img_to_bytes("images/google-advanced.jpg"),img_to_bytes("images/cyclistic-bike-share.png"), img_to_bytes("images/GenAI.png")
        ),unsafe_allow_html=True)

with st.sidebar.container():
    st.sidebar.markdown("""<p style="font-size:12px;">App is created using streamlit. Images are taken online. Emojis are taken from webfx. Lottie animations also have been used. </p>""", unsafe_allow_html=True)