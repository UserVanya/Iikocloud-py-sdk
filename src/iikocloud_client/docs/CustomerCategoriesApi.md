# iikocloud_client.CustomerCategoriesApi

All URIs are relative to *https://api-ru.iiko.services*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_customer_category**](CustomerCategoriesApi.md#add_customer_category) | **POST** /api/1/loyalty/iiko/customer_category/add | Add category for customer.
[**get_customer_categories**](CustomerCategoriesApi.md#get_customer_categories) | **POST** /api/1/loyalty/iiko/customer_category | Get customer categories.
[**remove_customer_category**](CustomerCategoriesApi.md#remove_customer_category) | **POST** /api/1/loyalty/iiko/customer_category/remove | Remove category for customer.


# **add_customer_category**
> object add_customer_category(timeout=timeout, change_category_for_customer_request=change_category_for_customer_request)

Add category for customer.

Add specified category for customer.

 > Restriction group: `Guests: changing`.

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.change_category_for_customer_request import ChangeCategoryForCustomerRequest
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
    api_instance = iikocloud_client.CustomerCategoriesApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    change_category_for_customer_request = iikocloud_client.ChangeCategoryForCustomerRequest() # ChangeCategoryForCustomerRequest |  (optional)

    try:
        # Add category for customer.
        api_response = await api_instance.add_customer_category(timeout=timeout, change_category_for_customer_request=change_category_for_customer_request)
        print("The response of CustomerCategoriesApi->add_customer_category:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomerCategoriesApi->add_customer_category: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **change_category_for_customer_request** | [**ChangeCategoryForCustomerRequest**](ChangeCategoryForCustomerRequest.md)|  | [optional] 

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

# **get_customer_categories**
> GetCategoriesResponse get_customer_categories(timeout=timeout, get_categories_request=get_categories_request)

Get customer categories.

Get all organization's customer categories.

 > Restriction group: `Loyalty: dictionaries`.

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.get_categories_request import GetCategoriesRequest
from iikocloud_client.models.get_categories_response import GetCategoriesResponse
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
    api_instance = iikocloud_client.CustomerCategoriesApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    get_categories_request = iikocloud_client.GetCategoriesRequest() # GetCategoriesRequest |  (optional)

    try:
        # Get customer categories.
        api_response = await api_instance.get_customer_categories(timeout=timeout, get_categories_request=get_categories_request)
        print("The response of CustomerCategoriesApi->get_customer_categories:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomerCategoriesApi->get_customer_categories: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **get_categories_request** | [**GetCategoriesRequest**](GetCategoriesRequest.md)|  | [optional] 

### Return type

[**GetCategoriesResponse**](GetCategoriesResponse.md)

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

# **remove_customer_category**
> object remove_customer_category(timeout=timeout, change_category_for_customer_request=change_category_for_customer_request)

Remove category for customer.

Remove specified category for customer.

 > Restriction group: `Guests: changing`.

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.change_category_for_customer_request import ChangeCategoryForCustomerRequest
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
    api_instance = iikocloud_client.CustomerCategoriesApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    change_category_for_customer_request = iikocloud_client.ChangeCategoryForCustomerRequest() # ChangeCategoryForCustomerRequest |  (optional)

    try:
        # Remove category for customer.
        api_response = await api_instance.remove_customer_category(timeout=timeout, change_category_for_customer_request=change_category_for_customer_request)
        print("The response of CustomerCategoriesApi->remove_customer_category:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomerCategoriesApi->remove_customer_category: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **change_category_for_customer_request** | [**ChangeCategoryForCustomerRequest**](ChangeCategoryForCustomerRequest.md)|  | [optional] 

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

