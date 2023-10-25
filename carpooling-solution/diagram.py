from diagrams import Cluster, Diagram
from diagrams.aws.network import ELB, VPC
from diagrams.aws.compute import EC2, ECS, Lambda
from diagrams.aws.database import RDS
from diagrams.aws.storage import S3
from diagrams.aws.security import IAM
from diagrams.aws.management import Cloudwatch
from diagrams.aws.integration import SNS

with Diagram("Solución Carpooling en AWS", show=False):

    with Cluster("VPC"):
        with Cluster("Frontend & Backend"):
            elb = ELB("Elastic Load Balancer")
            web = EC2("EC2 Web")
            mobile = EC2("EC2 Mobile")
            api = ECS("ECS API")
            elb >> [web, mobile, api]

        with Cluster("Base de datos"):
            db = RDS("RDS PostgreSQL")

        with Cluster("Almacenamiento"):
            storage = S3("S3 bucket")

        with Cluster("Notificaciones"):
            email = Lambda("Lambda Email") >> SNS("SES")
            sms = Lambda("Lambda SMS") >> SNS("SNS SMS")

        api >> db
        web >> storage
        mobile >> storage
        api >> [email, sms]

    IAM("IAM Roles & Policies")
    Cloudwatch("CloudWatch Monitoring")
