<!-- Start SDK Example Usage -->
```python
import keymate_api
from keymate_api.models import operations

s = keymate_api.KeymateAPI(
    bearer_auth="",
)


res = s.browse(numofpages='string', percentile='string', q='http://impressive-silence.info', paging='string')

if res.two_hundred_application_json_object is not None:
    # handle response
    pass
```
<!-- End SDK Example Usage -->