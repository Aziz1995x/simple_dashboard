pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                // Clone GitHub repository
                git branch: 'main', url: 'https://github.com/Aziz1995x/simple_dashboard.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                // Install Python dependencies
                sh 'python3 -m venv dash_env'
                sh '. dash_env/bin/activate && pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                // Run unit tests
                sh '. dash_env/bin/activate && pytest tests/'
            }
        }

        stage('Deploy Dashboard') {
            steps {
                // Deploy the dashboard
                sh '. dash_env/bin/activate && python app.py &'
            }
        }
    }

    post {
        always {
            echo 'Pipeline Completed!'
        }
    }
}
