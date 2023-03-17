## Setup

* Change to `backend` and install pipenv `pip install pipenv`
* Run `pipenv shell`
* `touch requirements.txt`
* Add libraries to `requirements.txt`
* run `pipenv install -r requirements.txt`
* `touch main.py`


## Setup Vue

* `cd ..`
* `cd frontend`
* Make sure `npm` is already installed in your computer.
* `npm install -g @vue/cli`
* install linter `npm install --save-dev eslint eslint-plugin-vue`
* Get new extension for vscode. `Vue Language Features (Volar)`
* Install `Prettier - Code formatter` from vscode extension.
* Create a vue project `vue create projectname` which is `vue create frontend`

```sh
Vue CLI v5.0.8
? Please pick a preset: Manually select features
? Check the features needed for your project: Babel, Router, Linter
? Choose a version of Vue.js that you want to start the project with 2.x
? Use history mode for router? (Requires proper server setup for index fallback in production) Yes

? Pick a linter / formatter config: Prettier
? Pick additional lint features: Lint on save
? Where do you prefer placing config for Babel, ESLint, etc.? In package.json
? Save this as a preset for future projects? No
```

* `cd frontend` thats is the second frontend  then run `npm run serve`
* We are focusing on source folder in frontend, 
  * assets folder is where files like images are stored in.
  * componets: where the UI components are stored.