pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'python3 -m venv venv'
                sh '. venv/bin/activate && pip install bandit'
            }
        }

        stage('Security Scan') {
            steps {
                sh '. venv/bin/activate && bandit -r .'
            }
        }
    }

    post {
        always {
            sh 'rm -rf venv'
        }
    }
}
