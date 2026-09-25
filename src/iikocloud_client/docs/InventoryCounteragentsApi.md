# iikocloud_client.InventoryCounteragentsApi

All URIs are relative to *https://api-ru.iiko.services*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_inventory_counteragents**](InventoryCounteragentsApi.md#list_inventory_counteragents) | **POST** /api/inventory/v1/counteragents/list | Get counteragents list
[**list_inventory_supplier_price_list**](InventoryCounteragentsApi.md#list_inventory_supplier_price_list) | **POST** /api/inventory/v1/counteragents/pricelist/list | Get supplier price list


# **list_inventory_counteragents**
> GetCounteragentsResponse list_inventory_counteragents(get_counteragents_request, timeout=timeout)

Get counteragents list

Gets a list of counteragents with pagination and type filtering support

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.get_counteragents_request import GetCounteragentsRequest
from iikocloud_client.models.get_counteragents_response import GetCounteragentsResponse
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
    api_instance = iikocloud_client.InventoryCounteragentsApi(api_client)
    get_counteragents_request = iikocloud_client.GetCounteragentsRequest() # GetCounteragentsRequest | Request parameters
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Get counteragents list
        api_response = await api_instance.list_inventory_counteragents(get_counteragents_request, timeout=timeout)
        print("The response of InventoryCounteragentsApi->list_inventory_counteragents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryCounteragentsApi->list_inventory_counteragents: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_counteragents_request** | [**GetCounteragentsRequest**](GetCounteragentsRequest.md)| Request parameters | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

### Return type

[**GetCounteragentsResponse**](GetCounteragentsResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Invalid input data |  -  |
**401** | Unauthorized |  -  |
**403** | Access forbidden |  -  |
**405** | Method not allowed |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_inventory_supplier_price_list**
> GetPriceListResponse list_inventory_supplier_price_list(get_price_list_request, timeout=timeout)

Get supplier price list

Gets a supplier's full price list. Returns the currently active price list

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.get_price_list_request import GetPriceListRequest
from iikocloud_client.models.get_price_list_response import GetPriceListResponse
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
    api_instance = iikocloud_client.InventoryCounteragentsApi(api_client)
    get_price_list_request = iikocloud_client.GetPriceListRequest() # GetPriceListRequest | Request parameters
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Get supplier price list
        api_response = await api_instance.list_inventory_supplier_price_list(get_price_list_request, timeout=timeout)
        print("The response of InventoryCounteragentsApi->list_inventory_supplier_price_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryCounteragentsApi->list_inventory_supplier_price_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **get_price_list_request** | [**GetPriceListRequest**](GetPriceListRequest.md)| Request parameters | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

### Return type

[**GetPriceListResponse**](GetPriceListResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Invalid input data |  -  |
**401** | Unauthorized |  -  |
**403** | Access forbidden |  -  |
**404** | Counteragent not found |  -  |
**405** | Method not allowed |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

