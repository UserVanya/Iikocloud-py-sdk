# iikocloud_client.FinanceCashFlowCategoryApi

All URIs are relative to *https://api-ru.iiko.services*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_finance_cash_flow_category**](FinanceCashFlowCategoryApi.md#create_finance_cash_flow_category) | **POST** /api/finance/v1/cash-flow-category/create | Create cash flow category
[**delete_finance_cash_flow_category**](FinanceCashFlowCategoryApi.md#delete_finance_cash_flow_category) | **POST** /api/finance/v1/cash-flow-category/delete | Delete cash flow category
[**get_finance_cash_flow_category**](FinanceCashFlowCategoryApi.md#get_finance_cash_flow_category) | **POST** /api/finance/v1/cash-flow-category/get | Get cash flow category
[**list_finance_cash_flow_categories**](FinanceCashFlowCategoryApi.md#list_finance_cash_flow_categories) | **POST** /api/finance/v1/cash-flow-category/list | List of cash flow categories
[**restore_finance_cash_flow_category**](FinanceCashFlowCategoryApi.md#restore_finance_cash_flow_category) | **POST** /api/finance/v1/cash-flow-category/restore | Restore cash flow category
[**update_finance_cash_flow_category**](FinanceCashFlowCategoryApi.md#update_finance_cash_flow_category) | **POST** /api/finance/v1/cash-flow-category/update | Update cash flow category


# **create_finance_cash_flow_category**
> CashFlowCategoryResponse create_finance_cash_flow_category(cash_flow_category_create_request, timeout=timeout)

Create cash flow category

Creates a cash flow category

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.cash_flow_category_create_request import CashFlowCategoryCreateRequest
from iikocloud_client.models.cash_flow_category_response import CashFlowCategoryResponse
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
    api_instance = iikocloud_client.FinanceCashFlowCategoryApi(api_client)
    cash_flow_category_create_request = iikocloud_client.CashFlowCategoryCreateRequest() # CashFlowCategoryCreateRequest | Request parameters
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Create cash flow category
        api_response = await api_instance.create_finance_cash_flow_category(cash_flow_category_create_request, timeout=timeout)
        print("The response of FinanceCashFlowCategoryApi->create_finance_cash_flow_category:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FinanceCashFlowCategoryApi->create_finance_cash_flow_category: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cash_flow_category_create_request** | [**CashFlowCategoryCreateRequest**](CashFlowCategoryCreateRequest.md)| Request parameters | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

### Return type

[**CashFlowCategoryResponse**](CashFlowCategoryResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successful response |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable entity |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |
**502** | Bad gateway |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_finance_cash_flow_category**
> CashFlowCategoryCascadeResponse delete_finance_cash_flow_category(cash_flow_category_delete_request, timeout=timeout)

Delete cash flow category

Marks a cash flow category and its active descendants as deleted

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.cash_flow_category_cascade_response import CashFlowCategoryCascadeResponse
from iikocloud_client.models.cash_flow_category_delete_request import CashFlowCategoryDeleteRequest
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
    api_instance = iikocloud_client.FinanceCashFlowCategoryApi(api_client)
    cash_flow_category_delete_request = iikocloud_client.CashFlowCategoryDeleteRequest() # CashFlowCategoryDeleteRequest | Request parameters
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Delete cash flow category
        api_response = await api_instance.delete_finance_cash_flow_category(cash_flow_category_delete_request, timeout=timeout)
        print("The response of FinanceCashFlowCategoryApi->delete_finance_cash_flow_category:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FinanceCashFlowCategoryApi->delete_finance_cash_flow_category: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cash_flow_category_delete_request** | [**CashFlowCategoryDeleteRequest**](CashFlowCategoryDeleteRequest.md)| Request parameters | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

### Return type

[**CashFlowCategoryCascadeResponse**](CashFlowCategoryCascadeResponse.md)

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
**404** | Not found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable entity |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |
**502** | Bad gateway |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_finance_cash_flow_category**
> CashFlowCategoryResponse get_finance_cash_flow_category(cash_flow_category_get_request, timeout=timeout)

Get cash flow category

Returns a cash flow category by id

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.cash_flow_category_get_request import CashFlowCategoryGetRequest
from iikocloud_client.models.cash_flow_category_response import CashFlowCategoryResponse
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
    api_instance = iikocloud_client.FinanceCashFlowCategoryApi(api_client)
    cash_flow_category_get_request = iikocloud_client.CashFlowCategoryGetRequest() # CashFlowCategoryGetRequest | Request parameters
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Get cash flow category
        api_response = await api_instance.get_finance_cash_flow_category(cash_flow_category_get_request, timeout=timeout)
        print("The response of FinanceCashFlowCategoryApi->get_finance_cash_flow_category:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FinanceCashFlowCategoryApi->get_finance_cash_flow_category: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cash_flow_category_get_request** | [**CashFlowCategoryGetRequest**](CashFlowCategoryGetRequest.md)| Request parameters | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

### Return type

[**CashFlowCategoryResponse**](CashFlowCategoryResponse.md)

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
**404** | Not found |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |
**502** | Bad gateway |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_finance_cash_flow_categories**
> CashFlowCategoryListResponse list_finance_cash_flow_categories(cash_flow_category_list_request, timeout=timeout)

List of cash flow categories

Returns a list of cash flow categories

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.cash_flow_category_list_request import CashFlowCategoryListRequest
from iikocloud_client.models.cash_flow_category_list_response import CashFlowCategoryListResponse
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
    api_instance = iikocloud_client.FinanceCashFlowCategoryApi(api_client)
    cash_flow_category_list_request = iikocloud_client.CashFlowCategoryListRequest() # CashFlowCategoryListRequest | Request parameters
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # List of cash flow categories
        api_response = await api_instance.list_finance_cash_flow_categories(cash_flow_category_list_request, timeout=timeout)
        print("The response of FinanceCashFlowCategoryApi->list_finance_cash_flow_categories:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FinanceCashFlowCategoryApi->list_finance_cash_flow_categories: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cash_flow_category_list_request** | [**CashFlowCategoryListRequest**](CashFlowCategoryListRequest.md)| Request parameters | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

### Return type

[**CashFlowCategoryListResponse**](CashFlowCategoryListResponse.md)

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
**502** | Bad gateway |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restore_finance_cash_flow_category**
> CashFlowCategoryCascadeResponse restore_finance_cash_flow_category(cash_flow_category_restore_request, timeout=timeout)

Restore cash flow category

Restores a cash flow category

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.cash_flow_category_cascade_response import CashFlowCategoryCascadeResponse
from iikocloud_client.models.cash_flow_category_restore_request import CashFlowCategoryRestoreRequest
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
    api_instance = iikocloud_client.FinanceCashFlowCategoryApi(api_client)
    cash_flow_category_restore_request = iikocloud_client.CashFlowCategoryRestoreRequest() # CashFlowCategoryRestoreRequest | Request parameters
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Restore cash flow category
        api_response = await api_instance.restore_finance_cash_flow_category(cash_flow_category_restore_request, timeout=timeout)
        print("The response of FinanceCashFlowCategoryApi->restore_finance_cash_flow_category:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FinanceCashFlowCategoryApi->restore_finance_cash_flow_category: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cash_flow_category_restore_request** | [**CashFlowCategoryRestoreRequest**](CashFlowCategoryRestoreRequest.md)| Request parameters | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

### Return type

[**CashFlowCategoryCascadeResponse**](CashFlowCategoryCascadeResponse.md)

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
**404** | Not found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable entity |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |
**502** | Bad gateway |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_finance_cash_flow_category**
> CashFlowCategoryResponse update_finance_cash_flow_category(cash_flow_category_update_request, timeout=timeout)

Update cash flow category

Updates a cash flow category

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.cash_flow_category_response import CashFlowCategoryResponse
from iikocloud_client.models.cash_flow_category_update_request import CashFlowCategoryUpdateRequest
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
    api_instance = iikocloud_client.FinanceCashFlowCategoryApi(api_client)
    cash_flow_category_update_request = iikocloud_client.CashFlowCategoryUpdateRequest() # CashFlowCategoryUpdateRequest | Request parameters
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Update cash flow category
        api_response = await api_instance.update_finance_cash_flow_category(cash_flow_category_update_request, timeout=timeout)
        print("The response of FinanceCashFlowCategoryApi->update_finance_cash_flow_category:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FinanceCashFlowCategoryApi->update_finance_cash_flow_category: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cash_flow_category_update_request** | [**CashFlowCategoryUpdateRequest**](CashFlowCategoryUpdateRequest.md)| Request parameters | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

### Return type

[**CashFlowCategoryResponse**](CashFlowCategoryResponse.md)

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
**404** | Not found |  -  |
**409** | Conflict |  -  |
**422** | Unprocessable entity |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |
**502** | Bad gateway |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

