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

        // Stage 3: Scan files for security vulnerabilities and save report
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

        // Stage 5: Start containers
        stage('Run Containers') {
            steps {
                sh 'docker run -d --name flask-app --network my-network flask-app'
                sh 'docker run -d --name nginx-proxy --network my-network -p 80:80 nginx-proxy'
                sh 'sleep 3'
            }
        }

        // Stage 6: Run integration tests against the live app
        stage('Unit Test') {
            steps {
                sh '''
                    python3 -m venv venv
                    venv/bin/pip install requests --quiet
                    venv/bin/python3 Task1/test_app.py -v
                '''
            }
        }

    }

    post {
        always {
            // Archive the Trivy scan results as a downloadable artifact
            archiveArtifacts artifacts: 'trivy-fs-results.json', allowEmptyArchive: true
        }
    }
}
