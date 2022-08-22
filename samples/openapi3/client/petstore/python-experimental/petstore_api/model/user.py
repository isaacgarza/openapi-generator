# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""

import re  # noqa: F401
import sys  # noqa: F401
import typing  # noqa: F401
import functools  # noqa: F401

from frozendict import frozendict  # noqa: F401

import decimal  # noqa: F401
from datetime import date, datetime  # noqa: F401
from frozendict import frozendict  # noqa: F401

from petstore_api import schemas  # noqa: F401


class User(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    id = schemas.Int64Schema
    username = schemas.StrSchema
    firstName = schemas.StrSchema
    lastName = schemas.StrSchema
    email = schemas.StrSchema
    password = schemas.StrSchema
    phone = schemas.StrSchema
    userStatus = schemas.Int32Schema
    objectWithNoDeclaredProps = schemas.DictSchema
    
    
    class objectWithNoDeclaredPropsNullable(
        schemas.SchemaTypeCheckerClsFactory(typing.Union[frozendict, schemas.NoneClass, ]),
        schemas.DictBase,
        schemas.NoneBase,
        schemas.Schema
    ):
    
        def __new__(
            cls,
            *args: typing.Union[dict, frozendict, None, ],
            _configuration: typing.Optional[schemas.Configuration] = None,
            **kwargs: typing.Type[schemas.Schema],
        ) -> 'objectWithNoDeclaredPropsNullable':
            return super().__new__(
                cls,
                *args,
                _configuration=_configuration,
                **kwargs,
            )
    anyTypeProp = schemas.AnyTypeSchema
    
    
    class anyTypeExceptNullProp(
        schemas.ComposedSchema,
    ):
    
        not_schema = schemas.NoneSchema
        
        @classmethod
        @property
        @functools.cache
        def _not(cls):
            # we need this here to make our import statements work
            # we must store _composed_schemas in here so the code is only run
            # when we invoke this method. If we kept this at the class
            # level we would get an error because the class level
            # code would be run when this module is imported, and these composed
            # classes don't exist yet because their module has not finished
            # loading
            return (
                cls.not_schema
            )
    
        def __new__(
            cls,
            *args: typing.Union[dict, frozendict, str, date, datetime, int, float, decimal.Decimal, None, list, tuple, bytes],
            _configuration: typing.Optional[schemas.Configuration] = None,
            **kwargs: typing.Type[schemas.Schema],
        ) -> 'anyTypeExceptNullProp':
            return super().__new__(
                cls,
                *args,
                _configuration=_configuration,
                **kwargs,
            )
    anyTypePropNullable = schemas.AnyTypeSchema


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict, ],
        id: typing.Union[id, schemas.Unset] = schemas.unset,
        username: typing.Union[username, schemas.Unset] = schemas.unset,
        firstName: typing.Union[firstName, schemas.Unset] = schemas.unset,
        lastName: typing.Union[lastName, schemas.Unset] = schemas.unset,
        email: typing.Union[email, schemas.Unset] = schemas.unset,
        password: typing.Union[password, schemas.Unset] = schemas.unset,
        phone: typing.Union[phone, schemas.Unset] = schemas.unset,
        userStatus: typing.Union[userStatus, schemas.Unset] = schemas.unset,
        objectWithNoDeclaredProps: typing.Union[objectWithNoDeclaredProps, schemas.Unset] = schemas.unset,
        objectWithNoDeclaredPropsNullable: typing.Union[objectWithNoDeclaredPropsNullable, schemas.Unset] = schemas.unset,
        anyTypeProp: typing.Union[anyTypeProp, schemas.Unset] = schemas.unset,
        anyTypeExceptNullProp: typing.Union[anyTypeExceptNullProp, schemas.Unset] = schemas.unset,
        anyTypePropNullable: typing.Union[anyTypePropNullable, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Type[schemas.Schema],
    ) -> 'User':
        return super().__new__(
            cls,
            *args,
            id=id,
            username=username,
            firstName=firstName,
            lastName=lastName,
            email=email,
            password=password,
            phone=phone,
            userStatus=userStatus,
            objectWithNoDeclaredProps=objectWithNoDeclaredProps,
            objectWithNoDeclaredPropsNullable=objectWithNoDeclaredPropsNullable,
            anyTypeProp=anyTypeProp,
            anyTypeExceptNullProp=anyTypeExceptNullProp,
            anyTypePropNullable=anyTypePropNullable,
            _configuration=_configuration,
            **kwargs,
        )
