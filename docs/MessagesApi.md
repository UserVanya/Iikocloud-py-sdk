# iikocloud_client.MessagesApi

All URIs are relative to *https://api-ru.iiko.services/api/1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**loyalty_iiko_check_sms_sending_possibility_post**](MessagesApi.md#loyalty_iiko_check_sms_sending_possibility_post) | **POST** /loyalty/iiko/check_sms_sending_possibility | Check sms sending possibility.
[**loyalty_iiko_check_sms_status_post**](MessagesApi.md#loyalty_iiko_check_sms_status_post) | **POST** /loyalty/iiko/check_sms_status | Check SMS status.
[**loyalty_iiko_message_send_email_post**](MessagesApi.md#loyalty_iiko_message_send_email_post) | **POST** /loyalty/iiko/message/send_email | Send email.
[**loyalty_iiko_message_send_sms_post**](MessagesApi.md#loyalty_iiko_message_send_sms_post) | **POST** /loyalty/iiko/message/send_sms | Send sms.


# **loyalty_iiko_check_sms_sending_possibility_post**
> IikoNetServiceContractsApiIikoTransportNotificationSmsSendingPossibilityResponse loyalty_iiko_check_sms_sending_possibility_post(timeout=timeout, iiko_net_service_contracts_api_iiko_transport_notification_sms_sending_possibility_request=iiko_net_service_contracts_api_iiko_transport_notification_sms_sending_possibility_request)

Check sms sending possibility.

Check sms sending possibility before send sms message.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.iiko_net_service_contracts_api_iiko_transport_notification_sms_sending_possibility_request import IikoNetServiceContractsApiIikoTransportNotificationSmsSendingPossibilityRequest
from iikocloud_client.models.iiko_net_service_contracts_api_iiko_transport_notification_sms_sending_possibility_response import IikoNetServiceContractsApiIikoTransportNotificationSmsSendingPossibilityResponse
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
    api_instance = iikocloud_client.MessagesApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    iiko_net_service_contracts_api_iiko_transport_notification_sms_sending_possibility_request = iikocloud_client.IikoNetServiceContractsApiIikoTransportNotificationSmsSendingPossibilityRequest() # IikoNetServiceContractsApiIikoTransportNotificationSmsSendingPossibilityRequest |  (optional)

    try:
        # Check sms sending possibility.
        api_response = await api_instance.loyalty_iiko_check_sms_sending_possibility_post(timeout=timeout, iiko_net_service_contracts_api_iiko_transport_notification_sms_sending_possibility_request=iiko_net_service_contracts_api_iiko_transport_notification_sms_sending_possibility_request)
        print("The response of MessagesApi->loyalty_iiko_check_sms_sending_possibility_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessagesApi->loyalty_iiko_check_sms_sending_possibility_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **iiko_net_service_contracts_api_iiko_transport_notification_sms_sending_possibility_request** | [**IikoNetServiceContractsApiIikoTransportNotificationSmsSendingPossibilityRequest**](IikoNetServiceContractsApiIikoTransportNotificationSmsSendingPossibilityRequest.md)|  | [optional] 

### Return type

[**IikoNetServiceContractsApiIikoTransportNotificationSmsSendingPossibilityResponse**](IikoNetServiceContractsApiIikoTransportNotificationSmsSendingPossibilityResponse.md)

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

# **loyalty_iiko_check_sms_status_post**
> IikoNetServiceContractsApiIikoTransportNotificationCheckSmsStatusResponse loyalty_iiko_check_sms_status_post(timeout=timeout, iiko_net_service_contracts_api_iiko_transport_notification_check_sms_status_request=iiko_net_service_contracts_api_iiko_transport_notification_check_sms_status_request)

Check SMS status.

Check the status of sending SMS messages.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.iiko_net_service_contracts_api_iiko_transport_notification_check_sms_status_request import IikoNetServiceContractsApiIikoTransportNotificationCheckSmsStatusRequest
from iikocloud_client.models.iiko_net_service_contracts_api_iiko_transport_notification_check_sms_status_response import IikoNetServiceContractsApiIikoTransportNotificationCheckSmsStatusResponse
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
    api_instance = iikocloud_client.MessagesApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    iiko_net_service_contracts_api_iiko_transport_notification_check_sms_status_request = iikocloud_client.IikoNetServiceContractsApiIikoTransportNotificationCheckSmsStatusRequest() # IikoNetServiceContractsApiIikoTransportNotificationCheckSmsStatusRequest |  (optional)

    try:
        # Check SMS status.
        api_response = await api_instance.loyalty_iiko_check_sms_status_post(timeout=timeout, iiko_net_service_contracts_api_iiko_transport_notification_check_sms_status_request=iiko_net_service_contracts_api_iiko_transport_notification_check_sms_status_request)
        print("The response of MessagesApi->loyalty_iiko_check_sms_status_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessagesApi->loyalty_iiko_check_sms_status_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **iiko_net_service_contracts_api_iiko_transport_notification_check_sms_status_request** | [**IikoNetServiceContractsApiIikoTransportNotificationCheckSmsStatusRequest**](IikoNetServiceContractsApiIikoTransportNotificationCheckSmsStatusRequest.md)|  | [optional] 

### Return type

[**IikoNetServiceContractsApiIikoTransportNotificationCheckSmsStatusResponse**](IikoNetServiceContractsApiIikoTransportNotificationCheckSmsStatusResponse.md)

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

# **loyalty_iiko_message_send_email_post**
> object loyalty_iiko_message_send_email_post(timeout=timeout, iiko_net_service_contracts_api_iiko_transport_notification_send_email_request=iiko_net_service_contracts_api_iiko_transport_notification_send_email_request)

Send email.

Send email message to specified email address. Sending proceed according iikoCard organization's settings.

 > Restriction group: `Loyalty: messages`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.iiko_net_service_contracts_api_iiko_transport_notification_send_email_request import IikoNetServiceContractsApiIikoTransportNotificationSendEmailRequest
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
    api_instance = iikocloud_client.MessagesApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    iiko_net_service_contracts_api_iiko_transport_notification_send_email_request = iikocloud_client.IikoNetServiceContractsApiIikoTransportNotificationSendEmailRequest() # IikoNetServiceContractsApiIikoTransportNotificationSendEmailRequest |  (optional)

    try:
        # Send email.
        api_response = await api_instance.loyalty_iiko_message_send_email_post(timeout=timeout, iiko_net_service_contracts_api_iiko_transport_notification_send_email_request=iiko_net_service_contracts_api_iiko_transport_notification_send_email_request)
        print("The response of MessagesApi->loyalty_iiko_message_send_email_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessagesApi->loyalty_iiko_message_send_email_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **iiko_net_service_contracts_api_iiko_transport_notification_send_email_request** | [**IikoNetServiceContractsApiIikoTransportNotificationSendEmailRequest**](IikoNetServiceContractsApiIikoTransportNotificationSendEmailRequest.md)|  | [optional] 

### Return type

**object**

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

# **loyalty_iiko_message_send_sms_post**
> IikoNetServiceContractsApiIikoTransportNotificationSendSmsResponse loyalty_iiko_message_send_sms_post(timeout=timeout, iiko_net_service_contracts_api_iiko_transport_notification_send_sms_request=iiko_net_service_contracts_api_iiko_transport_notification_send_sms_request)

Send sms.

Send sms message to specified phone number. Sending proceed according iikoCard organization's settings.

 > Restriction group: `Loyalty: messages`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.iiko_net_service_contracts_api_iiko_transport_notification_send_sms_request import IikoNetServiceContractsApiIikoTransportNotificationSendSmsRequest
from iikocloud_client.models.iiko_net_service_contracts_api_iiko_transport_notification_send_sms_response import IikoNetServiceContractsApiIikoTransportNotificationSendSmsResponse
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
    api_instance = iikocloud_client.MessagesApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    iiko_net_service_contracts_api_iiko_transport_notification_send_sms_request = iikocloud_client.IikoNetServiceContractsApiIikoTransportNotificationSendSmsRequest() # IikoNetServiceContractsApiIikoTransportNotificationSendSmsRequest |  (optional)

    try:
        # Send sms.
        api_response = await api_instance.loyalty_iiko_message_send_sms_post(timeout=timeout, iiko_net_service_contracts_api_iiko_transport_notification_send_sms_request=iiko_net_service_contracts_api_iiko_transport_notification_send_sms_request)
        print("The response of MessagesApi->loyalty_iiko_message_send_sms_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessagesApi->loyalty_iiko_message_send_sms_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **iiko_net_service_contracts_api_iiko_transport_notification_send_sms_request** | [**IikoNetServiceContractsApiIikoTransportNotificationSendSmsRequest**](IikoNetServiceContractsApiIikoTransportNotificationSendSmsRequest.md)|  | [optional] 

### Return type

[**IikoNetServiceContractsApiIikoTransportNotificationSendSmsResponse**](IikoNetServiceContractsApiIikoTransportNotificationSendSmsResponse.md)

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

