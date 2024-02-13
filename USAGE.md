<!-- Start SDK Example Usage [usage] -->
```python
import keymate_api

s = keymate_api.KeymateAPI(
    bearer_auth="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.browse(numofpages='string', percentile='string', q='http://impressive-silence.info', paging='string')

if res.two_hundred_application_json_object is not None:
    # handle response
    pass
```
<!-- End SDK Example Usage [usage] -->