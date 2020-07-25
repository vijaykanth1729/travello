node {
  checkout scm
  docker.withRegistry('https://hub.docker.com','dockerHub') {
  def customImage = docker.build("3117/my-python-project-new")
  customImage.push()
  }
}
