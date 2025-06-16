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

        stage('Setup Python Environment') {
            steps {
                bat """
                    python -m venv venv
                    venv\\Scripts\\pip install --upgrade pip
                    venv\\Scripts\\pip install paramiko==3.5.1 PyYAML==6.0.2 pytest==8.4.0 setuptools==80.9.0
                    venv\\Scripts\\pip install pytest-html  # Additional test reporting
                """
            }
        }

        stage('Run Tests') {
            steps {
                bat 'venv\\Scripts\\pytest test/ --html=report.html'
            }
            post {
                always {
                    archiveArtifacts artifacts: 'report.html', fingerprint: true
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