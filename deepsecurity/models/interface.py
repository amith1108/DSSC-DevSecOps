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


class Interface(object):
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
        'interface_type_id': 'int',
        'name': 'str',
        'display_name': 'str',
        'detected': 'bool',
        'id': 'int',
        'mac': 'str',
        'dhcp': 'bool',
        'ips': 'list[str]'
    }

    attribute_map = {
        'interface_type_id': 'interfaceTypeID',
        'name': 'name',
        'display_name': 'displayName',
        'detected': 'detected',
        'id': 'ID',
        'mac': 'MAC',
        'dhcp': 'DHCP',
        'ips': 'IPs'
    }

    def __init__(self, interface_type_id=None, name=None, display_name=None, detected=None, id=None, mac=None, dhcp=None, ips=None):  # noqa: E501
        """Interface - a model defined in Swagger"""  # noqa: E501

        self._interface_type_id = None
        self._name = None
        self._display_name = None
        self._detected = None
        self._id = None
        self._mac = None
        self._dhcp = None
        self._ips = None
        self.discriminator = None

        if interface_type_id is not None:
            self.interface_type_id = interface_type_id
        if name is not None:
            self.name = name
        if display_name is not None:
            self.display_name = display_name
        if detected is not None:
            self.detected = detected
        if id is not None:
            self.id = id
        if mac is not None:
            self.mac = mac
        if dhcp is not None:
            self.dhcp = dhcp
        if ips is not None:
            self.ips = ips

    @property
    def interface_type_id(self):
        """Gets the interface_type_id of this Interface.  # noqa: E501

        ID of the InterfaceType to which the Interface is mapped.  # noqa: E501

        :return: The interface_type_id of this Interface.  # noqa: E501
        :rtype: int
        """
        return self._interface_type_id

    @interface_type_id.setter
    def interface_type_id(self, interface_type_id):
        """Sets the interface_type_id of this Interface.

        ID of the InterfaceType to which the Interface is mapped.  # noqa: E501

        :param interface_type_id: The interface_type_id of this Interface.  # noqa: E501
        :type: int
        """

        self._interface_type_id = interface_type_id

    @property
    def name(self):
        """Gets the name of this Interface.  # noqa: E501

        Name of the Interface. Set automatically by the DSM.  # noqa: E501

        :return: The name of this Interface.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Interface.

        Name of the Interface. Set automatically by the DSM.  # noqa: E501

        :param name: The name of this Interface.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def display_name(self):
        """Gets the display_name of this Interface.  # noqa: E501

        Display name of the Interface. Optionally set by the user.  # noqa: E501

        :return: The display_name of this Interface.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this Interface.

        Display name of the Interface. Optionally set by the user.  # noqa: E501

        :param display_name: The display_name of this Interface.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def detected(self):
        """Gets the detected of this Interface.  # noqa: E501

        Indicates whether or not the interface is currently detected.  # noqa: E501

        :return: The detected of this Interface.  # noqa: E501
        :rtype: bool
        """
        return self._detected

    @detected.setter
    def detected(self, detected):
        """Sets the detected of this Interface.

        Indicates whether or not the interface is currently detected.  # noqa: E501

        :param detected: The detected of this Interface.  # noqa: E501
        :type: bool
        """

        self._detected = detected

    @property
    def id(self):
        """Gets the id of this Interface.  # noqa: E501

        ID of the Interface.  # noqa: E501

        :return: The id of this Interface.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Interface.

        ID of the Interface.  # noqa: E501

        :param id: The id of this Interface.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def mac(self):
        """Gets the mac of this Interface.  # noqa: E501

        MAC Address of the interface.  # noqa: E501

        :return: The mac of this Interface.  # noqa: E501
        :rtype: str
        """
        return self._mac

    @mac.setter
    def mac(self, mac):
        """Sets the mac of this Interface.

        MAC Address of the interface.  # noqa: E501

        :param mac: The mac of this Interface.  # noqa: E501
        :type: str
        """

        self._mac = mac

    @property
    def dhcp(self):
        """Gets the dhcp of this Interface.  # noqa: E501

        Indicates whether the interface uses DHCP. The value is true if it uses DHCP.  # noqa: E501

        :return: The dhcp of this Interface.  # noqa: E501
        :rtype: bool
        """
        return self._dhcp

    @dhcp.setter
    def dhcp(self, dhcp):
        """Sets the dhcp of this Interface.

        Indicates whether the interface uses DHCP. The value is true if it uses DHCP.  # noqa: E501

        :param dhcp: The dhcp of this Interface.  # noqa: E501
        :type: bool
        """

        self._dhcp = dhcp

    @property
    def ips(self):
        """Gets the ips of this Interface.  # noqa: E501

        List of IPs used by the interface.  # noqa: E501

        :return: The ips of this Interface.  # noqa: E501
        :rtype: list[str]
        """
        return self._ips

    @ips.setter
    def ips(self, ips):
        """Sets the ips of this Interface.

        List of IPs used by the interface.  # noqa: E501

        :param ips: The ips of this Interface.  # noqa: E501
        :type: list[str]
        """

        self._ips = ips

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
        if issubclass(Interface, dict):
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
        if not isinstance(other, Interface):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
