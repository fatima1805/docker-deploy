 pipeline {
    agent any

    stages {

        stage('Clean-up') {
            steps {
                sh 'docker rm -f flask-app nginx-proxy || true'
                sh 'docker network rm my-network || true'
            }
        }

        stage('Set-up') {
            steps {
                sh 'docker network create my-network'
            }
        }

        stage('File System Scan') {
            steps {
                sh 'trivy fs --severity HIGH,CRITICAL -f json -o trivy-fs-results.json .'
            }
        }

        stage('Build Images') {
            steps {
                sh 'docker build -t flask-app ./Task1'
                sh 'docker build -t nginx-proxy ./nginx'
            }
        }

        stage('Run Containers') {
            steps {
                sh 'docker run -d --name flask-app --network my-network flask-app'
                sh 'docker run -d --name nginx-proxy --network my-network -p 80:80 nginx-proxy'
                sh 'sleep 3'
            }
        }

        stage('Unit Test') {
            steps {
                sh 'pip install requests --quiet'
                sh 'python3 Task1/test_app.py -v'
            }
        }

    }

    post {
        always {
            archiveArtifacts artifacts: 'trivy-fs-results.json', allowEmptyArchive: true
        }
    }
}
