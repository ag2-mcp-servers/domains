# generated by fastapi-codegen:
#   filename:  openapi.yaml
#   timestamp: 2025-06-29T03:33:06+00:00

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Optional
from uuid import UUID

from pydantic import BaseModel, Field, RootModel


class Domain(BaseModel):
    correctCname: Optional[str] = None
    created: Optional[datetime] = None
    domain: str = Field(
        ..., description='The actual domain or sub-domain. e.g. www.hubspot.com'
    )
    id: str = Field(..., description='The unique ID of this domain.')
    isResolving: bool = Field(
        ...,
        description='Whether the DNS for this domain is optimally configured for use with HubSpot.',
    )
    isSslEnabled: Optional[bool] = None
    isSslOnly: Optional[bool] = None
    isUsedForBlogPost: bool = Field(
        ..., description='Whether the domain is used for CMS blog posts.'
    )
    isUsedForEmail: bool = Field(
        ..., description='Whether the domain is used for CMS email web pages.'
    )
    isUsedForKnowledge: bool = Field(
        ..., description='Whether the domain is used for CMS knowledge pages.'
    )
    isUsedForLandingPage: bool = Field(
        ..., description='Whether the domain is used for CMS landing pages.'
    )
    isUsedForSitePage: bool = Field(
        ..., description='Whether the domain is used for CMS site pages.'
    )
    manuallyMarkedAsResolving: Optional[bool] = None
    primaryBlogPost: Optional[bool] = None
    primaryEmail: Optional[bool] = None
    primaryKnowledge: Optional[bool] = None
    primaryLandingPage: Optional[bool] = None
    primarySitePage: Optional[bool] = None
    secondaryToDomain: Optional[str] = None
    updated: Optional[datetime] = None


class ErrorDetail(BaseModel):
    code: Optional[str] = Field(
        None, description='The status code associated with the error detail'
    )
    context: Optional[Dict[str, List[str]]] = Field(
        None,
        description='Context about the error condition',
        examples=[{'missingScopes': ['scope1', 'scope2']}],
    )
    in_: Optional[str] = Field(
        None,
        alias='in',
        description='The name of the field or parameter in which the error was found.',
    )
    message: str = Field(
        ...,
        description='A human readable message describing the error along with remediation steps where appropriate',
    )
    subCategory: Optional[str] = Field(
        None,
        description='A specific category that contains more specific detail about the error',
    )


class NextPage(BaseModel):
    after: str
    link: Optional[str] = None


class Sort(RootModel[List[str]]):
    root: List[str]


class Error(BaseModel):
    category: str = Field(..., description='The error category')
    context: Optional[Dict[str, List[str]]] = Field(
        None,
        description='Context about the error condition',
        examples=[
            {
                'invalidPropertyName': ['propertyValue'],
                'missingScopes': ['scope1', 'scope2'],
            }
        ],
    )
    correlationId: UUID = Field(
        ...,
        description='A unique identifier for the request. Include this value with any error reports or support tickets',
        examples=['aeb5f871-7f07-4993-9211-075dc63e7cbf'],
    )
    errors: Optional[List[ErrorDetail]] = Field(
        None, description='further information about the error'
    )
    links: Optional[Dict[str, str]] = Field(
        None,
        description='A map of link names to associated URIs containing documentation about the error or recommended remediation steps',
    )
    message: str = Field(
        ...,
        description='A human readable message describing the error along with remediation steps where appropriate',
        examples=['An error occurred'],
    )
    subCategory: Optional[str] = Field(
        None,
        description='A specific category that contains more specific detail about the error',
    )


class ForwardPaging(BaseModel):
    next: Optional[NextPage] = None


class CollectionResponseWithTotalDomainForwardPaging(BaseModel):
    paging: Optional[ForwardPaging] = None
    results: List[Domain]
    total: int
