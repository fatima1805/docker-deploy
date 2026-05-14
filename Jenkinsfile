pipeline {
    agent any

    stages {

        // Stage 1: Remove old containers and network
        stage('Clean-up') {
            steps {
                sh 'docker rm -f flask-app nginx-proxy || true'
                sh 'docker network rm my-network || true'
            }
        }

        // Stage 2: Create Docker network
        stage('Set-up') {
            steps {
                sh 'docker network create my-network'
            }
        }

        // Stage 3: Scan the filesystem for vulnerabilities and save results
        stage('File System Scan') {
            steps {
                sh 'trivy fs --severity HIGH,CRITICAL -f json -o trivy-fs-results.json .'
            }
        }

        // Stage 4: Build Docker images
        stage('Build Images') {
            steps {
                sh 'docker build -t flask-app ./Task1'
                sh 'docker build -t nginx-proxy ./nginx'
            }
        }

        // Stage 5: Start both containers
        stage('Run Containers') {
            steps {
                sh 'docker run -d --name flask-app --network my-network flask-app'
                sh 'docker run -d --name nginx-proxy --network my-network -p 80:80 nginx-proxy'
            }
        }

    }

    post {
        always {
            // Archive the Trivy scan results
            archiveArtifacts artifacts: 'trivy-fs-results.json', allowEmptyArchive: true
        }
    }
}
