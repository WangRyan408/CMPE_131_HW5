pipeline {
    agent any
    
    environment {
        DB_URL = 'mysql+pymysql://usr:pwd@host:/db'
    }
    
    stages {
        stage('Create Virtual Environment') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                '''
            }
        }
        
        stage('Build') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        
        stage('Test') {
            steps {
                sh 'pytest tests/ --junitxml=test-results.xml'
            }
        }
        
        stage('Deploy') {
            steps {
                sh 'python deploy.py'
            }
        }
    }
    
    post {
        always {
            junit 'test-results.xml'
        }
    }
}