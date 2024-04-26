/* Requires the Docker Pipeline plugin */
pipeline {
    agent { docker { image 'python:3.12.1-alpine3.19' } }
    environment {
        BASE_URL     = credentials('jenkins-front-base-url')
    }
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
            source .venv/bin/activate
            pip install -r requirements.txt
            sudo apt-get install chromium-chromedriver
                '''
            }
        }
        stage('run robot test') {
            steps {
                sh '''
                source .venv/bin/activate
                robot ./tests/robot/login-page.robot
                '''
            }
        }
    }
}
