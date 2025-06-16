pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout([
                    $class: 'GitSCM',
                    branches: [[name: '*/main']],
                    userRemoteConfigs: [[
                        credentialsId: 'github-token',
                        url: 'https://github.com/vishwarajP/coex_automation_test.git'
                    ]]
                ])
            }
        }

        stage('Setup') {
            steps {
                bat 'python -m venv venv'
                bat 'venv\\Scripts\\pip install -r requirements.txt'  // If you have one
                bat 'venv\\Scripts\\pip install pytest pytest-html paramiko'
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
                        reportName: 'Test Report'
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