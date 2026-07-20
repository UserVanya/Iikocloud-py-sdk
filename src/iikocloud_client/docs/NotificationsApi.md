# iikocloud_client.NotificationsApi

All URIs are relative to *https://api-ru.iiko.services*

Method | HTTP request | Description
------------- | ------------- | -------------
[**send_notification**](NotificationsApi.md#send_notification) | **POST** /api/1/notifications/send | Send notification to external systems.


# **send_notification**
> CorrelationIdResponse send_notification(timeout=timeout, send_notification_request=send_notification_request)

Send notification to external systems.



 > Restriction group: `Notifications`.

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.correlation_id_response import CorrelationIdResponse
from iikocloud_client.models.send_notification_request import SendNotificationRequest
from iikocloud_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-ru.iiko.services
# See configuration.py for a list of all supported configuration parameters.
configuration = iikocloud_client.Configuration(
    host = "https://api-ru.iiko.services"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: BearerAuth
configuration = iikocloud_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with iikocloud_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iikocloud_client.NotificationsApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    send_notification_request = iikocloud_client.SendNotificationRequest() # SendNotificationRequest |  (optional)

    try:
        # Send notification to external systems.
        api_response = await api_instance.send_notification(timeout=timeout, send_notification_request=send_notification_request)
        print("The response of NotificationsApi->send_notification:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationsApi->send_notification: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **send_notification_request** | [**SendNotificationRequest**](SendNotificationRequest.md)|  | [optional] 

### Return type

[**CorrelationIdResponse**](CorrelationIdResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**408** | Request Timeout |  -  |
**500** | Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

