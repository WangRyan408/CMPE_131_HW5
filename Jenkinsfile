pipeline {
    agent any
    
    environment {
        DB_URL = 'mysql+pymysql://usr:pwd@host:/db'
    }
    
    stages {
       stage('Setup Python/Build') {
            steps {
                withPythonEnv('Python3') {
                    sh '''
                        python -m venv venv
                        . venv/bin/activate
                        pip install -r requirements.txt
                    '''
                }
            }
        }
        
        stage('Test') {
            steps {
                withPythonEnv('Python3') {
                    sh 'pytest tests/ --junitxml=test-results.xml'
                }
            }
        }
        
        stage('Deploy') {
            steps {
                withPythonEnv('Python3') {
                     sh 'python deploy.py'
                }
            }
        }
    }
    
    post {
        always {
            junit 'test-results.xml'
        }
    }
}