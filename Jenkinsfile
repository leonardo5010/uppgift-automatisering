pipeline {
    agent any
    stages {
        stage('Testing GitHub-tests locally') {
            steps {
                dir('C:/Users/L_rad/OneDrive/Skrivbord/uppgift automatisering'){ 
                    bat 'python -m unittest'
                }
            }
        }
        stage('Clean Workspace'){
            steps {
                cleanWs()
            }
        }
        }
    }
