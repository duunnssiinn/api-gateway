The choosen build automation tool is Jenkins >> https://www.jenkins.io/

A Jenkinsfile has been added to the root of the application

To use the Jenkinsfile, a jenkins instance is needed.

Then the jenkins is connected to github via a webhook creation , 
such that once there is a commit or a push to the main branch, 

that triggers jenkins which then runs the pipeline script 
scripted into the provided Jenkinsfile.