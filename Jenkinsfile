pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/lukegadex/CEIT.git']])
            }
        }
         stage('Test') {
            steps {
                git branch: 'main', url: 'https://github.com/lukegadex/CEIT.git'
                sh 'python3 jenkins.py'
            }
        }
         stage('Deploy') {
            steps {
                sh 'python3 -m jenkins'
                echo 'Deploy code'
            }
        }
    }
    post {
        success {
               mail bcc: '', body: '''Build has been successful. Refer to the link for an insight 
                    https://github.com/jasminejack12345/ann.git''', cc: '', from: '', replyTo: '', subject: 'CI/CD Pipeline', to: 'jasmineejack@gmail.com, jahno743@gmail.com, blaisekilang4@gmail.com, lukegadebo@gmail.com'          
        }
        failure {
            mail bcc: '', body: 'For more infor on the pipeline failure, tap the link and build jenkinsfile to checkout the console output at https://github.com/jasminejack12345/ann.git', cc: '', from: '', replyTo: '', subject: 'CI/CD pipeline Build has failed,', to: 'anneludemejay@gmail.com, jahno743@gmail.com, blaisekilang4@gmail.com, lukegadebo@gmail.com'
           }
       }
}         
