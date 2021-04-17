# coding: utf-8

"""
     Seller Service Metrics API 

    The <i>Analytics API</i> provides data and information about a seller and their eBay business.  <br><br>The resources and methods in this API let sellers review information on their listing performance, metrics on their customer service performance, and details on their eBay seller performance rating.  <br><br>The three resources in the Analytics API provide the following data and information: <ul><li><b>Customer Service Metric</b> &ndash; Returns data on a seller's customer service performance as compared to other seller's in the same peer group.</li> <li><b>Traffic Report</b> &ndash; Returns data that shows how buyers are engaging with a seller's listings.</li> <li><b>Seller Standards Profile</b> &ndash; Returns data pertaining to a seller's performance rating.</li></ul> Sellers can use the data and information returned by the various Analytics API methods to determine where they can make improvements to increase sales and how they might improve their seller status as viewed by eBay buyers.  <br><br>For details on using this API, see <a href=\"/api-docs/sell/static/performance/analyzing-performance.html\" title=\"Selling Integration Guide\">Analyzing seller performance</a>.  # noqa: E501

    OpenAPI spec version: 1.2.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class GetCustomerServiceMetricResponse(object):
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
        'dimension_metrics': 'list[DimensionMetric]',
        'evaluation_cycle': 'EvaluationCycle',
        'marketplace_id': 'str'
    }

    attribute_map = {
        'dimension_metrics': 'dimensionMetrics',
        'evaluation_cycle': 'evaluationCycle',
        'marketplace_id': 'marketplaceId'
    }

    def __init__(self, dimension_metrics=None, evaluation_cycle=None, marketplace_id=None):  # noqa: E501
        """GetCustomerServiceMetricResponse - a model defined in Swagger"""  # noqa: E501
        self._dimension_metrics = None
        self._evaluation_cycle = None
        self._marketplace_id = None
        self.discriminator = None
        if dimension_metrics is not None:
            self.dimension_metrics = dimension_metrics
        if evaluation_cycle is not None:
            self.evaluation_cycle = evaluation_cycle
        if marketplace_id is not None:
            self.marketplace_id = marketplace_id

    @property
    def dimension_metrics(self):
        """Gets the dimension_metrics of this GetCustomerServiceMetricResponse.  # noqa: E501

        This container provides a seller's customer service metric performance for a given dimension. In the getCustomerServiceMetric request, specify values for the following request parameters to control the returned dimension and the associated metric values: customer_service_metric_type evaluation_type evaluation_marketplace_id  # noqa: E501

        :return: The dimension_metrics of this GetCustomerServiceMetricResponse.  # noqa: E501
        :rtype: list[DimensionMetric]
        """
        return self._dimension_metrics

    @dimension_metrics.setter
    def dimension_metrics(self, dimension_metrics):
        """Sets the dimension_metrics of this GetCustomerServiceMetricResponse.

        This container provides a seller's customer service metric performance for a given dimension. In the getCustomerServiceMetric request, specify values for the following request parameters to control the returned dimension and the associated metric values: customer_service_metric_type evaluation_type evaluation_marketplace_id  # noqa: E501

        :param dimension_metrics: The dimension_metrics of this GetCustomerServiceMetricResponse.  # noqa: E501
        :type: list[DimensionMetric]
        """

        self._dimension_metrics = dimension_metrics

    @property
    def evaluation_cycle(self):
        """Gets the evaluation_cycle of this GetCustomerServiceMetricResponse.  # noqa: E501


        :return: The evaluation_cycle of this GetCustomerServiceMetricResponse.  # noqa: E501
        :rtype: EvaluationCycle
        """
        return self._evaluation_cycle

    @evaluation_cycle.setter
    def evaluation_cycle(self, evaluation_cycle):
        """Sets the evaluation_cycle of this GetCustomerServiceMetricResponse.


        :param evaluation_cycle: The evaluation_cycle of this GetCustomerServiceMetricResponse.  # noqa: E501
        :type: EvaluationCycle
        """

        self._evaluation_cycle = evaluation_cycle

    @property
    def marketplace_id(self):
        """Gets the marketplace_id of this GetCustomerServiceMetricResponse.  # noqa: E501

        The eBay marketplace ID of the marketplace upon which the customer service metric evaluation is based. The customer_service_metric resource supports a limited set of marketplaces. For a complete list of the supported marketplaces, please see the Service metrics policy page. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/analytics/types/bas:MarketplaceIdEnum'>eBay API documentation</a>  # noqa: E501

        :return: The marketplace_id of this GetCustomerServiceMetricResponse.  # noqa: E501
        :rtype: str
        """
        return self._marketplace_id

    @marketplace_id.setter
    def marketplace_id(self, marketplace_id):
        """Sets the marketplace_id of this GetCustomerServiceMetricResponse.

        The eBay marketplace ID of the marketplace upon which the customer service metric evaluation is based. The customer_service_metric resource supports a limited set of marketplaces. For a complete list of the supported marketplaces, please see the Service metrics policy page. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/analytics/types/bas:MarketplaceIdEnum'>eBay API documentation</a>  # noqa: E501

        :param marketplace_id: The marketplace_id of this GetCustomerServiceMetricResponse.  # noqa: E501
        :type: str
        """

        self._marketplace_id = marketplace_id

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
        if issubclass(GetCustomerServiceMetricResponse, dict):
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
        if not isinstance(other, GetCustomerServiceMetricResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
