import json
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.cvm.v20170312 import cvm_client, models
try:
    SecretId = "AKIDvjNo11nKcgW7TaT7j9NM6seR3Rn3EE1a"
    SecretKey = "XXX"
    cred = credential.Credential("SecretId", "SecretKey")
    
    httpProfile = HttpProfile()
    httpProfile.endpoint = "cvm.tencentcloudapi.com"

    clientProfile = ClientProfile()
    clientProfile.httpProfile = httpProfile
    client = cvm_client.CvmClient(cred, "", clientProfile)

    req = models.DescribeZonesRequest()
    params = {

    }
    req.from_json_string(json.dumps(params))

    resp = client.DescribeZones(req)
    print(resp.to_json_string())

except TencentCloudSDKException as err:
    print(err)
