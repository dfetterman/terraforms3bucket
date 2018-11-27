

resource "aws_s3_bucket" "b" {
  bucket = "${var.Bucketname}"
  acl    = "private"

  tags {
    Name        = "${var.Bucketname}"
    Environment = "Dev"
  }
}



resource "aws_security_group" "c" {
  name = "${var.Bucketname}"
  tags {
        Name = "${var.prefix}"
  }
  description = "${var.prefix} SG"
  egress {
    from_port   = 0
    to_port     = 65535 # All outbound traffic
    protocol    = "TCP"
    cidr_blocks = ["0.0.0.0/0"]
   }
   ingress {
     from_port   = 443
     to_port     = 443 # All outbound traffic
     protocol    = "TCP"
     cidr_blocks = ["0.0.0.0/0"]
    }
}



output "BucketnameOutput" {
  value = "${aws_s3_bucket.b.bucket}"
}

output "SG" {
  value = "${aws_security_group.c.name}"
}


