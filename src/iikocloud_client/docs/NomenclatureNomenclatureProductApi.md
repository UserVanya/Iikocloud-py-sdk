# iikocloud_client.NomenclatureNomenclatureProductApi

All URIs are relative to *https://api-ru.iiko.services*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_nomenclature_product**](NomenclatureNomenclatureProductApi.md#create_nomenclature_product) | **POST** /api/nomenclature/v1/product/create | Create a product
[**create_nomenclature_product_v2**](NomenclatureNomenclatureProductApi.md#create_nomenclature_product_v2) | **POST** /api/nomenclature/v2/product/create | Create a product (v2)
[**delete_nomenclature_products**](NomenclatureNomenclatureProductApi.md#delete_nomenclature_products) | **POST** /api/nomenclature/v1/product/delete | Delete products
[**delete_nomenclature_products_v2**](NomenclatureNomenclatureProductApi.md#delete_nomenclature_products_v2) | **POST** /api/nomenclature/v2/product/delete | Delete products (v2)
[**list_nomenclature_products**](NomenclatureNomenclatureProductApi.md#list_nomenclature_products) | **POST** /api/nomenclature/v1/product/list | Get a list of products
[**list_nomenclature_products_v2**](NomenclatureNomenclatureProductApi.md#list_nomenclature_products_v2) | **POST** /api/nomenclature/v2/product/list | Get a list of products (v2)
[**restore_nomenclature_products**](NomenclatureNomenclatureProductApi.md#restore_nomenclature_products) | **POST** /api/nomenclature/v1/product/restore | Restore products
[**restore_nomenclature_products_v2**](NomenclatureNomenclatureProductApi.md#restore_nomenclature_products_v2) | **POST** /api/nomenclature/v2/product/restore | Restore products (v2)
[**update_nomenclature_product**](NomenclatureNomenclatureProductApi.md#update_nomenclature_product) | **POST** /api/nomenclature/v1/product/update | Update a product
[**update_nomenclature_product_barcodes**](NomenclatureNomenclatureProductApi.md#update_nomenclature_product_barcodes) | **POST** /api/nomenclature/v1/product/update_barcodes | Update product barcodes
[**update_nomenclature_product_barcodes_v2**](NomenclatureNomenclatureProductApi.md#update_nomenclature_product_barcodes_v2) | **POST** /api/nomenclature/v2/product/update_barcodes | Update product barcodes (v2)
[**update_nomenclature_product_v2**](NomenclatureNomenclatureProductApi.md#update_nomenclature_product_v2) | **POST** /api/nomenclature/v2/product/update | Update a product (v2)


# **create_nomenclature_product**
> NomenclatureProductCreateResponse create_nomenclature_product(nomenclature_product_create_request, timeout=timeout)

Create a product

Creates a new nomenclature product.
The `name`, `type` and `amountUnit` fields are required. All other fields are optional - if not provided or sent as `null`, default values are applied.
If `code` or `productArticle` are not provided explicitly, API server assigns them automatically.


### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.nomenclature_product_create_request import NomenclatureProductCreateRequest
from iikocloud_client.models.nomenclature_product_create_response import NomenclatureProductCreateResponse
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
    api_instance = iikocloud_client.NomenclatureNomenclatureProductApi(api_client)
    nomenclature_product_create_request = iikocloud_client.NomenclatureProductCreateRequest() # NomenclatureProductCreateRequest | Request body for creating a nomenclature product
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Create a product
        api_response = await api_instance.create_nomenclature_product(nomenclature_product_create_request, timeout=timeout)
        print("The response of NomenclatureNomenclatureProductApi->create_nomenclature_product:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NomenclatureNomenclatureProductApi->create_nomenclature_product: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nomenclature_product_create_request** | [**NomenclatureProductCreateRequest**](NomenclatureProductCreateRequest.md)| Request body for creating a nomenclature product | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

### Return type

[**NomenclatureProductCreateResponse**](NomenclatureProductCreateResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Product created successfully |  -  |
**400** | Bad request |  -  |
**401** | Authorisation required |  -  |
**403** | Access denied |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |
**502** | Internal API Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_nomenclature_product_v2**
> NomenclatureProductCreateResponse create_nomenclature_product_v2(nomenclature_product_create_request, timeout=timeout)

Create a product (v2)

Creates a new nomenclature product.
The `name`, `type` and `amountUnitId` fields are required. All other fields are optional - if not provided or sent as `null`, default values are applied.
If `code` or `productArticle` are not provided explicitly, API server assigns them automatically.


### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.nomenclature_product_create_request import NomenclatureProductCreateRequest
from iikocloud_client.models.nomenclature_product_create_response import NomenclatureProductCreateResponse
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
    api_instance = iikocloud_client.NomenclatureNomenclatureProductApi(api_client)
    nomenclature_product_create_request = iikocloud_client.NomenclatureProductCreateRequest() # NomenclatureProductCreateRequest | Request body for creating a nomenclature product
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Create a product (v2)
        api_response = await api_instance.create_nomenclature_product_v2(nomenclature_product_create_request, timeout=timeout)
        print("The response of NomenclatureNomenclatureProductApi->create_nomenclature_product_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NomenclatureNomenclatureProductApi->create_nomenclature_product_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nomenclature_product_create_request** | [**NomenclatureProductCreateRequest**](NomenclatureProductCreateRequest.md)| Request body for creating a nomenclature product | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

### Return type

[**NomenclatureProductCreateResponse**](NomenclatureProductCreateResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Product created successfully |  -  |
**400** | Bad request |  -  |
**401** | Authorisation required |  -  |
**403** | Access denied |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |
**502** | Internal API Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_nomenclature_products**
> NomenclatureProductDeleteResponse delete_nomenclature_products(nomenclature_product_delete_request, timeout=timeout)

Delete products

Marks the specified nomenclature products as deleted.


### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.nomenclature_product_delete_request import NomenclatureProductDeleteRequest
from iikocloud_client.models.nomenclature_product_delete_response import NomenclatureProductDeleteResponse
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
    api_instance = iikocloud_client.NomenclatureNomenclatureProductApi(api_client)
    nomenclature_product_delete_request = iikocloud_client.NomenclatureProductDeleteRequest() # NomenclatureProductDeleteRequest | Request body for deleting products
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Delete products
        api_response = await api_instance.delete_nomenclature_products(nomenclature_product_delete_request, timeout=timeout)
        print("The response of NomenclatureNomenclatureProductApi->delete_nomenclature_products:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NomenclatureNomenclatureProductApi->delete_nomenclature_products: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nomenclature_product_delete_request** | [**NomenclatureProductDeleteRequest**](NomenclatureProductDeleteRequest.md)| Request body for deleting products | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

### Return type

[**NomenclatureProductDeleteResponse**](NomenclatureProductDeleteResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Products deleted successfully |  -  |
**400** | Bad request |  -  |
**401** | Authorisation required |  -  |
**403** | Access denied |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |
**502** | Internal API Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_nomenclature_products_v2**
> NomenclatureProductDeleteResponse delete_nomenclature_products_v2(nomenclature_product_delete_request, timeout=timeout)

Delete products (v2)

Marks the specified nomenclature products as deleted.


### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.nomenclature_product_delete_request import NomenclatureProductDeleteRequest
from iikocloud_client.models.nomenclature_product_delete_response import NomenclatureProductDeleteResponse
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
    api_instance = iikocloud_client.NomenclatureNomenclatureProductApi(api_client)
    nomenclature_product_delete_request = iikocloud_client.NomenclatureProductDeleteRequest() # NomenclatureProductDeleteRequest | Request body for deleting products
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Delete products (v2)
        api_response = await api_instance.delete_nomenclature_products_v2(nomenclature_product_delete_request, timeout=timeout)
        print("The response of NomenclatureNomenclatureProductApi->delete_nomenclature_products_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NomenclatureNomenclatureProductApi->delete_nomenclature_products_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nomenclature_product_delete_request** | [**NomenclatureProductDeleteRequest**](NomenclatureProductDeleteRequest.md)| Request body for deleting products | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

### Return type

[**NomenclatureProductDeleteResponse**](NomenclatureProductDeleteResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Products deleted successfully |  -  |
**400** | Bad request |  -  |
**401** | Authorisation required |  -  |
**403** | Access denied |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |
**502** | Internal API Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_nomenclature_products**
> NomenclatureProductListResponse list_nomenclature_products(nomenclature_product_list_request, timeout=timeout)

Get a list of products

Returns the organisation's nomenclature — the catalogue of items used to build the menu, run warehouse accounting and generate sales reports. Supports filtering and pagination, which speeds up menu and reference synchronisation on the partner side.
By default (when no type filter is set) the method returns nomenclature items of all types available in the organisation's nomenclature. The following base nomenclature types are supported: GOODS (goods/ingredients), DISH (dishes), PREPARED (semi-prepared items), SERVICE (services), MODIFIER (modifiers). To narrow the result to specific types, apply a filter on the type field (for example op: "in").
Nomenclature groups are returned by a separate method /api/nomenclature/v1/group/list.


### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.nomenclature_product_list_request import NomenclatureProductListRequest
from iikocloud_client.models.nomenclature_product_list_response import NomenclatureProductListResponse
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
    api_instance = iikocloud_client.NomenclatureNomenclatureProductApi(api_client)
    nomenclature_product_list_request = iikocloud_client.NomenclatureProductListRequest() # NomenclatureProductListRequest | Parameters for the nomenclature product list request
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Get a list of products
        api_response = await api_instance.list_nomenclature_products(nomenclature_product_list_request, timeout=timeout)
        print("The response of NomenclatureNomenclatureProductApi->list_nomenclature_products:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NomenclatureNomenclatureProductApi->list_nomenclature_products: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nomenclature_product_list_request** | [**NomenclatureProductListRequest**](NomenclatureProductListRequest.md)| Parameters for the nomenclature product list request | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

### Return type

[**NomenclatureProductListResponse**](NomenclatureProductListResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of products |  -  |
**400** | Bad request |  -  |
**401** | Authorisation required |  -  |
**403** | Access denied |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_nomenclature_products_v2**
> NomenclatureProductListResponse list_nomenclature_products_v2(nomenclature_product_list_request, timeout=timeout)

Get a list of products (v2)

Returns the organisation's nomenclature — the catalogue of items used to build the menu, run warehouse accounting and generate sales reports. Supports filtering and pagination, which speeds up menu and reference synchronisation on the partner side.
By default (when no type filter is set) the method returns nomenclature items of all types available in the organisation's nomenclature. The following base nomenclature types are supported: GOODS (goods/ingredients), DISH (dishes), PREPARED (semi-prepared items), SERVICE (services), MODIFIER (modifiers). To narrow the result to specific types, apply a filter on the type field (for example op: "in").
Filter fields: `id` / `productId`, `type`, `name`, `code`, `productArticle`, `description`, `parentId`,
`categoryId`, `accountingCategoryId`, `taxCategoryId`, `isDeleted`, `system`, `revision`, `deletedAt`,
`createdAt`, `updatedAt`, `lastModifyNode`, `franchiseUniqueId`, `franchiseMasterId`.
Allowed operators: `id` / `productId`, `parentId`, `categoryId`, `accountingCategoryId`, `taxCategoryId`,
`franchiseUniqueId`, `franchiseMasterId` — eq, in; `type` — eq, ne, in, nin; `name`, `code`, `productArticle`,
`description` — eq, ne, in, nin, like, blank, notblank; `isDeleted`, `system` — eq (boolean); `revision`,
`createdAt`, `updatedAt` — eq, ne, gt, gte, lt, lte; `deletedAt` — eq, ne, gt, gte, lt, lte, blank, notblank;
`lastModifyNode` — eq, in, blank, notblank.
All filters are combined with AND. Pagination via `limit`/`offset`.
Nomenclature groups are returned by a separate method /api/nomenclature/v1/group/list.


### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.nomenclature_product_list_request import NomenclatureProductListRequest
from iikocloud_client.models.nomenclature_product_list_response import NomenclatureProductListResponse
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
    api_instance = iikocloud_client.NomenclatureNomenclatureProductApi(api_client)
    nomenclature_product_list_request = iikocloud_client.NomenclatureProductListRequest() # NomenclatureProductListRequest | Parameters for the nomenclature product list request
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Get a list of products (v2)
        api_response = await api_instance.list_nomenclature_products_v2(nomenclature_product_list_request, timeout=timeout)
        print("The response of NomenclatureNomenclatureProductApi->list_nomenclature_products_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NomenclatureNomenclatureProductApi->list_nomenclature_products_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nomenclature_product_list_request** | [**NomenclatureProductListRequest**](NomenclatureProductListRequest.md)| Parameters for the nomenclature product list request | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

### Return type

[**NomenclatureProductListResponse**](NomenclatureProductListResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of products |  -  |
**400** | Bad request |  -  |
**401** | Authorisation required |  -  |
**403** | Access denied |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restore_nomenclature_products**
> NomenclatureProductUndeleteResponse restore_nomenclature_products(nomenclature_product_undelete_request, timeout=timeout)

Restore products

Restores previously deleted nomenclature products.
The endpoint is named `restore` as specified.


### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.nomenclature_product_undelete_request import NomenclatureProductUndeleteRequest
from iikocloud_client.models.nomenclature_product_undelete_response import NomenclatureProductUndeleteResponse
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
    api_instance = iikocloud_client.NomenclatureNomenclatureProductApi(api_client)
    nomenclature_product_undelete_request = iikocloud_client.NomenclatureProductUndeleteRequest() # NomenclatureProductUndeleteRequest | Request body for restoring products
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Restore products
        api_response = await api_instance.restore_nomenclature_products(nomenclature_product_undelete_request, timeout=timeout)
        print("The response of NomenclatureNomenclatureProductApi->restore_nomenclature_products:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NomenclatureNomenclatureProductApi->restore_nomenclature_products: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nomenclature_product_undelete_request** | [**NomenclatureProductUndeleteRequest**](NomenclatureProductUndeleteRequest.md)| Request body for restoring products | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

### Return type

[**NomenclatureProductUndeleteResponse**](NomenclatureProductUndeleteResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Products restored successfully |  -  |
**400** | Bad request |  -  |
**401** | Authorisation required |  -  |
**403** | Access denied |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |
**502** | Internal API Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restore_nomenclature_products_v2**
> NomenclatureProductUndeleteResponse restore_nomenclature_products_v2(nomenclature_product_undelete_request, timeout=timeout)

Restore products (v2)

Restores previously deleted nomenclature products.
The endpoint is named `restore` as specified.


### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.nomenclature_product_undelete_request import NomenclatureProductUndeleteRequest
from iikocloud_client.models.nomenclature_product_undelete_response import NomenclatureProductUndeleteResponse
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
    api_instance = iikocloud_client.NomenclatureNomenclatureProductApi(api_client)
    nomenclature_product_undelete_request = iikocloud_client.NomenclatureProductUndeleteRequest() # NomenclatureProductUndeleteRequest | Request body for restoring products
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Restore products (v2)
        api_response = await api_instance.restore_nomenclature_products_v2(nomenclature_product_undelete_request, timeout=timeout)
        print("The response of NomenclatureNomenclatureProductApi->restore_nomenclature_products_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NomenclatureNomenclatureProductApi->restore_nomenclature_products_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nomenclature_product_undelete_request** | [**NomenclatureProductUndeleteRequest**](NomenclatureProductUndeleteRequest.md)| Request body for restoring products | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

### Return type

[**NomenclatureProductUndeleteResponse**](NomenclatureProductUndeleteResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Products restored successfully |  -  |
**400** | Bad request |  -  |
**401** | Authorisation required |  -  |
**403** | Access denied |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |
**502** | Internal API Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_nomenclature_product**
> NomenclatureProductUpdateResponse update_nomenclature_product(nomenclature_product_update_request, timeout=timeout)

Update a product

Updates an existing nomenclature product.
The `product` (UUID of the product to update), `name`, `type` and `amountUnit` fields are required.


### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.nomenclature_product_update_request import NomenclatureProductUpdateRequest
from iikocloud_client.models.nomenclature_product_update_response import NomenclatureProductUpdateResponse
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
    api_instance = iikocloud_client.NomenclatureNomenclatureProductApi(api_client)
    nomenclature_product_update_request = iikocloud_client.NomenclatureProductUpdateRequest() # NomenclatureProductUpdateRequest | Request body for updating a nomenclature product
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Update a product
        api_response = await api_instance.update_nomenclature_product(nomenclature_product_update_request, timeout=timeout)
        print("The response of NomenclatureNomenclatureProductApi->update_nomenclature_product:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NomenclatureNomenclatureProductApi->update_nomenclature_product: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nomenclature_product_update_request** | [**NomenclatureProductUpdateRequest**](NomenclatureProductUpdateRequest.md)| Request body for updating a nomenclature product | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

### Return type

[**NomenclatureProductUpdateResponse**](NomenclatureProductUpdateResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Product updated successfully |  -  |
**400** | Bad request |  -  |
**401** | Authorisation required |  -  |
**403** | Access denied |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |
**502** | Internal API Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_nomenclature_product_barcodes**
> NomenclatureProductUpdateBarcodesResponse update_nomenclature_product_barcodes(nomenclature_product_update_barcodes_request, timeout=timeout)

Update product barcodes

Replaces all existing barcodes for a specified nomenclature item with a new set.
<b>Note</b>: This is a full replacement operation. Any previously assigned barcode values are permanently removed and overwritten by the values provided in the request


### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.nomenclature_product_update_barcodes_request import NomenclatureProductUpdateBarcodesRequest
from iikocloud_client.models.nomenclature_product_update_barcodes_response import NomenclatureProductUpdateBarcodesResponse
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
    api_instance = iikocloud_client.NomenclatureNomenclatureProductApi(api_client)
    nomenclature_product_update_barcodes_request = iikocloud_client.NomenclatureProductUpdateBarcodesRequest() # NomenclatureProductUpdateBarcodesRequest | Product barcode update request
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Update product barcodes
        api_response = await api_instance.update_nomenclature_product_barcodes(nomenclature_product_update_barcodes_request, timeout=timeout)
        print("The response of NomenclatureNomenclatureProductApi->update_nomenclature_product_barcodes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NomenclatureNomenclatureProductApi->update_nomenclature_product_barcodes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nomenclature_product_update_barcodes_request** | [**NomenclatureProductUpdateBarcodesRequest**](NomenclatureProductUpdateBarcodesRequest.md)| Product barcode update request | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

### Return type

[**NomenclatureProductUpdateBarcodesResponse**](NomenclatureProductUpdateBarcodesResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Product barcodes successfully updated |  -  |
**400** | Bad request |  -  |
**401** | Authorisation required |  -  |
**403** | Access denied |  -  |
**404** | Not found |  -  |
**405** | Method not allowed |  -  |
**409** | Conflict |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |
**502** | Internal API Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_nomenclature_product_barcodes_v2**
> NomenclatureProductUpdateBarcodesResponse update_nomenclature_product_barcodes_v2(nomenclature_product_update_barcodes_request, timeout=timeout)

Update product barcodes (v2)

Replaces all existing barcodes for a specified nomenclature item with a new set.
<b>Note</b>: This is a full replacement operation. Any previously assigned barcode values are permanently removed and overwritten by the values provided in the request


### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.nomenclature_product_update_barcodes_request import NomenclatureProductUpdateBarcodesRequest
from iikocloud_client.models.nomenclature_product_update_barcodes_response import NomenclatureProductUpdateBarcodesResponse
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
    api_instance = iikocloud_client.NomenclatureNomenclatureProductApi(api_client)
    nomenclature_product_update_barcodes_request = iikocloud_client.NomenclatureProductUpdateBarcodesRequest() # NomenclatureProductUpdateBarcodesRequest | Product barcode update request
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Update product barcodes (v2)
        api_response = await api_instance.update_nomenclature_product_barcodes_v2(nomenclature_product_update_barcodes_request, timeout=timeout)
        print("The response of NomenclatureNomenclatureProductApi->update_nomenclature_product_barcodes_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NomenclatureNomenclatureProductApi->update_nomenclature_product_barcodes_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nomenclature_product_update_barcodes_request** | [**NomenclatureProductUpdateBarcodesRequest**](NomenclatureProductUpdateBarcodesRequest.md)| Product barcode update request | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

### Return type

[**NomenclatureProductUpdateBarcodesResponse**](NomenclatureProductUpdateBarcodesResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Product barcodes successfully updated |  -  |
**400** | Bad request |  -  |
**401** | Authorisation required |  -  |
**403** | Access denied |  -  |
**404** | Not found |  -  |
**405** | Method not allowed |  -  |
**409** | Conflict |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |
**502** | Internal API Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_nomenclature_product_v2**
> NomenclatureProductUpdateResponse update_nomenclature_product_v2(nomenclature_product_update_request, timeout=timeout)

Update a product (v2)

Updates an existing nomenclature product.
The `productId` (UUID of the product to update), `name`, `type` and `amountUnitId` fields are required.


### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.nomenclature_product_update_request import NomenclatureProductUpdateRequest
from iikocloud_client.models.nomenclature_product_update_response import NomenclatureProductUpdateResponse
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
    api_instance = iikocloud_client.NomenclatureNomenclatureProductApi(api_client)
    nomenclature_product_update_request = iikocloud_client.NomenclatureProductUpdateRequest() # NomenclatureProductUpdateRequest | Request body for updating a nomenclature product
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Update a product (v2)
        api_response = await api_instance.update_nomenclature_product_v2(nomenclature_product_update_request, timeout=timeout)
        print("The response of NomenclatureNomenclatureProductApi->update_nomenclature_product_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NomenclatureNomenclatureProductApi->update_nomenclature_product_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nomenclature_product_update_request** | [**NomenclatureProductUpdateRequest**](NomenclatureProductUpdateRequest.md)| Request body for updating a nomenclature product | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

### Return type

[**NomenclatureProductUpdateResponse**](NomenclatureProductUpdateResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Product updated successfully |  -  |
**400** | Bad request |  -  |
**401** | Authorisation required |  -  |
**403** | Access denied |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |
**502** | Internal API Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

