# openapi_client.NotesApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**notes_get**](NotesApi.md#notes_get) | **GET** /notes | Получение всех заметок.
[**notes_head**](NotesApi.md#notes_head) | **HEAD** /notes | Получение всех заметок.
[**notes_id_delete**](NotesApi.md#notes_id_delete) | **DELETE** /notes/{id} | Удаление заметки.
[**notes_id_get**](NotesApi.md#notes_id_get) | **GET** /notes/{id} | Получение заметки по id.
[**notes_id_head**](NotesApi.md#notes_id_head) | **HEAD** /notes/{id} | Получение заметки по id.
[**notes_id_put**](NotesApi.md#notes_id_put) | **PUT** /notes/{id} | Изменение заметки.
[**notes_post**](NotesApi.md#notes_post) | **POST** /notes | Создание новой заметки


# **notes_get**
> List[Note] notes_get()

Получение всех заметок.

### Example


```python
import openapi_client
from openapi_client.models.note import Note
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.NotesApi(api_client)

    try:
        # Получение всех заметок.
        api_response = await api_instance.notes_get()
        print("The response of NotesApi->notes_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotesApi->notes_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[Note]**](Note.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Заметки получены |  -  |
**500** | Ошибка сервера |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **notes_head**
> List[Note] notes_head()

Получение всех заметок.

### Example


```python
import openapi_client
from openapi_client.models.note import Note
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.NotesApi(api_client)

    try:
        # Получение всех заметок.
        api_response = await api_instance.notes_head()
        print("The response of NotesApi->notes_head:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotesApi->notes_head: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[Note]**](Note.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Заметки получены |  -  |
**500** | Ошибка сервера |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **notes_id_delete**
> notes_id_delete(id)

Удаление заметки.

### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.NotesApi(api_client)
    id = 56 # int | 

    try:
        # Удаление заметки.
        await api_instance.notes_id_delete(id)
    except Exception as e:
        print("Exception when calling NotesApi->notes_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Заметка удалена |  -  |
**422** | Ошибка валидации |  -  |
**500** | Ошибка сервера |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **notes_id_get**
> Note notes_id_get(id)

Получение заметки по id.

### Example


```python
import openapi_client
from openapi_client.models.note import Note
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.NotesApi(api_client)
    id = 56 # int | 

    try:
        # Получение заметки по id.
        api_response = await api_instance.notes_id_get(id)
        print("The response of NotesApi->notes_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotesApi->notes_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**Note**](Note.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Заметка получена |  -  |
**404** | Заметка не найдена |  -  |
**422** | Ошибка валидации |  -  |
**500** | Ошибка сервера |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **notes_id_head**
> Note notes_id_head(id)

Получение заметки по id.

### Example


```python
import openapi_client
from openapi_client.models.note import Note
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.NotesApi(api_client)
    id = 56 # int | 

    try:
        # Получение заметки по id.
        api_response = await api_instance.notes_id_head(id)
        print("The response of NotesApi->notes_id_head:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotesApi->notes_id_head: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**Note**](Note.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Заметка получена |  -  |
**404** | Заметка не найдена |  -  |
**422** | Ошибка валидации |  -  |
**500** | Ошибка сервера |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **notes_id_put**
> Note notes_id_put(id, note_text=note_text)

Изменение заметки.

### Example


```python
import openapi_client
from openapi_client.models.note import Note
from openapi_client.models.note_text import NoteText
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.NotesApi(api_client)
    id = 56 # int | 
    note_text = openapi_client.NoteText() # NoteText |  (optional)

    try:
        # Изменение заметки.
        api_response = await api_instance.notes_id_put(id, note_text=note_text)
        print("The response of NotesApi->notes_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotesApi->notes_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **note_text** | [**NoteText**](NoteText.md)|  | [optional] 

### Return type

[**Note**](Note.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Заметка изменена |  -  |
**404** | Заметка не найдена |  -  |
**422** | Ошибка валидации |  -  |
**500** | Ошибка сервера |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **notes_post**
> Note notes_post(note_text=note_text)

Создание новой заметки

### Example


```python
import openapi_client
from openapi_client.models.note import Note
from openapi_client.models.note_text import NoteText
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
async with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.NotesApi(api_client)
    note_text = openapi_client.NoteText() # NoteText |  (optional)

    try:
        # Создание новой заметки
        api_response = await api_instance.notes_post(note_text=note_text)
        print("The response of NotesApi->notes_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling NotesApi->notes_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **note_text** | [**NoteText**](NoteText.md)|  | [optional] 

### Return type

[**Note**](Note.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Заметка создана |  -  |
**422** | Ошибка валидации |  -  |
**500** | Ошибка сервера |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

