pipeline {
    agent any 
    stages {

        stage("Install app dependencies"){
            sh "pip3 install -r requirements.txt"
        }

        stage("Run unit tests"){
            sh "cd src && python -m pytest"
        }
    }
}