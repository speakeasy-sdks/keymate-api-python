"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from dataclasses_json import Undefined, dataclass_json
from keymate_api import utils
from typing import List, Optional


@dataclasses.dataclass
class BrowseByURLRequest:
    numofpages: str = dataclasses.field(metadata={'query_param': { 'field_name': 'numofpages', 'style': 'form', 'explode': True }})
    r"""Set it as '1'"""
    percentile: str = dataclasses.field(metadata={'query_param': { 'field_name': 'percentile', 'style': 'form', 'explode': True }})
    r"""Start it as '1', increase to '2' if ResponseTooLarge occurs you can multiply it with 2 for each retry."""
    q: str = dataclasses.field(metadata={'query_param': { 'field_name': 'q', 'style': 'form', 'explode': True }})
    r"""URL of the website."""
    paging: Optional[str] = dataclasses.field(default=None, metadata={'query_param': { 'field_name': 'paging', 'style': 'form', 'explode': True }})
    r"""Set it as '1' first then according to results you can increase it by one to get the other part of the same page."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class BrowseByURLResponseResponseBody:
    r"""Error fetching search results"""
    error: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('error'), 'exclude': lambda f: f is None }})
    r"""Error message"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class BrowseByURLResults:
    full_content: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('full_content'), 'exclude': lambda f: f is None }})
    r"""The entire HTML content of the search result (available for the first three results)"""
    link: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('link'), 'exclude': lambda f: f is None }})
    r"""The URL of the search result"""
    summary: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('summary'), 'exclude': lambda f: f is None }})
    r"""A summary of the HTML content of the search result (available for the first five results)"""
    title: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('title'), 'exclude': lambda f: f is None }})
    r"""The title of the search result"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class BrowseByURLResponseBody:
    r"""Successful operation"""
    results: Optional[List[BrowseByURLResults]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('results'), 'exclude': lambda f: f is None }})
    rules: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('rules'), 'exclude': lambda f: f is None }})
    r"""The rules which recommend gpt to follow."""
    



@dataclasses.dataclass
class BrowseByURLResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    two_hundred_application_json_object: Optional[BrowseByURLResponseBody] = dataclasses.field(default=None)
    r"""Successful operation"""
    default_application_json_object: Optional[BrowseByURLResponseResponseBody] = dataclasses.field(default=None)
    r"""Error fetching search results"""
    

