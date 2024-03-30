# assignment04-github.py
# Author: Rebecca Feeley

# Write a program in python that will read a file from a repository, 
# The program should then replace all the instances of the text "Andrew" with your name. 
# The program should then commit those changes and push the file back to the repository.

import requests 
import urllib.parse
from config import apikey as cfg  #importing the required apikey from config.py
from github import Github

url = "https://api.github.com/repos/rebeccaf1918/WSAA-coursework"

apikey = cfg["githubkey"]
g = Github(apikey)

repo = g.get_repo("rebeccaf1918/WSAA-coursework") # getting the repository so I can interact with it
contents = repo.get_contents("name.txt") # Get the file contents from the specified repository
file_content = contents.decoded_content.decode("utf-8") # using utf-8 to decode from bytes to strings

def replace_name(file_content): # defining a function to complete the changing of the name Andrew to Rebecca
    updated_content = file_content.replace("Andrew", "Rebecca") # replacing instances of Andrew with Rebecca
    return updated_content

updated_content = replace_name(file_content) 

# Update the file in the repository with the changes included with a commit messsage 
repo.update_file(contents.path, f"Assignment 04: Updated name", updated_content, contents.sha, branch = "main")

