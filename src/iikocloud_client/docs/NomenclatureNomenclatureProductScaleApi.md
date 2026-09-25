# iikocloud_client.NomenclatureNomenclatureProductScaleApi

All URIs are relative to *https://api-ru.iiko.services*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_nomenclature_product_scale**](NomenclatureNomenclatureProductScaleApi.md#create_nomenclature_product_scale) | **POST** /api/nomenclature/v1/product-scale/create | Create a product size scale
[**delete_nomenclature_product_scale**](NomenclatureNomenclatureProductScaleApi.md#delete_nomenclature_product_scale) | **POST** /api/nomenclature/v1/product-scale/delete | Delete a product size scale
[**get_nomenclature_product_scale**](NomenclatureNomenclatureProductScaleApi.md#get_nomenclature_product_scale) | **POST** /api/nomenclature/v1/product-scale/get | Get a product size scale by ID
[**list_nomenclature_product_scales**](NomenclatureNomenclatureProductScaleApi.md#list_nomenclature_product_scales) | **POST** /api/nomenclature/v1/product-scale/list | Get a list of product size scales
[**update_nomenclature_product_scale**](NomenclatureNomenclatureProductScaleApi.md#update_nomenclature_product_scale) | **POST** /api/nomenclature/v1/product-scale/update | Update a product size scale


# **create_nomenclature_product_scale**
> ProductScaleResponse create_nomenclature_product_scale(product_size_create_request, timeout=timeout)

Create a product size scale

Creates a new product size scale (ProductScale) together with the full set of sizes (productSizes[]).


### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.product_scale_response import ProductScaleResponse
from iikocloud_client.models.product_size_create_request import ProductSizeCreateRequest
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
    api_instance = iikocloud_client.NomenclatureNomenclatureProductScaleApi(api_client)
    product_size_create_request = iikocloud_client.ProductSizeCreateRequest() # ProductSizeCreateRequest | Request body for creating a product size scale
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Create a product size scale
        api_response = await api_instance.create_nomenclature_product_scale(product_size_create_request, timeout=timeout)
        print("The response of NomenclatureNomenclatureProductScaleApi->create_nomenclature_product_scale:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NomenclatureNomenclatureProductScaleApi->create_nomenclature_product_scale: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_size_create_request** | [**ProductSizeCreateRequest**](ProductSizeCreateRequest.md)| Request body for creating a product size scale | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

### Return type

[**ProductScaleResponse**](ProductScaleResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Product size scale created successfully |  -  |
**400** | Bad request |  -  |
**401** | Authorisation required |  -  |
**403** | Access denied |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |
**502** | Internal API Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_nomenclature_product_scale**
> ProductScaleResponse delete_nomenclature_product_scale(product_size_delete_request, timeout=timeout)

Delete a product size scale

Marks the specified product size scale as deleted. The scale must not be in use by any products or modifier schemas.


### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.product_scale_response import ProductScaleResponse
from iikocloud_client.models.product_size_delete_request import ProductSizeDeleteRequest
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
    api_instance = iikocloud_client.NomenclatureNomenclatureProductScaleApi(api_client)
    product_size_delete_request = iikocloud_client.ProductSizeDeleteRequest() # ProductSizeDeleteRequest | Request body for deleting a product size scale
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Delete a product size scale
        api_response = await api_instance.delete_nomenclature_product_scale(product_size_delete_request, timeout=timeout)
        print("The response of NomenclatureNomenclatureProductScaleApi->delete_nomenclature_product_scale:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NomenclatureNomenclatureProductScaleApi->delete_nomenclature_product_scale: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_size_delete_request** | [**ProductSizeDeleteRequest**](ProductSizeDeleteRequest.md)| Request body for deleting a product size scale | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

### Return type

[**ProductScaleResponse**](ProductScaleResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Product size scale deleted successfully |  -  |
**400** | Bad request |  -  |
**401** | Authorisation required |  -  |
**403** | Access denied |  -  |
**404** | Not found |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |
**502** | Internal API Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_nomenclature_product_scale**
> ProductScaleResponse get_nomenclature_product_scale(product_size_get_request, timeout=timeout)

Get a product size scale by ID

Returns a single product size scale (ProductScale) by UUID together with its nested sizes.


### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.product_scale_response import ProductScaleResponse
from iikocloud_client.models.product_size_get_request import ProductSizeGetRequest
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
    api_instance = iikocloud_client.NomenclatureNomenclatureProductScaleApi(api_client)
    product_size_get_request = iikocloud_client.ProductSizeGetRequest() # ProductSizeGetRequest | Request body for getting a product size scale
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Get a product size scale by ID
        api_response = await api_instance.get_nomenclature_product_scale(product_size_get_request, timeout=timeout)
        print("The response of NomenclatureNomenclatureProductScaleApi->get_nomenclature_product_scale:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NomenclatureNomenclatureProductScaleApi->get_nomenclature_product_scale: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_size_get_request** | [**ProductSizeGetRequest**](ProductSizeGetRequest.md)| Request body for getting a product size scale | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

### Return type

[**ProductScaleResponse**](ProductScaleResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Product size scale |  -  |
**400** | Bad request |  -  |
**401** | Authorisation required |  -  |
**403** | Access denied |  -  |
**404** | Not found |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |
**502** | Internal API Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_nomenclature_product_scales**
> ProductScaleListResponse list_nomenclature_product_scales(product_size_list_request, timeout=timeout)

Get a list of product size scales

Returns a list of product size scales (ProductScale) with nested sizes (productSizes[]).
Filter fields: `id`, `name`, `deleted`, `revision`.
Allowed operators: `id`, `name`, `deleted` — eq, ne, like, blank, notblank, in, nin; `revision` — eq only (integer).
A `revision` filter with `eq` limits the result to scales changed after the specified revision; other operators are not supported for `revision`.
All filters are combined with AND. Pagination via `limit`/`offset`.


### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.product_scale_list_response import ProductScaleListResponse
from iikocloud_client.models.product_size_list_request import ProductSizeListRequest
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
    api_instance = iikocloud_client.NomenclatureNomenclatureProductScaleApi(api_client)
    product_size_list_request = iikocloud_client.ProductSizeListRequest() # ProductSizeListRequest | Parameters for the product size scale list request
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Get a list of product size scales
        api_response = await api_instance.list_nomenclature_product_scales(product_size_list_request, timeout=timeout)
        print("The response of NomenclatureNomenclatureProductScaleApi->list_nomenclature_product_scales:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NomenclatureNomenclatureProductScaleApi->list_nomenclature_product_scales: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_size_list_request** | [**ProductSizeListRequest**](ProductSizeListRequest.md)| Parameters for the product size scale list request | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

### Return type

[**ProductScaleListResponse**](ProductScaleListResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of product size scales |  -  |
**400** | Bad request |  -  |
**401** | Authorisation required |  -  |
**403** | Access denied |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |
**502** | Internal API Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_nomenclature_product_scale**
> ProductScaleResponse update_nomenclature_product_scale(product_size_update_request, timeout=timeout)

Update a product size scale

Updates a product size scale and the complete list of sizes inside it. Sizes absent from the request will be marked deleted.


### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.product_scale_response import ProductScaleResponse
from iikocloud_client.models.product_size_update_request import ProductSizeUpdateRequest
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
    api_instance = iikocloud_client.NomenclatureNomenclatureProductScaleApi(api_client)
    product_size_update_request = iikocloud_client.ProductSizeUpdateRequest() # ProductSizeUpdateRequest | Request body for updating a product size scale
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Update a product size scale
        api_response = await api_instance.update_nomenclature_product_scale(product_size_update_request, timeout=timeout)
        print("The response of NomenclatureNomenclatureProductScaleApi->update_nomenclature_product_scale:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NomenclatureNomenclatureProductScaleApi->update_nomenclature_product_scale: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_size_update_request** | [**ProductSizeUpdateRequest**](ProductSizeUpdateRequest.md)| Request body for updating a product size scale | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

### Return type

[**ProductScaleResponse**](ProductScaleResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Product size scale updated successfully |  -  |
**400** | Bad request |  -  |
**401** | Authorisation required |  -  |
**403** | Access denied |  -  |
**404** | Not found |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |
**502** | Internal API Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

