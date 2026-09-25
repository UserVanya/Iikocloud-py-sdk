# iikocloud_client.FinanceAccountApi

All URIs are relative to *https://api-ru.iiko.services*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_finance_account**](FinanceAccountApi.md#create_finance_account) | **POST** /api/finance/v1/account/create | Create financial account
[**delete_finance_account**](FinanceAccountApi.md#delete_finance_account) | **POST** /api/finance/v1/account/delete | Delete financial account
[**get_finance_account**](FinanceAccountApi.md#get_finance_account) | **POST** /api/finance/v1/account/get | Get financial account
[**list_finance_accounts**](FinanceAccountApi.md#list_finance_accounts) | **POST** /api/finance/v1/account/list | List of financial accounts
[**restore_finance_account**](FinanceAccountApi.md#restore_finance_account) | **POST** /api/finance/v1/account/restore | Restore financial account
[**update_finance_account**](FinanceAccountApi.md#update_finance_account) | **POST** /api/finance/v1/account/update | Update financial account


# **create_finance_account**
> AccountResponse create_finance_account(account_create_request, timeout=timeout)

Create financial account

Creates a financial account

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.account_create_request import AccountCreateRequest
from iikocloud_client.models.account_response import AccountResponse
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
    api_instance = iikocloud_client.FinanceAccountApi(api_client)
    account_create_request = iikocloud_client.AccountCreateRequest() # AccountCreateRequest | Request parameters
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Create financial account
        api_response = await api_instance.create_finance_account(account_create_request, timeout=timeout)
        print("The response of FinanceAccountApi->create_finance_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FinanceAccountApi->create_finance_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_create_request** | [**AccountCreateRequest**](AccountCreateRequest.md)| Request parameters | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

### Return type

[**AccountResponse**](AccountResponse.md)

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

# **delete_finance_account**
> AccountDeleteResponse delete_finance_account(account_delete_request, timeout=timeout)

Delete financial account

Marks a financial account as deleted

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.account_delete_request import AccountDeleteRequest
from iikocloud_client.models.account_delete_response import AccountDeleteResponse
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
    api_instance = iikocloud_client.FinanceAccountApi(api_client)
    account_delete_request = iikocloud_client.AccountDeleteRequest() # AccountDeleteRequest | Request parameters
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Delete financial account
        api_response = await api_instance.delete_finance_account(account_delete_request, timeout=timeout)
        print("The response of FinanceAccountApi->delete_finance_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FinanceAccountApi->delete_finance_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_delete_request** | [**AccountDeleteRequest**](AccountDeleteRequest.md)| Request parameters | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

### Return type

[**AccountDeleteResponse**](AccountDeleteResponse.md)

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

# **get_finance_account**
> AccountResponse get_finance_account(account_get_request, timeout=timeout)

Get financial account

Returns a financial account by id

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.account_get_request import AccountGetRequest
from iikocloud_client.models.account_response import AccountResponse
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
    api_instance = iikocloud_client.FinanceAccountApi(api_client)
    account_get_request = iikocloud_client.AccountGetRequest() # AccountGetRequest | Request parameters
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Get financial account
        api_response = await api_instance.get_finance_account(account_get_request, timeout=timeout)
        print("The response of FinanceAccountApi->get_finance_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FinanceAccountApi->get_finance_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_get_request** | [**AccountGetRequest**](AccountGetRequest.md)| Request parameters | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

### Return type

[**AccountResponse**](AccountResponse.md)

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

# **list_finance_accounts**
> AccountListResponse list_finance_accounts(account_list_request, timeout=timeout)

List of financial accounts

Returns a list of financial accounts

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.account_list_request import AccountListRequest
from iikocloud_client.models.account_list_response import AccountListResponse
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
    api_instance = iikocloud_client.FinanceAccountApi(api_client)
    account_list_request = iikocloud_client.AccountListRequest() # AccountListRequest | Request parameters
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # List of financial accounts
        api_response = await api_instance.list_finance_accounts(account_list_request, timeout=timeout)
        print("The response of FinanceAccountApi->list_finance_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FinanceAccountApi->list_finance_accounts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_list_request** | [**AccountListRequest**](AccountListRequest.md)| Request parameters | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

### Return type

[**AccountListResponse**](AccountListResponse.md)

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

# **restore_finance_account**
> AccountRestoreResponse restore_finance_account(account_restore_request, timeout=timeout)

Restore financial account

Restores a deleted financial account

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.account_restore_request import AccountRestoreRequest
from iikocloud_client.models.account_restore_response import AccountRestoreResponse
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
    api_instance = iikocloud_client.FinanceAccountApi(api_client)
    account_restore_request = iikocloud_client.AccountRestoreRequest() # AccountRestoreRequest | Request parameters
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Restore financial account
        api_response = await api_instance.restore_finance_account(account_restore_request, timeout=timeout)
        print("The response of FinanceAccountApi->restore_finance_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FinanceAccountApi->restore_finance_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_restore_request** | [**AccountRestoreRequest**](AccountRestoreRequest.md)| Request parameters | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

### Return type

[**AccountRestoreResponse**](AccountRestoreResponse.md)

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

# **update_finance_account**
> AccountResponse update_finance_account(account_update_request, timeout=timeout)

Update financial account

Updates a financial account

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.account_response import AccountResponse
from iikocloud_client.models.account_update_request import AccountUpdateRequest
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
    api_instance = iikocloud_client.FinanceAccountApi(api_client)
    account_update_request = iikocloud_client.AccountUpdateRequest() # AccountUpdateRequest | Request parameters
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Update financial account
        api_response = await api_instance.update_finance_account(account_update_request, timeout=timeout)
        print("The response of FinanceAccountApi->update_finance_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FinanceAccountApi->update_finance_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_update_request** | [**AccountUpdateRequest**](AccountUpdateRequest.md)| Request parameters | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

### Return type

[**AccountResponse**](AccountResponse.md)

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

