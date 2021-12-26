import pandas as pd
from sklearn import datasets
import streamlit as st
from sklearn.ensemble import RandomForestClassifier

st.title('Simple Iris Flower Prediction App')
st.markdown("""
This app predicts the **Iris flower** type!
""")
expander_bar = st.expander("About")
expander_bar.write("""
* **Python libraries: **pandas, sklearn, streamlit
""")

# sidebar
st.sidebar.header("User Input Parameters")

def user_input_features():
	sepal_length = st.sidebar.slider('Sepal Length', 4.3, 7.9, 5.4)
	sepal_width = st.sidebar.slider("Sepal Width", 2.0, 4.4, 3.4)
	petal_length = st.sidebar.slider("Petal Length", 1.0, 6.9, 1.3)
	petal_width = st.sidebar.slider("Petal Width", 0.1, 2.5, 0.2)

	data = {
		'sepal_length': sepal_length,
		'sepal_width': sepal_width,
		'petal_length': petal_length,
		'petal_width': petal_width
	}
	features = pd.DataFrame(data, index = [0])
	return features

df = user_input_features()

st.subheader("User Input Features")
st.dataframe(df)

iris = datasets.load_iris()
# st.write(iris)
X = iris.data
Y = iris.target
# st.write(X)
# st.markdown("""
# ***
# """)
# st.write(Y)

classifier = RandomForestClassifier()
classifier.fit(X,Y)

prediction = classifier.predict(df)
prediction_probablity = classifier.predict_proba(df)

st.subheader('Class labels and their corresponding index number')
st.dataframe(iris.target_names)

st.subheader("Prediction")
st.write(iris.target_names[prediction])

st.subheader("Prediction Probability")
st.write(prediction_probablity)