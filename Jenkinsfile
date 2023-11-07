pipeline {
    agent any

    stages {
        stage('version') {
            steps {
                sh 'python3 --version'
            }
        }
        stage('jenkins') {
            steps {
                sh 'python3 jenkins.py'
            }
        }
        stage('Email Notification') {
            steps {
                mail bcc: '', body: 'Test has failed.', cc: '', from: '', replyTo: '', subject: 'Jenkins Code Test', to: 'lukeceit57@gmail.com'
            }
        }
    }
}
