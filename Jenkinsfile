pipeline {
    agent any  // Runs on any available Jenkins agent

    stages {
        // Stage 1: Checkout code from GitHub
        stage('Checkout') {
            steps {
                git 'https://github.com/vishwarajP/coex_automation_test.git'
            }
        }

        // Stage 2: Setup Python & dependencies
        stage('Setup') {
            steps {
                bat 'python -m venv venv'
                bat 'venv\\Scripts\\pip install pytest pytest-html'
            }
        }

        // Stage 3: Run tests
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

    // Clean up after build
    post {
        always {
            cleanWs()  // Cleans workspace
        }
    }
}