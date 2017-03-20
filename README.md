# aws-lambda-fetch-url-to-s3
AWS Lambda Python Script to fetch/save a URL on S3

This is a simple Python script for an AWS Lambda function that fetches the content of a URL specified in the parameters and save its content in a bucket/path on Amazon S3. It can be useful to move large files without having to fully download them first.

The original idea was to use it to transfer Heroku Postgres backups from the URL links provided by the heroku-cli to a more permanent location in our own S3 buckets. Unfortunately there is a 5-minutes limitation in AWS Lambda right and the size of our backups would require at least 30 minutes.

### Local Testing
To test the script locally create a `~/.boto` file in your home directory with the right AWS Access Key/Secret:

    [Credentials]
    aws_access_key_id = YOUR_ACCESS_KEY_ID
    aws_secret_access_key = YOUR_SECRET_ACCESS_KEY

### Deploy on AWS Lambda
1. Go to AWS Lambda and create a [Function](https://console.aws.amazon.com/lambda/home?region=us-east-1#/functions)
2. Configure it for at least 512Mb of RAM and set the `handler` to `lambda_function.lambda_handler`
3. Make sure to assign it a IAM Role which allows the `ObjectPut` operation on the S3 bucket you want to write to and its descendents (`.../*`)
