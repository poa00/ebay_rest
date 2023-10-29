# coding: utf-8

"""
    Inventory API

    The Inventory API is used to create and manage inventory, and then to publish and manage this inventory on an eBay marketplace. There are also methods in this API that will convert eligible, active eBay listings into the Inventory API model.  # noqa: E501

    OpenAPI spec version: 1.17.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Charity(object):
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
        'charity_id': 'str',
        'donation_percentage': 'str'
    }

    attribute_map = {
        'charity_id': 'charityId',
        'donation_percentage': 'donationPercentage'
    }

    def __init__(self, charity_id=None, donation_percentage=None):  # noqa: E501
        """Charity - a model defined in Swagger"""  # noqa: E501
        self._charity_id = None
        self._donation_percentage = None
        self.discriminator = None
        if charity_id is not None:
            self.charity_id = charity_id
        if donation_percentage is not None:
            self.donation_percentage = donation_percentage

    @property
    def charity_id(self):
        """Gets the charity_id of this Charity.  # noqa: E501

        The eBay-assigned unique identifier of the charitable organization that will receive a percentage of the sales proceeds. The charitable organization must be reqistered with the PayPal Giving Fund in order to receive sales proceeds through eBay listings.<br><br>This field is conditionally required if a seller is planning on donating a percentage of the sale proceeds to a charitable organization.<br><br>The eBay-assigned unique identifier of a charitable organization can be found using the <strong>getCharityOrgs</strong> method of the Charity API. In the <strong>getCharityOrgs</strong> response, this unique identifier is shown in the <a href=\"/api-docs/commerce/charity/resources/charity_org/methods/getCharityOrgs#response.charityOrgs.charityOrgId\" target=\"_blank\">charityOrgId</a> field.  # noqa: E501

        :return: The charity_id of this Charity.  # noqa: E501
        :rtype: str
        """
        return self._charity_id

    @charity_id.setter
    def charity_id(self, charity_id):
        """Sets the charity_id of this Charity.

        The eBay-assigned unique identifier of the charitable organization that will receive a percentage of the sales proceeds. The charitable organization must be reqistered with the PayPal Giving Fund in order to receive sales proceeds through eBay listings.<br><br>This field is conditionally required if a seller is planning on donating a percentage of the sale proceeds to a charitable organization.<br><br>The eBay-assigned unique identifier of a charitable organization can be found using the <strong>getCharityOrgs</strong> method of the Charity API. In the <strong>getCharityOrgs</strong> response, this unique identifier is shown in the <a href=\"/api-docs/commerce/charity/resources/charity_org/methods/getCharityOrgs#response.charityOrgs.charityOrgId\" target=\"_blank\">charityOrgId</a> field.  # noqa: E501

        :param charity_id: The charity_id of this Charity.  # noqa: E501
        :type: str
        """

        self._charity_id = charity_id

    @property
    def donation_percentage(self):
        """Gets the donation_percentage of this Charity.  # noqa: E501

        This field is the percentage of the purchase price that the charitable organization (identified in the <strong>charityId</strong> field) will receive for each sale that the listing generates. This field is conditionally required if a seller is planning on donating a percentage of the sale proceeds to a charitable organization. This numeric value can range from 10 to 100, and in any 5 (percent) increments in between this range (e.g. <code>10</code>, <code>15</code>, <code>20</code>...<code>95</code>,... <code>100</code>). The seller would pass in <code>10</code> for 10 percent, <code>15</code> for 15 percent, <code>20</code> for 20 percent, and so on, all the way to <code>100</code> for 100 percent.  # noqa: E501

        :return: The donation_percentage of this Charity.  # noqa: E501
        :rtype: str
        """
        return self._donation_percentage

    @donation_percentage.setter
    def donation_percentage(self, donation_percentage):
        """Sets the donation_percentage of this Charity.

        This field is the percentage of the purchase price that the charitable organization (identified in the <strong>charityId</strong> field) will receive for each sale that the listing generates. This field is conditionally required if a seller is planning on donating a percentage of the sale proceeds to a charitable organization. This numeric value can range from 10 to 100, and in any 5 (percent) increments in between this range (e.g. <code>10</code>, <code>15</code>, <code>20</code>...<code>95</code>,... <code>100</code>). The seller would pass in <code>10</code> for 10 percent, <code>15</code> for 15 percent, <code>20</code> for 20 percent, and so on, all the way to <code>100</code> for 100 percent.  # noqa: E501

        :param donation_percentage: The donation_percentage of this Charity.  # noqa: E501
        :type: str
        """

        self._donation_percentage = donation_percentage

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
        if issubclass(Charity, dict):
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
        if not isinstance(other, Charity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
