# iikocloud_client.NomenclatureNomenclatureCategoryApi

All URIs are relative to *https://api-ru.iiko.services*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_nomenclature_product_category**](NomenclatureNomenclatureCategoryApi.md#create_nomenclature_product_category) | **POST** /api/nomenclature/v1/nomenclature/category/create | Create a product category
[**delete_nomenclature_product_category**](NomenclatureNomenclatureCategoryApi.md#delete_nomenclature_product_category) | **POST** /api/nomenclature/v1/nomenclature/category/delete | Delete a product category
[**list_nomenclature_product_categories**](NomenclatureNomenclatureCategoryApi.md#list_nomenclature_product_categories) | **POST** /api/nomenclature/v1/nomenclature/category/list | Get a list of product categories
[**restore_nomenclature_product_category**](NomenclatureNomenclatureCategoryApi.md#restore_nomenclature_product_category) | **POST** /api/nomenclature/v1/nomenclature/category/restore | Restore a product category
[**update_nomenclature_product_category**](NomenclatureNomenclatureCategoryApi.md#update_nomenclature_product_category) | **POST** /api/nomenclature/v1/nomenclature/category/update | Update a product category


# **create_nomenclature_product_category**
> NomenclatureCategoryWriteResponse create_nomenclature_product_category(nomenclature_category_create_request, timeout=timeout)

Create a product category

Creates a new product category.
Only the `name` field is required.


### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.nomenclature_category_create_request import NomenclatureCategoryCreateRequest
from iikocloud_client.models.nomenclature_category_write_response import NomenclatureCategoryWriteResponse
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
    api_instance = iikocloud_client.NomenclatureNomenclatureCategoryApi(api_client)
    nomenclature_category_create_request = iikocloud_client.NomenclatureCategoryCreateRequest() # NomenclatureCategoryCreateRequest | Request body for creating a product category
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Create a product category
        api_response = await api_instance.create_nomenclature_product_category(nomenclature_category_create_request, timeout=timeout)
        print("The response of NomenclatureNomenclatureCategoryApi->create_nomenclature_product_category:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NomenclatureNomenclatureCategoryApi->create_nomenclature_product_category: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nomenclature_category_create_request** | [**NomenclatureCategoryCreateRequest**](NomenclatureCategoryCreateRequest.md)| Request body for creating a product category | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

### Return type

[**NomenclatureCategoryWriteResponse**](NomenclatureCategoryWriteResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Product category created successfully |  -  |
**400** | Bad request |  -  |
**401** | Authorisation required |  -  |
**403** | Access denied |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |
**502** | Internal API Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_nomenclature_product_category**
> NomenclatureCategoryWriteResponse delete_nomenclature_product_category(nomenclature_category_delete_request, timeout=timeout)

Delete a product category

Soft-deletes a product category by UUID.
Already deleted categories cannot be deleted again.


### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.nomenclature_category_delete_request import NomenclatureCategoryDeleteRequest
from iikocloud_client.models.nomenclature_category_write_response import NomenclatureCategoryWriteResponse
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
    api_instance = iikocloud_client.NomenclatureNomenclatureCategoryApi(api_client)
    nomenclature_category_delete_request = iikocloud_client.NomenclatureCategoryDeleteRequest() # NomenclatureCategoryDeleteRequest | Request body for deleting a product category
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Delete a product category
        api_response = await api_instance.delete_nomenclature_product_category(nomenclature_category_delete_request, timeout=timeout)
        print("The response of NomenclatureNomenclatureCategoryApi->delete_nomenclature_product_category:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NomenclatureNomenclatureCategoryApi->delete_nomenclature_product_category: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nomenclature_category_delete_request** | [**NomenclatureCategoryDeleteRequest**](NomenclatureCategoryDeleteRequest.md)| Request body for deleting a product category | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

### Return type

[**NomenclatureCategoryWriteResponse**](NomenclatureCategoryWriteResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Product category deleted successfully |  -  |
**400** | Bad request |  -  |
**401** | Authorisation required |  -  |
**403** | Access denied |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |
**502** | Internal API Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_nomenclature_product_categories**
> NomenclatureCategoryListResponse list_nomenclature_product_categories(nomenclature_category_list_request, timeout=timeout)

Get a list of product categories

Returns a list of product categories.
The list can be narrowed by passing the `ids` array; pass `includeDeleted: true` to include soft-deleted categories.
Pagination is supported via `limit` / `offset`: `limit` is the maximum number of categories in the response page,
`offset` is the number of categories to skip from the beginning. If `limit` is not passed or is <= 0, all
matching categories are returned. The `totalCount` field always contains the total number of matching categories
(before pagination).


### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.nomenclature_category_list_request import NomenclatureCategoryListRequest
from iikocloud_client.models.nomenclature_category_list_response import NomenclatureCategoryListResponse
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
    api_instance = iikocloud_client.NomenclatureNomenclatureCategoryApi(api_client)
    nomenclature_category_list_request = iikocloud_client.NomenclatureCategoryListRequest() # NomenclatureCategoryListRequest | Request body for listing product categories
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Get a list of product categories
        api_response = await api_instance.list_nomenclature_product_categories(nomenclature_category_list_request, timeout=timeout)
        print("The response of NomenclatureNomenclatureCategoryApi->list_nomenclature_product_categories:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NomenclatureNomenclatureCategoryApi->list_nomenclature_product_categories: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nomenclature_category_list_request** | [**NomenclatureCategoryListRequest**](NomenclatureCategoryListRequest.md)| Request body for listing product categories | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

### Return type

[**NomenclatureCategoryListResponse**](NomenclatureCategoryListResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of product categories |  -  |
**400** | Bad request |  -  |
**401** | Authorisation required |  -  |
**403** | Access denied |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |
**502** | Internal API Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restore_nomenclature_product_category**
> NomenclatureCategoryWriteResponse restore_nomenclature_product_category(nomenclature_category_restore_request, timeout=timeout)

Restore a product category

Restores a previously deleted product category by UUID.
Only deleted categories can be restored.


### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.nomenclature_category_restore_request import NomenclatureCategoryRestoreRequest
from iikocloud_client.models.nomenclature_category_write_response import NomenclatureCategoryWriteResponse
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
    api_instance = iikocloud_client.NomenclatureNomenclatureCategoryApi(api_client)
    nomenclature_category_restore_request = iikocloud_client.NomenclatureCategoryRestoreRequest() # NomenclatureCategoryRestoreRequest | Request body for restoring a product category
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Restore a product category
        api_response = await api_instance.restore_nomenclature_product_category(nomenclature_category_restore_request, timeout=timeout)
        print("The response of NomenclatureNomenclatureCategoryApi->restore_nomenclature_product_category:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NomenclatureNomenclatureCategoryApi->restore_nomenclature_product_category: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nomenclature_category_restore_request** | [**NomenclatureCategoryRestoreRequest**](NomenclatureCategoryRestoreRequest.md)| Request body for restoring a product category | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

### Return type

[**NomenclatureCategoryWriteResponse**](NomenclatureCategoryWriteResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Product category restored successfully |  -  |
**400** | Bad request |  -  |
**401** | Authorisation required |  -  |
**403** | Access denied |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |
**502** | Internal API Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_nomenclature_product_category**
> NomenclatureCategoryWriteResponse update_nomenclature_product_category(nomenclature_category_update_request, timeout=timeout)

Update a product category

Updates an existing product category.
Both `id` (UUID of the category to update) and `name` (new name) are required.


### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.nomenclature_category_update_request import NomenclatureCategoryUpdateRequest
from iikocloud_client.models.nomenclature_category_write_response import NomenclatureCategoryWriteResponse
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
    api_instance = iikocloud_client.NomenclatureNomenclatureCategoryApi(api_client)
    nomenclature_category_update_request = iikocloud_client.NomenclatureCategoryUpdateRequest() # NomenclatureCategoryUpdateRequest | Request body for updating a product category
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Update a product category
        api_response = await api_instance.update_nomenclature_product_category(nomenclature_category_update_request, timeout=timeout)
        print("The response of NomenclatureNomenclatureCategoryApi->update_nomenclature_product_category:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NomenclatureNomenclatureCategoryApi->update_nomenclature_product_category: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nomenclature_category_update_request** | [**NomenclatureCategoryUpdateRequest**](NomenclatureCategoryUpdateRequest.md)| Request body for updating a product category | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

### Return type

[**NomenclatureCategoryWriteResponse**](NomenclatureCategoryWriteResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Product category updated successfully |  -  |
**400** | Bad request |  -  |
**401** | Authorisation required |  -  |
**403** | Access denied |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |
**502** | Internal API Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

