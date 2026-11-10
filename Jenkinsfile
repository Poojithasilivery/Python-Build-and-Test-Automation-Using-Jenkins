
pipeline {
    agent any

    stages {

        stage('Build') {
            steps {
                echo 'Checking Python Application'
                bat '"C:\\Users\\siliv\\AppData\\Local\\Programs\\Python\\Python312\\python.exe" -m py_compile app.py'
            }
        }

        stage('Test') {
            steps {
                echo 'Running Automated Tests'
                bat '"C:\\Users\\siliv\\AppData\\Local\\Programs\\Python\\Python312\\python.exe" -m unittest test_app -v'
            }
        }

        stage('Success') {
            steps {
                echo 'Smart Parking Project Build Successful!'
            }
        }
    }
}
