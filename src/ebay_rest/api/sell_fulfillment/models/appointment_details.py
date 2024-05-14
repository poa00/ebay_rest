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

class AppointmentDetails(object):
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
        'appointment_end_time': 'str',
        'appointment_start_time': 'str',
        'appointment_status': 'str',
        'appointment_type': 'str',
        'appointment_window': 'str',
        'service_provider_appointment_date': 'str'
    }

    attribute_map = {
        'appointment_end_time': 'appointmentEndTime',
        'appointment_start_time': 'appointmentStartTime',
        'appointment_status': 'appointmentStatus',
        'appointment_type': 'appointmentType',
        'appointment_window': 'appointmentWindow',
        'service_provider_appointment_date': 'serviceProviderAppointmentDate'
    }

    def __init__(self, appointment_end_time=None, appointment_start_time=None, appointment_status=None, appointment_type=None, appointment_window=None, service_provider_appointment_date=None):  # noqa: E501
        """AppointmentDetails - a model defined in Swagger"""  # noqa: E501
        self._appointment_end_time = None
        self._appointment_start_time = None
        self._appointment_status = None
        self._appointment_type = None
        self._appointment_window = None
        self._service_provider_appointment_date = None
        self.discriminator = None
        if appointment_end_time is not None:
            self.appointment_end_time = appointment_end_time
        if appointment_start_time is not None:
            self.appointment_start_time = appointment_start_time
        if appointment_status is not None:
            self.appointment_status = appointment_status
        if appointment_type is not None:
            self.appointment_type = appointment_type
        if appointment_window is not None:
            self.appointment_window = appointment_window
        if service_provider_appointment_date is not None:
            self.service_provider_appointment_date = service_provider_appointment_date

    @property
    def appointment_end_time(self):
        """Gets the appointment_end_time of this AppointmentDetails.  # noqa: E501

        The date and time the appointment ends, formatted as an <a href=\"https://www.iso.org/iso-8601-date-and-time-format.html \" title=\"https://www.iso.org \" target=\"_blank\">ISO 8601</a> string, which is based on the 24-hour Coordinated Universal Time (UTC) clock. Required for tire installation. <br><br><b>Format:</b> <code>[YYYY]-[MM]-[DD]T[hh]:[mm]:[ss].[sss]Z</code> <br><b>Example:</b> <code>2022-10-28T00:00:00.000Z</code>  # noqa: E501

        :return: The appointment_end_time of this AppointmentDetails.  # noqa: E501
        :rtype: str
        """
        return self._appointment_end_time

    @appointment_end_time.setter
    def appointment_end_time(self, appointment_end_time):
        """Sets the appointment_end_time of this AppointmentDetails.

        The date and time the appointment ends, formatted as an <a href=\"https://www.iso.org/iso-8601-date-and-time-format.html \" title=\"https://www.iso.org \" target=\"_blank\">ISO 8601</a> string, which is based on the 24-hour Coordinated Universal Time (UTC) clock. Required for tire installation. <br><br><b>Format:</b> <code>[YYYY]-[MM]-[DD]T[hh]:[mm]:[ss].[sss]Z</code> <br><b>Example:</b> <code>2022-10-28T00:00:00.000Z</code>  # noqa: E501

        :param appointment_end_time: The appointment_end_time of this AppointmentDetails.  # noqa: E501
        :type: str
        """

        self._appointment_end_time = appointment_end_time

    @property
    def appointment_start_time(self):
        """Gets the appointment_start_time of this AppointmentDetails.  # noqa: E501

        The date and time the appointment begins, formatted as an <a href=\"https://www.iso.org/iso-8601-date-and-time-format.html \" title=\"https://www.iso.org \" target=\"_blank\">ISO 8601</a> string, which is based on the 24-hour Coordinated Universal Time (UTC) clock.  <br><br><b>Format:</b> <code>[YYYY]-[MM]-[DD]T[hh]:[mm]:[ss].[sss]Z</code> <br><b>Example:</b> <code>2022-10-28T00:10:00.000Z</code>  # noqa: E501

        :return: The appointment_start_time of this AppointmentDetails.  # noqa: E501
        :rtype: str
        """
        return self._appointment_start_time

    @appointment_start_time.setter
    def appointment_start_time(self, appointment_start_time):
        """Sets the appointment_start_time of this AppointmentDetails.

        The date and time the appointment begins, formatted as an <a href=\"https://www.iso.org/iso-8601-date-and-time-format.html \" title=\"https://www.iso.org \" target=\"_blank\">ISO 8601</a> string, which is based on the 24-hour Coordinated Universal Time (UTC) clock.  <br><br><b>Format:</b> <code>[YYYY]-[MM]-[DD]T[hh]:[mm]:[ss].[sss]Z</code> <br><b>Example:</b> <code>2022-10-28T00:10:00.000Z</code>  # noqa: E501

        :param appointment_start_time: The appointment_start_time of this AppointmentDetails.  # noqa: E501
        :type: str
        """

        self._appointment_start_time = appointment_start_time

    @property
    def appointment_status(self):
        """Gets the appointment_status of this AppointmentDetails.  # noqa: E501

        The status of the appointment. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/fulfillment/types/sel:AppointmentStatusEnum'>eBay API documentation</a>  # noqa: E501

        :return: The appointment_status of this AppointmentDetails.  # noqa: E501
        :rtype: str
        """
        return self._appointment_status

    @appointment_status.setter
    def appointment_status(self, appointment_status):
        """Sets the appointment_status of this AppointmentDetails.

        The status of the appointment. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/fulfillment/types/sel:AppointmentStatusEnum'>eBay API documentation</a>  # noqa: E501

        :param appointment_status: The appointment_status of this AppointmentDetails.  # noqa: E501
        :type: str
        """

        self._appointment_status = appointment_status

    @property
    def appointment_type(self):
        """Gets the appointment_type of this AppointmentDetails.  # noqa: E501

        The type of appointment. MACRO appointments only have a start time (not bounded with end time). TIME_SLOT appointments have a period (both start time and end time). Required for tire installation. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/fulfillment/types/sel:AppointmentTypeEnum'>eBay API documentation</a>  # noqa: E501

        :return: The appointment_type of this AppointmentDetails.  # noqa: E501
        :rtype: str
        """
        return self._appointment_type

    @appointment_type.setter
    def appointment_type(self, appointment_type):
        """Sets the appointment_type of this AppointmentDetails.

        The type of appointment. MACRO appointments only have a start time (not bounded with end time). TIME_SLOT appointments have a period (both start time and end time). Required for tire installation. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/fulfillment/types/sel:AppointmentTypeEnum'>eBay API documentation</a>  # noqa: E501

        :param appointment_type: The appointment_type of this AppointmentDetails.  # noqa: E501
        :type: str
        """

        self._appointment_type = appointment_type

    @property
    def appointment_window(self):
        """Gets the appointment_window of this AppointmentDetails.  # noqa: E501

        Appointment window for MACRO appointments. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/fulfillment/types/sel:AppointmentWindowEnum'>eBay API documentation</a>  # noqa: E501

        :return: The appointment_window of this AppointmentDetails.  # noqa: E501
        :rtype: str
        """
        return self._appointment_window

    @appointment_window.setter
    def appointment_window(self, appointment_window):
        """Sets the appointment_window of this AppointmentDetails.

        Appointment window for MACRO appointments. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/fulfillment/types/sel:AppointmentWindowEnum'>eBay API documentation</a>  # noqa: E501

        :param appointment_window: The appointment_window of this AppointmentDetails.  # noqa: E501
        :type: str
        """

        self._appointment_window = appointment_window

    @property
    def service_provider_appointment_date(self):
        """Gets the service_provider_appointment_date of this AppointmentDetails.  # noqa: E501

        Service provider date of the appointment (no time stamp). Returned only for MACRO appointment types.  # noqa: E501

        :return: The service_provider_appointment_date of this AppointmentDetails.  # noqa: E501
        :rtype: str
        """
        return self._service_provider_appointment_date

    @service_provider_appointment_date.setter
    def service_provider_appointment_date(self, service_provider_appointment_date):
        """Sets the service_provider_appointment_date of this AppointmentDetails.

        Service provider date of the appointment (no time stamp). Returned only for MACRO appointment types.  # noqa: E501

        :param service_provider_appointment_date: The service_provider_appointment_date of this AppointmentDetails.  # noqa: E501
        :type: str
        """

        self._service_provider_appointment_date = service_provider_appointment_date

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
        if issubclass(AppointmentDetails, dict):
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
        if not isinstance(other, AppointmentDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
