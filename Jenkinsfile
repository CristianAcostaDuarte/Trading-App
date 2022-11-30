pipeline {
  agent any
  stages {
    stage("verify tooling") {
      steps {
        sh '''
          docker version
          docker info
          docker compose version 
          curl --version
          jq --version
        '''
      }
    }
    stage('Prune Docker data') {
      steps {
        sh 'docker system prune -a --volumes -f'
      }
    }
    stage('Fetch code') {
      steps {
        sh 'sudo apt-get update'
        sh 'sudo apt-get install git-all'
        sh 'git clone https://github.com/CristianAcostaDuarte/StockApp'
      }
    }
    stage('Start container') {
      steps {
        sh 'docker compose up -d --no-color --wait'
        sh 'docker compose ps'
      }
    }
    stage('Run tests against the container') {
      steps {
        sh 'test.py'
      }
    }
  }
  post {
    always {
      sh 'docker compose down --remove-orphans -v'
      sh 'docker compose ps'
    }
  }
}