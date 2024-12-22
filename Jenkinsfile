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
                bat 'python -m venv dash_env'
                bat '.\\dash_env\\Scripts\\activate && pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                // Run unit tests
                bat '.\\dash_env\\Scripts\\activate && pytest tests\\'
            }
        }

        stage('Deploy Dashboard') {
            steps {
                // Deploy the dashboard
                bat '.\\dash_env\\Scripts\\activate && python app.py &'
            }
        }
    }

    post {
        always {
            echo 'Pipeline Completed!'
        }
    }
}
