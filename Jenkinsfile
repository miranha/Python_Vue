pipeline {
    environment {
        PATH = "$PATH:/usr/local/bin"
    }
    agent {
        docker {
            image 'jenkins/jenkins:lts'
        }
    }
    stages {
        stage('Build') {
            steps {
                sh '/usr/local/bin/docker-compose build'
            }
        }
        stage('Deploy') {
            steps {
                sh '/usr/local/bin/docker-compose up -d'
            }
        }
    }
    post {
        always {
            sh '/usr/local/bin/docker-compose down'
        }
    }
}