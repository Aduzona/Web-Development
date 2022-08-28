### How To Serialize Models
+ Data serialization is the process of converting structured data to a format that allows sharing or storage of the data in a form that allows recovery of its original structure. In some cases, the secondary intention of data serialization is to minimize the data’s size which then reduces disk space or bandwidth requirements.

#### Tools
+ pickle
+ joblib
+ ray
+ json

### Basic Example
import pickle

#### Here's an example dict
estimates = { 'Apple': 89, 'Google': 72, 'Microsoft': 87 }

#### We use dumps to convert the object to a serialized string
serial_estimate = pickle.dumps(estimates)

#### We use loads to de-serialize an object
received_grades = pickle.loads( serial_estimages )

### Using Pickle For Saving or Serializing Models
```python
import pickle
with open('model_logit.pkl',"wb") as f:
	pickle.dump(model,f)

loaded_model = pickle.load('model_logit.pkl')
```

### Using Joblib From Sklearn.externals For Saving or Serializing Models
```python
from sklearn.externals import joblib
joblib.dump(model,'model_logit.joblib')
loaded_model2 = joblib.load('model_logit.joblib')
```

### Using Joblib For Saving or Serializing Models
```python
import joblib
joblib.dump(model,'model_logit.joblib')
loaded_model2 = joblib.load('model_logit.joblib')
```


### Thanks
+ Jesus Saves @JCharisTech