# iikocloud_client.FinanceDirectoriesApi

All URIs are relative to *https://api-ru.iiko.services*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_finance_item_categories**](FinanceDirectoriesApi.md#list_finance_item_categories) | **POST** /api/finance/v1/item-category/list | Get a list of fiscal categories
[**list_finance_tax_categories**](FinanceDirectoriesApi.md#list_finance_tax_categories) | **POST** /api/finance/v1/tax-category/list | Get a list of tax categories


# **list_finance_item_categories**
> ItemCategoryListResponse list_finance_item_categories(item_category_list_request, timeout=timeout)

Get a list of fiscal categories

Returns a list of fiscal categories

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.item_category_list_request import ItemCategoryListRequest
from iikocloud_client.models.item_category_list_response import ItemCategoryListResponse
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
    api_instance = iikocloud_client.FinanceDirectoriesApi(api_client)
    item_category_list_request = iikocloud_client.ItemCategoryListRequest() # ItemCategoryListRequest | Request parameters
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Get a list of fiscal categories
        api_response = await api_instance.list_finance_item_categories(item_category_list_request, timeout=timeout)
        print("The response of FinanceDirectoriesApi->list_finance_item_categories:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FinanceDirectoriesApi->list_finance_item_categories: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_category_list_request** | [**ItemCategoryListRequest**](ItemCategoryListRequest.md)| Request parameters | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

### Return type

[**ItemCategoryListResponse**](ItemCategoryListResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_finance_tax_categories**
> TaxCategoryListResponse list_finance_tax_categories(tax_category_list_request, timeout=timeout)

Get a list of tax categories

Returns a list of tax categories

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.tax_category_list_request import TaxCategoryListRequest
from iikocloud_client.models.tax_category_list_response import TaxCategoryListResponse
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
    api_instance = iikocloud_client.FinanceDirectoriesApi(api_client)
    tax_category_list_request = iikocloud_client.TaxCategoryListRequest() # TaxCategoryListRequest | Request parameters
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Get a list of tax categories
        api_response = await api_instance.list_finance_tax_categories(tax_category_list_request, timeout=timeout)
        print("The response of FinanceDirectoriesApi->list_finance_tax_categories:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FinanceDirectoriesApi->list_finance_tax_categories: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tax_category_list_request** | [**TaxCategoryListRequest**](TaxCategoryListRequest.md)| Request parameters | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

### Return type

[**TaxCategoryListResponse**](TaxCategoryListResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

