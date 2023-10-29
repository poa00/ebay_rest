# coding: utf-8

"""
    Fulfillment API

    Use the Fulfillment API to complete the process of packaging, addressing, handling, and shipping each order on behalf of the seller, in accordance with the payment method and timing specified at checkout.  # noqa: E501

    OpenAPI spec version: v1.20.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ShippingFulfillmentDetails(object):
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
        'line_items': 'list[LineItemReference]',
        'shipped_date': 'str',
        'shipping_carrier_code': 'str',
        'tracking_number': 'str'
    }

    attribute_map = {
        'line_items': 'lineItems',
        'shipped_date': 'shippedDate',
        'shipping_carrier_code': 'shippingCarrierCode',
        'tracking_number': 'trackingNumber'
    }

    def __init__(self, line_items=None, shipped_date=None, shipping_carrier_code=None, tracking_number=None):  # noqa: E501
        """ShippingFulfillmentDetails - a model defined in Swagger"""  # noqa: E501
        self._line_items = None
        self._shipped_date = None
        self._shipping_carrier_code = None
        self._tracking_number = None
        self.discriminator = None
        if line_items is not None:
            self.line_items = line_items
        if shipped_date is not None:
            self.shipped_date = shipped_date
        if shipping_carrier_code is not None:
            self.shipping_carrier_code = shipping_carrier_code
        if tracking_number is not None:
            self.tracking_number = tracking_number

    @property
    def line_items(self):
        """Gets the line_items of this ShippingFulfillmentDetails.  # noqa: E501

        This array contains a list of or more line items and the quantity that will be shipped in the same package.  # noqa: E501

        :return: The line_items of this ShippingFulfillmentDetails.  # noqa: E501
        :rtype: list[LineItemReference]
        """
        return self._line_items

    @line_items.setter
    def line_items(self, line_items):
        """Sets the line_items of this ShippingFulfillmentDetails.

        This array contains a list of or more line items and the quantity that will be shipped in the same package.  # noqa: E501

        :param line_items: The line_items of this ShippingFulfillmentDetails.  # noqa: E501
        :type: list[LineItemReference]
        """

        self._line_items = line_items

    @property
    def shipped_date(self):
        """Gets the shipped_date of this ShippingFulfillmentDetails.  # noqa: E501

        This is the actual date and time that the fulfillment package was shipped. This timestamp is in ISO 8601 format, which uses the 24-hour Universal Coordinated Time (UTC) clock. The seller should use the actual date/time that the package was shipped, but if this field is omitted, it will default to the current date/time.<br><br><b>Format:</b> <code>[YYYY]-[MM]-[DD]T[hh]:[mm]:[ss].[sss]Z</code> <br><b>Example:</b> <code>2015-08-04T19:09:02.768Z</code><br><br><b>Default:</b> The current date and time.  # noqa: E501

        :return: The shipped_date of this ShippingFulfillmentDetails.  # noqa: E501
        :rtype: str
        """
        return self._shipped_date

    @shipped_date.setter
    def shipped_date(self, shipped_date):
        """Sets the shipped_date of this ShippingFulfillmentDetails.

        This is the actual date and time that the fulfillment package was shipped. This timestamp is in ISO 8601 format, which uses the 24-hour Universal Coordinated Time (UTC) clock. The seller should use the actual date/time that the package was shipped, but if this field is omitted, it will default to the current date/time.<br><br><b>Format:</b> <code>[YYYY]-[MM]-[DD]T[hh]:[mm]:[ss].[sss]Z</code> <br><b>Example:</b> <code>2015-08-04T19:09:02.768Z</code><br><br><b>Default:</b> The current date and time.  # noqa: E501

        :param shipped_date: The shipped_date of this ShippingFulfillmentDetails.  # noqa: E501
        :type: str
        """

        self._shipped_date = shipped_date

    @property
    def shipping_carrier_code(self):
        """Gets the shipping_carrier_code of this ShippingFulfillmentDetails.  # noqa: E501

        The unique identifier of the shipping carrier being used to ship the line item(s). Technically, the <strong>shippingCarrierCode</strong> and <strong>trackingNumber</strong> fields are optional, but generally these fields will be provided if the shipping carrier and tracking number are known. <br><br><span class=\"tablenote\"><strong>Note:</strong> Use the Trading API's <a href=\"https://developer.ebay.com/devzone/XML/docs/Reference/eBay/GeteBayDetails.html \" target=\"_blank\">GeteBayDetails</a> call to retrieve the latest shipping carrier enumeration values. When making the <a href=\"https://developer.ebay.com/devzone/XML/docs/Reference/eBay/GeteBayDetails.html \" target=\"_blank\">GeteBayDetails</a> call, include the <strong>DetailName</strong> field in the request payload and set its value to <code>ShippingCarrierDetails</code>. Each valid shipping carrier enumeration value is returned in a <strong>ShippingCarrierDetails.ShippingCarrier</strong> field in the response payload.</span>  # noqa: E501

        :return: The shipping_carrier_code of this ShippingFulfillmentDetails.  # noqa: E501
        :rtype: str
        """
        return self._shipping_carrier_code

    @shipping_carrier_code.setter
    def shipping_carrier_code(self, shipping_carrier_code):
        """Sets the shipping_carrier_code of this ShippingFulfillmentDetails.

        The unique identifier of the shipping carrier being used to ship the line item(s). Technically, the <strong>shippingCarrierCode</strong> and <strong>trackingNumber</strong> fields are optional, but generally these fields will be provided if the shipping carrier and tracking number are known. <br><br><span class=\"tablenote\"><strong>Note:</strong> Use the Trading API's <a href=\"https://developer.ebay.com/devzone/XML/docs/Reference/eBay/GeteBayDetails.html \" target=\"_blank\">GeteBayDetails</a> call to retrieve the latest shipping carrier enumeration values. When making the <a href=\"https://developer.ebay.com/devzone/XML/docs/Reference/eBay/GeteBayDetails.html \" target=\"_blank\">GeteBayDetails</a> call, include the <strong>DetailName</strong> field in the request payload and set its value to <code>ShippingCarrierDetails</code>. Each valid shipping carrier enumeration value is returned in a <strong>ShippingCarrierDetails.ShippingCarrier</strong> field in the response payload.</span>  # noqa: E501

        :param shipping_carrier_code: The shipping_carrier_code of this ShippingFulfillmentDetails.  # noqa: E501
        :type: str
        """

        self._shipping_carrier_code = shipping_carrier_code

    @property
    def tracking_number(self):
        """Gets the tracking_number of this ShippingFulfillmentDetails.  # noqa: E501

        The tracking number provided by the shipping carrier for this fulfillment. The seller should be careful that this tracking number is accurate since the buyer will use this tracking number to track shipment, and eBay has no way to verify the accuracy of this number.<br><br>This field and the <b>shippingCarrierCode</b> field are mutually dependent. If you include one, you must also include the other.<br><br><span class=\"tablenote\"><strong>Note:</strong> If you include <b>trackingNumber</b> (and <b>shippingCarrierCode</b>) in the request, the resulting fulfillment's ID (returned in the HTTP location code) is the tracking number. If you do not include shipment tracking information, the resulting fulfillment ID will default to an arbitrary number such as <code>999</code>.</span><br><span class=\"tablenote\"><strong>Note:</strong> Only alphanumeric characters are supported for shipment tracking numbers. Spaces, hyphens, and all other special characters are not supported. Do not include a space in the tracking number even if a space appears in the tracking number on the shipping label.</span>  # noqa: E501

        :return: The tracking_number of this ShippingFulfillmentDetails.  # noqa: E501
        :rtype: str
        """
        return self._tracking_number

    @tracking_number.setter
    def tracking_number(self, tracking_number):
        """Sets the tracking_number of this ShippingFulfillmentDetails.

        The tracking number provided by the shipping carrier for this fulfillment. The seller should be careful that this tracking number is accurate since the buyer will use this tracking number to track shipment, and eBay has no way to verify the accuracy of this number.<br><br>This field and the <b>shippingCarrierCode</b> field are mutually dependent. If you include one, you must also include the other.<br><br><span class=\"tablenote\"><strong>Note:</strong> If you include <b>trackingNumber</b> (and <b>shippingCarrierCode</b>) in the request, the resulting fulfillment's ID (returned in the HTTP location code) is the tracking number. If you do not include shipment tracking information, the resulting fulfillment ID will default to an arbitrary number such as <code>999</code>.</span><br><span class=\"tablenote\"><strong>Note:</strong> Only alphanumeric characters are supported for shipment tracking numbers. Spaces, hyphens, and all other special characters are not supported. Do not include a space in the tracking number even if a space appears in the tracking number on the shipping label.</span>  # noqa: E501

        :param tracking_number: The tracking_number of this ShippingFulfillmentDetails.  # noqa: E501
        :type: str
        """

        self._tracking_number = tracking_number

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
        if issubclass(ShippingFulfillmentDetails, dict):
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
        if not isinstance(other, ShippingFulfillmentDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
