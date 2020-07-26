node {
  stage 'Checkout'
  git 'https://github.com/vijaykanth1729/docker-web-app.git'

  stage 'Docker build'
  docker.build('demo')

  stage 'Docker push'
  docker.withRegistry('https://587354497551.dkr.ecr.us-east-1.amazonaws.com', 'ecr:us-east-1:myAws') {
    docker.image('demo').push('latest')
  }
}
