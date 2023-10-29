# coding: utf-8

"""
    Metadata API

    The Metadata API has operations that retrieve configuration details pertaining to the different eBay marketplaces. In addition to marketplace information, the API also has operations that get information that helps sellers list items on eBay.  # noqa: E501

    OpenAPI spec version: v1.7.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ItemConditionDescriptor(object):
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
        'condition_descriptor_constraint': 'ItemConditionDescriptorConstraint',
        'condition_descriptor_help_text': 'str',
        'condition_descriptor_id': 'str',
        'condition_descriptor_name': 'str',
        'condition_descriptor_values': 'list[ItemConditionDescriptorValue]'
    }

    attribute_map = {
        'condition_descriptor_constraint': 'conditionDescriptorConstraint',
        'condition_descriptor_help_text': 'conditionDescriptorHelpText',
        'condition_descriptor_id': 'conditionDescriptorId',
        'condition_descriptor_name': 'conditionDescriptorName',
        'condition_descriptor_values': 'conditionDescriptorValues'
    }

    def __init__(self, condition_descriptor_constraint=None, condition_descriptor_help_text=None, condition_descriptor_id=None, condition_descriptor_name=None, condition_descriptor_values=None):  # noqa: E501
        """ItemConditionDescriptor - a model defined in Swagger"""  # noqa: E501
        self._condition_descriptor_constraint = None
        self._condition_descriptor_help_text = None
        self._condition_descriptor_id = None
        self._condition_descriptor_name = None
        self._condition_descriptor_values = None
        self.discriminator = None
        if condition_descriptor_constraint is not None:
            self.condition_descriptor_constraint = condition_descriptor_constraint
        if condition_descriptor_help_text is not None:
            self.condition_descriptor_help_text = condition_descriptor_help_text
        if condition_descriptor_id is not None:
            self.condition_descriptor_id = condition_descriptor_id
        if condition_descriptor_name is not None:
            self.condition_descriptor_name = condition_descriptor_name
        if condition_descriptor_values is not None:
            self.condition_descriptor_values = condition_descriptor_values

    @property
    def condition_descriptor_constraint(self):
        """Gets the condition_descriptor_constraint of this ItemConditionDescriptor.  # noqa: E501


        :return: The condition_descriptor_constraint of this ItemConditionDescriptor.  # noqa: E501
        :rtype: ItemConditionDescriptorConstraint
        """
        return self._condition_descriptor_constraint

    @condition_descriptor_constraint.setter
    def condition_descriptor_constraint(self, condition_descriptor_constraint):
        """Sets the condition_descriptor_constraint of this ItemConditionDescriptor.


        :param condition_descriptor_constraint: The condition_descriptor_constraint of this ItemConditionDescriptor.  # noqa: E501
        :type: ItemConditionDescriptorConstraint
        """

        self._condition_descriptor_constraint = condition_descriptor_constraint

    @property
    def condition_descriptor_help_text(self):
        """Gets the condition_descriptor_help_text of this ItemConditionDescriptor.  # noqa: E501

        A description of the condition descriptor that directs a user to its condition descriptor values.<br><br> For example, the help text for <code>Card Condition</code> is <code>Select ungraded condition</code>.  # noqa: E501

        :return: The condition_descriptor_help_text of this ItemConditionDescriptor.  # noqa: E501
        :rtype: str
        """
        return self._condition_descriptor_help_text

    @condition_descriptor_help_text.setter
    def condition_descriptor_help_text(self, condition_descriptor_help_text):
        """Sets the condition_descriptor_help_text of this ItemConditionDescriptor.

        A description of the condition descriptor that directs a user to its condition descriptor values.<br><br> For example, the help text for <code>Card Condition</code> is <code>Select ungraded condition</code>.  # noqa: E501

        :param condition_descriptor_help_text: The condition_descriptor_help_text of this ItemConditionDescriptor.  # noqa: E501
        :type: str
        """

        self._condition_descriptor_help_text = condition_descriptor_help_text

    @property
    def condition_descriptor_id(self):
        """Gets the condition_descriptor_id of this ItemConditionDescriptor.  # noqa: E501

        The unique identification number of a condition descriptor associated with with a <b>conditionDescriptorName</b>. <br><br>For example, <code>40001</code> is the ID for <code>Card Condition</code>.<br><br>These IDs are used in the addItem family of calls of the <b>Trading API</b> to provide condition descriptor names for the item. These IDs are used by the inventoryItem family of calls of the <b>Inventory API</b> to provide condition descriptor names for the item.  # noqa: E501

        :return: The condition_descriptor_id of this ItemConditionDescriptor.  # noqa: E501
        :rtype: str
        """
        return self._condition_descriptor_id

    @condition_descriptor_id.setter
    def condition_descriptor_id(self, condition_descriptor_id):
        """Sets the condition_descriptor_id of this ItemConditionDescriptor.

        The unique identification number of a condition descriptor associated with with a <b>conditionDescriptorName</b>. <br><br>For example, <code>40001</code> is the ID for <code>Card Condition</code>.<br><br>These IDs are used in the addItem family of calls of the <b>Trading API</b> to provide condition descriptor names for the item. These IDs are used by the inventoryItem family of calls of the <b>Inventory API</b> to provide condition descriptor names for the item.  # noqa: E501

        :param condition_descriptor_id: The condition_descriptor_id of this ItemConditionDescriptor.  # noqa: E501
        :type: str
        """

        self._condition_descriptor_id = condition_descriptor_id

    @property
    def condition_descriptor_name(self):
        """Gets the condition_descriptor_name of this ItemConditionDescriptor.  # noqa: E501

        The human-readable label for the condition descriptor associated with the <b>conditionDescriptorID</b>. <br><br>For example, <code>Card Condition</code> is the condition descriptor name for ID <code>40001</code>  # noqa: E501

        :return: The condition_descriptor_name of this ItemConditionDescriptor.  # noqa: E501
        :rtype: str
        """
        return self._condition_descriptor_name

    @condition_descriptor_name.setter
    def condition_descriptor_name(self, condition_descriptor_name):
        """Sets the condition_descriptor_name of this ItemConditionDescriptor.

        The human-readable label for the condition descriptor associated with the <b>conditionDescriptorID</b>. <br><br>For example, <code>Card Condition</code> is the condition descriptor name for ID <code>40001</code>  # noqa: E501

        :param condition_descriptor_name: The condition_descriptor_name of this ItemConditionDescriptor.  # noqa: E501
        :type: str
        """

        self._condition_descriptor_name = condition_descriptor_name

    @property
    def condition_descriptor_values(self):
        """Gets the condition_descriptor_values of this ItemConditionDescriptor.  # noqa: E501

        This array shows the possible values that map to the corresponding <b>conditionDescriptorName</b> values. Constraint information and help text are also shown for each value. <br><br>For example, The ID <code>40001</code> is ID for the condition descriptor <code>card condition</code>. The ID <code>400012</code> is the ID for the <code>Very Good</code> card condition value.  # noqa: E501

        :return: The condition_descriptor_values of this ItemConditionDescriptor.  # noqa: E501
        :rtype: list[ItemConditionDescriptorValue]
        """
        return self._condition_descriptor_values

    @condition_descriptor_values.setter
    def condition_descriptor_values(self, condition_descriptor_values):
        """Sets the condition_descriptor_values of this ItemConditionDescriptor.

        This array shows the possible values that map to the corresponding <b>conditionDescriptorName</b> values. Constraint information and help text are also shown for each value. <br><br>For example, The ID <code>40001</code> is ID for the condition descriptor <code>card condition</code>. The ID <code>400012</code> is the ID for the <code>Very Good</code> card condition value.  # noqa: E501

        :param condition_descriptor_values: The condition_descriptor_values of this ItemConditionDescriptor.  # noqa: E501
        :type: list[ItemConditionDescriptorValue]
        """

        self._condition_descriptor_values = condition_descriptor_values

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
        if issubclass(ItemConditionDescriptor, dict):
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
        if not isinstance(other, ItemConditionDescriptor):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
