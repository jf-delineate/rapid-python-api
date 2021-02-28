project = "companies"

# Labels can be specified for organizational purposes.
labels = { "foo" = "bar" }

# An application to deploy
app "companies-api" {
  build {
    use "pack" { }
  }

  deploy {
    use "docker" {
      service_port = 8000
    }
  }
}
