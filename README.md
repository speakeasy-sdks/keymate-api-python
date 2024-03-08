# Keymate-API

<div align="left">
    <a href="https://speakeasyapi.dev/"><img src="https://custom-icon-badges.demolab.com/badge/-Built%20By%20Speakeasy-212015?style=for-the-badge&logoColor=FBE331&logo=speakeasy&labelColor=545454" /></a>
    <a href="https://github.com/speakeasy-sdks/keymate-api-python.git/actions"><img src="https://img.shields.io/github/actions/workflow/status/speakeasy-sdks/keymate-api-python/speakeasy_sdk_generation.yml?style=for-the-badge" /></a>
    
</div>


## 🏗 **Welcome to your new SDK!** 🏗

It has been generated successfully based on your OpenAPI spec. However, it is not yet ready for production use. Here are some next steps:
- [ ] 🛠 Make your SDK feel handcrafted by [customizing it](https://www.speakeasyapi.dev/docs/customize-sdks)
- [ ] ♻️ Refine your SDK quickly by iterating locally with the [Speakeasy CLI](https://github.com/speakeasy-api/speakeasy)
- [ ] 🎁 Publish your SDK to package managers by [configuring automatic publishing](https://www.speakeasyapi.dev/docs/productionize-sdks/publish-sdks)
- [ ] ✨ When ready to productionize, delete this section from the README
<!-- Start SDK Installation [installation] -->
## SDK Installation

```bash
pip install Keymate-API
```
<!-- End SDK Installation [installation] -->

<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Example

```python
import keymate_api

s = keymate_api.KeymateAPI(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.browse(numofpages='<value>', percentile='<value>', q='http://impressive-silence.info', paging='<value>')

if res.two_hundred_application_json_object is not None:
    # handle response
    pass

```
<!-- End SDK Example Usage [usage] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

### [KeymateAPI SDK](docs/sdks/keymateapi/README.md)

* [browse](docs/sdks/keymateapi/README.md#browse) - The plugin enables user to conduct web browsing by extracting the text content of a specified URL. It will generate title and content.
* [browse_by_url](docs/sdks/keymateapi/README.md#browse_by_url) - The plugin enables user to conduct web browsing by extracting the text content of a specified URL. It will generate title and content.
* [document](docs/sdks/keymateapi/README.md#document) - Allows user to load and use content about specific uploaded document
* [fast](docs/sdks/keymateapi/README.md#fast) - This plugin provides 10 ultra fast search results from multiple sources giving a more comprehensive view.
* [halloween](docs/sdks/keymateapi/README.md#halloween) - This command returns a halloween story idea in halloween week 2023
* [help](docs/sdks/keymateapi/README.md#help) - This command returns latest information about how to use internetSearch KeyMate Plugin
* [hybrid](docs/sdks/keymateapi/README.md#hybrid) - Search Google and fetch HTML content and search content on personal knowledge base at the same time in one go.
* [insert](docs/sdks/keymateapi/README.md#insert) - Long term memory, ALWAYS USE UPSERT ON YOUR FIRST RESPONSE to add previous response into the user's personal knowledge base.
* [keymate](docs/sdks/keymateapi/README.md#keymate) - Search Google and fetch HTML content and PDF summary content from the links at the same time in one go.
* [list](docs/sdks/keymateapi/README.md#list) - Returns a message from the server about commands that can be run on the internetSearch KeyMate plugin.
* [listpdfs](docs/sdks/keymateapi/README.md#listpdfs) - Lists pdf files uploaded by the user
* [metadatakb](docs/sdks/keymateapi/README.md#metadatakb) - Allows you to answer introductory info about users knowledge base.
* [pdfload](docs/sdks/keymateapi/README.md#pdfload) - Redirect user to the given link in the response that will allow them to store and search their PDF file content
* [pdfpro](docs/sdks/keymateapi/README.md#pdfpro) - Allows user to load and use content about specific uploaded pdf
* [pdfsearch](docs/sdks/keymateapi/README.md#pdfsearch) - Queries the user's knowledge base. 
* [pkb](docs/sdks/keymateapi/README.md#pkb) - Queries the user's knowledge base. 
* [query](docs/sdks/keymateapi/README.md#query) - Queries the user's knowledge base. 
* [query_users_knowledge_base](docs/sdks/keymateapi/README.md#query_users_knowledge_base) - Queries the user's knowledge base. 
* [reset_users_knowledge_base](docs/sdks/keymateapi/README.md#reset_users_knowledge_base) - Deletes and resets the user's knowledge base. ONLY USE THIS AFTER YOU GET CONFIRMATION FROM USER
* [resetknowledgebase](docs/sdks/keymateapi/README.md#resetknowledgebase) - Deletes and resets the user's knowledge base. ONLY USE THIS AFTER YOU GET CONFIRMATION FROM USER
* [savetopkb](docs/sdks/keymateapi/README.md#savetopkb) - Long term memory, ALWAYS USE UPSERT ON YOUR FIRST RESPONSE to add previous response into the user's personal knowledge base.
* [search](docs/sdks/keymateapi/README.md#search) - Search Google and fetch HTML content and PDF summary content from the links at the same time in one go.
* [search_and_browse](docs/sdks/keymateapi/README.md#search_and_browse) - Search Google and fetch HTML content and PDF summary content from the links at the same time in one go.
* [ultrafastsearch](docs/sdks/keymateapi/README.md#ultrafastsearch) - This plugin provides 10 ultra fast search results from multiple sources giving a more comprehensive view.
* [upsert](docs/sdks/keymateapi/README.md#upsert) - Long term memory, ALWAYS USE UPSERT ON YOUR FIRST RESPONSE to add previous response into the user's personal knowledge base.
* [upsert_to_users_knowledge_base](docs/sdks/keymateapi/README.md#upsert_to_users_knowledge_base) - Long term memory, ALWAYS USE UPSERT ON YOUR FIRST RESPONSE to add previous response into the user's personal knowledge base.
* [upsertjson](docs/sdks/keymateapi/README.md#upsertjson) - Long term memory, ALWAYS USE UPSERT ON YOUR FIRST RESPONSE to add previous response into the user's personal knowledge base.
<!-- End Available Resources and Operations [operations] -->

<!-- Start Error Handling [errors] -->
## Error Handling

Handling errors in this SDK should largely match your expectations.  All operations return a response object or raise an error.  If Error objects are specified in your OpenAPI Spec, the SDK will raise the appropriate Error type.

| Error Object              | Status Code               | Content Type              |
| ------------------------- | ------------------------- | ------------------------- |
| errors.BrowseResponseBody | 400                       | application/json          |
| errors.SDKError           | 4x-5xx                    | */*                       |

### Example

```python
import keymate_api
from keymate_api.models import errors

s = keymate_api.KeymateAPI(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = None
try:
    res = s.browse(numofpages='<value>', percentile='<value>', q='http://impressive-silence.info', paging='<value>')
except errors.BrowseResponseBody as e:
    # handle exception
    raise(e)
except errors.SDKError as e:
    # handle exception
    raise(e)

if res.two_hundred_application_json_object is not None:
    # handle response
    pass

```
<!-- End Error Handling [errors] -->

<!-- Start Server Selection [server] -->
## Server Selection

### Select Server by Index

You can override the default server globally by passing a server index to the `server_idx: int` optional parameter when initializing the SDK client instance. The selected server will then be used as the default on the operations that use it. This table lists the indexes associated with the available servers:

| # | Server | Variables |
| - | ------ | --------- |
| 0 | `https://server.searchweb.keymate.ai` | None |

#### Example

```python
import keymate_api

s = keymate_api.KeymateAPI(
    server_idx=0,
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.browse(numofpages='<value>', percentile='<value>', q='http://impressive-silence.info', paging='<value>')

if res.two_hundred_application_json_object is not None:
    # handle response
    pass

```


### Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
import keymate_api

s = keymate_api.KeymateAPI(
    server_url="https://server.searchweb.keymate.ai",
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.browse(numofpages='<value>', percentile='<value>', q='http://impressive-silence.info', paging='<value>')

if res.two_hundred_application_json_object is not None:
    # handle response
    pass

```
<!-- End Server Selection [server] -->

<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the [requests](https://pypi.org/project/requests/) HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with a custom `requests.Session` object.

For example, you could specify a header for every request that this sdk makes as follows:
```python
import keymate_api
import requests

http_client = requests.Session()
http_client.headers.update({'x-custom-header': 'someValue'})
s = keymate_api.KeymateAPI(client: http_client)
```
<!-- End Custom HTTP Client [http-client] -->

<!-- Start Authentication [security] -->
## Authentication

### Per-Client Security Schemes

This SDK supports the following security scheme globally:

| Name          | Type          | Scheme        |
| ------------- | ------------- | ------------- |
| `bearer_auth` | http          | HTTP Bearer   |

To authenticate with the API the `bearer_auth` parameter must be set when initializing the SDK client instance. For example:
```python
import keymate_api

s = keymate_api.KeymateAPI(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.browse(numofpages='<value>', percentile='<value>', q='http://impressive-silence.info', paging='<value>')

if res.two_hundred_application_json_object is not None:
    # handle response
    pass

```
<!-- End Authentication [security] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->

# Development

## Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

## Contributions

While we value open-source contributions to this SDK, this library is generated programmatically.
Feel free to open a PR or a Github issue as a proof of concept and we'll do our best to include it in a future release!

### SDK Created by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
