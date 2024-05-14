# coding: utf-8

"""
    Inventory API

    The Inventory API is used to create and manage inventory, and then to publish and manage this inventory on an eBay marketplace. There are also methods in this API that will convert eligible, active eBay listings into the Inventory API model.  # noqa: E501

    OpenAPI spec version: 1.17.4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class PickupAtLocationAvailability(object):
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
        'availability_type': 'str',
        'fulfillment_time': 'TimeDuration',
        'merchant_location_key': 'str',
        'quantity': 'int'
    }

    attribute_map = {
        'availability_type': 'availabilityType',
        'fulfillment_time': 'fulfillmentTime',
        'merchant_location_key': 'merchantLocationKey',
        'quantity': 'quantity'
    }

    def __init__(self, availability_type=None, fulfillment_time=None, merchant_location_key=None, quantity=None):  # noqa: E501
        """PickupAtLocationAvailability - a model defined in Swagger"""  # noqa: E501
        self._availability_type = None
        self._fulfillment_time = None
        self._merchant_location_key = None
        self._quantity = None
        self.discriminator = None
        if availability_type is not None:
            self.availability_type = availability_type
        if fulfillment_time is not None:
            self.fulfillment_time = fulfillment_time
        if merchant_location_key is not None:
            self.merchant_location_key = merchant_location_key
        if quantity is not None:
            self.quantity = quantity

    @property
    def availability_type(self):
        """Gets the availability_type of this PickupAtLocationAvailability.  # noqa: E501

        The enumeration value in this field indicates the availability status of the inventory item at the merchant's physical store specified by the <strong>pickupAtLocationAvailability.merchantLocationKey</strong> field. This field is required if the <strong>pickupAtLocationAvailability</strong> container is used, and is always returned with the <strong>pickupAtLocationAvailability</strong> container.  <br><br> See <a href=\"/api-docs/sell/inventory/types/slr:AvailabilityTypeEnum\" target=\"_blank\">AvailabilityTypeEnum</a> for more information about how/when you use each enumeration value. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/inventory/types/slr:AvailabilityTypeEnum'>eBay API documentation</a>  # noqa: E501

        :return: The availability_type of this PickupAtLocationAvailability.  # noqa: E501
        :rtype: str
        """
        return self._availability_type

    @availability_type.setter
    def availability_type(self, availability_type):
        """Sets the availability_type of this PickupAtLocationAvailability.

        The enumeration value in this field indicates the availability status of the inventory item at the merchant's physical store specified by the <strong>pickupAtLocationAvailability.merchantLocationKey</strong> field. This field is required if the <strong>pickupAtLocationAvailability</strong> container is used, and is always returned with the <strong>pickupAtLocationAvailability</strong> container.  <br><br> See <a href=\"/api-docs/sell/inventory/types/slr:AvailabilityTypeEnum\" target=\"_blank\">AvailabilityTypeEnum</a> for more information about how/when you use each enumeration value. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/inventory/types/slr:AvailabilityTypeEnum'>eBay API documentation</a>  # noqa: E501

        :param availability_type: The availability_type of this PickupAtLocationAvailability.  # noqa: E501
        :type: str
        """

        self._availability_type = availability_type

    @property
    def fulfillment_time(self):
        """Gets the fulfillment_time of this PickupAtLocationAvailability.  # noqa: E501


        :return: The fulfillment_time of this PickupAtLocationAvailability.  # noqa: E501
        :rtype: TimeDuration
        """
        return self._fulfillment_time

    @fulfillment_time.setter
    def fulfillment_time(self, fulfillment_time):
        """Sets the fulfillment_time of this PickupAtLocationAvailability.


        :param fulfillment_time: The fulfillment_time of this PickupAtLocationAvailability.  # noqa: E501
        :type: TimeDuration
        """

        self._fulfillment_time = fulfillment_time

    @property
    def merchant_location_key(self):
        """Gets the merchant_location_key of this PickupAtLocationAvailability.  # noqa: E501

        The unique identifier of a merchant's store where the In-Store Pickup inventory item is currently located, or where inventory will be sent to. If the merchant's store is currently awaiting for inventory, the <strong>availabilityType</strong> value should be <code>SHIP_TO_STORE</code>. This field is required if the <strong>pickupAtLocationAvailability</strong> container is used, and is always returned with the <strong>pickupAtLocationAvailability</strong> container.<br><br>Use the <a href=\"/api-docs/sell/inventory/resources/location/methods/getInventoryLocations\" target=\"_blank\">getInventoryLocations</a> method to retrieve merchant location keys.<br><br><b>Max length</b>: 36  # noqa: E501

        :return: The merchant_location_key of this PickupAtLocationAvailability.  # noqa: E501
        :rtype: str
        """
        return self._merchant_location_key

    @merchant_location_key.setter
    def merchant_location_key(self, merchant_location_key):
        """Sets the merchant_location_key of this PickupAtLocationAvailability.

        The unique identifier of a merchant's store where the In-Store Pickup inventory item is currently located, or where inventory will be sent to. If the merchant's store is currently awaiting for inventory, the <strong>availabilityType</strong> value should be <code>SHIP_TO_STORE</code>. This field is required if the <strong>pickupAtLocationAvailability</strong> container is used, and is always returned with the <strong>pickupAtLocationAvailability</strong> container.<br><br>Use the <a href=\"/api-docs/sell/inventory/resources/location/methods/getInventoryLocations\" target=\"_blank\">getInventoryLocations</a> method to retrieve merchant location keys.<br><br><b>Max length</b>: 36  # noqa: E501

        :param merchant_location_key: The merchant_location_key of this PickupAtLocationAvailability.  # noqa: E501
        :type: str
        """

        self._merchant_location_key = merchant_location_key

    @property
    def quantity(self):
        """Gets the quantity of this PickupAtLocationAvailability.  # noqa: E501

        This integer value indicates the quantity of the inventory item that is available for In-Store Pickup at the store identified by the  <strong>merchantLocationKey</strong> value.  The value of <strong>quantity</strong> should be an integer value greater than <code>0</code>, unless the inventory item is out of stock. This field is required if the <strong>pickupAtLocationAvailability</strong> container is used, and is always returned with the <strong>pickupAtLocationAvailability</strong> container.  # noqa: E501

        :return: The quantity of this PickupAtLocationAvailability.  # noqa: E501
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this PickupAtLocationAvailability.

        This integer value indicates the quantity of the inventory item that is available for In-Store Pickup at the store identified by the  <strong>merchantLocationKey</strong> value.  The value of <strong>quantity</strong> should be an integer value greater than <code>0</code>, unless the inventory item is out of stock. This field is required if the <strong>pickupAtLocationAvailability</strong> container is used, and is always returned with the <strong>pickupAtLocationAvailability</strong> container.  # noqa: E501

        :param quantity: The quantity of this PickupAtLocationAvailability.  # noqa: E501
        :type: int
        """

        self._quantity = quantity

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
        if issubclass(PickupAtLocationAvailability, dict):
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
        if not isinstance(other, PickupAtLocationAvailability):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
