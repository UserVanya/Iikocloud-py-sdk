# iikocloud_client.DeliveryRestrictionsApi

All URIs are relative to *https://api-ru.iiko.services*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_allowed_delivery_restrictions**](DeliveryRestrictionsApi.md#get_allowed_delivery_restrictions) | **POST** /api/1/delivery_restrictions/allowed | Get suitable terminal groups for delivery restrictions.
[**get_delivery_restrictions**](DeliveryRestrictionsApi.md#get_delivery_restrictions) | **POST** /api/1/delivery_restrictions | Retrieve list of delivery restrictions.


# **get_allowed_delivery_restrictions**
> GetAllowedRestrictionsResponse get_allowed_delivery_restrictions(timeout=timeout, get_allowed_restrictions_request=get_allowed_restrictions_request)

Get suitable terminal groups for delivery restrictions.



 > Allowed from version `6.4.16`.

 > Restriction group: `Orders: preparing`.

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.get_allowed_restrictions_request import GetAllowedRestrictionsRequest
from iikocloud_client.models.get_allowed_restrictions_response import GetAllowedRestrictionsResponse
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
    api_instance = iikocloud_client.DeliveryRestrictionsApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    get_allowed_restrictions_request = iikocloud_client.GetAllowedRestrictionsRequest() # GetAllowedRestrictionsRequest |  (optional)

    try:
        # Get suitable terminal groups for delivery restrictions.
        api_response = await api_instance.get_allowed_delivery_restrictions(timeout=timeout, get_allowed_restrictions_request=get_allowed_restrictions_request)
        print("The response of DeliveryRestrictionsApi->get_allowed_delivery_restrictions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeliveryRestrictionsApi->get_allowed_delivery_restrictions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **get_allowed_restrictions_request** | [**GetAllowedRestrictionsRequest**](GetAllowedRestrictionsRequest.md)|  | [optional] 

### Return type

[**GetAllowedRestrictionsResponse**](GetAllowedRestrictionsResponse.md)

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

# **get_delivery_restrictions**
> GetDeliveryRestrictionsResponse get_delivery_restrictions(timeout=timeout, get_delivery_restrictions_request=get_delivery_restrictions_request)

Retrieve list of delivery restrictions.



 > Allowed from version `6.4.16`.

 > Restriction group: `Data: dictionaries`.

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.get_delivery_restrictions_request import GetDeliveryRestrictionsRequest
from iikocloud_client.models.get_delivery_restrictions_response import GetDeliveryRestrictionsResponse
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
    api_instance = iikocloud_client.DeliveryRestrictionsApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    get_delivery_restrictions_request = iikocloud_client.GetDeliveryRestrictionsRequest() # GetDeliveryRestrictionsRequest |  (optional)

    try:
        # Retrieve list of delivery restrictions.
        api_response = await api_instance.get_delivery_restrictions(timeout=timeout, get_delivery_restrictions_request=get_delivery_restrictions_request)
        print("The response of DeliveryRestrictionsApi->get_delivery_restrictions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeliveryRestrictionsApi->get_delivery_restrictions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **get_delivery_restrictions_request** | [**GetDeliveryRestrictionsRequest**](GetDeliveryRestrictionsRequest.md)|  | [optional] 

### Return type

[**GetDeliveryRestrictionsResponse**](GetDeliveryRestrictionsResponse.md)

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

