# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

# {fact rule=python-cdk-document-db-cluster-backup-retention-period@v1.0 defects=0}
import aws_cdk as cdk
from aws_cdk import Stack, Duration
from aws_cdk.aws_docdb import DatabaseCluster
from aws_cdk.aws_docdb import Login, BackupProps
from aws_cdk.aws_ec2 import InstanceType, InstanceClass, InstanceSize, Vpc

class CdkStarter(cdk.Stack):
    def __init__(self, scope: cdk.App, id: str):
        super(scope, id)

        # Compliant: Configures backup retention for 7 days, ensuring data recovery.
        DatabaseCluster(Stack, 'rDatabaseCluster', 
            instance_type=InstanceType.of(InstanceClass.R5, InstanceSize.LARGE),
            vpc=Vpc(Stack, 'rVpc'),
            backup=BackupProps(retention=Duration.days(7),),
            master_user=Login(
                username='foo',
                password='bar'
            )
        )
# {/fact}