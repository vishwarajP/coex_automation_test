pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout([
                    $class: 'GitSCM',
                    branches: [[name: '*/main']], // Change to '*/master' if needed
                    extensions: [],
                    userRemoteConfigs: [[
                        credentialsId: 'github-token', // Create this in Jenkins Credentials
                        url: 'https://github.com/vishwarajP/coex_automation_test.git'
                    ]]
                ])
            }
        }

        stage('Setup') {
            steps {
                bat 'python -m venv venv'
                bat 'venv\\Scripts\\pip install pytest pytest-html'
            }
        }

        stage('Test') {
            steps {
                bat 'venv\\Scripts\\pytest test/ --html=report.html'
            }
            post {
                always {
                    publishHTML(target: [
                        reportDir: '.',
                        reportFiles: 'report.html',
                        reportName: 'Test Results'
                    ])
                }
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}