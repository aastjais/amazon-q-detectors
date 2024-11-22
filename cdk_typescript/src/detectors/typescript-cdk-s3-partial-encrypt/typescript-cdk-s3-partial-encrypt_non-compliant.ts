// Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: MIT-0

// {fact rule=typescript-cdk-s3-partial-encrypt@v1.0 defects=0}
import * as cdk from 'aws-cdk-lib';
import { Bucket } from 'aws-cdk-lib/aws-s3';

export class CdkStarterStack extends cdk.Stack {
  constructor(scope: cdk.App, id: string, props?: cdk.StackProps) {
    super(scope, id, props);
    // Noncomplaint: Lacks encryption, leaving data unprotected.
    const badBucketDirect = new Bucket(this, 's3-bucket-bad')
  }
}
// {/fact}