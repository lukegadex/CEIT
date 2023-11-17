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
                mail bcc: '', body: 'Testing Pipeline Script', cc: '', from: '', replyTo: '', subject: '', to: 'lukeceit57@gmail.com, blaisekilang4@gmail.com, jasmineejack@gmail.com'
        }
    }
}
