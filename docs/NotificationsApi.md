# iikocloud_client.NotificationsApi

All URIs are relative to *https://api-ru.iiko.services*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api1_notifications_send_post**](NotificationsApi.md#api1_notifications_send_post) | **POST** /api/1/notifications/send | Send notification to external systems (iikoFront and iikoWeb).


# **api1_notifications_send_post**
> TransportCommonCorrelationIdResponse api1_notifications_send_post(timeout=timeout, transport_notifications_send_notification_request=transport_notifications_send_notification_request)

Send notification to external systems (iikoFront and iikoWeb).



 > Restriction group: `Notifications`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.transport_common_correlation_id_response import TransportCommonCorrelationIdResponse
from iikocloud_client.models.transport_notifications_send_notification_request import TransportNotificationsSendNotificationRequest
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

# Configure Bearer authorization (JWT): Bearer
configuration = iikocloud_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with iikocloud_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iikocloud_client.NotificationsApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    transport_notifications_send_notification_request = iikocloud_client.TransportNotificationsSendNotificationRequest() # TransportNotificationsSendNotificationRequest |  (optional)

    try:
        # Send notification to external systems (iikoFront and iikoWeb).
        api_response = await api_instance.api1_notifications_send_post(timeout=timeout, transport_notifications_send_notification_request=transport_notifications_send_notification_request)
        print("The response of NotificationsApi->api1_notifications_send_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationsApi->api1_notifications_send_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **transport_notifications_send_notification_request** | [**TransportNotificationsSendNotificationRequest**](TransportNotificationsSendNotificationRequest.md)|  | [optional] 

### Return type

[**TransportCommonCorrelationIdResponse**](TransportCommonCorrelationIdResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized |  -  |
**500** | Server Error |  -  |
**408** | Request Timeout |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

