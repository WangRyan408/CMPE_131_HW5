pipeline {
    agent any
    
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
                    python -m pytest -v test_weather_station.py
                    pytest --junitxml=test-results.xml
                    '''
            }
        }
    }
    
}