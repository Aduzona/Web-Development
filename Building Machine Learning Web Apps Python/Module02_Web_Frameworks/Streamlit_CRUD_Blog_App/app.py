import streamlit as st
# EDA Pkgs
import pandas as pd 
import matplotlib.pyplot as plt 
import matplotlib 
matplotlib.use('Agg')
from wordcloud import WordCloud,STOPWORDS,ImageColorGenerator

# Security
import hashlib
def make_hashes(password):
	return hashlib.sha256(str.encode(password)).hexdigest()

def check_hashes(password,hashed):
	if make_hashes(password) == hashed:
		return hashed
	return False

# DB
from db_fxns import *



# Reading Time
def readingTime(mytext):
	total_words = len([ token for token in mytext.split(" ")])
	estimatedTime = total_words/200.0
	return estimatedTime

# Layout Templates
title_temp ="""
	<div style="background-color:#464e5f;padding:10px;border-radius:10px;margin:10px;">
	<h4 style="color:white;text-align:center;">{}</h1>
	<img src="https://www.w3schools.com/howto/img_avatar.png" alt="Avatar" style="vertical-align: middle;float:left;width: 50px;height: 50px;border-radius: 50%;" >
	<h6>Author:{}</h6>
	<br/>
	<br/>	
	<p style="text-align:justify">{}</p>
	</div>
	"""
article_temp ="""
	<div style="background-color:#464e5f;padding:10px;border-radius:5px;margin:10px;">
	<h4 style="color:white;text-align:center;">{}</h1>
	<h6>Author:{}</h6> 
	<h6>Post Date: {}</h6>
	<img src="https://www.w3schools.com/howto/img_avatar.png" alt="Avatar" style="vertical-align: middle;width: 50px;height: 50px;border-radius: 50%;" >
	<br/>
	<br/>
	<p style="text-align:justify">{}</p>
	</div>
	"""
head_message_temp ="""
	<div style="background-color:#464e5f;padding:10px;border-radius:5px;margin:10px;">
	<h4 style="color:white;text-align:center;">{}</h1>
	<img src="https://www.w3schools.com/howto/img_avatar.png" alt="Avatar" style="vertical-align: middle;float:left;width: 50px;height: 50px;border-radius: 50%;">
	<h6>Author:{}</h6> 		
	<h6>Post Date: {}</h6>		
	</div>
	"""
full_message_temp ="""
	<div style="background-color:silver;overflow-x: auto; padding:10px;border-radius:5px;margin:10px;">
		<p style="text-align:justify;color:black;padding:10px">{}</p>
	</div>
	"""




def main():
	"""A Simple CRUD  Blog"""
	html_temp = """
		<div style="background-color:{};padding:10px;border-radius:10px">
		<h1 style="color:{};text-align:center;">Simple Blog </h1>
		</div>
		"""
	st.markdown(html_temp.format('royalblue','white'),unsafe_allow_html=True)

	menu = ["Home","View Posts","Search","Login","SignUp","About"]
	choice = st.sidebar.selectbox("Menu",menu)

	if choice == "Home":
		st.subheader("Home")
		result = view_all_notes()
		
		for i in result:
			b_author = i[0]
			b_title = i[1]
			b_article = str(i[2])[0:30]
			b_post_date = i[3]
			st.markdown(title_temp.format(b_title,b_author,b_article,b_post_date),unsafe_allow_html=True)

	elif choice == "View Posts":
		st.subheader("View Articles")
		all_titles = [i[0] for i in view_all_titles()]
		postlist = st.sidebar.selectbox("View Posts",all_titles)
		post_result = get_blog_by_title(postlist)
		for i in post_result:
			b_author = i[0]
			b_title = i[1]
			b_article = i[2]
			b_post_date = i[3]
			st.text("Reading Time:{}".format(readingTime(b_article)))
			st.markdown(head_message_temp.format(b_title,b_author,b_post_date),unsafe_allow_html=True)
			st.markdown(full_message_temp.format(b_article),unsafe_allow_html=True)


	elif choice == "Login":
		user = st.sidebar.text_input('Username')
		passwd = st.sidebar.text_input('Password',type='password')
		if st.sidebar.checkbox('Login') :
			create_usertable()
			hashed_pswd = make_hashes(passwd)
			result = login_user(user,check_hashes(passwd,hashed_pswd))
			if result:
				st.success("Logged In as {}".format(user))

				# Tasks For Only Logged In Users
				task = st.selectbox('Select Task',['Add Posts','Manage Blog','User Settings'])
				if task == "Add Posts":
					st.subheader("Add Articles")
					create_table()
					blog_author = st.text_input("Enter Author Name",max_chars=50)
					blog_title = st.text_input("Enter Post Title")
					blog_article = st.text_area("Post Article Here",height=200)
					blog_post_date = st.date_input("Date")
					if st.button("Add"):
						add_data(blog_author,blog_title,blog_article,blog_post_date)
						st.success("Post:{} saved".format(blog_title))

				elif task == "Manage Blog":
					st.subheader("Manage Articles")

					result = view_all_notes()
					clean_db = pd.DataFrame(result,columns=["Author","Title","Articles","Post Date"])
					st.dataframe(clean_db)

					unique_titles = [i[0] for i in view_all_titles()]
					delete_blog_by_title = st.selectbox("Unique Title",unique_titles)
					new_df = clean_db
					if st.button("Delete"):
						delete_data(delete_blog_by_title)
						st.warning("Deleted: '{}'".format(delete_blog_by_title))


					if st.checkbox("Metrics"):
						
						new_df['Length'] = new_df['Articles'].str.len()
						st.dataframe(new_df)


						st.subheader("Author Stats")
						new_df["Author"].value_counts().plot(kind='bar')
						st.pyplot()

						st.subheader("Author Stats")
						new_df['Author'].value_counts().plot.pie(autopct="%1.1f%%")
						st.pyplot()

					if st.checkbox("Word Cloud"):
						st.subheader("Generate Word Cloud")
						# text = new_df['Articles'].iloc[0]
						text = ','.join(new_df['Articles'])
						wordcloud = WordCloud().generate(text)
						plt.imshow(wordcloud,interpolation='bilinear')
						plt.axis("off")
						st.pyplot()

					if st.checkbox("BarH Plot"):
						st.subheader("Length of Articles")
						new_df = clean_db
						new_df['Length'] = new_df['Articles'].str.len()
						barh_plot = new_df.plot.barh(x='Author',y='Length',figsize=(20,10))
						st.pyplot()
				elif task == 'User Settings':
					users_result = view_all_users()
					clean_db = pd.DataFrame(users_result,columns=["Username","Password"])
					st.dataframe(clean_db)

			else:

				st.warning('Access Denied: Wrong Username/Password')
				st.info('Retry or SignUp')

	elif choice == "SignUp":
		st.subheader("Create an Account")
		new_user = st.text_input('Username')
		new_passwd = st.text_input('Password',type='password')
		if st.button('SignUp'):
			create_usertable()
			add_userdata(new_user,make_hashes(new_passwd))
			st.success("You have successfully created an account.Go to the Login Menu to login")
		







	




	




	elif choice == "Search":
		st.subheader("Search Articles")
		search_term = st.text_input('Enter Search Term')
		search_choice = st.radio("Field to Search By",("title","author"))
		
		if st.button("Search"):

			if search_choice == "title":
				article_result = get_blog_by_title(search_term)
			elif search_choice == "author":
				article_result = get_blog_by_author(search_term)


			for i in article_result:
				b_author = i[0]
				b_title = i[1]
				b_article = i[2]
				b_post_date = i[3]
				st.text("Reading Time:{}".format(readingTime(b_article)))
				st.markdown(head_message_temp.format(b_title,b_author,b_post_date),unsafe_allow_html=True)
				st.markdown(full_message_temp.format(b_article),unsafe_allow_html=True)




	






if __name__ == '__main__':
	main()