

resource "aws_s3_bucket" "b" {
  bucket = "${var.Bucketname}"
  acl    = "private"

  tags {
    Name        = "${var.Bucketname}"
    Environment = "Dev"
  }
}

output "BucketnameOutput" {
  value = "${aws_s3_bucket.b.bucket}"
}

output "TestOutput" {
  value = "${aws_s3_bucket.b.tags}
}

