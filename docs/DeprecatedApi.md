# iikocloud_client.DeprecatedApi

All URIs are relative to *https://api-ru.iiko.services/api/1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deliveries_check_create_post**](DeprecatedApi.md#deliveries_check_create_post) | **POST** /deliveries/check_create | Check create delivery.
[**deliveries_update_order_payments_post**](DeprecatedApi.md#deliveries_update_order_payments_post) | **POST** /deliveries/update_order_payments | Update order payment details.
[**organizations_get**](DeprecatedApi.md#organizations_get) | **GET** /organizations | Returns organizations available to api-login user.


# **deliveries_check_create_post**
> TransportDeliveriesResponseCheckCreateOrderResponse deliveries_check_create_post(timeout=timeout, transport_deliveries_request_create_order_request=transport_deliveries_request_create_order_request)

Check create delivery.

> Deprecated, all checks are available in `api/1/deliveries/create`.

 > Restriction group: `Deprecated`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.transport_deliveries_request_create_order_request import TransportDeliveriesRequestCreateOrderRequest
from iikocloud_client.models.transport_deliveries_response_check_create_order_response import TransportDeliveriesResponseCheckCreateOrderResponse
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
    api_instance = iikocloud_client.DeprecatedApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    transport_deliveries_request_create_order_request = iikocloud_client.TransportDeliveriesRequestCreateOrderRequest() # TransportDeliveriesRequestCreateOrderRequest |  (optional)

    try:
        # Check create delivery.
        api_response = await api_instance.deliveries_check_create_post(timeout=timeout, transport_deliveries_request_create_order_request=transport_deliveries_request_create_order_request)
        print("The response of DeprecatedApi->deliveries_check_create_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeprecatedApi->deliveries_check_create_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **transport_deliveries_request_create_order_request** | [**TransportDeliveriesRequestCreateOrderRequest**](TransportDeliveriesRequestCreateOrderRequest.md)|  | [optional] 

### Return type

[**TransportDeliveriesResponseCheckCreateOrderResponse**](TransportDeliveriesResponseCheckCreateOrderResponse.md)

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

# **deliveries_update_order_payments_post**
> TransportCommonCorrelationIdResponse deliveries_update_order_payments_post(timeout=timeout, transport_deliveries_request_update_order_payments_request=transport_deliveries_request_update_order_payments_request)

Update order payment details.

> Deprecated, use `api/1/deliveries/change_payments` method instead.

 > This method is a command. Use `api/1/commands/status` method to get the progress status.

 > Restriction group: `Deprecated`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.transport_common_correlation_id_response import TransportCommonCorrelationIdResponse
from iikocloud_client.models.transport_deliveries_request_update_order_payments_request import TransportDeliveriesRequestUpdateOrderPaymentsRequest
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
    api_instance = iikocloud_client.DeprecatedApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    transport_deliveries_request_update_order_payments_request = iikocloud_client.TransportDeliveriesRequestUpdateOrderPaymentsRequest() # TransportDeliveriesRequestUpdateOrderPaymentsRequest |  (optional)

    try:
        # Update order payment details.
        api_response = await api_instance.deliveries_update_order_payments_post(timeout=timeout, transport_deliveries_request_update_order_payments_request=transport_deliveries_request_update_order_payments_request)
        print("The response of DeprecatedApi->deliveries_update_order_payments_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeprecatedApi->deliveries_update_order_payments_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **transport_deliveries_request_update_order_payments_request** | [**TransportDeliveriesRequestUpdateOrderPaymentsRequest**](TransportDeliveriesRequestUpdateOrderPaymentsRequest.md)|  | [optional] 

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

# **organizations_get**
> TransportOrganizationsGetSimpleOrganizationsResponse organizations_get(timeout=timeout)

Returns organizations available to api-login user.

> Deprecated, use `POST api/1/organizations`.

 > Restriction group: `Data: dictionaries`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.transport_organizations_get_simple_organizations_response import TransportOrganizationsGetSimpleOrganizationsResponse
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
    api_instance = iikocloud_client.DeprecatedApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)

    try:
        # Returns organizations available to api-login user.
        api_response = await api_instance.organizations_get(timeout=timeout)
        print("The response of DeprecatedApi->organizations_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeprecatedApi->organizations_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]

### Return type

[**TransportOrganizationsGetSimpleOrganizationsResponse**](TransportOrganizationsGetSimpleOrganizationsResponse.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
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

