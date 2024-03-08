node('docker-agent-python') {
    // Define your Git credentials ID (configured in Jenkins)
    def gitCredentialsId = '94b3e0b8-6217-47a1-815e-bff2fc6c2545'

    stage('Checkout') {
        // Checkout code from Git repository using credentials
        checkout([$class: 'GitSCM', branches: [[name: '*/main']], userRemoteConfigs: [[credentialsId: gitCredentialsId , url: 'https://github.com/aman1011/superprof-chris.git']]])
    }

    stage('Install Dependencies') {
        try {
            sh 'pip install -r requirements.txt --break-system-packages'
        } catch (Exception e) {
            echo "Failed to install dependencies: ${e.message}"
            currentBuild.result = 'FAILURE'
            return
        }
    }

    stage('Run Unit Test') {
        try {
            sh 'python -m unittest discover'
        } catch (Exception e) {
            echo "Failed to run unit tests: ${e.message}"
            currentBuild.result = 'FAILURE'
            return
        }
    }

    stage('Linting') {
        try {
            sh 'pylint app.py test_app.py'
        } catch (Exception e) {
            echo "Failed to run linting: ${e.message}"
            currentBuild.result = 'FAILURE'
            return
        }
    }
}
