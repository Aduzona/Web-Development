import streamlit as st
#EDA Pkgs
import pandas as pd 
import numpy as np 

# Data Viz Pkg
import matplotlib
matplotlib.use('Agg')# Tkagg
import matplotlib.pyplot as plt 
import seaborn as sns 
import joblib,os


# Get Value
def get_value(val,my_dicts):
	for key,value in my_dicts.items():
		if val == key:
			return value

def get_key(val,my_dicts):
	for key,value in my_dicts.items():
		if val == value:
			return key


# Loading Models
def load_prediction_model(model_file):
	loaded_model = joblib.load(open(os.path.join(model_file),"rb"))
	return loaded_model


def main():
	"""CMC Predictor with Streamlit """

	st.title("CMC Predictor ML App")
	

	html_templ = """
	<div style="background-color:magenta;padding:10px;">
	<h2 style="color:white">ML App with Streamlit</h2>
	</div>
	"""

	st.markdown(html_templ,unsafe_allow_html=True)

	activity = ["Descriptive","Predictive"]
	choice = st.sidebar.selectbox("Choose Analytics Type",activity)

	if choice == 'Descriptive':
		st.subheader("EDA Aspect")
		# Preview Dataset

		df = pd.read_csv("data_cmc/cmc_dataset.csv")

		if st.checkbox("Preview Dataset"):
			number = st.number_input("Select Number of Rows To View")
			st.dataframe(df.head(number))

		if st.checkbox("Shape of Dataset"):
			st.write(df.shape)
			data_dim = st.radio("Show Dimensions By ",("Rows","Columns"))
			if data_dim == 'Rows':
				st.text("Showing the Rows")
				st.write(df.shape[0])
			if data_dim == 'Columns':
				st.text("Showing the Columns")
				st.write(df.shape[1])

		if st.checkbox("Select Columns"):
			all_columns = df.columns.tolist()
			selected_columns = st.multiselect("Select Columns",all_columns)
			new_df = df[selected_columns]
			st.dataframe(new_df)

		if st.button("Summary of Dataset"):
			st.write(df.describe())

		if st.button("Value Counts"):
			st.text("Value Counts By Target")
			st.write(df.iloc[:,-1].value_counts())

		st.subheader("Data Visualization")
		# Correlation Plot
		if st.checkbox("Correlation Plot with Matplotlib"):
			plt.matshow(df.corr())
			st.pyplot()

		if st.checkbox("Correlation Plot with Seaborn"):
			st.write(sns.heatmap(df.corr(),annot=True))
			st.pyplot()

		if st.checkbox("Pie Chart"):
			if st.button("Generate Pie Chart"):
				st.write(df.iloc[:,-1].value_counts().plot.pie(autopct="%1.1f%%"))
				st.pyplot()

		if st.checkbox("Plot Value Counts"):
			st.write(df.iloc[:,-1].value_counts().plot(kind='bar'))
			st.pyplot()


		if st.checkbox("Plot Value Counts By Columns"):
			st.text("Value Counts By Target/Class")

			all_columns_names = df.columns.tolist()
			primary_col = st.selectbox('Select Primary Column To Group By',all_columns_names)
			selected_column_names = st.multiselect('Select Columns',all_columns_names)
			if st.button("Plot"):
				st.text("Generating Plot for: {} and {}".format(primary_col,selected_column_names))
				if selected_column_names:
					vc_plot = df.groupby(primary_col)[selected_column_names].count()		
				else:
					vc_plot = df.iloc[:,-1].value_counts()
				st.write(vc_plot.plot(kind='bar'))
				st.pyplot()

		





	if choice == 'Predictive':
		st.subheader("Prediction Aspect")


		age = st.slider("Select Age",16,60)
		wife_education = st.number_input("Wife's Education Level(low2High) [1,4]",1,4)
		husband_education = st.number_input("Husband's Education Level(low2High) [1,4]",1,4)
		num_of_children_ever_born = st.number_input("Number of Children")

		wife_reg = {"Non_Religious":0,"Religious":1}
		choice_wife_reg = st.radio("Wife's Religion",tuple(wife_reg.keys()))
		result_wife_reg = get_value(choice_wife_reg,wife_reg)
		


		wife_working = {"Yes":0,"No":1}
		choice_wife_working = st.radio("Is the Wife Currently Working",tuple(wife_working.keys()))
		result_wife_working = get_value(choice_wife_working,wife_working)
		


		husband_occupation = st.number_input("Husband Occupation(low2High) [1,4]",1,4)
		standard_of_living = st.slider("Standard of Living (low2High) [1,4]",1,4)

		media_exposure = {"Good":0,"Not Good":1}
		choice_media_exposure = st.radio("Media Exposure",tuple(media_exposure.keys()))
		result_media_exposure = get_value(choice_media_exposure,media_exposure)

			# Result and in json format
		results = [age,wife_education,husband_education,num_of_children_ever_born,result_wife_reg,result_wife_working,husband_occupation,standard_of_living,result_media_exposure]
		displayed_results = [age,wife_education,husband_education,num_of_children_ever_born,choice_wife_reg,choice_wife_working,husband_occupation,standard_of_living,choice_media_exposure]
		prettified_result = {"age":age,
		"wife_education":wife_education,
		"husband_education":husband_education,
		"num_of_children_ever_born":num_of_children_ever_born,
		"result_wife_reg":choice_wife_reg,
		"result_wife_working":choice_wife_working,
		"husband_occupation":husband_occupation,
		"standard_of_living":standard_of_living,
		"media_exposure":choice_media_exposure}
		sample_data = np.array(results).reshape(1, -1)

		st.info(results)
		st.json(prettified_result)


		st.subheader("Prediction Aspects")
		if st.checkbox("Make Prediction"):
			all_ml_dict = ["LR","Decision Tree","Naive Bayes","RFOREST"]
			model_choice = st.selectbox("Model Choice",all_ml_dict)

			if st.button("Predict"):
				prediction_label = {"No_use":1,"Long_term":2,"Short_term":3}
				if model_choice == 'LR':
					predictor = load_prediction_model("models/contraceptives_logit_model.pkl")
					prediction = predictor.predict(sample_data)
				elif model_choice == 'Decision Tree':
					predictor = load_prediction_model("models/contraceptives_dcTree_model.pkl")
					prediction = predictor.predict(sample_data)

				elif model_choice == 'Naive Bayes':
					predictor = load_prediction_model("models/contraceptives_nv_model.pkl")
					prediction = predictor.predict(sample_data)

				elif model_choice == "RFOREST":
					predictor = load_prediction_model("models/contraceptives_rf_model.pkl")
					prediction = predictor.predict(sample_data)


				final_result = get_key(prediction,prediction_label)
				st.success(final_result)


			















if __name__ == '__main__':
	main()