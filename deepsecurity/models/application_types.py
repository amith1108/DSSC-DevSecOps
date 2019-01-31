# coding: utf-8

"""
    Trend Micro Deep Security API

    Get protected, stay secured, and keep informed with Trend Micro Deep Security's new RESTful API. Access system data and manage security configurations to automate your security workflows and integrate Deep Security into your CI/CD pipeline.  # noqa: E501

    OpenAPI spec version: 11.3.184
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from deepsecurity.models.application_type import ApplicationType  # noqa: F401,E501


class ApplicationTypes(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'application_types': 'list[ApplicationType]'
    }

    attribute_map = {
        'application_types': 'applicationTypes'
    }

    def __init__(self, application_types=None):  # noqa: E501
        """ApplicationTypes - a model defined in Swagger"""  # noqa: E501

        self._application_types = None
        self.discriminator = None

        if application_types is not None:
            self.application_types = application_types

    @property
    def application_types(self):
        """Gets the application_types of this ApplicationTypes.  # noqa: E501


        :return: The application_types of this ApplicationTypes.  # noqa: E501
        :rtype: list[ApplicationType]
        """
        return self._application_types

    @application_types.setter
    def application_types(self, application_types):
        """Sets the application_types of this ApplicationTypes.


        :param application_types: The application_types of this ApplicationTypes.  # noqa: E501
        :type: list[ApplicationType]
        """

        self._application_types = application_types

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(ApplicationTypes, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ApplicationTypes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
