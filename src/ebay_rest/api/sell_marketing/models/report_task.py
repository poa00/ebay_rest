# coding: utf-8

"""
    Marketing API

    <p>The <i>Marketing API </i> offers two platforms that sellers can use to promote and advertise their products:</p> <ul><li><b>Promoted Listings</b> is an eBay ad service that lets sellers set up <i>ad campaigns </i> for the products they want to promote. eBay displays the ads in search results and in other marketing modules as <b>SPONSORED</b> listings. If an item in a Promoted Listings campaign sells, the seller is assessed a Promoted Listings fee, which is a seller-specified percentage applied to the sales price. For complete details, see <a href=\"/api-docs/sell/static/marketing/promoted-listings.html\">Promoted Listings</a>.</li>  <li><b>Promotions Manager</b> gives sellers a way to offer discounts on specific items as a way to attract buyers to their inventory. Sellers can set up discounts (such as \"20% off\" and other types of offers) on specific items or on an entire customer order. To further attract buyers, eBay prominently displays promotion <i>teasers</i> throughout buyer flows. For complete details, see <a href=\"/api-docs/sell/static/marketing/promotions-manager.html\">Promotions Manager</a>.</li></ul>  <p><b>Marketing reports</b>, on both the Promoted Listings and Promotions Manager platforms, give sellers information that shows the effectiveness of their marketing strategies. The data gives sellers the ability to review and fine tune their marketing efforts.</p> <p class=\"tablenote\"><b>Important!</b> Sellers must have an active eBay Store subscription, and they must accept the <b>Terms and Conditions</b> before they can make requests to these APIs in the Production environment. There are also site-specific listings requirements and restrictions associated with these marketing tools, as listed in the \"requirements and restrictions\" sections for <a href=\"/api-docs/sell/marketing/static/overview.html#PL-requirements\">Promoted Listings</a> and <a href=\"/api-docs/sell/marketing/static/overview.html#PM-requirements\">Promotions Manager</a>.</p> <p>The table below lists all the Marketing API calls grouped by resource.</p>  # noqa: E501

    OpenAPI spec version: v1.10.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ReportTask(object):
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
        'campaign_ids': 'list[str]',
        'date_from': 'str',
        'date_to': 'str',
        'dimensions': 'list[Dimension]',
        'inventory_references': 'list[InventoryReference]',
        'listing_ids': 'list[str]',
        'marketplace_id': 'str',
        'metric_keys': 'list[str]',
        'report_expiration_date': 'str',
        'report_format': 'str',
        'report_href': 'str',
        'report_id': 'str',
        'report_name': 'str',
        'report_task_completion_date': 'str',
        'report_task_creation_date': 'str',
        'report_task_expected_completion_date': 'str',
        'report_task_id': 'str',
        'report_task_status': 'str',
        'report_task_status_message': 'str',
        'report_type': 'str'
    }

    attribute_map = {
        'campaign_ids': 'campaignIds',
        'date_from': 'dateFrom',
        'date_to': 'dateTo',
        'dimensions': 'dimensions',
        'inventory_references': 'inventoryReferences',
        'listing_ids': 'listingIds',
        'marketplace_id': 'marketplaceId',
        'metric_keys': 'metricKeys',
        'report_expiration_date': 'reportExpirationDate',
        'report_format': 'reportFormat',
        'report_href': 'reportHref',
        'report_id': 'reportId',
        'report_name': 'reportName',
        'report_task_completion_date': 'reportTaskCompletionDate',
        'report_task_creation_date': 'reportTaskCreationDate',
        'report_task_expected_completion_date': 'reportTaskExpectedCompletionDate',
        'report_task_id': 'reportTaskId',
        'report_task_status': 'reportTaskStatus',
        'report_task_status_message': 'reportTaskStatusMessage',
        'report_type': 'reportType'
    }

    def __init__(self, campaign_ids=None, date_from=None, date_to=None, dimensions=None, inventory_references=None, listing_ids=None, marketplace_id=None, metric_keys=None, report_expiration_date=None, report_format=None, report_href=None, report_id=None, report_name=None, report_task_completion_date=None, report_task_creation_date=None, report_task_expected_completion_date=None, report_task_id=None, report_task_status=None, report_task_status_message=None, report_type=None):  # noqa: E501
        """ReportTask - a model defined in Swagger"""  # noqa: E501
        self._campaign_ids = None
        self._date_from = None
        self._date_to = None
        self._dimensions = None
        self._inventory_references = None
        self._listing_ids = None
        self._marketplace_id = None
        self._metric_keys = None
        self._report_expiration_date = None
        self._report_format = None
        self._report_href = None
        self._report_id = None
        self._report_name = None
        self._report_task_completion_date = None
        self._report_task_creation_date = None
        self._report_task_expected_completion_date = None
        self._report_task_id = None
        self._report_task_status = None
        self._report_task_status_message = None
        self._report_type = None
        self.discriminator = None
        if campaign_ids is not None:
            self.campaign_ids = campaign_ids
        if date_from is not None:
            self.date_from = date_from
        if date_to is not None:
            self.date_to = date_to
        if dimensions is not None:
            self.dimensions = dimensions
        if inventory_references is not None:
            self.inventory_references = inventory_references
        if listing_ids is not None:
            self.listing_ids = listing_ids
        if marketplace_id is not None:
            self.marketplace_id = marketplace_id
        if metric_keys is not None:
            self.metric_keys = metric_keys
        if report_expiration_date is not None:
            self.report_expiration_date = report_expiration_date
        if report_format is not None:
            self.report_format = report_format
        if report_href is not None:
            self.report_href = report_href
        if report_id is not None:
            self.report_id = report_id
        if report_name is not None:
            self.report_name = report_name
        if report_task_completion_date is not None:
            self.report_task_completion_date = report_task_completion_date
        if report_task_creation_date is not None:
            self.report_task_creation_date = report_task_creation_date
        if report_task_expected_completion_date is not None:
            self.report_task_expected_completion_date = report_task_expected_completion_date
        if report_task_id is not None:
            self.report_task_id = report_task_id
        if report_task_status is not None:
            self.report_task_status = report_task_status
        if report_task_status_message is not None:
            self.report_task_status_message = report_task_status_message
        if report_type is not None:
            self.report_type = report_type

    @property
    def campaign_ids(self):
        """Gets the campaign_ids of this ReportTask.  # noqa: E501

        A list of campaign IDs to be included in the report. A campaign ID is a unique eBay-assigned identifier of the campaign that's generated when the campaign is created. Call <b>getCampaigns</b> to return the current campaign IDs for a seller.  <br><br><p class=\"tablenote\"><b>Note: </b> Currently, you can specify only one campaign ID.  # noqa: E501

        :return: The campaign_ids of this ReportTask.  # noqa: E501
        :rtype: list[str]
        """
        return self._campaign_ids

    @campaign_ids.setter
    def campaign_ids(self, campaign_ids):
        """Sets the campaign_ids of this ReportTask.

        A list of campaign IDs to be included in the report. A campaign ID is a unique eBay-assigned identifier of the campaign that's generated when the campaign is created. Call <b>getCampaigns</b> to return the current campaign IDs for a seller.  <br><br><p class=\"tablenote\"><b>Note: </b> Currently, you can specify only one campaign ID.  # noqa: E501

        :param campaign_ids: The campaign_ids of this ReportTask.  # noqa: E501
        :type: list[str]
        """

        self._campaign_ids = campaign_ids

    @property
    def date_from(self):
        """Gets the date_from of this ReportTask.  # noqa: E501

        The date defining the start of the timespan covered by the report, formatted as an <a href=\"https://www.iso.org/iso-8601-date-and-time-format.html\" title=\"https://www.iso.org\" target=\"_blank\">ISO 8601</a> timestamp.  # noqa: E501

        :return: The date_from of this ReportTask.  # noqa: E501
        :rtype: str
        """
        return self._date_from

    @date_from.setter
    def date_from(self, date_from):
        """Sets the date_from of this ReportTask.

        The date defining the start of the timespan covered by the report, formatted as an <a href=\"https://www.iso.org/iso-8601-date-and-time-format.html\" title=\"https://www.iso.org\" target=\"_blank\">ISO 8601</a> timestamp.  # noqa: E501

        :param date_from: The date_from of this ReportTask.  # noqa: E501
        :type: str
        """

        self._date_from = date_from

    @property
    def date_to(self):
        """Gets the date_to of this ReportTask.  # noqa: E501

        The date defining the end of the timespan covered by the report, formatted as an <a href=\"https://www.iso.org/iso-8601-date-and-time-format.html\" title=\"https://www.iso.org\" target=\"_blank\">ISO 8601</a> timestamp.  # noqa: E501

        :return: The date_to of this ReportTask.  # noqa: E501
        :rtype: str
        """
        return self._date_to

    @date_to.setter
    def date_to(self, date_to):
        """Sets the date_to of this ReportTask.

        The date defining the end of the timespan covered by the report, formatted as an <a href=\"https://www.iso.org/iso-8601-date-and-time-format.html\" title=\"https://www.iso.org\" target=\"_blank\">ISO 8601</a> timestamp.  # noqa: E501

        :param date_to: The date_to of this ReportTask.  # noqa: E501
        :type: str
        """

        self._date_to = date_to

    @property
    def dimensions(self):
        """Gets the dimensions of this ReportTask.  # noqa: E501

        A list containing the dimension in the report.  # noqa: E501

        :return: The dimensions of this ReportTask.  # noqa: E501
        :rtype: list[Dimension]
        """
        return self._dimensions

    @dimensions.setter
    def dimensions(self, dimensions):
        """Sets the dimensions of this ReportTask.

        A list containing the dimension in the report.  # noqa: E501

        :param dimensions: The dimensions of this ReportTask.  # noqa: E501
        :type: list[Dimension]
        """

        self._dimensions = dimensions

    @property
    def inventory_references(self):
        """Gets the inventory_references of this ReportTask.  # noqa: E501

        If supplied in the request, this field returns a list of the seller's inventory reference IDs included in the report.  <p>Each item is referenced by a pair of <inventoryRefernceID</b> and <b>inventoryReferenceType</b> values, where an inventory reference ID can be either a seller-defined <b>SKU</b> value or an <b>inventoryItemGroupKey</b>. An <b>inventoryItemGroupKey</b> is seller-defined ID for an inventory item group (a multiple-variation listing), and is created and used by the <a href=\"/api-docs/sell/inventory/resources/methods\">Inventory API</a>.</p>  # noqa: E501

        :return: The inventory_references of this ReportTask.  # noqa: E501
        :rtype: list[InventoryReference]
        """
        return self._inventory_references

    @inventory_references.setter
    def inventory_references(self, inventory_references):
        """Sets the inventory_references of this ReportTask.

        If supplied in the request, this field returns a list of the seller's inventory reference IDs included in the report.  <p>Each item is referenced by a pair of <inventoryRefernceID</b> and <b>inventoryReferenceType</b> values, where an inventory reference ID can be either a seller-defined <b>SKU</b> value or an <b>inventoryItemGroupKey</b>. An <b>inventoryItemGroupKey</b> is seller-defined ID for an inventory item group (a multiple-variation listing), and is created and used by the <a href=\"/api-docs/sell/inventory/resources/methods\">Inventory API</a>.</p>  # noqa: E501

        :param inventory_references: The inventory_references of this ReportTask.  # noqa: E501
        :type: list[InventoryReference]
        """

        self._inventory_references = inventory_references

    @property
    def listing_ids(self):
        """Gets the listing_ids of this ReportTask.  # noqa: E501

        If supplied in the request, this field returns a list of the listing IDs included in the report. A listing ID is an eBay-assigned ID that's generated when a listing is created.  # noqa: E501

        :return: The listing_ids of this ReportTask.  # noqa: E501
        :rtype: list[str]
        """
        return self._listing_ids

    @listing_ids.setter
    def listing_ids(self, listing_ids):
        """Sets the listing_ids of this ReportTask.

        If supplied in the request, this field returns a list of the listing IDs included in the report. A listing ID is an eBay-assigned ID that's generated when a listing is created.  # noqa: E501

        :param listing_ids: The listing_ids of this ReportTask.  # noqa: E501
        :type: list[str]
        """

        self._listing_ids = listing_ids

    @property
    def marketplace_id(self):
        """Gets the marketplace_id of this ReportTask.  # noqa: E501

        The ID of the eBay marketplace used by the report task. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/marketing/types/ba:MarketplaceIdEnum'>eBay API documentation</a>  # noqa: E501

        :return: The marketplace_id of this ReportTask.  # noqa: E501
        :rtype: str
        """
        return self._marketplace_id

    @marketplace_id.setter
    def marketplace_id(self, marketplace_id):
        """Sets the marketplace_id of this ReportTask.

        The ID of the eBay marketplace used by the report task. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/marketing/types/ba:MarketplaceIdEnum'>eBay API documentation</a>  # noqa: E501

        :param marketplace_id: The marketplace_id of this ReportTask.  # noqa: E501
        :type: str
        """

        self._marketplace_id = marketplace_id

    @property
    def metric_keys(self):
        """Gets the metric_keys of this ReportTask.  # noqa: E501

        A list of metrics for the report task.  # noqa: E501

        :return: The metric_keys of this ReportTask.  # noqa: E501
        :rtype: list[str]
        """
        return self._metric_keys

    @metric_keys.setter
    def metric_keys(self, metric_keys):
        """Sets the metric_keys of this ReportTask.

        A list of metrics for the report task.  # noqa: E501

        :param metric_keys: The metric_keys of this ReportTask.  # noqa: E501
        :type: list[str]
        """

        self._metric_keys = metric_keys

    @property
    def report_expiration_date(self):
        """Gets the report_expiration_date of this ReportTask.  # noqa: E501

        The date after which the report is no longer be available. Reports are available for 30 days and you cannot download a report after it has expired.  <br><br><b>Format (UTC): </b> yyyy-MM-ddThh:mm:ss.sssZ  # noqa: E501

        :return: The report_expiration_date of this ReportTask.  # noqa: E501
        :rtype: str
        """
        return self._report_expiration_date

    @report_expiration_date.setter
    def report_expiration_date(self, report_expiration_date):
        """Sets the report_expiration_date of this ReportTask.

        The date after which the report is no longer be available. Reports are available for 30 days and you cannot download a report after it has expired.  <br><br><b>Format (UTC): </b> yyyy-MM-ddThh:mm:ss.sssZ  # noqa: E501

        :param report_expiration_date: The report_expiration_date of this ReportTask.  # noqa: E501
        :type: str
        """

        self._report_expiration_date = report_expiration_date

    @property
    def report_format(self):
        """Gets the report_format of this ReportTask.  # noqa: E501

        Indicates the format of the report. Currently, only <code>TSV_GZIP</code> is supported. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/marketing/types/plr:ReportFormatEnum'>eBay API documentation</a>  # noqa: E501

        :return: The report_format of this ReportTask.  # noqa: E501
        :rtype: str
        """
        return self._report_format

    @report_format.setter
    def report_format(self, report_format):
        """Sets the report_format of this ReportTask.

        Indicates the format of the report. Currently, only <code>TSV_GZIP</code> is supported. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/marketing/types/plr:ReportFormatEnum'>eBay API documentation</a>  # noqa: E501

        :param report_format: The report_format of this ReportTask.  # noqa: E501
        :type: str
        """

        self._report_format = report_format

    @property
    def report_href(self):
        """Gets the report_href of this ReportTask.  # noqa: E501

        The URL of the generated report, which can be used to download the report once it has been generated.  # noqa: E501

        :return: The report_href of this ReportTask.  # noqa: E501
        :rtype: str
        """
        return self._report_href

    @report_href.setter
    def report_href(self, report_href):
        """Sets the report_href of this ReportTask.

        The URL of the generated report, which can be used to download the report once it has been generated.  # noqa: E501

        :param report_href: The report_href of this ReportTask.  # noqa: E501
        :type: str
        """

        self._report_href = report_href

    @property
    def report_id(self):
        """Gets the report_id of this ReportTask.  # noqa: E501

        A unique eBay-assigned ID for the report.  # noqa: E501

        :return: The report_id of this ReportTask.  # noqa: E501
        :rtype: str
        """
        return self._report_id

    @report_id.setter
    def report_id(self, report_id):
        """Sets the report_id of this ReportTask.

        A unique eBay-assigned ID for the report.  # noqa: E501

        :param report_id: The report_id of this ReportTask.  # noqa: E501
        :type: str
        """

        self._report_id = report_id

    @property
    def report_name(self):
        """Gets the report_name of this ReportTask.  # noqa: E501

        An eBay-assigned name for the report that's created by the <b>createReportTask</b> call. This name is unique for the seller.  # noqa: E501

        :return: The report_name of this ReportTask.  # noqa: E501
        :rtype: str
        """
        return self._report_name

    @report_name.setter
    def report_name(self, report_name):
        """Sets the report_name of this ReportTask.

        An eBay-assigned name for the report that's created by the <b>createReportTask</b> call. This name is unique for the seller.  # noqa: E501

        :param report_name: The report_name of this ReportTask.  # noqa: E501
        :type: str
        """

        self._report_name = report_name

    @property
    def report_task_completion_date(self):
        """Gets the report_task_completion_date of this ReportTask.  # noqa: E501

        The date the report task completed the report generation.  <br><br><b>Format (UTC): </b> yyyy-MM-ddThh:mm:ss.sssZ  # noqa: E501

        :return: The report_task_completion_date of this ReportTask.  # noqa: E501
        :rtype: str
        """
        return self._report_task_completion_date

    @report_task_completion_date.setter
    def report_task_completion_date(self, report_task_completion_date):
        """Sets the report_task_completion_date of this ReportTask.

        The date the report task completed the report generation.  <br><br><b>Format (UTC): </b> yyyy-MM-ddThh:mm:ss.sssZ  # noqa: E501

        :param report_task_completion_date: The report_task_completion_date of this ReportTask.  # noqa: E501
        :type: str
        """

        self._report_task_completion_date = report_task_completion_date

    @property
    def report_task_creation_date(self):
        """Gets the report_task_creation_date of this ReportTask.  # noqa: E501

        The date the report task was created.  <br><br><b>Format (UTC): </b> yyyy-MM-ddThh:mm:ss.sssZ  # noqa: E501

        :return: The report_task_creation_date of this ReportTask.  # noqa: E501
        :rtype: str
        """
        return self._report_task_creation_date

    @report_task_creation_date.setter
    def report_task_creation_date(self, report_task_creation_date):
        """Sets the report_task_creation_date of this ReportTask.

        The date the report task was created.  <br><br><b>Format (UTC): </b> yyyy-MM-ddThh:mm:ss.sssZ  # noqa: E501

        :param report_task_creation_date: The report_task_creation_date of this ReportTask.  # noqa: E501
        :type: str
        """

        self._report_task_creation_date = report_task_creation_date

    @property
    def report_task_expected_completion_date(self):
        """Gets the report_task_expected_completion_date of this ReportTask.  # noqa: E501

        The date the report task is expected to complete the report generation.  <br><br><b>Format (UTC): </b> yyyy-MM-ddThh:mm:ss.sssZ  # noqa: E501

        :return: The report_task_expected_completion_date of this ReportTask.  # noqa: E501
        :rtype: str
        """
        return self._report_task_expected_completion_date

    @report_task_expected_completion_date.setter
    def report_task_expected_completion_date(self, report_task_expected_completion_date):
        """Sets the report_task_expected_completion_date of this ReportTask.

        The date the report task is expected to complete the report generation.  <br><br><b>Format (UTC): </b> yyyy-MM-ddThh:mm:ss.sssZ  # noqa: E501

        :param report_task_expected_completion_date: The report_task_expected_completion_date of this ReportTask.  # noqa: E501
        :type: str
        """

        self._report_task_expected_completion_date = report_task_expected_completion_date

    @property
    def report_task_id(self):
        """Gets the report_task_id of this ReportTask.  # noqa: E501

        The unique eBay-assigned ID of the report task. This value is generated when the report task is created with a call to <b>createReportTask</b>.  # noqa: E501

        :return: The report_task_id of this ReportTask.  # noqa: E501
        :rtype: str
        """
        return self._report_task_id

    @report_task_id.setter
    def report_task_id(self, report_task_id):
        """Sets the report_task_id of this ReportTask.

        The unique eBay-assigned ID of the report task. This value is generated when the report task is created with a call to <b>createReportTask</b>.  # noqa: E501

        :param report_task_id: The report_task_id of this ReportTask.  # noqa: E501
        :type: str
        """

        self._report_task_id = report_task_id

    @property
    def report_task_status(self):
        """Gets the report_task_status of this ReportTask.  # noqa: E501

        Indicates the current state of the report task. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/marketing/types/plr:TaskStatusEnum'>eBay API documentation</a>  # noqa: E501

        :return: The report_task_status of this ReportTask.  # noqa: E501
        :rtype: str
        """
        return self._report_task_status

    @report_task_status.setter
    def report_task_status(self, report_task_status):
        """Sets the report_task_status of this ReportTask.

        Indicates the current state of the report task. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/marketing/types/plr:TaskStatusEnum'>eBay API documentation</a>  # noqa: E501

        :param report_task_status: The report_task_status of this ReportTask.  # noqa: E501
        :type: str
        """

        self._report_task_status = report_task_status

    @property
    def report_task_status_message(self):
        """Gets the report_task_status_message of this ReportTask.  # noqa: E501

        A status message with additional information about the report task.  # noqa: E501

        :return: The report_task_status_message of this ReportTask.  # noqa: E501
        :rtype: str
        """
        return self._report_task_status_message

    @report_task_status_message.setter
    def report_task_status_message(self, report_task_status_message):
        """Sets the report_task_status_message of this ReportTask.

        A status message with additional information about the report task.  # noqa: E501

        :param report_task_status_message: The report_task_status_message of this ReportTask.  # noqa: E501
        :type: str
        """

        self._report_task_status_message = report_task_status_message

    @property
    def report_type(self):
        """Gets the report_type of this ReportTask.  # noqa: E501

        Indicates type of report associated with the report task. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/marketing/types/plr:ReportTypeEnum'>eBay API documentation</a>  # noqa: E501

        :return: The report_type of this ReportTask.  # noqa: E501
        :rtype: str
        """
        return self._report_type

    @report_type.setter
    def report_type(self, report_type):
        """Sets the report_type of this ReportTask.

        Indicates type of report associated with the report task. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/sell/marketing/types/plr:ReportTypeEnum'>eBay API documentation</a>  # noqa: E501

        :param report_type: The report_type of this ReportTask.  # noqa: E501
        :type: str
        """

        self._report_type = report_type

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
        if issubclass(ReportTask, dict):
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
        if not isinstance(other, ReportTask):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
