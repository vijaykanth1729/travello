node {
  checkout scm
  docker.withRegistry('https://587354497551.dkr.ecr.us-east-1.amazonaws.com','demo-ecr-credentials') {
  def customImage = docker.build("demo")
  customImage.push()
  }
}
