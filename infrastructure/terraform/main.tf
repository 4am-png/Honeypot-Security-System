provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "honeypot" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"
  key_name      = "my-key"

  tags = {
    Name = "HoneypotServer"
  }
}
