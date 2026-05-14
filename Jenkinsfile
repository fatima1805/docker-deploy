pipeline {
    agent any

    stages {

        // Remove old containers
        stage('Clean-up') {
            steps {
                sh 'docker rm -f flask-app nginx-proxy || true'
                sh 'docker network rm my-network || true'
            }
        }

        // Create Docker network
        stage('Set-up') {
            steps {
                sh 'docker network create my-network'
            }
        }

        // Build images
        stage('Build Images') {
            steps {
                sh 'docker build -t flask-app ./Task1'
                sh 'docker build -t nginx-proxy ./nginx'
            }
        }

        // Start containers
        stage('Run Containers') {
            steps {
                sh 'docker run -d --name flask-app --network my-network flask-app'
                sh 'docker run -d --name nginx-proxy --network my-network -p 80:80 nginx-proxy'
            }
        }

    }
}
