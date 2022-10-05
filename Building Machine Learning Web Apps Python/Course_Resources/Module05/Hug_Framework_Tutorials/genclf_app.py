import hug
import joblib

import warnings
warnings.filterwarnings("ignore")

# Vectorizer
gender_vectorizer = open("models/gender_vectorizer.pkl","rb")
gender_cv = joblib.load(gender_vectorizer)

# Models
gender_nv_model = open("models/gender_nv_model.pkl","rb")
gender_clf = joblib.load(gender_nv_model)


# Local Usage as Pkg
@hug.cli()
@hug.get('/gender',examples="name=Jesse")
@hug.local()
def predict(name:hug.types.text):
	"""Predict Gender  By First Name"""
	vectorized_name = gender_cv.transform([name]).toarray()
	prediction = gender_clf.predict(vectorized_name)

	if prediction[0] == 0:
		result = "female"
	elif prediction[0] == 1:
		result = "male"

	return {"original_name":name.title(),"prediction":result}


if __name__ == '__main__':
	predict.interface.cli()