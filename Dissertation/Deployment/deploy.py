import streamlit as st
import pickle

def predict(g2,g1,absences,age,health):

    if health == 'Very Bad':
        health = 0
    elif health == 'Bad':
        health = 1
    elif health == 'Average':
        health = 2
    elif health == 'Good':
        health = 3
    else:
        health = 4
    
    m_classify = select_model(model_selection)
    userPrediction = m_classify.predict([[g2,g1,absences,age,health]])
    g3 = userPrediction[0]
    return g3


def select_model(model_selection):
    pickle_in_random_forest = open('Documents/Dissertation/Deployment/Random_forest_model_.pkl', 'rb') 
    random_forest = pickle.load(pickle_in_random_forest)
    
    pickle_in_linear_regression = open('Documents/Dissertation/Deployment/linear_regression_model_.pkl', 'rb') 
    linear_regression = pickle.load(pickle_in_linear_regression)    
    
    if model_selection == 'Random Forest':
        m_classify = random_forest
    else:
        m_classify = linear_regression
    
    return m_classify

def main():
    html = """
    <div style ="background-color:rgb(240,242,246);padding:15px;"> 
    <h1 style ="text-align:center;">Student's Grade Prediction</h1> 
    </div>
    """
    global model_selection
    st.markdown(html, unsafe_allow_html = True)
    model_selection= st.selectbox('Prediction Model', ("Random Forest", "Linear Regression "))
    subject = st.selectbox('Subject', ("Maths", "Portuguese"))
    g1 = st.number_input("First Grade (G1)", min_value=0.0, max_value=20.0)
    g2 = st.number_input("Second Grade (G2)", min_value=0.0, max_value=20.0)
    age = st.number_input("Age",min_value=0, step = 1)
    absences = st.number_input("No. of School Absense",min_value=0)
    health =  st.selectbox("Health Status", ("Very Bad", "Bad", "Average","Good" ,"Very Good"), index = 2)


    if st.button("Predict"):
        final_prediction = predict(g2,g1,absences,age,health)
        st.success('Final Predicted Grade is {}'.format(final_prediction))
        
    
if __name__ == '__main__':
    main()