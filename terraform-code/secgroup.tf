resource "aws_security_group" "crypto" {
  name = "${var.Bucketname}"
  tags {
        Name = "${var.Bucketname}"
  }
  description = "${var.Bucketname} SG"
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
