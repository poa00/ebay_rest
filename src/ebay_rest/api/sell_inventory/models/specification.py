# coding: utf-8

"""
    Inventory API

    The Inventory API is used to create and manage inventory, and then to publish and manage this inventory on an eBay marketplace. There are also methods in this API that will convert eligible, active eBay listings into the Inventory API model.  # noqa: E501

    OpenAPI spec version: 1.16.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Specification(object):
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
        'name': 'str',
        'values': 'list[str]'
    }

    attribute_map = {
        'name': 'name',
        'values': 'values'
    }

    def __init__(self, name=None, values=None):  # noqa: E501
        """Specification - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._values = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if values is not None:
            self.values = values

    @property
    def name(self):
        """Gets the name of this Specification.  # noqa: E501

        This is the name of product variation aspect. Typically, for clothing, typical aspect names are <code>\"Size\"</code> and <code>\"Color\"</code>. Product variation aspects are not required immediately upon creating an inventory item group, but these aspects will be required before a multiple-variation listing containing this inventory item group is published. For each product variation aspect that is specified through the <strong>specifications</strong> container, one <strong>name</strong> value is required and two or more variations of this aspect are required through the <strong>values</strong> array.<br/><br/> <span class=\"tablenote\"> <strong>Note:</strong> Each member of the inventory item group should have these same aspect names specified through the <strong>product.aspects</strong> container when the inventory item is created with the <strong>createOrReplaceInventoryItem</strong> or <strong>bulkCreateOrReplaceInventoryItem</strong> call. </span><br/><strong>Max Length</strong>: 40  # noqa: E501

        :return: The name of this Specification.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Specification.

        This is the name of product variation aspect. Typically, for clothing, typical aspect names are <code>\"Size\"</code> and <code>\"Color\"</code>. Product variation aspects are not required immediately upon creating an inventory item group, but these aspects will be required before a multiple-variation listing containing this inventory item group is published. For each product variation aspect that is specified through the <strong>specifications</strong> container, one <strong>name</strong> value is required and two or more variations of this aspect are required through the <strong>values</strong> array.<br/><br/> <span class=\"tablenote\"> <strong>Note:</strong> Each member of the inventory item group should have these same aspect names specified through the <strong>product.aspects</strong> container when the inventory item is created with the <strong>createOrReplaceInventoryItem</strong> or <strong>bulkCreateOrReplaceInventoryItem</strong> call. </span><br/><strong>Max Length</strong>: 40  # noqa: E501

        :param name: The name of this Specification.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def values(self):
        """Gets the values of this Specification.  # noqa: E501

        This is an array of values pertaining to the corresponding product variation aspect (specified in the <strong>name</strong> field). Below is a sample of how these values will appear under a <strong>specifications</strong> container: <br/> <pre><code>\"specifications\": [{<br/> \"name\": \"Size\",<br/> \"values\": [\"Small\",<br/> \"Medium\",<br/> \"Large\"]<br/> },<br/> { <br/> \"name\": \"Color\",<br/> \"values\": [\"Blue\",<br/> \"White\",<br/> \"Red\"] <br/> }] </pre></code><span class=\"tablenote\"> <strong>Note:</strong> Each member of the inventory item group should have these same aspect names, and each individual inventory item should have each variation of the product aspect values specified through the <strong>product.aspects</strong> container when the inventory item is created with the <strong>createOrReplaceInventoryItem</strong> or <strong>bulkCreateOrReplaceInventoryItem</strong> call. </span><br/><strong>Max Length</strong>: 50  # noqa: E501

        :return: The values of this Specification.  # noqa: E501
        :rtype: list[str]
        """
        return self._values

    @values.setter
    def values(self, values):
        """Sets the values of this Specification.

        This is an array of values pertaining to the corresponding product variation aspect (specified in the <strong>name</strong> field). Below is a sample of how these values will appear under a <strong>specifications</strong> container: <br/> <pre><code>\"specifications\": [{<br/> \"name\": \"Size\",<br/> \"values\": [\"Small\",<br/> \"Medium\",<br/> \"Large\"]<br/> },<br/> { <br/> \"name\": \"Color\",<br/> \"values\": [\"Blue\",<br/> \"White\",<br/> \"Red\"] <br/> }] </pre></code><span class=\"tablenote\"> <strong>Note:</strong> Each member of the inventory item group should have these same aspect names, and each individual inventory item should have each variation of the product aspect values specified through the <strong>product.aspects</strong> container when the inventory item is created with the <strong>createOrReplaceInventoryItem</strong> or <strong>bulkCreateOrReplaceInventoryItem</strong> call. </span><br/><strong>Max Length</strong>: 50  # noqa: E501

        :param values: The values of this Specification.  # noqa: E501
        :type: list[str]
        """

        self._values = values

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
        if issubclass(Specification, dict):
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
        if not isinstance(other, Specification):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
