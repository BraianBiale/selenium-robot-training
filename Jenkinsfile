/* Requires the Docker Pipeline plugin */
pipeline {
    agent { docker { image 'python:3.12.1-alpine3.19' } }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
            }
        }
        stage('install requirements') {
            steps {
                sh '''
            python -m venv .venv
            . .venv/bin/activate
            pip install -r requirements.txt
                '''
            }
        }
        stage('run robot test') {
            steps {
                sh 'robot ./tests/robot/login-page.robot'
            }
        }
    }
}
