pipeline {
    agent any
    environment {
      registryCredential = 'mrunalsh'
    }
  stages {
    stage('Checkout') {
      steps {
        // git clone
        checkout scm
      }
    }
    stage('Build') {
      steps {
        // calling bild function from docker
        script {
          app = docker.build('python-app-todo')
        }
      }
    }
    stage('Test') {
      steps {
        // access app
        script {
          app.inside {
            sh 'echo test pass'
          }
        }
      }
    }
    stage('Deploy Image') {
      steps {
          sh 'docker push python-app-todo' 
          // script {
          //   docker.withRegistry('', registryCredential) {
          //   dockerImage.push("$BUILD_NUMBER")
          //   dockerImage.push('latest')
          //   }
          }
      }
    }
  }

