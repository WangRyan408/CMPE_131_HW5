pipeline {
    agent any
    
    environment {
        DB_URL = 'mysql+pymysql://usr:pwd@host:/db'
    }
    
    stages {
       stage('Setup Python') {
            steps {
                sh '''
                    python3 -m venv .venv
                    . .venv/bin/activate
                    python -m pip install --upgrade pip
                    python -m pip install -r requirements.txt
                '''
            }
        }
        
        stage('Test') {
            steps {
                    sh '''
                     . .venv/bin/activate
                    python -m pytest
                    pytest tests/ --junitxml=test-results.xml
                    '''
            }
        }
    }
    
    post {
        always {
            junit 'test-results.xml'
        }
    }
}