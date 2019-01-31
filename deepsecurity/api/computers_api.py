# coding: utf-8

"""
    Trend Micro Deep Security API

    Get protected, stay secured, and keep informed with Trend Micro Deep Security's new RESTful API. Access system data and manage security configurations to automate your security workflows and integrate Deep Security into your CI/CD pipeline.  # noqa: E501

    OpenAPI spec version: 11.3.184
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from deepsecurity.api_client import ApiClient


class ComputersApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_computer(self, computer, api_version, **kwargs):  # noqa: E501
        """Create a Computer  # noqa: E501

        Create a new computer.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_computer(computer, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Computer computer: The settings of the new computer. (required)
        :param str api_version: The version of the api being called. (required)
        :param bool overrides: Show only overrides defined for the current computer.
        :return: Computer
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_computer_with_http_info(computer, api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.create_computer_with_http_info(computer, api_version, **kwargs)  # noqa: E501
            return data

    def create_computer_with_http_info(self, computer, api_version, **kwargs):  # noqa: E501
        """Create a Computer  # noqa: E501

        Create a new computer.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_computer_with_http_info(computer, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Computer computer: The settings of the new computer. (required)
        :param str api_version: The version of the api being called. (required)
        :param bool overrides: Show only overrides defined for the current computer.
        :return: Computer
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['computer', 'api_version', 'overrides']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_computer" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'computer' is set
        if ('computer' not in params or
                params['computer'] is None):
            raise ValueError("Missing the required parameter `computer` when calling `create_computer`")  # noqa: E501
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `create_computer`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'overrides' in params:
            query_params.append(('overrides', params['overrides']))  # noqa: E501

        header_params = {}
        if 'api_version' in params:
            header_params['api-version'] = params['api_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'computer' in params:
            body_params = params['computer']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['DefaultAuthentication']  # noqa: E501

        return self.api_client.call_api(
            '/computers', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Computer',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_computer(self, computer_id, api_version, **kwargs):  # noqa: E501
        """Delete a Computer  # noqa: E501

        Delete a computer by ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_computer(computer_id, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int computer_id: The ID number of the computer to delete. (required)
        :param str api_version: The version of the api being called. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_computer_with_http_info(computer_id, api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_computer_with_http_info(computer_id, api_version, **kwargs)  # noqa: E501
            return data

    def delete_computer_with_http_info(self, computer_id, api_version, **kwargs):  # noqa: E501
        """Delete a Computer  # noqa: E501

        Delete a computer by ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_computer_with_http_info(computer_id, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int computer_id: The ID number of the computer to delete. (required)
        :param str api_version: The version of the api being called. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['computer_id', 'api_version']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_computer" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'computer_id' is set
        if ('computer_id' not in params or
                params['computer_id'] is None):
            raise ValueError("Missing the required parameter `computer_id` when calling `delete_computer`")  # noqa: E501
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `delete_computer`")  # noqa: E501

        if 'computer_id' in params and not re.search('\\d+', str(params['computer_id'])):  # noqa: E501
            raise ValueError("Invalid value for parameter `computer_id` when calling `delete_computer`, must conform to the pattern `/\\d+/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'computer_id' in params:
            path_params['computerID'] = params['computer_id']  # noqa: E501

        query_params = []

        header_params = {}
        if 'api_version' in params:
            header_params['api-version'] = params['api_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['DefaultAuthentication']  # noqa: E501

        return self.api_client.call_api(
            '/computers/{computerID}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def describe_computer(self, computer_id, api_version, **kwargs):  # noqa: E501
        """Describe a Computer  # noqa: E501

        Describe a computer by ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.describe_computer(computer_id, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int computer_id: The ID number of the computer to describe. (required)
        :param str api_version: The version of the api being called. (required)
        :param bool overrides: Show only overrides defined for the current computer.
        :return: Computer
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.describe_computer_with_http_info(computer_id, api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.describe_computer_with_http_info(computer_id, api_version, **kwargs)  # noqa: E501
            return data

    def describe_computer_with_http_info(self, computer_id, api_version, **kwargs):  # noqa: E501
        """Describe a Computer  # noqa: E501

        Describe a computer by ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.describe_computer_with_http_info(computer_id, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int computer_id: The ID number of the computer to describe. (required)
        :param str api_version: The version of the api being called. (required)
        :param bool overrides: Show only overrides defined for the current computer.
        :return: Computer
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['computer_id', 'api_version', 'overrides']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method describe_computer" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'computer_id' is set
        if ('computer_id' not in params or
                params['computer_id'] is None):
            raise ValueError("Missing the required parameter `computer_id` when calling `describe_computer`")  # noqa: E501
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `describe_computer`")  # noqa: E501

        if 'computer_id' in params and not re.search('\\d+', str(params['computer_id'])):  # noqa: E501
            raise ValueError("Invalid value for parameter `computer_id` when calling `describe_computer`, must conform to the pattern `/\\d+/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'computer_id' in params:
            path_params['computerID'] = params['computer_id']  # noqa: E501

        query_params = []
        if 'overrides' in params:
            query_params.append(('overrides', params['overrides']))  # noqa: E501

        header_params = {}
        if 'api_version' in params:
            header_params['api-version'] = params['api_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['DefaultAuthentication']  # noqa: E501

        return self.api_client.call_api(
            '/computers/{computerID}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Computer',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_computers(self, api_version, **kwargs):  # noqa: E501
        """List Computers  # noqa: E501

        Lists all computers.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_computers(api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str api_version: The version of the api being called. (required)
        :param bool overrides: Show only overrides defined for the current computer.
        :return: Computers
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_computers_with_http_info(api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.list_computers_with_http_info(api_version, **kwargs)  # noqa: E501
            return data

    def list_computers_with_http_info(self, api_version, **kwargs):  # noqa: E501
        """List Computers  # noqa: E501

        Lists all computers.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_computers_with_http_info(api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str api_version: The version of the api being called. (required)
        :param bool overrides: Show only overrides defined for the current computer.
        :return: Computers
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['api_version', 'overrides']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_computers" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `list_computers`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'overrides' in params:
            query_params.append(('overrides', params['overrides']))  # noqa: E501

        header_params = {}
        if 'api_version' in params:
            header_params['api-version'] = params['api_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['DefaultAuthentication']  # noqa: E501

        return self.api_client.call_api(
            '/computers', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Computers',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def modify_computer(self, computer_id, computer, api_version, **kwargs):  # noqa: E501
        """Modify a Computer  # noqa: E501

        Modify a computer by ID. Any unset elements will be left unchanged.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.modify_computer(computer_id, computer, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int computer_id: The ID number of the computer to modify. (required)
        :param Computer computer: The settings of the computer to modify. (required)
        :param str api_version: The version of the api being called. (required)
        :param bool overrides: Show only overrides defined for the current computer.
        :return: Computer
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.modify_computer_with_http_info(computer_id, computer, api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.modify_computer_with_http_info(computer_id, computer, api_version, **kwargs)  # noqa: E501
            return data

    def modify_computer_with_http_info(self, computer_id, computer, api_version, **kwargs):  # noqa: E501
        """Modify a Computer  # noqa: E501

        Modify a computer by ID. Any unset elements will be left unchanged.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.modify_computer_with_http_info(computer_id, computer, api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int computer_id: The ID number of the computer to modify. (required)
        :param Computer computer: The settings of the computer to modify. (required)
        :param str api_version: The version of the api being called. (required)
        :param bool overrides: Show only overrides defined for the current computer.
        :return: Computer
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['computer_id', 'computer', 'api_version', 'overrides']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method modify_computer" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'computer_id' is set
        if ('computer_id' not in params or
                params['computer_id'] is None):
            raise ValueError("Missing the required parameter `computer_id` when calling `modify_computer`")  # noqa: E501
        # verify the required parameter 'computer' is set
        if ('computer' not in params or
                params['computer'] is None):
            raise ValueError("Missing the required parameter `computer` when calling `modify_computer`")  # noqa: E501
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `modify_computer`")  # noqa: E501

        if 'computer_id' in params and not re.search('\\d+', str(params['computer_id'])):  # noqa: E501
            raise ValueError("Invalid value for parameter `computer_id` when calling `modify_computer`, must conform to the pattern `/\\d+/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'computer_id' in params:
            path_params['computerID'] = params['computer_id']  # noqa: E501

        query_params = []
        if 'overrides' in params:
            query_params.append(('overrides', params['overrides']))  # noqa: E501

        header_params = {}
        if 'api_version' in params:
            header_params['api-version'] = params['api_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'computer' in params:
            body_params = params['computer']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['DefaultAuthentication']  # noqa: E501

        return self.api_client.call_api(
            '/computers/{computerID}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Computer',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def search_computers(self, api_version, **kwargs):  # noqa: E501
        """Search Computers  # noqa: E501

        Search for computers using optional filters.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_computers(api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str api_version: The version of the api being called. (required)
        :param SearchFilter search_filter: A collection of options used to filter the search results.
        :param bool overrides: Show only overrides defined for the current computer.
        :return: Computers
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.search_computers_with_http_info(api_version, **kwargs)  # noqa: E501
        else:
            (data) = self.search_computers_with_http_info(api_version, **kwargs)  # noqa: E501
            return data

    def search_computers_with_http_info(self, api_version, **kwargs):  # noqa: E501
        """Search Computers  # noqa: E501

        Search for computers using optional filters.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_computers_with_http_info(api_version, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str api_version: The version of the api being called. (required)
        :param SearchFilter search_filter: A collection of options used to filter the search results.
        :param bool overrides: Show only overrides defined for the current computer.
        :return: Computers
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['api_version', 'search_filter', 'overrides']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_computers" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'api_version' is set
        if ('api_version' not in params or
                params['api_version'] is None):
            raise ValueError("Missing the required parameter `api_version` when calling `search_computers`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'overrides' in params:
            query_params.append(('overrides', params['overrides']))  # noqa: E501

        header_params = {}
        if 'api_version' in params:
            header_params['api-version'] = params['api_version']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'search_filter' in params:
            body_params = params['search_filter']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['DefaultAuthentication']  # noqa: E501

        return self.api_client.call_api(
            '/computers/search', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Computers',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
