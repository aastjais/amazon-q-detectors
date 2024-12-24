# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

# {fact rule=python-cdk-enabled-access-logging-for-cloudfront-distribution@v1.0 defects=0}
from aws_cdk.aws_cloudfront import Distribution, BehaviorOptions, OriginAccessIdentity
from aws_cdk.aws_s3 import Bucket
import aws_cdk as cdk
   
class CdkStarter(cdk.Stack):
    def __init__(self, scope: cdk.App, id: str):
        super(scope, id)
    
        # Compliant: Specifies `log_bucket` for logging.
        logs_bucket = Bucket(self, "LoggingBucket")  
        Distribution(self, "Distribution",
            default_behavior=BehaviorOptions(
                origin=OriginAccessIdentity(
                    Bucket(self, "OriginBucket") 
                )
            ),
            log_bucket=logs_bucket
        )
# {/fact}