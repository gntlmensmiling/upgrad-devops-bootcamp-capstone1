pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                script {
                    docker.build('hello_world_image')
                }
            }
        }
        stage('Deploy') {
            steps {
                script {
                    sh 'kubectl apply -f deployment.yaml'
                    sh 'kubectl apply -f service.yaml'
                }
            }
        }
    }
}
