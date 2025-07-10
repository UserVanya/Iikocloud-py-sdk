# iiko_cloud_client.MessagesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api1_loyalty_iiko_check_sms_sending_possibility_post**](MessagesApi.md#api1_loyalty_iiko_check_sms_sending_possibility_post) | **POST** /api/1/loyalty/iiko/check_sms_sending_possibility | Check sms sending possibility.
[**api1_loyalty_iiko_check_sms_status_post**](MessagesApi.md#api1_loyalty_iiko_check_sms_status_post) | **POST** /api/1/loyalty/iiko/check_sms_status | Check SMS status.
[**api1_loyalty_iiko_message_send_email_post**](MessagesApi.md#api1_loyalty_iiko_message_send_email_post) | **POST** /api/1/loyalty/iiko/message/send_email | Send email.
[**api1_loyalty_iiko_message_send_sms_post**](MessagesApi.md#api1_loyalty_iiko_message_send_sms_post) | **POST** /api/1/loyalty/iiko/message/send_sms | Send sms.


# **api1_loyalty_iiko_check_sms_sending_possibility_post**
> NetNotificationSmsSendingPossibilityResponse api1_loyalty_iiko_check_sms_sending_possibility_post(authorization, timeout=timeout, net_notification_sms_sending_possibility_request=net_notification_sms_sending_possibility_request)

Check sms sending possibility.

Check sms sending possibility before send sms message.

### Example


```python
import iiko_cloud_client
from iiko_cloud_client.models.net_notification_sms_sending_possibility_request import NetNotificationSmsSendingPossibilityRequest
from iiko_cloud_client.models.net_notification_sms_sending_possibility_response import NetNotificationSmsSendingPossibilityResponse
from iiko_cloud_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = iiko_cloud_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with iiko_cloud_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iiko_cloud_client.MessagesApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    net_notification_sms_sending_possibility_request = iiko_cloud_client.NetNotificationSmsSendingPossibilityRequest() # NetNotificationSmsSendingPossibilityRequest |  (optional)

    try:
        # Check sms sending possibility.
        api_response = await api_instance.api1_loyalty_iiko_check_sms_sending_possibility_post(authorization, timeout=timeout, net_notification_sms_sending_possibility_request=net_notification_sms_sending_possibility_request)
        print("The response of MessagesApi->api1_loyalty_iiko_check_sms_sending_possibility_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessagesApi->api1_loyalty_iiko_check_sms_sending_possibility_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **net_notification_sms_sending_possibility_request** | [**NetNotificationSmsSendingPossibilityRequest**](NetNotificationSmsSendingPossibilityRequest.md)|  | [optional] 

### Return type

[**NetNotificationSmsSendingPossibilityResponse**](NetNotificationSmsSendingPossibilityResponse.md)

### Authorization

No authorization required

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

# **api1_loyalty_iiko_check_sms_status_post**
> NetNotificationCheckSmsStatusResponse api1_loyalty_iiko_check_sms_status_post(authorization, timeout=timeout, net_notification_check_sms_status_request=net_notification_check_sms_status_request)

Check SMS status.

Check the status of sending SMS messages.

### Example


```python
import iiko_cloud_client
from iiko_cloud_client.models.net_notification_check_sms_status_request import NetNotificationCheckSmsStatusRequest
from iiko_cloud_client.models.net_notification_check_sms_status_response import NetNotificationCheckSmsStatusResponse
from iiko_cloud_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = iiko_cloud_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with iiko_cloud_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iiko_cloud_client.MessagesApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    net_notification_check_sms_status_request = iiko_cloud_client.NetNotificationCheckSmsStatusRequest() # NetNotificationCheckSmsStatusRequest |  (optional)

    try:
        # Check SMS status.
        api_response = await api_instance.api1_loyalty_iiko_check_sms_status_post(authorization, timeout=timeout, net_notification_check_sms_status_request=net_notification_check_sms_status_request)
        print("The response of MessagesApi->api1_loyalty_iiko_check_sms_status_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessagesApi->api1_loyalty_iiko_check_sms_status_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **net_notification_check_sms_status_request** | [**NetNotificationCheckSmsStatusRequest**](NetNotificationCheckSmsStatusRequest.md)|  | [optional] 

### Return type

[**NetNotificationCheckSmsStatusResponse**](NetNotificationCheckSmsStatusResponse.md)

### Authorization

No authorization required

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

# **api1_loyalty_iiko_message_send_email_post**
> object api1_loyalty_iiko_message_send_email_post(authorization, timeout=timeout, net_notification_send_email_request=net_notification_send_email_request)

Send email.

Send email message to specified email address. Sending proceed according iikoCard organization's settings.

 > Restriction group: `Loyalty: messages`.

### Example


```python
import iiko_cloud_client
from iiko_cloud_client.models.net_notification_send_email_request import NetNotificationSendEmailRequest
from iiko_cloud_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = iiko_cloud_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with iiko_cloud_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iiko_cloud_client.MessagesApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    net_notification_send_email_request = iiko_cloud_client.NetNotificationSendEmailRequest() # NetNotificationSendEmailRequest |  (optional)

    try:
        # Send email.
        api_response = await api_instance.api1_loyalty_iiko_message_send_email_post(authorization, timeout=timeout, net_notification_send_email_request=net_notification_send_email_request)
        print("The response of MessagesApi->api1_loyalty_iiko_message_send_email_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessagesApi->api1_loyalty_iiko_message_send_email_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **net_notification_send_email_request** | [**NetNotificationSendEmailRequest**](NetNotificationSendEmailRequest.md)|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

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

# **api1_loyalty_iiko_message_send_sms_post**
> NetNotificationSendSmsResponse api1_loyalty_iiko_message_send_sms_post(authorization, timeout=timeout, net_notification_send_sms_request=net_notification_send_sms_request)

Send sms.

Send sms message to specified phone number. Sending proceed according iikoCard organization's settings.

 > Restriction group: `Loyalty: messages`.

### Example


```python
import iiko_cloud_client
from iiko_cloud_client.models.net_notification_send_sms_request import NetNotificationSendSmsRequest
from iiko_cloud_client.models.net_notification_send_sms_response import NetNotificationSendSmsResponse
from iiko_cloud_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = iiko_cloud_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with iiko_cloud_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iiko_cloud_client.MessagesApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    net_notification_send_sms_request = iiko_cloud_client.NetNotificationSendSmsRequest() # NetNotificationSendSmsRequest |  (optional)

    try:
        # Send sms.
        api_response = await api_instance.api1_loyalty_iiko_message_send_sms_post(authorization, timeout=timeout, net_notification_send_sms_request=net_notification_send_sms_request)
        print("The response of MessagesApi->api1_loyalty_iiko_message_send_sms_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessagesApi->api1_loyalty_iiko_message_send_sms_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **net_notification_send_sms_request** | [**NetNotificationSendSmsRequest**](NetNotificationSendSmsRequest.md)|  | [optional] 

### Return type

[**NetNotificationSendSmsResponse**](NetNotificationSendSmsResponse.md)

### Authorization

No authorization required

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

