pipeline {
    agent any
	tools {
		maven ‘Maven’	
	}

    environment {
        DOCKER_IMAGE_NAME = 'my-calculator-app'
    }

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/your-repo/my-calculator-app.git', branch: 'main'
            }
        }

        stage('Build and Package') {
            steps {
                script {
                    sh 'mvn clean package -DskipTests'
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker build -t ${DOCKER_IMAGE_NAME} .'
                }
            }
        }

        stage('Deploy') {
            steps {
                    echo 'Deploy stage here’
                }
            }
        }
    }

    post {
        always {
            sh 'docker system prune -af'
        }
    }
}
