# iikocloud_client.DeprecatedApi

All URIs are relative to *https://api-ru.iiko.services/api/1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**deliveries_update_order_payments_post**](DeprecatedApi.md#deliveries_update_order_payments_post) | **POST** /deliveries/update_order_payments | Update order payment details.
[**organizations_get**](DeprecatedApi.md#organizations_get) | **GET** /organizations | Returns organizations available to api-login user.


# **deliveries_update_order_payments_post**
> IikoTransportPublicApiContractsCommonCorrelationIdResponse deliveries_update_order_payments_post(authorization, timeout=timeout, iiko_transport_public_api_contracts_deliveries_request_update_order_payments_request=iiko_transport_public_api_contracts_deliveries_request_update_order_payments_request)

Update order payment details.

> Deprecated, use `api/1/deliveries/change_payments` method instead.

 > This method is a command. Use `api/1/commands/status` method to get the progress status.

 > Restriction group: `Deprecated`.

### Example


```python
import iikocloud_client
from iikocloud_client.models.iiko_transport_public_api_contracts_common_correlation_id_response import IikoTransportPublicApiContractsCommonCorrelationIdResponse
from iikocloud_client.models.iiko_transport_public_api_contracts_deliveries_request_update_order_payments_request import IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderPaymentsRequest
from iikocloud_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-ru.iiko.services/api/1
# See configuration.py for a list of all supported configuration parameters.
configuration = iikocloud_client.Configuration(
    host = "https://api-ru.iiko.services/api/1"
)


# Enter a context with an instance of the API client
async with iikocloud_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iikocloud_client.DeprecatedApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    iiko_transport_public_api_contracts_deliveries_request_update_order_payments_request = iikocloud_client.IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderPaymentsRequest() # IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderPaymentsRequest |  (optional)

    try:
        # Update order payment details.
        api_response = await api_instance.deliveries_update_order_payments_post(authorization, timeout=timeout, iiko_transport_public_api_contracts_deliveries_request_update_order_payments_request=iiko_transport_public_api_contracts_deliveries_request_update_order_payments_request)
        print("The response of DeprecatedApi->deliveries_update_order_payments_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeprecatedApi->deliveries_update_order_payments_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **iiko_transport_public_api_contracts_deliveries_request_update_order_payments_request** | [**IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderPaymentsRequest**](IikoTransportPublicApiContractsDeliveriesRequestUpdateOrderPaymentsRequest.md)|  | [optional] 

### Return type

[**IikoTransportPublicApiContractsCommonCorrelationIdResponse**](IikoTransportPublicApiContractsCommonCorrelationIdResponse.md)

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

# **organizations_get**
> IikoTransportPublicApiContractsOrganizationsGetSimpleOrganizationsResponse organizations_get(authorization, timeout=timeout)

Returns organizations available to api-login user.

> Deprecated, use `POST api/1/organizations`.

 > Restriction group: `Data: dictionaries`.

### Example


```python
import iikocloud_client
from iikocloud_client.models.iiko_transport_public_api_contracts_organizations_get_simple_organizations_response import IikoTransportPublicApiContractsOrganizationsGetSimpleOrganizationsResponse
from iikocloud_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api-ru.iiko.services/api/1
# See configuration.py for a list of all supported configuration parameters.
configuration = iikocloud_client.Configuration(
    host = "https://api-ru.iiko.services/api/1"
)


# Enter a context with an instance of the API client
async with iikocloud_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = iikocloud_client.DeprecatedApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)

    try:
        # Returns organizations available to api-login user.
        api_response = await api_instance.organizations_get(authorization, timeout=timeout)
        print("The response of DeprecatedApi->organizations_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeprecatedApi->organizations_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]

### Return type

[**IikoTransportPublicApiContractsOrganizationsGetSimpleOrganizationsResponse**](IikoTransportPublicApiContractsOrganizationsGetSimpleOrganizationsResponse.md)

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

