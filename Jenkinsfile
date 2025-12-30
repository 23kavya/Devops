pipeline {
    agent any

    stages {

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t campus-helpdesk .'
            }
        }

        stage('Run Container') {
            steps {
                sh '''
                docker stop campus-helpdesk || true
                docker rm campus-helpdesk || true
                docker run -d --name campus-helpdesk -p 5000:5000 campus-helpdesk
                '''
            }
        }
    }
}
