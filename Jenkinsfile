pipeline {

    agent any

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/YOUR_USERNAME/linear-regression-ml.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    python3 -m pip install -r requirements.txt
                '''
            }
        }

        stage('Test ML Application') {
            steps {
                sh '''
                    python3 -c "import pandas; import sklearn; import flask; print('Dependencies OK')"
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                    docker build -t linear-regression-ml:latest .
                '''
            }
        }

        stage('Run Docker Container') {
            steps {
                sh '''
                    docker stop linear-regression-ml || true
                    docker rm linear-regression-ml || true

                    docker run -d \
                        --name linear-regression-ml \
                        -p 5000:5000 \
                        linear-regression-ml:latest
                '''
            }
        }
    }
}