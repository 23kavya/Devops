pipeline {
    agent any

    stages {

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t campus-helpdesk .'
            }
        }

        stage('Run Container') {
            steps {
                bat '''
                docker stop campus-helpdesk || exit 0
                docker rm campus-helpdesk || exit 0
                docker run -d --name campus-helpdesk -p 5000:5000 campus-helpdesk
                '''
            }
        }
    }
}
