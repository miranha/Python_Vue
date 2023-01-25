pipeline {
    agent {
        docker {
            image 'jenkins/jenkins:lts'
        }
    }
    stages {
        stage('Build') {
            steps {
                sh 'which docker-compose'
                sh 'docker-compose build'
            }
        }
        stage('Deploy') {
            steps {
                sh 'docker-compose up -d'
            }
        }
    }
    post {
        always {
            sh 'docker-compose down'
        }
    }
}