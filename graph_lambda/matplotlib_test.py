import matplotlib.pyplot as plt
import boto3

def lambda_handler(event, context):
    x = [10,20,30]
    y = [1,2,3]
    
    plt.plot(x, y)
    plt.savefig('/tmp/plot.png')
    
    s3 = boto3.resource('s3')
    s3.meta.client.upload_file('/tmp/plot.png', 'linkedinwebscrap', 'plot.png')