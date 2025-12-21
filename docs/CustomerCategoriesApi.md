# iikocloud_client.CustomerCategoriesApi

All URIs are relative to *https://api-ru.iiko.services/api/1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**loyalty_iiko_customer_category_add_post**](CustomerCategoriesApi.md#loyalty_iiko_customer_category_add_post) | **POST** /loyalty/iiko/customer_category/add | Add category for customer.
[**loyalty_iiko_customer_category_post**](CustomerCategoriesApi.md#loyalty_iiko_customer_category_post) | **POST** /loyalty/iiko/customer_category | Get customer categories.
[**loyalty_iiko_customer_category_remove_post**](CustomerCategoriesApi.md#loyalty_iiko_customer_category_remove_post) | **POST** /loyalty/iiko/customer_category/remove | Remove category for customer.


# **loyalty_iiko_customer_category_add_post**
> object loyalty_iiko_customer_category_add_post(timeout=timeout, iiko_net_service_contracts_api_iiko_transport_customer_change_category_for_customer_request=iiko_net_service_contracts_api_iiko_transport_customer_change_category_for_customer_request)

Add category for customer.

Add specified category for customer.

 > Restriction group: `Guests: changing`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.iiko_net_service_contracts_api_iiko_transport_customer_change_category_for_customer_request import IikoNetServiceContractsApiIikoTransportCustomerChangeCategoryForCustomerRequest
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
    api_instance = iikocloud_client.CustomerCategoriesApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    iiko_net_service_contracts_api_iiko_transport_customer_change_category_for_customer_request = iikocloud_client.IikoNetServiceContractsApiIikoTransportCustomerChangeCategoryForCustomerRequest() # IikoNetServiceContractsApiIikoTransportCustomerChangeCategoryForCustomerRequest |  (optional)

    try:
        # Add category for customer.
        api_response = await api_instance.loyalty_iiko_customer_category_add_post(timeout=timeout, iiko_net_service_contracts_api_iiko_transport_customer_change_category_for_customer_request=iiko_net_service_contracts_api_iiko_transport_customer_change_category_for_customer_request)
        print("The response of CustomerCategoriesApi->loyalty_iiko_customer_category_add_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomerCategoriesApi->loyalty_iiko_customer_category_add_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **iiko_net_service_contracts_api_iiko_transport_customer_change_category_for_customer_request** | [**IikoNetServiceContractsApiIikoTransportCustomerChangeCategoryForCustomerRequest**](IikoNetServiceContractsApiIikoTransportCustomerChangeCategoryForCustomerRequest.md)|  | [optional] 

### Return type

**object**

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

# **loyalty_iiko_customer_category_post**
> IikoNetServiceContractsApiIikoTransportCustomerGetCategoriesResponse loyalty_iiko_customer_category_post(timeout=timeout, iiko_net_service_contracts_api_iiko_transport_customer_get_categories_request=iiko_net_service_contracts_api_iiko_transport_customer_get_categories_request)

Get customer categories.

Get all organization's customer categories.

 > Restriction group: `Loyalty: dictionaries`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.iiko_net_service_contracts_api_iiko_transport_customer_get_categories_request import IikoNetServiceContractsApiIikoTransportCustomerGetCategoriesRequest
from iikocloud_client.models.iiko_net_service_contracts_api_iiko_transport_customer_get_categories_response import IikoNetServiceContractsApiIikoTransportCustomerGetCategoriesResponse
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
    api_instance = iikocloud_client.CustomerCategoriesApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    iiko_net_service_contracts_api_iiko_transport_customer_get_categories_request = iikocloud_client.IikoNetServiceContractsApiIikoTransportCustomerGetCategoriesRequest() # IikoNetServiceContractsApiIikoTransportCustomerGetCategoriesRequest |  (optional)

    try:
        # Get customer categories.
        api_response = await api_instance.loyalty_iiko_customer_category_post(timeout=timeout, iiko_net_service_contracts_api_iiko_transport_customer_get_categories_request=iiko_net_service_contracts_api_iiko_transport_customer_get_categories_request)
        print("The response of CustomerCategoriesApi->loyalty_iiko_customer_category_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomerCategoriesApi->loyalty_iiko_customer_category_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **iiko_net_service_contracts_api_iiko_transport_customer_get_categories_request** | [**IikoNetServiceContractsApiIikoTransportCustomerGetCategoriesRequest**](IikoNetServiceContractsApiIikoTransportCustomerGetCategoriesRequest.md)|  | [optional] 

### Return type

[**IikoNetServiceContractsApiIikoTransportCustomerGetCategoriesResponse**](IikoNetServiceContractsApiIikoTransportCustomerGetCategoriesResponse.md)

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

# **loyalty_iiko_customer_category_remove_post**
> object loyalty_iiko_customer_category_remove_post(timeout=timeout, iiko_net_service_contracts_api_iiko_transport_customer_change_category_for_customer_request=iiko_net_service_contracts_api_iiko_transport_customer_change_category_for_customer_request)

Remove category for customer.

Remove specified category for customer.

 > Restriction group: `Guests: changing`.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import iikocloud_client
from iikocloud_client.models.iiko_net_service_contracts_api_iiko_transport_customer_change_category_for_customer_request import IikoNetServiceContractsApiIikoTransportCustomerChangeCategoryForCustomerRequest
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
    api_instance = iikocloud_client.CustomerCategoriesApi(api_client)
    timeout = 15 # int | Timeout in seconds. (optional) (default to 15)
    iiko_net_service_contracts_api_iiko_transport_customer_change_category_for_customer_request = iikocloud_client.IikoNetServiceContractsApiIikoTransportCustomerChangeCategoryForCustomerRequest() # IikoNetServiceContractsApiIikoTransportCustomerChangeCategoryForCustomerRequest |  (optional)

    try:
        # Remove category for customer.
        api_response = await api_instance.loyalty_iiko_customer_category_remove_post(timeout=timeout, iiko_net_service_contracts_api_iiko_transport_customer_change_category_for_customer_request=iiko_net_service_contracts_api_iiko_transport_customer_change_category_for_customer_request)
        print("The response of CustomerCategoriesApi->loyalty_iiko_customer_category_remove_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CustomerCategoriesApi->loyalty_iiko_customer_category_remove_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timeout** | **int**| Timeout in seconds. | [optional] [default to 15]
 **iiko_net_service_contracts_api_iiko_transport_customer_change_category_for_customer_request** | [**IikoNetServiceContractsApiIikoTransportCustomerChangeCategoryForCustomerRequest**](IikoNetServiceContractsApiIikoTransportCustomerChangeCategoryForCustomerRequest.md)|  | [optional] 

### Return type

**object**

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

