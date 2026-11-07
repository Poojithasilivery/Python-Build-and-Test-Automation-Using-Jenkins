pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Starting Python Build'
                bat '"C:\\Users\\siliv\\AppData\\Local\\Microsoft\\WindowsApps\\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\\python.exe" app.py'
            }
        }

        stage('Test') {
            steps {
                echo 'Running Python Tests'
                bat '"C:\\Users\\siliv\\AppData\\Local\\Microsoft\\WindowsApps\\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\\python.exe" -m unittest test_app'
            }
        }

        stage('Success') {
            steps {
                echo 'Build and Testing Completed Successfully'
            }
        }
    }
}