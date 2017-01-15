# Week 1 Exercises

## GIT
1.  Create a GitHub account (it's free for public repositories).
****Already existing; [see here](https://github.com/eronlloyd).****

2.  Create a repository for the work that you will do in this class.
Class repository online at
****[eronlloyd/pynet_lab](https://github.com/eronlloyd/pynet_lab)****

3.  Clone the repository that you just created on GitHub into your home directory in the lab environment.
****Complete****

4.  Add a file to the repository in the lab environment and then push it up
to GitHub.
****Complete****

5.  Create a  'test' branch in your repository.
    a. Switch between the 'master' branch and the 'test' branch.
    b. Add a file to the 'test' branch.
    c. Switch back to the 'master' branch.
    d. Merge this 'test' branch into your 'master' branch.
****Complete****

## YAML/JSON
6.  Write a Python program that creates a list. One of the elements of the list should be a dictionary with at least two keys. Write this list out to a file using both YAML and JSON formats. The YAML file should be in the expanded form.
****Complete; see list_outputs.py****

7.  Write a Python program that reads both the YAML file and the JSON file
created in exercise6 and pretty prints the data structure that is returned.  
****Complete; see list_inputs.py****

## ciscoconfparse
8.  Write a Python program using ciscoconfparse that parses this config file. Note, this config file is not fully valid (i.e. parts of the configuration are missing). The script should find all of the crypto map entries in the file (lines that begin with 'crypto map CRYPTO') and for each crypto map entry print out its children.
****Complete; see cisco_parser.py****

9.  Find all of the crypto map entries that are using PFS group2
****Complete; see cisco_parser.py****

10. Using ciscoconfparse find the crypto maps that are not using AES (based-on the transform set name). Print these entries and their corresponding transform set name.
****Complete; see cisco_parser.py****

11. Check the answers for exercises 6-10 into Git and push them up to Github
****Done!****
