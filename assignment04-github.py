# Write a program in python that will read a file from a repository, 
# The program should then replace all the instances of the text "Andrew" with your name. 
# The program should then commit those changes and push the file back to the repository.

import requests 
import urllib.parse
from config import apikey as cfg  #importing the required apikey from config.py
from github import Github


old_name = "Andrew"
new_name = "Rebecca"

apikey = cfg["githubkey"]
g = Github(apikey)

repos = g.get_repo("rebeccaf1918/WSAA-coursework")
file_path = "rebeccaf1918/WSAA-coursework/name.txt"
contents = repos.get_contents(file_path)
file_content = contents.decoded_content.decode("utf-8")

def replace_name(file_content):
    updated_content = file_content.replace(old_name, new_name)
    return updated_content

updated_content = replace_name(file_content)

# Update the file in the repository
repos.update_file(file_path, f"Assignment 04: Updated name from {old_name} to {new_name}", updated_content, contents.sha)

