# iikocloud_client.DeliveryRestrictionsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api1_delivery_restrictions_allowed_post**](DeliveryRestrictionsApi.md#api1_delivery_restrictions_allowed_post) | **POST** /api/1/delivery_restrictions/allowed | Get suitable terminal groups for delivery restrictions.
[**api1_delivery_restrictions_post**](DeliveryRestrictionsApi.md#api1_delivery_restrictions_post) | **POST** /api/1/delivery_restrictions | Retrieve list of delivery restrictions.


# **api1_delivery_restrictions_allowed_post**
> TransportDeliveryRestrictionsAllowedRestrictionsGetAllowedRestrictionsResponse api1_delivery_restrictions_allowed_post(authorization, timeout=timeout, transport_delivery_restrictions_allowed_restrictions_get_allowed_restrictions_request=transport_delivery_restrictions_allowed_restrictions_get_allowed_restrictions_request)

Get suitable terminal groups for delivery restrictions.



 > Allowed from version `6.4.16`.

 > Restriction group: `Orders: preparing`.

### Example


```python
import iikocloud_client
from iikocloud_client.models.transport_delivery_restrictions_allowed_restrictions_get_allowed_restrictions_request import TransportDeliveryRestrictionsAllowedRestrictionsGetAllowedRestrictionsRequest
from iikocloud_client.models.transport_delivery_restrictions_allowed_restrictions_get_allowed_restrictions_response import TransportDeliveryRestrictionsAllowedRestrictionsGetAllowedRestrictionsResponse
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
    api_instance = iikocloud_client.DeliveryRestrictionsApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    transport_delivery_restrictions_allowed_restrictions_get_allowed_restrictions_request = iikocloud_client.TransportDeliveryRestrictionsAllowedRestrictionsGetAllowedRestrictionsRequest() # TransportDeliveryRestrictionsAllowedRestrictionsGetAllowedRestrictionsRequest |  (optional)

    try:
        # Get suitable terminal groups for delivery restrictions.
        api_response = await api_instance.api1_delivery_restrictions_allowed_post(authorization, timeout=timeout, transport_delivery_restrictions_allowed_restrictions_get_allowed_restrictions_request=transport_delivery_restrictions_allowed_restrictions_get_allowed_restrictions_request)
        print("The response of DeliveryRestrictionsApi->api1_delivery_restrictions_allowed_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeliveryRestrictionsApi->api1_delivery_restrictions_allowed_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **transport_delivery_restrictions_allowed_restrictions_get_allowed_restrictions_request** | [**TransportDeliveryRestrictionsAllowedRestrictionsGetAllowedRestrictionsRequest**](TransportDeliveryRestrictionsAllowedRestrictionsGetAllowedRestrictionsRequest.md)|  | [optional] 

### Return type

[**TransportDeliveryRestrictionsAllowedRestrictionsGetAllowedRestrictionsResponse**](TransportDeliveryRestrictionsAllowedRestrictionsGetAllowedRestrictionsResponse.md)

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

# **api1_delivery_restrictions_post**
> TransportDeliveryRestrictionsGetDeliveryRestrictionsResponse api1_delivery_restrictions_post(authorization, timeout=timeout, transport_delivery_restrictions_get_delivery_restrictions_request=transport_delivery_restrictions_get_delivery_restrictions_request)

Retrieve list of delivery restrictions.



 > Allowed from version `6.4.16`.

 > Restriction group: `Data: dictionaries`.

### Example


```python
import iikocloud_client
from iikocloud_client.models.transport_delivery_restrictions_get_delivery_restrictions_request import TransportDeliveryRestrictionsGetDeliveryRestrictionsRequest
from iikocloud_client.models.transport_delivery_restrictions_get_delivery_restrictions_response import TransportDeliveryRestrictionsGetDeliveryRestrictionsResponse
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
    api_instance = iikocloud_client.DeliveryRestrictionsApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    transport_delivery_restrictions_get_delivery_restrictions_request = iikocloud_client.TransportDeliveryRestrictionsGetDeliveryRestrictionsRequest() # TransportDeliveryRestrictionsGetDeliveryRestrictionsRequest |  (optional)

    try:
        # Retrieve list of delivery restrictions.
        api_response = await api_instance.api1_delivery_restrictions_post(authorization, timeout=timeout, transport_delivery_restrictions_get_delivery_restrictions_request=transport_delivery_restrictions_get_delivery_restrictions_request)
        print("The response of DeliveryRestrictionsApi->api1_delivery_restrictions_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeliveryRestrictionsApi->api1_delivery_restrictions_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **transport_delivery_restrictions_get_delivery_restrictions_request** | [**TransportDeliveryRestrictionsGetDeliveryRestrictionsRequest**](TransportDeliveryRestrictionsGetDeliveryRestrictionsRequest.md)|  | [optional] 

### Return type

[**TransportDeliveryRestrictionsGetDeliveryRestrictionsResponse**](TransportDeliveryRestrictionsGetDeliveryRestrictionsResponse.md)

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

