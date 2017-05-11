'''
Filename : app.py
Latest update : 17th March 2017
Description : This is the main application file which implement the routing logic presented in the browser
			  This application make use of Flask Api 

Created by : Abhishek Chaudhary
'''

############################################## IMPORTING THE REQUIRED MODULES ##################################################
import sys
from github import Github
from flask import Flask

############################################## IMPORTING THE REQUIRED MODULES ##################################################

app = Flask(__name__)

# getting the github credentials authenticated by passing them as an argument to the Github constructor
g = Github();
user = g.get_user('sithu')

#Getting the URL to the github repo which is explicitly passed as a command line argument by the user
gitUrl = sys.argv[1];

#Splitting the github URL and obtaining the name of the repository whose files need to be accessed
gitUrl = gitUrl.split("/");
repo = user.get_repo(gitUrl[-1])



############################################## ESTABLISHING THE NAVIGATION ROUTES ##################################################

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/v1/<filename>-config.json")
def msgJson(filename):
	file_path = filename+"-config.json"
	file = repo.get_file_contents(file_path)
	return "%s"%file.decoded_content

@app.route("/v1/<filename>-config.yml")
def msgYml(filename):
	file_path = filename+"-config.yml"
	file = repo.get_file_contents(file_path)

	return "%s"%file.decoded_content

if __name__ == "__main__":
    app.run()

##################################################### END OF FILE #########################################################
