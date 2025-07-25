# iikocloud_client.CustomerCategoriesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api1_loyalty_iiko_customer_category_add_post**](CustomerCategoriesApi.md#api1_loyalty_iiko_customer_category_add_post) | **POST** /api/1/loyalty/iiko/customer_category/add | Add category for customer.
[**api1_loyalty_iiko_customer_category_post**](CustomerCategoriesApi.md#api1_loyalty_iiko_customer_category_post) | **POST** /api/1/loyalty/iiko/customer_category | Get customer categories.
[**api1_loyalty_iiko_customer_category_remove_post**](CustomerCategoriesApi.md#api1_loyalty_iiko_customer_category_remove_post) | **POST** /api/1/loyalty/iiko/customer_category/remove | Remove category for customer.


# **api1_loyalty_iiko_customer_category_add_post**
> object api1_loyalty_iiko_customer_category_add_post(authorization, timeout=timeout, net_customer_change_category_for_customer_request=net_customer_change_category_for_customer_request)

Add category for customer.

Add specified category for customer.

 > Restriction group: `Guests: changing`.

### Example


```python
import iikocloud_client
from iikocloud_client.models.net_customer_change_category_for_customer_request import NetCustomerChangeCategoryForCustomerRequest
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
    api_instance = iikocloud_client.CustomerCategoriesApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    net_customer_change_category_for_customer_request = iikocloud_client.NetCustomerChangeCategoryForCustomerRequest() # NetCustomerChangeCategoryForCustomerRequest |  (optional)

    try:
        # Add category for customer.
        api_response = await api_instance.api1_loyalty_iiko_customer_category_add_post(authorization, timeout=timeout, net_customer_change_category_for_customer_request=net_customer_change_category_for_customer_request)
        print("The response of CustomerCategoriesApi->api1_loyalty_iiko_customer_category_add_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomerCategoriesApi->api1_loyalty_iiko_customer_category_add_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **net_customer_change_category_for_customer_request** | [**NetCustomerChangeCategoryForCustomerRequest**](NetCustomerChangeCategoryForCustomerRequest.md)|  | [optional] 

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

# **api1_loyalty_iiko_customer_category_post**
> NetCustomerGetCategoriesResponse api1_loyalty_iiko_customer_category_post(authorization, timeout=timeout, net_customer_get_categories_request=net_customer_get_categories_request)

Get customer categories.

Get all organization's customer categories.

 > Restriction group: `Loyalty: dictionaries`.

### Example


```python
import iikocloud_client
from iikocloud_client.models.net_customer_get_categories_request import NetCustomerGetCategoriesRequest
from iikocloud_client.models.net_customer_get_categories_response import NetCustomerGetCategoriesResponse
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
    api_instance = iikocloud_client.CustomerCategoriesApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    net_customer_get_categories_request = iikocloud_client.NetCustomerGetCategoriesRequest() # NetCustomerGetCategoriesRequest |  (optional)

    try:
        # Get customer categories.
        api_response = await api_instance.api1_loyalty_iiko_customer_category_post(authorization, timeout=timeout, net_customer_get_categories_request=net_customer_get_categories_request)
        print("The response of CustomerCategoriesApi->api1_loyalty_iiko_customer_category_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomerCategoriesApi->api1_loyalty_iiko_customer_category_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **net_customer_get_categories_request** | [**NetCustomerGetCategoriesRequest**](NetCustomerGetCategoriesRequest.md)|  | [optional] 

### Return type

[**NetCustomerGetCategoriesResponse**](NetCustomerGetCategoriesResponse.md)

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

# **api1_loyalty_iiko_customer_category_remove_post**
> object api1_loyalty_iiko_customer_category_remove_post(authorization, timeout=timeout, net_customer_change_category_for_customer_request=net_customer_change_category_for_customer_request)

Remove category for customer.

Remove specified category for customer.

 > Restriction group: `Guests: changing`.

### Example


```python
import iikocloud_client
from iikocloud_client.models.net_customer_change_category_for_customer_request import NetCustomerChangeCategoryForCustomerRequest
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
    api_instance = iikocloud_client.CustomerCategoriesApi(api_client)
    authorization = 'Bearer nRzIn0dJu1LpbGMbVfnCFDjKM4iwPhDV8tMlh7X5eWBR64iw' # str | Authorization token.
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    net_customer_change_category_for_customer_request = iikocloud_client.NetCustomerChangeCategoryForCustomerRequest() # NetCustomerChangeCategoryForCustomerRequest |  (optional)

    try:
        # Remove category for customer.
        api_response = await api_instance.api1_loyalty_iiko_customer_category_remove_post(authorization, timeout=timeout, net_customer_change_category_for_customer_request=net_customer_change_category_for_customer_request)
        print("The response of CustomerCategoriesApi->api1_loyalty_iiko_customer_category_remove_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomerCategoriesApi->api1_loyalty_iiko_customer_category_remove_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**| Authorization token. | 
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **net_customer_change_category_for_customer_request** | [**NetCustomerChangeCategoryForCustomerRequest**](NetCustomerChangeCategoryForCustomerRequest.md)|  | [optional] 

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

