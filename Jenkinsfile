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
                    call venv\\Scripts\\activate
                    python -m pip install --upgrade pip
                    pip install paramiko==3.5.1 PyYAML==6.0.2 pytest==8.4.0 setuptools==80.9.0
                    pip install pytest-html
                """
            }
        }

        stage('Run Tests') {
            steps {
                bat """
                    call venv\\Scripts\\activate
                    pytest test/ --html=report.html
                """
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