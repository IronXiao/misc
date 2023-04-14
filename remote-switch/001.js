
/**
 * @fileoverview Template to compose HTTP reqeuest.
 * 
 */

const url = `https://api.smart.jd.com/c/service/integration/v1/controlDeviceCard?plat=iPhone&hard_platform=iPhone14,5&app_version=1.6.3&plat_version=15.5&device_id=92c583e25de6700cf329470b690ad&channel=AppStore`;
const method = `POST`;
const headers = {
'appversion' : `1.6.3`,
'tgt' : `AAJii77ZAECia9BaxLuVQ3MrOmJzidVjX0iKZE2gTOUpbBfViM3Vvfn0khgblPI-7w00TfaZneI`,
'appplatform' : `iPhone14,5`,
'authorization' : `smart a188caaf009839ba200bfa38407a595c2a:::NLQchaaCKWjTHheus=:::2022-05-24T01:22:27.095Z`,
'content-type' : `application/json; charset=utf-8`,
'app_identity' : `WL`,
'host' : `api.smart.jd.com`,
'user-agent' : `Dart/2.16 (dart:io)`,
'accept-encoding' : `gzip`,
'appplatformversion' : `15.5`
};
const body = `{"json":{"version":"2.0","feed_id":"9078913327","command":[{"stream_id":"Power","options":[{"0":"关"},{"1":"开"}]}]}}`;

const myRequest = {
    url: url,
    method: method,
    headers: headers,
    body: body
};

$task.fetch(myRequest).then(response => {
    console.log(response.statusCode + "\n\n" + response.body);
    $done();
}, reason => {
    console.log(reason.error);
    $done();
});
