provider "aws" {
    region = "ap-south-1"
}

resource "aws_instance" "foo" {
  ami           = "ami-007020fd9c84e18c7" 
  instance_type = "t2.micro"
  vpc_security_group_ids = "sg-046e334f94d46f520"
  key_name = "ssh-key.pem"

  tags = {
    Name = "tf-example"
  }
}
  
