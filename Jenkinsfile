node {
  checkout scm
  docker.withRegistry('https://registry.hub.docker.com','dockerHub') {
  def customImage = docker.build("3117/my-python-project")
  customImage.push()
  }
}
