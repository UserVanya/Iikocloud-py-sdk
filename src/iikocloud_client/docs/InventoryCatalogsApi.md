# iikocloud_client.InventoryCatalogsApi

All URIs are relative to *https://api-ru.iiko.services*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_inventory_accounting_category**](InventoryCatalogsApi.md#get_inventory_accounting_category) | **POST** /api/inventory/v1/accounting_categories/get | Get accounting category by ID
[**get_inventory_conception**](InventoryCatalogsApi.md#get_inventory_conception) | **POST** /api/inventory/v1/conceptions/get | Get conception by ID
[**get_inventory_measure_unit**](InventoryCatalogsApi.md#get_inventory_measure_unit) | **POST** /api/inventory/v1/measure_units/get | Get measure unit by ID
[**get_inventory_payment_type**](InventoryCatalogsApi.md#get_inventory_payment_type) | **POST** /api/inventory/v1/payment_types/get | Get payment type by ID
[**list_inventory_accounting_categories**](InventoryCatalogsApi.md#list_inventory_accounting_categories) | **POST** /api/inventory/v1/accounting_categories/list | Get accounting categories list
[**list_inventory_conceptions**](InventoryCatalogsApi.md#list_inventory_conceptions) | **POST** /api/inventory/v1/conceptions/list | Get conceptions list
[**list_inventory_measure_units**](InventoryCatalogsApi.md#list_inventory_measure_units) | **POST** /api/inventory/v1/measure_units/list | Get measure units list
[**list_inventory_payment_types**](InventoryCatalogsApi.md#list_inventory_payment_types) | **POST** /api/inventory/v1/payment_types/list | Get payment types list


# **get_inventory_accounting_category**
> AccountingCategory get_inventory_accounting_category(accounting_category_get_by_id_request, timeout=timeout)

Get accounting category by ID

Returns a single accounting category by its identifier

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.accounting_category import AccountingCategory
from iikocloud_client.models.accounting_category_get_by_id_request import AccountingCategoryGetByIDRequest
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
    api_instance = iikocloud_client.InventoryCatalogsApi(api_client)
    accounting_category_get_by_id_request = iikocloud_client.AccountingCategoryGetByIDRequest() # AccountingCategoryGetByIDRequest | Request parameters
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Get accounting category by ID
        api_response = await api_instance.get_inventory_accounting_category(accounting_category_get_by_id_request, timeout=timeout)
        print("The response of InventoryCatalogsApi->get_inventory_accounting_category:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryCatalogsApi->get_inventory_accounting_category: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accounting_category_get_by_id_request** | [**AccountingCategoryGetByIDRequest**](AccountingCategoryGetByIDRequest.md)| Request parameters | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

### Return type

[**AccountingCategory**](AccountingCategory.md)

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
**404** | Accounting category not found |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_inventory_conception**
> InventoryConception get_inventory_conception(conception_get_by_id_request, timeout=timeout)

Get conception by ID

Returns a single conception by its identifier

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.conception_get_by_id_request import ConceptionGetByIDRequest
from iikocloud_client.models.inventory_conception import InventoryConception
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
    api_instance = iikocloud_client.InventoryCatalogsApi(api_client)
    conception_get_by_id_request = iikocloud_client.ConceptionGetByIDRequest() # ConceptionGetByIDRequest | Request parameters
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Get conception by ID
        api_response = await api_instance.get_inventory_conception(conception_get_by_id_request, timeout=timeout)
        print("The response of InventoryCatalogsApi->get_inventory_conception:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryCatalogsApi->get_inventory_conception: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conception_get_by_id_request** | [**ConceptionGetByIDRequest**](ConceptionGetByIDRequest.md)| Request parameters | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

### Return type

[**InventoryConception**](InventoryConception.md)

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
**404** | Conception not found |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_inventory_measure_unit**
> MeasureUnit get_inventory_measure_unit(measure_unit_get_by_id_request, timeout=timeout)

Get measure unit by ID

Returns a single measure unit by its identifier

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.measure_unit import MeasureUnit
from iikocloud_client.models.measure_unit_get_by_id_request import MeasureUnitGetByIDRequest
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
    api_instance = iikocloud_client.InventoryCatalogsApi(api_client)
    measure_unit_get_by_id_request = iikocloud_client.MeasureUnitGetByIDRequest() # MeasureUnitGetByIDRequest | Request parameters
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Get measure unit by ID
        api_response = await api_instance.get_inventory_measure_unit(measure_unit_get_by_id_request, timeout=timeout)
        print("The response of InventoryCatalogsApi->get_inventory_measure_unit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryCatalogsApi->get_inventory_measure_unit: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **measure_unit_get_by_id_request** | [**MeasureUnitGetByIDRequest**](MeasureUnitGetByIDRequest.md)| Request parameters | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

### Return type

[**MeasureUnit**](MeasureUnit.md)

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
**404** | Measure unit not found |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_inventory_payment_type**
> PaymentType get_inventory_payment_type(payment_type_get_by_id_request, timeout=timeout)

Get payment type by ID

Returns a single payment type by its identifier

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.payment_type import PaymentType
from iikocloud_client.models.payment_type_get_by_id_request import PaymentTypeGetByIDRequest
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
    api_instance = iikocloud_client.InventoryCatalogsApi(api_client)
    payment_type_get_by_id_request = iikocloud_client.PaymentTypeGetByIDRequest() # PaymentTypeGetByIDRequest | Request parameters
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Get payment type by ID
        api_response = await api_instance.get_inventory_payment_type(payment_type_get_by_id_request, timeout=timeout)
        print("The response of InventoryCatalogsApi->get_inventory_payment_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryCatalogsApi->get_inventory_payment_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_type_get_by_id_request** | [**PaymentTypeGetByIDRequest**](PaymentTypeGetByIDRequest.md)| Request parameters | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

### Return type

[**PaymentType**](PaymentType.md)

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
**404** | Payment type not found |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_inventory_accounting_categories**
> AccountingCategoryListResponse list_inventory_accounting_categories(accounting_category_list_request, timeout=timeout)

Get accounting categories list

Returns the list of accounting categories with optional filtering by isDeleted and revision, and pagination

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.accounting_category_list_request import AccountingCategoryListRequest
from iikocloud_client.models.accounting_category_list_response import AccountingCategoryListResponse
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
    api_instance = iikocloud_client.InventoryCatalogsApi(api_client)
    accounting_category_list_request = iikocloud_client.AccountingCategoryListRequest() # AccountingCategoryListRequest | Request parameters
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Get accounting categories list
        api_response = await api_instance.list_inventory_accounting_categories(accounting_category_list_request, timeout=timeout)
        print("The response of InventoryCatalogsApi->list_inventory_accounting_categories:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryCatalogsApi->list_inventory_accounting_categories: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accounting_category_list_request** | [**AccountingCategoryListRequest**](AccountingCategoryListRequest.md)| Request parameters | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

### Return type

[**AccountingCategoryListResponse**](AccountingCategoryListResponse.md)

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
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_inventory_conceptions**
> ConceptionListResponse list_inventory_conceptions(conception_list_request, timeout=timeout)

Get conceptions list

Returns the list of conceptions with optional filtering by isDeleted and revision, and pagination

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.conception_list_request import ConceptionListRequest
from iikocloud_client.models.conception_list_response import ConceptionListResponse
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
    api_instance = iikocloud_client.InventoryCatalogsApi(api_client)
    conception_list_request = iikocloud_client.ConceptionListRequest() # ConceptionListRequest | Request parameters
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Get conceptions list
        api_response = await api_instance.list_inventory_conceptions(conception_list_request, timeout=timeout)
        print("The response of InventoryCatalogsApi->list_inventory_conceptions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryCatalogsApi->list_inventory_conceptions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **conception_list_request** | [**ConceptionListRequest**](ConceptionListRequest.md)| Request parameters | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

### Return type

[**ConceptionListResponse**](ConceptionListResponse.md)

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
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_inventory_measure_units**
> MeasureUnitListResponse list_inventory_measure_units(measure_unit_list_request, timeout=timeout)

Get measure units list

Returns the list of measure units with optional filtering by isDeleted and revision, and pagination

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.measure_unit_list_request import MeasureUnitListRequest
from iikocloud_client.models.measure_unit_list_response import MeasureUnitListResponse
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
    api_instance = iikocloud_client.InventoryCatalogsApi(api_client)
    measure_unit_list_request = iikocloud_client.MeasureUnitListRequest() # MeasureUnitListRequest | Request parameters
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Get measure units list
        api_response = await api_instance.list_inventory_measure_units(measure_unit_list_request, timeout=timeout)
        print("The response of InventoryCatalogsApi->list_inventory_measure_units:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryCatalogsApi->list_inventory_measure_units: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **measure_unit_list_request** | [**MeasureUnitListRequest**](MeasureUnitListRequest.md)| Request parameters | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

### Return type

[**MeasureUnitListResponse**](MeasureUnitListResponse.md)

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
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_inventory_payment_types**
> PaymentTypeListResponse list_inventory_payment_types(payment_type_list_request, timeout=timeout)

Get payment types list

Returns the list of payment types with optional filtering by isDeleted and revision, and pagination

### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.payment_type_list_request import PaymentTypeListRequest
from iikocloud_client.models.payment_type_list_response import PaymentTypeListResponse
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
    api_instance = iikocloud_client.InventoryCatalogsApi(api_client)
    payment_type_list_request = iikocloud_client.PaymentTypeListRequest() # PaymentTypeListRequest | Request parameters
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Get payment types list
        api_response = await api_instance.list_inventory_payment_types(payment_type_list_request, timeout=timeout)
        print("The response of InventoryCatalogsApi->list_inventory_payment_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InventoryCatalogsApi->list_inventory_payment_types: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_type_list_request** | [**PaymentTypeListRequest**](PaymentTypeListRequest.md)| Request parameters | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

### Return type

[**PaymentTypeListResponse**](PaymentTypeListResponse.md)

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
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

