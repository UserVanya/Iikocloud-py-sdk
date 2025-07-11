# iikocloud_client.DeprecatedApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api1_deliveries_check_create_post**](DeprecatedApi.md#api1_deliveries_check_create_post) | **POST** /api/1/deliveries/check_create | Check create delivery.
[**api1_deliveries_update_order_payments_post**](DeprecatedApi.md#api1_deliveries_update_order_payments_post) | **POST** /api/1/deliveries/update_order_payments | Update order payment details.
[**api1_organizations_get**](DeprecatedApi.md#api1_organizations_get) | **GET** /api/1/organizations | Returns organizations available to api-login user.


# **api1_deliveries_check_create_post**
> TransportDeliveriesResponseCheckCreateOrderResponse api1_deliveries_check_create_post(authorization, timeout=timeout, transport_deliveries_request_create_order_request=transport_deliveries_request_create_order_request)

Check create delivery.

> Deprecated, all checks are available in `api/1/deliveries/create`.

 > Restriction group: `Deprecated`.

### Example


```python
import iikocloud_client
from iikocloud_client.models.transport_deliveries_request_create_order_request import TransportDeliveriesRequestCreateOrderRequest
from iikocloud_client.models.transport_deliveries_response_check_create_order_response import TransportDeliveriesResponseCheckCreateOrderResponse
from iikocloud_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = iikocloud_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with iikocloud_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iikocloud_client.DeprecatedApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    transport_deliveries_request_create_order_request = iikocloud_client.TransportDeliveriesRequestCreateOrderRequest() # TransportDeliveriesRequestCreateOrderRequest |  (optional)

    try:
        # Check create delivery.
        api_response = await api_instance.api1_deliveries_check_create_post(authorization, timeout=timeout, transport_deliveries_request_create_order_request=transport_deliveries_request_create_order_request)
        print("The response of DeprecatedApi->api1_deliveries_check_create_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeprecatedApi->api1_deliveries_check_create_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **transport_deliveries_request_create_order_request** | [**TransportDeliveriesRequestCreateOrderRequest**](TransportDeliveriesRequestCreateOrderRequest.md)|  | [optional] 

### Return type

[**TransportDeliveriesResponseCheckCreateOrderResponse**](TransportDeliveriesResponseCheckCreateOrderResponse.md)

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

# **api1_deliveries_update_order_payments_post**
> TransportCommonCorrelationIdResponse api1_deliveries_update_order_payments_post(authorization, timeout=timeout, transport_deliveries_request_update_order_payments_request=transport_deliveries_request_update_order_payments_request)

Update order payment details.

> Deprecated, use `api/1/deliveries/change_payments` method instead.

 > This method is a command. Use `api/1/commands/status` method to get the progress status.

 > Restriction group: `Deprecated`.

### Example


```python
import iikocloud_client
from iikocloud_client.models.transport_common_correlation_id_response import TransportCommonCorrelationIdResponse
from iikocloud_client.models.transport_deliveries_request_update_order_payments_request import TransportDeliveriesRequestUpdateOrderPaymentsRequest
from iikocloud_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = iikocloud_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with iikocloud_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iikocloud_client.DeprecatedApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    transport_deliveries_request_update_order_payments_request = iikocloud_client.TransportDeliveriesRequestUpdateOrderPaymentsRequest() # TransportDeliveriesRequestUpdateOrderPaymentsRequest |  (optional)

    try:
        # Update order payment details.
        api_response = await api_instance.api1_deliveries_update_order_payments_post(authorization, timeout=timeout, transport_deliveries_request_update_order_payments_request=transport_deliveries_request_update_order_payments_request)
        print("The response of DeprecatedApi->api1_deliveries_update_order_payments_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeprecatedApi->api1_deliveries_update_order_payments_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **transport_deliveries_request_update_order_payments_request** | [**TransportDeliveriesRequestUpdateOrderPaymentsRequest**](TransportDeliveriesRequestUpdateOrderPaymentsRequest.md)|  | [optional] 

### Return type

[**TransportCommonCorrelationIdResponse**](TransportCommonCorrelationIdResponse.md)

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

# **api1_organizations_get**
> TransportOrganizationsGetSimpleOrganizationsResponse api1_organizations_get(authorization, timeout=timeout)

Returns organizations available to api-login user.

> Deprecated, use `POST api/1/organizations`.

 > Restriction group: `Data: dictionaries`.

### Example


```python
import iikocloud_client
from iikocloud_client.models.transport_organizations_get_simple_organizations_response import TransportOrganizationsGetSimpleOrganizationsResponse
from iikocloud_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = iikocloud_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with iikocloud_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iikocloud_client.DeprecatedApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)

    try:
        # Returns organizations available to api-login user.
        api_response = await api_instance.api1_organizations_get(authorization, timeout=timeout)
        print("The response of DeprecatedApi->api1_organizations_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeprecatedApi->api1_organizations_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]

### Return type

[**TransportOrganizationsGetSimpleOrganizationsResponse**](TransportOrganizationsGetSimpleOrganizationsResponse.md)

### Authorization

No authorization required

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

