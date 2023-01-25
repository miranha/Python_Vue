pipeline {
    agent {
        docker {
            image 'jenkins/jenkins:lts'
        }
    }
    stages {
        stage('Build') {
            steps {
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