
pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Starting Python Build'
                bat 'python app.py'
            }
        }

        stage('Test') {
            steps {
                echo 'Running Python Tests'
                bat 'python -m unittest test_app'
            }
        }

        stage('Success') {
            steps {
                echo 'Build and Testing Completed Successfully'
            }
        }
    }
}
