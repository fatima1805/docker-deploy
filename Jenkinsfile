pipeline {
    agent any  // run on any available Jenkins agent

    stages {

        // STAGE 1: Delete old containers so we start fresh
        stage('Clean-up') {
            steps {
                sh '''
                    ssh -o StrictHostKeyChecking=no ubuntu@54.235.58.138 \
                    "docker rm -f flask-app nginx-proxy || true && docker network rm my-network || true"
                '''
            }
        }

        // STAGE 2: Create a Docker network so containers can talk to each other
        stage('Set-up') {
            steps {
                sh '''
                    ssh -o StrictHostKeyChecking=no ubuntu@54.235.58.138 \
                    "docker network create my-network"
                '''
            }
        }

        // STAGE 3: Copy files to docker server and build the images
        stage('Build Images') {
            steps {
                sh '''
                    scp -o StrictHostKeyChecking=no -r Task1 ubuntu@54.235.58.138:~/Task1
                    scp -o StrictHostKeyChecking=no -r nginx ubuntu@54.235.58.138:~/nginx
                    ssh -o StrictHostKeyChecking=no ubuntu@54.235.58.138 \
                    "docker build -t flask-app ~/Task1 && docker build -t nginx-proxy ~/nginx"
                '''
            }
        }

        // STAGE 4: Start both containers on the network
        stage('Run Containers') {
            steps {
                sh '''
                    ssh -o StrictHostKeyChecking=no ubuntu@54.235.58.138 \
                    "docker run -d --name flask-app --network my-network flask-app && \
                     docker run -d --name nginx-proxy --network my-network -p 80:80 nginx-proxy"
                '''
            }
        }

    }
}
