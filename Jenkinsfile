pipeline {

    agent any

    stages {

        stage('Install Dependencies') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Test ML Application') {
            steps {
                sh '''
                    . venv/bin/activate
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
