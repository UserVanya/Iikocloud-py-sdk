# iikocloud_client.MessagesApi

All URIs are relative to *https://api-ru.iiko.services*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_sms_sending_possibility**](MessagesApi.md#check_sms_sending_possibility) | **POST** /api/1/loyalty/iiko/check_sms_sending_possibility | Check sms sending possibility.
[**check_sms_status**](MessagesApi.md#check_sms_status) | **POST** /api/1/loyalty/iiko/check_sms_status | Check SMS status.
[**send_loyalty_email**](MessagesApi.md#send_loyalty_email) | **POST** /api/1/loyalty/iiko/message/send_email | Send email.
[**send_loyalty_sms**](MessagesApi.md#send_loyalty_sms) | **POST** /api/1/loyalty/iiko/message/send_sms | Send sms.


# **check_sms_sending_possibility**
> SmsSendingPossibilityResponse check_sms_sending_possibility(timeout=timeout, sms_sending_possibility_request=sms_sending_possibility_request)

Check sms sending possibility.

Check sms sending possibility before send sms message.

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.sms_sending_possibility_request import SmsSendingPossibilityRequest
from iikocloud_client.models.sms_sending_possibility_response import SmsSendingPossibilityResponse
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
    api_instance = iikocloud_client.MessagesApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    sms_sending_possibility_request = iikocloud_client.SmsSendingPossibilityRequest() # SmsSendingPossibilityRequest |  (optional)

    try:
        # Check sms sending possibility.
        api_response = await api_instance.check_sms_sending_possibility(timeout=timeout, sms_sending_possibility_request=sms_sending_possibility_request)
        print("The response of MessagesApi->check_sms_sending_possibility:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessagesApi->check_sms_sending_possibility: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **sms_sending_possibility_request** | [**SmsSendingPossibilityRequest**](SmsSendingPossibilityRequest.md)|  | [optional] 

### Return type

[**SmsSendingPossibilityResponse**](SmsSendingPossibilityResponse.md)

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

# **check_sms_status**
> CheckSmsStatusResponse check_sms_status(timeout=timeout, check_sms_status_request=check_sms_status_request)

Check SMS status.

Check the status of sending SMS messages.

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.check_sms_status_request import CheckSmsStatusRequest
from iikocloud_client.models.check_sms_status_response import CheckSmsStatusResponse
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
    api_instance = iikocloud_client.MessagesApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    check_sms_status_request = iikocloud_client.CheckSmsStatusRequest() # CheckSmsStatusRequest |  (optional)

    try:
        # Check SMS status.
        api_response = await api_instance.check_sms_status(timeout=timeout, check_sms_status_request=check_sms_status_request)
        print("The response of MessagesApi->check_sms_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessagesApi->check_sms_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **check_sms_status_request** | [**CheckSmsStatusRequest**](CheckSmsStatusRequest.md)|  | [optional] 

### Return type

[**CheckSmsStatusResponse**](CheckSmsStatusResponse.md)

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

# **send_loyalty_email**
> object send_loyalty_email(timeout=timeout, send_email_request=send_email_request)

Send email.

Send email message to specified email address. Sending proceed according iikoCard organization's settings.

 > Restriction group: `Loyalty: messages`.

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.send_email_request import SendEmailRequest
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
    api_instance = iikocloud_client.MessagesApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    send_email_request = iikocloud_client.SendEmailRequest() # SendEmailRequest |  (optional)

    try:
        # Send email.
        api_response = await api_instance.send_loyalty_email(timeout=timeout, send_email_request=send_email_request)
        print("The response of MessagesApi->send_loyalty_email:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessagesApi->send_loyalty_email: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **send_email_request** | [**SendEmailRequest**](SendEmailRequest.md)|  | [optional] 

### Return type

**object**

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

# **send_loyalty_sms**
> SendSmsResponse send_loyalty_sms(timeout=timeout, send_sms_request=send_sms_request)

Send sms.

Send sms message to specified phone number. Sending proceed according iikoCard organization's settings.

 > Restriction group: `Loyalty: messages`.

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.send_sms_request import SendSmsRequest
from iikocloud_client.models.send_sms_response import SendSmsResponse
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
    api_instance = iikocloud_client.MessagesApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    send_sms_request = iikocloud_client.SendSmsRequest() # SendSmsRequest |  (optional)

    try:
        # Send sms.
        api_response = await api_instance.send_loyalty_sms(timeout=timeout, send_sms_request=send_sms_request)
        print("The response of MessagesApi->send_loyalty_sms:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MessagesApi->send_loyalty_sms: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **send_sms_request** | [**SendSmsRequest**](SendSmsRequest.md)|  | [optional] 

### Return type

[**SendSmsResponse**](SendSmsResponse.md)

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

