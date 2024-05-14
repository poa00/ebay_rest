# coding: utf-8

"""
    Account API

    The <b>Account API</b> gives sellers the ability to configure their eBay seller accounts, including the seller's policies (eBay business policies and seller-defined custom policies), opt in and out of eBay seller programs, configure sales tax tables, and get account information.  <br><br>For details on the availability of the methods in this API, see <a href=\"/api-docs/sell/account/overview.html#requirements\">Account API requirements and restrictions</a>.  # noqa: E501

    OpenAPI spec version: v1.9.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class RegionSet(object):
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
        'region_excluded': 'list[Region]',
        'region_included': 'list[Region]'
    }

    attribute_map = {
        'region_excluded': 'regionExcluded',
        'region_included': 'regionIncluded'
    }

    def __init__(self, region_excluded=None, region_included=None):  # noqa: E501
        """RegionSet - a model defined in Swagger"""  # noqa: E501
        self._region_excluded = None
        self._region_included = None
        self.discriminator = None
        if region_excluded is not None:
            self.region_excluded = region_excluded
        if region_included is not None:
            self.region_included = region_included

    @property
    def region_excluded(self):
        """Gets the region_excluded of this RegionSet.  # noqa: E501

        An array of one or more <b>regionName</b> values that specify the areas to where a seller does not ship. A <b>regionExcluded</b> list should only be set in the top-level <b>shipToLocations</b> container and not within the <b>shippingServices.shipToLocations</b> container used to specify which shipping regions are serviced by each available shipping service option. <p>Many sellers are willing to ship to many international locations, but they may want to exclude some world regions or some countries as places they are willing to ship to.<br><br>This array will be returned as empty if no shipping regions are excluded with the fulfillment business policy.<br> <br><span class=\"tablenote\"><b>Note: </b> The <b>regionExcluded</b> array is not applicable for motor vehicle business policies on the US, CA, or UK marketplaces. If this array is used in a <b>createFulfillmentPolicy</b> or <b>updateFulfillmentPolicy</b> request, it will be ignored.</span>  # noqa: E501

        :return: The region_excluded of this RegionSet.  # noqa: E501
        :rtype: list[Region]
        """
        return self._region_excluded

    @region_excluded.setter
    def region_excluded(self, region_excluded):
        """Sets the region_excluded of this RegionSet.

        An array of one or more <b>regionName</b> values that specify the areas to where a seller does not ship. A <b>regionExcluded</b> list should only be set in the top-level <b>shipToLocations</b> container and not within the <b>shippingServices.shipToLocations</b> container used to specify which shipping regions are serviced by each available shipping service option. <p>Many sellers are willing to ship to many international locations, but they may want to exclude some world regions or some countries as places they are willing to ship to.<br><br>This array will be returned as empty if no shipping regions are excluded with the fulfillment business policy.<br> <br><span class=\"tablenote\"><b>Note: </b> The <b>regionExcluded</b> array is not applicable for motor vehicle business policies on the US, CA, or UK marketplaces. If this array is used in a <b>createFulfillmentPolicy</b> or <b>updateFulfillmentPolicy</b> request, it will be ignored.</span>  # noqa: E501

        :param region_excluded: The region_excluded of this RegionSet.  # noqa: E501
        :type: list[Region]
        """

        self._region_excluded = region_excluded

    @property
    def region_included(self):
        """Gets the region_included of this RegionSet.  # noqa: E501

        An array of one or more <b>regionName</b> fields that specify the areas to where a seller ships. <br>Each eBay marketplace supports its own set of allowable shipping locations.<br> <br><span class=\"tablenote\"><b>Note: </b> The <b>regionIncluded</b> array is not applicable for motor vehicle business policies on the US, CA, or UK marketplaces. If this array is used in a <b>createFulfillmentPolicy</b> or <b>updateFulfillmentPolicy</b> request, it will be ignored.</span>  # noqa: E501

        :return: The region_included of this RegionSet.  # noqa: E501
        :rtype: list[Region]
        """
        return self._region_included

    @region_included.setter
    def region_included(self, region_included):
        """Sets the region_included of this RegionSet.

        An array of one or more <b>regionName</b> fields that specify the areas to where a seller ships. <br>Each eBay marketplace supports its own set of allowable shipping locations.<br> <br><span class=\"tablenote\"><b>Note: </b> The <b>regionIncluded</b> array is not applicable for motor vehicle business policies on the US, CA, or UK marketplaces. If this array is used in a <b>createFulfillmentPolicy</b> or <b>updateFulfillmentPolicy</b> request, it will be ignored.</span>  # noqa: E501

        :param region_included: The region_included of this RegionSet.  # noqa: E501
        :type: list[Region]
        """

        self._region_included = region_included

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
        if issubclass(RegionSet, dict):
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
        if not isinstance(other, RegionSet):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
