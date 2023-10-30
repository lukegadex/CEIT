pipeline {
    agent any

    stages {
        stage('version') {
            steps {
                sh 'python --version'
            }
        }
        stage('jenkins') {
            steps {
                sh 'python3 jenkins.py'
            }
        }
    }
}
