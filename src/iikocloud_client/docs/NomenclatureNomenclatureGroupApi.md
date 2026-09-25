# iikocloud_client.NomenclatureNomenclatureGroupApi

All URIs are relative to *https://api-ru.iiko.services*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_nomenclature_group**](NomenclatureNomenclatureGroupApi.md#create_nomenclature_group) | **POST** /api/nomenclature/v1/group/create | Create a nomenclature group
[**create_nomenclature_group_v2**](NomenclatureNomenclatureGroupApi.md#create_nomenclature_group_v2) | **POST** /api/nomenclature/v2/group/create | Create a nomenclature group (v2)
[**delete_nomenclature_groups**](NomenclatureNomenclatureGroupApi.md#delete_nomenclature_groups) | **POST** /api/nomenclature/v1/group/delete | Delete nomenclature groups
[**delete_nomenclature_groups_v2**](NomenclatureNomenclatureGroupApi.md#delete_nomenclature_groups_v2) | **POST** /api/nomenclature/v2/group/delete | Delete nomenclature groups (v2)
[**list_nomenclature_groups**](NomenclatureNomenclatureGroupApi.md#list_nomenclature_groups) | **POST** /api/nomenclature/v1/group/list | Get a list of nomenclature groups
[**list_nomenclature_groups_v2**](NomenclatureNomenclatureGroupApi.md#list_nomenclature_groups_v2) | **POST** /api/nomenclature/v2/group/list | Get a list of nomenclature groups (v2)
[**restore_nomenclature_groups**](NomenclatureNomenclatureGroupApi.md#restore_nomenclature_groups) | **POST** /api/nomenclature/v1/group/restore | Restore nomenclature groups
[**restore_nomenclature_groups_v2**](NomenclatureNomenclatureGroupApi.md#restore_nomenclature_groups_v2) | **POST** /api/nomenclature/v2/group/restore | Restore nomenclature groups (v2)
[**update_nomenclature_group**](NomenclatureNomenclatureGroupApi.md#update_nomenclature_group) | **POST** /api/nomenclature/v1/group/update | Update a nomenclature group
[**update_nomenclature_group_v2**](NomenclatureNomenclatureGroupApi.md#update_nomenclature_group_v2) | **POST** /api/nomenclature/v2/group/update | Update a nomenclature group (v2)


# **create_nomenclature_group**
> NomenclatureGroupCreateResponse create_nomenclature_group(nomenclature_group_create_request, timeout=timeout)

Create a nomenclature group

Creates a new nomenclature group.
Only the `name` field is required. All other fields are optional - if not provided or sent as `null`, default values are applied.
The `groupArticle` field must be unique within the organisation.


### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.nomenclature_group_create_request import NomenclatureGroupCreateRequest
from iikocloud_client.models.nomenclature_group_create_response import NomenclatureGroupCreateResponse
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
    api_instance = iikocloud_client.NomenclatureNomenclatureGroupApi(api_client)
    nomenclature_group_create_request = iikocloud_client.NomenclatureGroupCreateRequest() # NomenclatureGroupCreateRequest | Request body for creating a nomenclature group
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Create a nomenclature group
        api_response = await api_instance.create_nomenclature_group(nomenclature_group_create_request, timeout=timeout)
        print("The response of NomenclatureNomenclatureGroupApi->create_nomenclature_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NomenclatureNomenclatureGroupApi->create_nomenclature_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nomenclature_group_create_request** | [**NomenclatureGroupCreateRequest**](NomenclatureGroupCreateRequest.md)| Request body for creating a nomenclature group | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

### Return type

[**NomenclatureGroupCreateResponse**](NomenclatureGroupCreateResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Group created successfully |  -  |
**400** | Bad request |  -  |
**401** | Authorisation required |  -  |
**403** | Access denied |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |
**502** | Internal API Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_nomenclature_group_v2**
> NomenclatureGroupCreateResponse create_nomenclature_group_v2(nomenclature_group_create_request, timeout=timeout)

Create a nomenclature group (v2)

Creates a new nomenclature group.
Only the `name` field is required. All other fields are optional - if not provided or sent as `null`, default values are applied.
The `groupArticle` field must be unique within the organisation.


### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.nomenclature_group_create_request import NomenclatureGroupCreateRequest
from iikocloud_client.models.nomenclature_group_create_response import NomenclatureGroupCreateResponse
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
    api_instance = iikocloud_client.NomenclatureNomenclatureGroupApi(api_client)
    nomenclature_group_create_request = iikocloud_client.NomenclatureGroupCreateRequest() # NomenclatureGroupCreateRequest | Request body for creating a nomenclature group
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Create a nomenclature group (v2)
        api_response = await api_instance.create_nomenclature_group_v2(nomenclature_group_create_request, timeout=timeout)
        print("The response of NomenclatureNomenclatureGroupApi->create_nomenclature_group_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NomenclatureNomenclatureGroupApi->create_nomenclature_group_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nomenclature_group_create_request** | [**NomenclatureGroupCreateRequest**](NomenclatureGroupCreateRequest.md)| Request body for creating a nomenclature group | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

### Return type

[**NomenclatureGroupCreateResponse**](NomenclatureGroupCreateResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Group created successfully |  -  |
**400** | Bad request |  -  |
**401** | Authorisation required |  -  |
**403** | Access denied |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |
**502** | Internal API Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_nomenclature_groups**
> NomenclatureGroupDeleteResponse delete_nomenclature_groups(nomenclature_group_delete_request, timeout=timeout)

Delete nomenclature groups

Marks the specified nomenclature groups as deleted.
Deletion is recursive: each group's child groups and products are deleted together with it.


### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.nomenclature_group_delete_request import NomenclatureGroupDeleteRequest
from iikocloud_client.models.nomenclature_group_delete_response import NomenclatureGroupDeleteResponse
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
    api_instance = iikocloud_client.NomenclatureNomenclatureGroupApi(api_client)
    nomenclature_group_delete_request = iikocloud_client.NomenclatureGroupDeleteRequest() # NomenclatureGroupDeleteRequest | Request body for deleting nomenclature groups
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Delete nomenclature groups
        api_response = await api_instance.delete_nomenclature_groups(nomenclature_group_delete_request, timeout=timeout)
        print("The response of NomenclatureNomenclatureGroupApi->delete_nomenclature_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NomenclatureNomenclatureGroupApi->delete_nomenclature_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nomenclature_group_delete_request** | [**NomenclatureGroupDeleteRequest**](NomenclatureGroupDeleteRequest.md)| Request body for deleting nomenclature groups | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

### Return type

[**NomenclatureGroupDeleteResponse**](NomenclatureGroupDeleteResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Groups deleted successfully |  -  |
**400** | Bad request |  -  |
**401** | Authorisation required |  -  |
**403** | Access denied |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |
**502** | Internal API Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_nomenclature_groups_v2**
> NomenclatureGroupDeleteResponse delete_nomenclature_groups_v2(nomenclature_group_delete_request, timeout=timeout)

Delete nomenclature groups (v2)

Marks the specified nomenclature groups as deleted.
Deletion is recursive: each group's child groups and products are deleted together with it.


### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.nomenclature_group_delete_request import NomenclatureGroupDeleteRequest
from iikocloud_client.models.nomenclature_group_delete_response import NomenclatureGroupDeleteResponse
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
    api_instance = iikocloud_client.NomenclatureNomenclatureGroupApi(api_client)
    nomenclature_group_delete_request = iikocloud_client.NomenclatureGroupDeleteRequest() # NomenclatureGroupDeleteRequest | Request body for deleting nomenclature groups
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Delete nomenclature groups (v2)
        api_response = await api_instance.delete_nomenclature_groups_v2(nomenclature_group_delete_request, timeout=timeout)
        print("The response of NomenclatureNomenclatureGroupApi->delete_nomenclature_groups_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NomenclatureNomenclatureGroupApi->delete_nomenclature_groups_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nomenclature_group_delete_request** | [**NomenclatureGroupDeleteRequest**](NomenclatureGroupDeleteRequest.md)| Request body for deleting nomenclature groups | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

### Return type

[**NomenclatureGroupDeleteResponse**](NomenclatureGroupDeleteResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Groups deleted successfully |  -  |
**400** | Bad request |  -  |
**401** | Authorisation required |  -  |
**403** | Access denied |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |
**502** | Internal API Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_nomenclature_groups**
> NomenclatureGroupListResponse list_nomenclature_groups(nomenclature_group_list_request, timeout=timeout)

Get a list of nomenclature groups

Returns a list of nomenclature groups with support for filtering, field selection and pagination.
Always returns only PRODUCTS-type groups for the current organisation (`uocId`).
Deleted records are excluded by default; pass `includeDeleted: true` to include them.


### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.nomenclature_group_list_request import NomenclatureGroupListRequest
from iikocloud_client.models.nomenclature_group_list_response import NomenclatureGroupListResponse
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
    api_instance = iikocloud_client.NomenclatureNomenclatureGroupApi(api_client)
    nomenclature_group_list_request = iikocloud_client.NomenclatureGroupListRequest() # NomenclatureGroupListRequest | Parameters for the nomenclature group list request
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Get a list of nomenclature groups
        api_response = await api_instance.list_nomenclature_groups(nomenclature_group_list_request, timeout=timeout)
        print("The response of NomenclatureNomenclatureGroupApi->list_nomenclature_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NomenclatureNomenclatureGroupApi->list_nomenclature_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nomenclature_group_list_request** | [**NomenclatureGroupListRequest**](NomenclatureGroupListRequest.md)| Parameters for the nomenclature group list request | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

### Return type

[**NomenclatureGroupListResponse**](NomenclatureGroupListResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of nomenclature groups |  -  |
**400** | Bad request |  -  |
**401** | Authorisation required |  -  |
**403** | Access denied |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_nomenclature_groups_v2**
> NomenclatureGroupListResponse list_nomenclature_groups_v2(nomenclature_group_list_request, timeout=timeout)

Get a list of nomenclature groups (v2)

Returns a list of nomenclature groups of the current organisation with filtering and pagination support.
Only groups of the PRODUCTS type are returned (the `type` filter is applied internally and cannot be overridden).
Deleted groups are returned unless the `isDeleted eq false` filter is passed.
Filter fields: `id` / `groupId`, `name`, `code`, `groupArticle`, `parentId`, `isDeleted`, `system`,
`description`, `includeInReport`, `isChainRoot`, `revision`, `categoryId`, `accountingCategoryId`,
`taxCategoryId`, `franchiseUniqueId`, `franchiseMasterId`.
All the standard operators (eq, ne, in, nin, like, blank, notblank, gt, gte, lt, lte) are accepted for every
listed field; their applicability depends on the field type: eq/in for UUID fields, eq for boolean fields,
range operators (gt, gte, lt, lte) for the numeric `revision` field.
All filters are combined with AND. Pagination via `limit`/`offset`.


### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.nomenclature_group_list_request import NomenclatureGroupListRequest
from iikocloud_client.models.nomenclature_group_list_response import NomenclatureGroupListResponse
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
    api_instance = iikocloud_client.NomenclatureNomenclatureGroupApi(api_client)
    nomenclature_group_list_request = iikocloud_client.NomenclatureGroupListRequest() # NomenclatureGroupListRequest | Parameters for the nomenclature group list request
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Get a list of nomenclature groups (v2)
        api_response = await api_instance.list_nomenclature_groups_v2(nomenclature_group_list_request, timeout=timeout)
        print("The response of NomenclatureNomenclatureGroupApi->list_nomenclature_groups_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NomenclatureNomenclatureGroupApi->list_nomenclature_groups_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nomenclature_group_list_request** | [**NomenclatureGroupListRequest**](NomenclatureGroupListRequest.md)| Parameters for the nomenclature group list request | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

### Return type

[**NomenclatureGroupListResponse**](NomenclatureGroupListResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of nomenclature groups |  -  |
**400** | Bad request |  -  |
**401** | Authorisation required |  -  |
**403** | Access denied |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restore_nomenclature_groups**
> NomenclatureGroupUndeleteResponse restore_nomenclature_groups(nomenclature_group_undelete_request, timeout=timeout)

Restore nomenclature groups

Restores previously deleted nomenclature groups.
When `recursively: true`, all child groups and their products are also restored.


### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.nomenclature_group_undelete_request import NomenclatureGroupUndeleteRequest
from iikocloud_client.models.nomenclature_group_undelete_response import NomenclatureGroupUndeleteResponse
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
    api_instance = iikocloud_client.NomenclatureNomenclatureGroupApi(api_client)
    nomenclature_group_undelete_request = iikocloud_client.NomenclatureGroupUndeleteRequest() # NomenclatureGroupUndeleteRequest | Request body for restoring nomenclature groups
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Restore nomenclature groups
        api_response = await api_instance.restore_nomenclature_groups(nomenclature_group_undelete_request, timeout=timeout)
        print("The response of NomenclatureNomenclatureGroupApi->restore_nomenclature_groups:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NomenclatureNomenclatureGroupApi->restore_nomenclature_groups: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nomenclature_group_undelete_request** | [**NomenclatureGroupUndeleteRequest**](NomenclatureGroupUndeleteRequest.md)| Request body for restoring nomenclature groups | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

### Return type

[**NomenclatureGroupUndeleteResponse**](NomenclatureGroupUndeleteResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Groups restored successfully |  -  |
**400** | Bad request |  -  |
**401** | Authorisation required |  -  |
**403** | Access denied |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |
**502** | Internal API Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restore_nomenclature_groups_v2**
> NomenclatureGroupUndeleteResponse restore_nomenclature_groups_v2(nomenclature_group_undelete_request, timeout=timeout)

Restore nomenclature groups (v2)

Restores previously deleted nomenclature groups.
When `recursively: true`, all child groups and their products are also restored.


### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.nomenclature_group_undelete_request import NomenclatureGroupUndeleteRequest
from iikocloud_client.models.nomenclature_group_undelete_response import NomenclatureGroupUndeleteResponse
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
    api_instance = iikocloud_client.NomenclatureNomenclatureGroupApi(api_client)
    nomenclature_group_undelete_request = iikocloud_client.NomenclatureGroupUndeleteRequest() # NomenclatureGroupUndeleteRequest | Request body for restoring nomenclature groups
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Restore nomenclature groups (v2)
        api_response = await api_instance.restore_nomenclature_groups_v2(nomenclature_group_undelete_request, timeout=timeout)
        print("The response of NomenclatureNomenclatureGroupApi->restore_nomenclature_groups_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NomenclatureNomenclatureGroupApi->restore_nomenclature_groups_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nomenclature_group_undelete_request** | [**NomenclatureGroupUndeleteRequest**](NomenclatureGroupUndeleteRequest.md)| Request body for restoring nomenclature groups | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

### Return type

[**NomenclatureGroupUndeleteResponse**](NomenclatureGroupUndeleteResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Groups restored successfully |  -  |
**400** | Bad request |  -  |
**401** | Authorisation required |  -  |
**403** | Access denied |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |
**502** | Internal API Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_nomenclature_group**
> NomenclatureGroupUpdateResponse update_nomenclature_group(nomenclature_group_update_request, timeout=timeout)

Update a nomenclature group

Updates an existing nomenclature group.
The `group` (UUID of the group to update) and `name` fields are required.
The position (`position`) is not changed during an update.
The `groupArticle` field must be unique within the organisation (a match with the current record is allowed).


### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.nomenclature_group_update_request import NomenclatureGroupUpdateRequest
from iikocloud_client.models.nomenclature_group_update_response import NomenclatureGroupUpdateResponse
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
    api_instance = iikocloud_client.NomenclatureNomenclatureGroupApi(api_client)
    nomenclature_group_update_request = iikocloud_client.NomenclatureGroupUpdateRequest() # NomenclatureGroupUpdateRequest | Request body for updating a nomenclature group
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Update a nomenclature group
        api_response = await api_instance.update_nomenclature_group(nomenclature_group_update_request, timeout=timeout)
        print("The response of NomenclatureNomenclatureGroupApi->update_nomenclature_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NomenclatureNomenclatureGroupApi->update_nomenclature_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nomenclature_group_update_request** | [**NomenclatureGroupUpdateRequest**](NomenclatureGroupUpdateRequest.md)| Request body for updating a nomenclature group | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

### Return type

[**NomenclatureGroupUpdateResponse**](NomenclatureGroupUpdateResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Group updated successfully |  -  |
**400** | Bad request |  -  |
**401** | Authorisation required |  -  |
**403** | Access denied |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |
**502** | Internal API Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_nomenclature_group_v2**
> NomenclatureGroupUpdateResponse update_nomenclature_group_v2(nomenclature_group_update_request, timeout=timeout)

Update a nomenclature group (v2)

Updates an existing nomenclature group.
The `groupId` (UUID of the group to update) and `name` fields are required.
The position (`position`) is not changed during an update.
The `groupArticle` field must be unique within the organisation (a match with the current record is allowed).


### Example

* Bearer Authentication (BearerAuth):

```python
import iikocloud_client
from iikocloud_client.models.nomenclature_group_update_request import NomenclatureGroupUpdateRequest
from iikocloud_client.models.nomenclature_group_update_response import NomenclatureGroupUpdateResponse
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
    api_instance = iikocloud_client.NomenclatureNomenclatureGroupApi(api_client)
    nomenclature_group_update_request = iikocloud_client.NomenclatureGroupUpdateRequest() # NomenclatureGroupUpdateRequest | Request body for updating a nomenclature group
    timeout = 56 # int | Default: <code>15</code></br> Example: <code>10</code></br> Timeout in seconds.  (optional)

    try:
        # Update a nomenclature group (v2)
        api_response = await api_instance.update_nomenclature_group_v2(nomenclature_group_update_request, timeout=timeout)
        print("The response of NomenclatureNomenclatureGroupApi->update_nomenclature_group_v2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NomenclatureNomenclatureGroupApi->update_nomenclature_group_v2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nomenclature_group_update_request** | [**NomenclatureGroupUpdateRequest**](NomenclatureGroupUpdateRequest.md)| Request body for updating a nomenclature group | 
 **timeout** | **int**| Default: &lt;code&gt;15&lt;/code&gt;&lt;/br&gt; Example: &lt;code&gt;10&lt;/code&gt;&lt;/br&gt; Timeout in seconds.  | [optional] 

### Return type

[**NomenclatureGroupUpdateResponse**](NomenclatureGroupUpdateResponse.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Group updated successfully |  -  |
**400** | Bad request |  -  |
**401** | Authorisation required |  -  |
**403** | Access denied |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |
**502** | Internal API Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

