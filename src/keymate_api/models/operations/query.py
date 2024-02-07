"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from dataclasses_json import Undefined, dataclass_json
from keymate_api import utils
from typing import List, Optional


@dataclasses.dataclass
class QueryRequest:
    q: str = dataclasses.field(metadata={'query_param': { 'field_name': 'q', 'style': 'form', 'explode': True }})
    r"""The context you are searching from user's personal knowledge base history."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class QueryMetadata:
    text: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('text'), 'exclude': lambda f: f is None }})
    r"""Your nearest neighbour response to the user related to your query"""
    



@dataclasses.dataclass
class QuerySparseValues:
    pass


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class QueryMatches:
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    r"""User's unique id with timestamp the data was inserted to long term memory."""
    items: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('items'), 'exclude': lambda f: f is None }})
    metadata: Optional[QueryMetadata] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('metadata'), 'exclude': lambda f: f is None }})
    score: Optional[float] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('score'), 'exclude': lambda f: f is None }})
    r"""How close was the results to your query"""
    sparse_values: Optional[QuerySparseValues] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sparseValues'), 'exclude': lambda f: f is None }})
    values: Optional[List[str]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('values'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class QueryResponseBody:
    r"""Successful operation"""
    matches: Optional[List[QueryMatches]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('matches'), 'exclude': lambda f: f is None }})
    



@dataclasses.dataclass
class QueryResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    object: Optional[QueryResponseBody] = dataclasses.field(default=None)
    r"""Successful operation"""
    

