# iikocloud_client.NotificationsApi

All URIs are relative to *https://api-ru.iiko.services/api/1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**notifications_send_post**](NotificationsApi.md#notifications_send_post) | **POST** /notifications/send | Send notification to external systems.


# **notifications_send_post**
> IikoTransportPublicApiContractsCommonCorrelationIdResponse notifications_send_post(timeout=timeout, iiko_transport_public_api_contracts_notifications_send_notification_request=iiko_transport_public_api_contracts_notifications_send_notification_request)

Send notification to external systems.



 > Restriction group: `Notifications`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.iiko_transport_public_api_contracts_common_correlation_id_response import IikoTransportPublicApiContractsCommonCorrelationIdResponse
from iikocloud_client.models.iiko_transport_public_api_contracts_notifications_send_notification_request import IikoTransportPublicApiContractsNotificationsSendNotificationRequest
from iikocloud_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-ru.iiko.services/api/1
# See configuration.py for a list of all supported configuration parameters.
configuration = iikocloud_client.Configuration(
    host = "https://api-ru.iiko.services/api/1"
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
    iiko_transport_public_api_contracts_notifications_send_notification_request = iikocloud_client.IikoTransportPublicApiContractsNotificationsSendNotificationRequest() # IikoTransportPublicApiContractsNotificationsSendNotificationRequest |  (optional)

    try:
        # Send notification to external systems.
        api_response = await api_instance.notifications_send_post(timeout=timeout, iiko_transport_public_api_contracts_notifications_send_notification_request=iiko_transport_public_api_contracts_notifications_send_notification_request)
        print("The response of NotificationsApi->notifications_send_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotificationsApi->notifications_send_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **iiko_transport_public_api_contracts_notifications_send_notification_request** | [**IikoTransportPublicApiContractsNotificationsSendNotificationRequest**](IikoTransportPublicApiContractsNotificationsSendNotificationRequest.md)|  | [optional] 

### Return type

[**IikoTransportPublicApiContractsCommonCorrelationIdResponse**](IikoTransportPublicApiContractsCommonCorrelationIdResponse.md)

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

