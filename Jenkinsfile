node {
  checkout scm
  docker.withRegistry('https://587354497551.dkr.ecr.us-east-1.amazonaws.com','myAws') {
  def customImage = docker.build("my-python-project-new")
  customImage.push()
  }
}
