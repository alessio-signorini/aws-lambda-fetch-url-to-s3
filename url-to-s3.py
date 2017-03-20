import urllib2
import boto3
import time

def lambda_handler(event, context):
    url  = event["url"]
    path = "%s/%s" % (event["path"], time.time())

    response = urllib2.urlopen(url)

    s3 = boto3.resource('s3')
    o  = s3.Object('backups', path).initiate_multipart_upload()

    i = 1
    parts = []
    while True:
        chunk = response.read(200 * 1000000)
        if chunk:
            x = o.Part(i).upload(Body=chunk)
            parts.append({"ETag":x["ETag"], "PartNumber":i})
            del(chunk)
            if i == 3:
                break
        else:
            break
        print i
        i = i + 1


    r = o.complete(
        MultipartUpload={
            'Parts': parts
        }
    )

    return 'Ok'



if __name__ == '__main__':
    url = 'http://static.echonest.com/millionsongsubset_full.tar.gz'
    event = {"url":url, "path":"datasets/millionsongs"}
    print lambda_handler(event,{})
