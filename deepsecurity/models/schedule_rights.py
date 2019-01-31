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


class ScheduleRights(object):
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
        'can_create_new_schedules': 'bool',
        'can_delete_schedules': 'bool',
        'can_edit_schedule_properties': 'bool'
    }

    attribute_map = {
        'can_create_new_schedules': 'canCreateNewSchedules',
        'can_delete_schedules': 'canDeleteSchedules',
        'can_edit_schedule_properties': 'canEditScheduleProperties'
    }

    def __init__(self, can_create_new_schedules=None, can_delete_schedules=None, can_edit_schedule_properties=None):  # noqa: E501
        """ScheduleRights - a model defined in Swagger"""  # noqa: E501

        self._can_create_new_schedules = None
        self._can_delete_schedules = None
        self._can_edit_schedule_properties = None
        self.discriminator = None

        if can_create_new_schedules is not None:
            self.can_create_new_schedules = can_create_new_schedules
        if can_delete_schedules is not None:
            self.can_delete_schedules = can_delete_schedules
        if can_edit_schedule_properties is not None:
            self.can_edit_schedule_properties = can_edit_schedule_properties

    @property
    def can_create_new_schedules(self):
        """Gets the can_create_new_schedules of this ScheduleRights.  # noqa: E501

        Right to create new schedules.  # noqa: E501

        :return: The can_create_new_schedules of this ScheduleRights.  # noqa: E501
        :rtype: bool
        """
        return self._can_create_new_schedules

    @can_create_new_schedules.setter
    def can_create_new_schedules(self, can_create_new_schedules):
        """Sets the can_create_new_schedules of this ScheduleRights.

        Right to create new schedules.  # noqa: E501

        :param can_create_new_schedules: The can_create_new_schedules of this ScheduleRights.  # noqa: E501
        :type: bool
        """

        self._can_create_new_schedules = can_create_new_schedules

    @property
    def can_delete_schedules(self):
        """Gets the can_delete_schedules of this ScheduleRights.  # noqa: E501

        Right to delete schedules.  # noqa: E501

        :return: The can_delete_schedules of this ScheduleRights.  # noqa: E501
        :rtype: bool
        """
        return self._can_delete_schedules

    @can_delete_schedules.setter
    def can_delete_schedules(self, can_delete_schedules):
        """Sets the can_delete_schedules of this ScheduleRights.

        Right to delete schedules.  # noqa: E501

        :param can_delete_schedules: The can_delete_schedules of this ScheduleRights.  # noqa: E501
        :type: bool
        """

        self._can_delete_schedules = can_delete_schedules

    @property
    def can_edit_schedule_properties(self):
        """Gets the can_edit_schedule_properties of this ScheduleRights.  # noqa: E501

        Right to edit schedule properties.  # noqa: E501

        :return: The can_edit_schedule_properties of this ScheduleRights.  # noqa: E501
        :rtype: bool
        """
        return self._can_edit_schedule_properties

    @can_edit_schedule_properties.setter
    def can_edit_schedule_properties(self, can_edit_schedule_properties):
        """Sets the can_edit_schedule_properties of this ScheduleRights.

        Right to edit schedule properties.  # noqa: E501

        :param can_edit_schedule_properties: The can_edit_schedule_properties of this ScheduleRights.  # noqa: E501
        :type: bool
        """

        self._can_edit_schedule_properties = can_edit_schedule_properties

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
        if issubclass(ScheduleRights, dict):
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
        if not isinstance(other, ScheduleRights):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
