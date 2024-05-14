# coding: utf-8

"""
    Fulfillment API

    Use the Fulfillment API to complete the process of packaging, addressing, handling, and shipping each order on behalf of the seller, in accordance with the payment method and timing specified at checkout.  # noqa: E501

    OpenAPI spec version: v1.20.4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class FulfillmentStartInstruction(object):
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
        'appointment': 'AppointmentDetails',
        'ebay_supported_fulfillment': 'bool',
        'final_destination_address': 'Address',
        'fulfillment_instructions_type': 'str',
        'max_estimated_delivery_date': 'str',
        'min_estimated_delivery_date': 'str',
        'pickup_step': 'PickupStep',
        'shipping_step': 'ShippingStep'
    }

    attribute_map = {
        'appointment': 'appointment',
        'ebay_supported_fulfillment': 'ebaySupportedFulfillment',
        'final_destination_address': 'finalDestinationAddress',
        'fulfillment_instructions_type': 'fulfillmentInstructionsType',
        'max_estimated_delivery_date': 'maxEstimatedDeliveryDate',
        'min_estimated_delivery_date': 'minEstimatedDeliveryDate',
        'pickup_step': 'pickupStep',
        'shipping_step': 'shippingStep'
    }

    def __init__(self, appointment=None, ebay_supported_fulfillment=None, final_destination_address=None, fulfillment_instructions_type=None, max_estimated_delivery_date=None, min_estimated_delivery_date=None, pickup_step=None, shipping_step=None):  # noqa: E501
        """FulfillmentStartInstruction - a model defined in Swagger"""  # noqa: E501
        self._appointment = None
        self._ebay_supported_fulfillment = None
        self._final_destination_address = None
        self._fulfillment_instructions_type = None
        self._max_estimated_delivery_date = None
        self._min_estimated_delivery_date = None
        self._pickup_step = None
        self._shipping_step = None
        self.discriminator = None
        if appointment is not None:
            self.appointment = appointment
        if ebay_supported_fulfillment is not None:
            self.ebay_supported_fulfillment = ebay_supported_fulfillment
        if final_destination_address is not None:
            self.final_destination_address = final_destination_address
        if fulfillment_instructions_type is not None:
            self.fulfillment_instructions_type = fulfillment_instructions_type
        if max_estimated_delivery_date is not None:
            self.max_estimated_delivery_date = max_estimated_delivery_date
        if min_estimated_delivery_date is not None:
            self.min_estimated_delivery_date = min_estimated_delivery_date
        if pickup_step is not None:
            self.pickup_step = pickup_step
        if shipping_step is not None:
            self.shipping_step = shipping_step

    @property
    def appointment(self):
        """Gets the appointment of this FulfillmentStartInstruction.  # noqa: E501


        :return: The appointment of this FulfillmentStartInstruction.  # noqa: E501
        :rtype: AppointmentDetails
        """
        return self._appointment

    @appointment.setter
    def appointment(self, appointment):
        """Sets the appointment of this FulfillmentStartInstruction.


        :param appointment: The appointment of this FulfillmentStartInstruction.  # noqa: E501
        :type: AppointmentDetails
        """

        self._appointment = appointment

    @property
    def ebay_supported_fulfillment(self):
        """Gets the ebay_supported_fulfillment of this FulfillmentStartInstruction.  # noqa: E501

        This field is only returned if its value is <code>true</code> and indicates that the fulfillment will be shipped via eBay's Global Shipping Program, eBay International Shipping, or the Authenticity Guarantee service program. <br><br>For more information, see the <a href=\"https://www.ebay.com/help/selling/shipping-items/setting-shipping-options/global-shipping-program?id=4646 \" target=\"_blank\">Global Shipping Program</a> help topic.  # noqa: E501

        :return: The ebay_supported_fulfillment of this FulfillmentStartInstruction.  # noqa: E501
        :rtype: bool
        """
        return self._ebay_supported_fulfillment

    @ebay_supported_fulfillment.setter
    def ebay_supported_fulfillment(self, ebay_supported_fulfillment):
        """Sets the ebay_supported_fulfillment of this FulfillmentStartInstruction.

        This field is only returned if its value is <code>true</code> and indicates that the fulfillment will be shipped via eBay's Global Shipping Program, eBay International Shipping, or the Authenticity Guarantee service program. <br><br>For more information, see the <a href=\"https://www.ebay.com/help/selling/shipping-items/setting-shipping-options/global-shipping-program?id=4646 \" target=\"_blank\">Global Shipping Program</a> help topic.  # noqa: E501

        :param ebay_supported_fulfillment: The ebay_supported_fulfillment of this FulfillmentStartInstruction.  # noqa: E501
        :type: bool
        """

        self._ebay_supported_fulfillment = ebay_supported_fulfillment

    @property
    def final_destination_address(self):
        """Gets the final_destination_address of this FulfillmentStartInstruction.  # noqa: E501


        :return: The final_destination_address of this FulfillmentStartInstruction.  # noqa: E501
        :rtype: Address
        """
        return self._final_destination_address

    @final_destination_address.setter
    def final_destination_address(self, final_destination_address):
        """Sets the final_destination_address of this FulfillmentStartInstruction.


        :param final_destination_address: The final_destination_address of this FulfillmentStartInstruction.  # noqa: E501
        :type: Address
        """

        self._final_destination_address = final_destination_address

    @property
    def fulfillment_instructions_type(self):
        """Gets the fulfillment_instructions_type of this FulfillmentStartInstruction.  # noqa: E501

        The enumeration value returned in this field indicates the method of fulfillment that will be used to deliver this set of line items (this package) to the buyer. This field will have a value of <code>SHIP_TO</code> if the <b>ebaySupportedFulfillment</b> field is returned with a value of <code>true</code>. See the <strong>FulfillmentInstructionsType</strong> definition for more information about different fulfillment types. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/fulfillment/types/sel:FulfillmentInstructionsType'>eBay API documentation</a>  # noqa: E501

        :return: The fulfillment_instructions_type of this FulfillmentStartInstruction.  # noqa: E501
        :rtype: str
        """
        return self._fulfillment_instructions_type

    @fulfillment_instructions_type.setter
    def fulfillment_instructions_type(self, fulfillment_instructions_type):
        """Sets the fulfillment_instructions_type of this FulfillmentStartInstruction.

        The enumeration value returned in this field indicates the method of fulfillment that will be used to deliver this set of line items (this package) to the buyer. This field will have a value of <code>SHIP_TO</code> if the <b>ebaySupportedFulfillment</b> field is returned with a value of <code>true</code>. See the <strong>FulfillmentInstructionsType</strong> definition for more information about different fulfillment types. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/fulfillment/types/sel:FulfillmentInstructionsType'>eBay API documentation</a>  # noqa: E501

        :param fulfillment_instructions_type: The fulfillment_instructions_type of this FulfillmentStartInstruction.  # noqa: E501
        :type: str
        """

        self._fulfillment_instructions_type = fulfillment_instructions_type

    @property
    def max_estimated_delivery_date(self):
        """Gets the max_estimated_delivery_date of this FulfillmentStartInstruction.  # noqa: E501

        This is the estimated latest date that the fulfillment will be completed. This timestamp is in ISO 8601 format, which uses the 24-hour Universal Coordinated Time (UTC) clock. This field is not returned ifthe value of the <b>fulfillmentInstructionsType</b> field is <code>DIGITAL</code> or <code>PREPARE_FOR_PICKUP</code>.  <br><br><b>Format:</b> <code>[YYYY]-[MM]-[DD]T[hh]:[mm]:[ss].[sss]Z</code> <br><b>Example:</b> <code>2015-08-04T19:09:02.768Z</code>  # noqa: E501

        :return: The max_estimated_delivery_date of this FulfillmentStartInstruction.  # noqa: E501
        :rtype: str
        """
        return self._max_estimated_delivery_date

    @max_estimated_delivery_date.setter
    def max_estimated_delivery_date(self, max_estimated_delivery_date):
        """Sets the max_estimated_delivery_date of this FulfillmentStartInstruction.

        This is the estimated latest date that the fulfillment will be completed. This timestamp is in ISO 8601 format, which uses the 24-hour Universal Coordinated Time (UTC) clock. This field is not returned ifthe value of the <b>fulfillmentInstructionsType</b> field is <code>DIGITAL</code> or <code>PREPARE_FOR_PICKUP</code>.  <br><br><b>Format:</b> <code>[YYYY]-[MM]-[DD]T[hh]:[mm]:[ss].[sss]Z</code> <br><b>Example:</b> <code>2015-08-04T19:09:02.768Z</code>  # noqa: E501

        :param max_estimated_delivery_date: The max_estimated_delivery_date of this FulfillmentStartInstruction.  # noqa: E501
        :type: str
        """

        self._max_estimated_delivery_date = max_estimated_delivery_date

    @property
    def min_estimated_delivery_date(self):
        """Gets the min_estimated_delivery_date of this FulfillmentStartInstruction.  # noqa: E501

        This is the estimated earliest date that the fulfillment will be completed. This timestamp is in ISO 8601 format, which uses the 24-hour Universal Coordinated Time (UTC) clock. This field is not returned if  the value of the <b>fulfillmentInstructionsType</b> field is <code>DIGITAL</code> or <code>PREPARE_FOR_PICKUP</code>.  <br><br><b>Format:</b> <code>[YYYY]-[MM]-[DD]T[hh]:[mm]:[ss].[sss]Z</code> <br><b>Example:</b> <code>2015-08-04T19:09:02.768Z</code>  # noqa: E501

        :return: The min_estimated_delivery_date of this FulfillmentStartInstruction.  # noqa: E501
        :rtype: str
        """
        return self._min_estimated_delivery_date

    @min_estimated_delivery_date.setter
    def min_estimated_delivery_date(self, min_estimated_delivery_date):
        """Sets the min_estimated_delivery_date of this FulfillmentStartInstruction.

        This is the estimated earliest date that the fulfillment will be completed. This timestamp is in ISO 8601 format, which uses the 24-hour Universal Coordinated Time (UTC) clock. This field is not returned if  the value of the <b>fulfillmentInstructionsType</b> field is <code>DIGITAL</code> or <code>PREPARE_FOR_PICKUP</code>.  <br><br><b>Format:</b> <code>[YYYY]-[MM]-[DD]T[hh]:[mm]:[ss].[sss]Z</code> <br><b>Example:</b> <code>2015-08-04T19:09:02.768Z</code>  # noqa: E501

        :param min_estimated_delivery_date: The min_estimated_delivery_date of this FulfillmentStartInstruction.  # noqa: E501
        :type: str
        """

        self._min_estimated_delivery_date = min_estimated_delivery_date

    @property
    def pickup_step(self):
        """Gets the pickup_step of this FulfillmentStartInstruction.  # noqa: E501


        :return: The pickup_step of this FulfillmentStartInstruction.  # noqa: E501
        :rtype: PickupStep
        """
        return self._pickup_step

    @pickup_step.setter
    def pickup_step(self, pickup_step):
        """Sets the pickup_step of this FulfillmentStartInstruction.


        :param pickup_step: The pickup_step of this FulfillmentStartInstruction.  # noqa: E501
        :type: PickupStep
        """

        self._pickup_step = pickup_step

    @property
    def shipping_step(self):
        """Gets the shipping_step of this FulfillmentStartInstruction.  # noqa: E501


        :return: The shipping_step of this FulfillmentStartInstruction.  # noqa: E501
        :rtype: ShippingStep
        """
        return self._shipping_step

    @shipping_step.setter
    def shipping_step(self, shipping_step):
        """Sets the shipping_step of this FulfillmentStartInstruction.


        :param shipping_step: The shipping_step of this FulfillmentStartInstruction.  # noqa: E501
        :type: ShippingStep
        """

        self._shipping_step = shipping_step

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
        if issubclass(FulfillmentStartInstruction, dict):
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
        if not isinstance(other, FulfillmentStartInstruction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
