# iikocloud_client.DeprecatedApi

All URIs are relative to *https://api-ru.iiko.services*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_organizations**](DeprecatedApi.md#list_organizations) | **GET** /api/1/organizations | Returns organizations available to api-login user.
[**update_delivery_order_payments**](DeprecatedApi.md#update_delivery_order_payments) | **POST** /api/1/deliveries/update_order_payments | Update order payment details.


# **list_organizations**
> GetSimpleOrganizationsResponse list_organizations(timeout=timeout)

Returns organizations available to api-login user.

> Deprecated, use `POST api/1/organizations`.

 > Restriction group: `Data: dictionaries`.

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.get_simple_organizations_response import GetSimpleOrganizationsResponse
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
    api_instance = iikocloud_client.DeprecatedApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)

    try:
        # Returns organizations available to api-login user.
        api_response = await api_instance.list_organizations(timeout=timeout)
        print("The response of DeprecatedApi->list_organizations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeprecatedApi->list_organizations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]

### Return type

[**GetSimpleOrganizationsResponse**](GetSimpleOrganizationsResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
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

# **update_delivery_order_payments**
> CorrelationIdResponse update_delivery_order_payments(timeout=timeout, update_order_payments_request=update_order_payments_request)

Update order payment details.

> Deprecated, use `api/1/deliveries/change_payments` method instead.

 > This method is a command. Use `api/1/commands/status` method to get the progress status.

 > Restriction group: `Deprecated`.

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.correlation_id_response import CorrelationIdResponse
from iikocloud_client.models.update_order_payments_request import UpdateOrderPaymentsRequest
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
    api_instance = iikocloud_client.DeprecatedApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    update_order_payments_request = iikocloud_client.UpdateOrderPaymentsRequest() # UpdateOrderPaymentsRequest |  (optional)

    try:
        # Update order payment details.
        api_response = await api_instance.update_delivery_order_payments(timeout=timeout, update_order_payments_request=update_order_payments_request)
        print("The response of DeprecatedApi->update_delivery_order_payments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeprecatedApi->update_delivery_order_payments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **update_order_payments_request** | [**UpdateOrderPaymentsRequest**](UpdateOrderPaymentsRequest.md)|  | [optional] 

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

