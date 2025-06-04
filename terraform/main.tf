provider "aws" {
  region = "us-east-1"
}

resource "aws_s3_bucket" "mlops_bucket" {
  bucket = "mlops-model-artifact-bucket-ak"
  force_destroy = true
}