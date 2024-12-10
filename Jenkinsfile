pipeline {
    agent any
    
    environment {
        DB_URL = 'mysql+pymysql://usr:pwd@host:/db'
    }
    
    stages {
        stage('Build') {
            steps {
                sh 'source venv/bin/activate'
                sh 'pip install -r requirements.txt'
            }
        }
        
        stage('Test') {
            steps {
                sh 'source venv/bin/activate'
                sh 'pytest tests/ --junitxml=test-results.xml'
            }
        }
        
        stage('Deploy') {
            steps {
                sh 'source venv/bin/activate'
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