pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/sameabrazao/qaia_api.git' // Replace with your repository URL
            }
        }

        stage('Set up Python Environment') {
            steps {
                sh 'python3 -m venv venv'
                sh '. venv/bin/activate'
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh '. venv/bin/activate && python -m unittest discover -s tests'
            }
        }
    }

    post {
        always {
            junit '**/test-results.xml'
        }
    }
}