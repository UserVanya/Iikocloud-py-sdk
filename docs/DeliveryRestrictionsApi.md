# iikocloud_client.DeliveryRestrictionsApi

All URIs are relative to *https://api-ru.iiko.services/api/1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delivery_restrictions_allowed_post**](DeliveryRestrictionsApi.md#delivery_restrictions_allowed_post) | **POST** /delivery_restrictions/allowed | Get suitable terminal groups for delivery restrictions.
[**delivery_restrictions_post**](DeliveryRestrictionsApi.md#delivery_restrictions_post) | **POST** /delivery_restrictions | Retrieve list of delivery restrictions.


# **delivery_restrictions_allowed_post**
> IikoTransportPublicApiContractsDeliveryRestrictionsAllowedRestrictionsGetAllowedRestrictionsResponse delivery_restrictions_allowed_post(timeout=timeout, iiko_transport_public_api_contracts_delivery_restrictions_allowed_restrictions_get_allowed_restrictions_request=iiko_transport_public_api_contracts_delivery_restrictions_allowed_restrictions_get_allowed_restrictions_request)

Get suitable terminal groups for delivery restrictions.



 > Allowed from version `6.4.16`.

 > Restriction group: `Orders: preparing`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.iiko_transport_public_api_contracts_delivery_restrictions_allowed_restrictions_get_allowed_restrictions_request import IikoTransportPublicApiContractsDeliveryRestrictionsAllowedRestrictionsGetAllowedRestrictionsRequest
from iikocloud_client.models.iiko_transport_public_api_contracts_delivery_restrictions_allowed_restrictions_get_allowed_restrictions_response import IikoTransportPublicApiContractsDeliveryRestrictionsAllowedRestrictionsGetAllowedRestrictionsResponse
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
    api_instance = iikocloud_client.DeliveryRestrictionsApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    iiko_transport_public_api_contracts_delivery_restrictions_allowed_restrictions_get_allowed_restrictions_request = iikocloud_client.IikoTransportPublicApiContractsDeliveryRestrictionsAllowedRestrictionsGetAllowedRestrictionsRequest() # IikoTransportPublicApiContractsDeliveryRestrictionsAllowedRestrictionsGetAllowedRestrictionsRequest |  (optional)

    try:
        # Get suitable terminal groups for delivery restrictions.
        api_response = await api_instance.delivery_restrictions_allowed_post(timeout=timeout, iiko_transport_public_api_contracts_delivery_restrictions_allowed_restrictions_get_allowed_restrictions_request=iiko_transport_public_api_contracts_delivery_restrictions_allowed_restrictions_get_allowed_restrictions_request)
        print("The response of DeliveryRestrictionsApi->delivery_restrictions_allowed_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeliveryRestrictionsApi->delivery_restrictions_allowed_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **iiko_transport_public_api_contracts_delivery_restrictions_allowed_restrictions_get_allowed_restrictions_request** | [**IikoTransportPublicApiContractsDeliveryRestrictionsAllowedRestrictionsGetAllowedRestrictionsRequest**](IikoTransportPublicApiContractsDeliveryRestrictionsAllowedRestrictionsGetAllowedRestrictionsRequest.md)|  | [optional] 

### Return type

[**IikoTransportPublicApiContractsDeliveryRestrictionsAllowedRestrictionsGetAllowedRestrictionsResponse**](IikoTransportPublicApiContractsDeliveryRestrictionsAllowedRestrictionsGetAllowedRestrictionsResponse.md)

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

# **delivery_restrictions_post**
> IikoTransportPublicApiContractsDeliveryRestrictionsGetDeliveryRestrictionsResponse delivery_restrictions_post(timeout=timeout, iiko_transport_public_api_contracts_delivery_restrictions_get_delivery_restrictions_request=iiko_transport_public_api_contracts_delivery_restrictions_get_delivery_restrictions_request)

Retrieve list of delivery restrictions.



 > Allowed from version `6.4.16`.

 > Restriction group: `Data: dictionaries`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.iiko_transport_public_api_contracts_delivery_restrictions_get_delivery_restrictions_request import IikoTransportPublicApiContractsDeliveryRestrictionsGetDeliveryRestrictionsRequest
from iikocloud_client.models.iiko_transport_public_api_contracts_delivery_restrictions_get_delivery_restrictions_response import IikoTransportPublicApiContractsDeliveryRestrictionsGetDeliveryRestrictionsResponse
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
    api_instance = iikocloud_client.DeliveryRestrictionsApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    iiko_transport_public_api_contracts_delivery_restrictions_get_delivery_restrictions_request = iikocloud_client.IikoTransportPublicApiContractsDeliveryRestrictionsGetDeliveryRestrictionsRequest() # IikoTransportPublicApiContractsDeliveryRestrictionsGetDeliveryRestrictionsRequest |  (optional)

    try:
        # Retrieve list of delivery restrictions.
        api_response = await api_instance.delivery_restrictions_post(timeout=timeout, iiko_transport_public_api_contracts_delivery_restrictions_get_delivery_restrictions_request=iiko_transport_public_api_contracts_delivery_restrictions_get_delivery_restrictions_request)
        print("The response of DeliveryRestrictionsApi->delivery_restrictions_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeliveryRestrictionsApi->delivery_restrictions_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **iiko_transport_public_api_contracts_delivery_restrictions_get_delivery_restrictions_request** | [**IikoTransportPublicApiContractsDeliveryRestrictionsGetDeliveryRestrictionsRequest**](IikoTransportPublicApiContractsDeliveryRestrictionsGetDeliveryRestrictionsRequest.md)|  | [optional] 

### Return type

[**IikoTransportPublicApiContractsDeliveryRestrictionsGetDeliveryRestrictionsResponse**](IikoTransportPublicApiContractsDeliveryRestrictionsGetDeliveryRestrictionsResponse.md)

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

