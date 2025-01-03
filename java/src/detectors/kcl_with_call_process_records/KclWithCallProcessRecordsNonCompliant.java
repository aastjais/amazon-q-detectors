// Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: MIT-0

// {fact rule=java-kcl-with-call-process-records-even-for-empty-record-list@v1.0 defects=1}
import com.amazonaws.auth.AWSCredentialsProvider;
import com.amazonaws.services.kinesis.clientlibrary.lib.worker.InitialPositionInStream;
import com.amazonaws.services.kinesis.clientlibrary.lib.worker.KinesisClientLibConfiguration;

public class KclWithCallProcessRecordsNonCompliant {

    private String applicationName;
    private String streamARN;
    private AWSCredentialsProvider ddbStreamCredentials;
    private String workerID;
    private int maxRecords;
    private long idleTimeBetweenReadsInMillis;
    private long leaseFailOverTimeInMillis;

    // Noncompliant: KinesisClientLibConfiguration initialized without setting withCallProcessRecordsEvenForEmptyRecordList.
    public KinesisClientLibConfiguration nonCompliant() {
        KinesisClientLibConfiguration kclConfig = new KinesisClientLibConfiguration(applicationName,
                streamARN, ddbStreamCredentials, workerID)
                .withMaxRecords(maxRecords)
                .withIdleTimeBetweenReadsInMillis(idleTimeBetweenReadsInMillis)
                .withFailoverTimeMillis(leaseFailOverTimeInMillis)
                .withInitialPositionInStream(InitialPositionInStream.TRIM_HORIZON);
        return kclConfig;
    }
}
// {/fact}
