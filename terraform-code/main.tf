provider "aws" {
  region     = "us-east-1"
}



variable "Bucketname" {
  type = "string"
  default = "blahblahblah5" # limit 15 characters
}



resource "aws_s3_bucket" "b" {
  bucket = "${var.Bucketname}"
  acl    = "private"

  tags {
    Name        = "${var.Bucketname}"
    Environment = "Dev"
  }
}