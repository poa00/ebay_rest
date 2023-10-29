# coding: utf-8

"""
    Deal API

    <span class=\"tablenote\"><b>Note:</b> This is a <a href=\"https://developer.ebay.com/api-docs/static/versioning.html#limited\" target=\"_blank\"> <img src=\"/cms/img/docs/partners-api.svg\" class=\"legend-icon partners-icon\" title=\"Limited Release\"  alt=\"Limited Release\" />(Limited Release)</a> API available only to select developers approved by business units. For information on how to obtain access to this API in production, see the <a href=\"/../api-docs/buy/static/buy-requirements.html\" target=\"_blank\">Buy APIs Requirements</a>.</span><br /><br />This API allows third-party developers to search for and retrieve details about eBay deals and events, as well as the items associated with those deals and events.  # noqa: E501

    OpenAPI spec version: v1.3.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class EventItem(object):
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
        'additional_images': 'list[Image]',
        'category_ancestor_ids': 'list[str]',
        'category_id': 'str',
        'energy_efficiency_class': 'str',
        'event_id': 'str',
        'image': 'Image',
        'item_affiliate_web_url': 'str',
        'item_group_id': 'str',
        'item_group_type': 'str',
        'item_id': 'str',
        'item_web_url': 'str',
        'legacy_item_id': 'str',
        'marketing_price': 'MarketingPrice',
        'price': 'Amount',
        'qualified_programs': 'list[str]',
        'shipping_options': 'list[ShippingOption]',
        'title': 'str',
        'unit_price': 'Amount',
        'unit_pricing_measure': 'str'
    }

    attribute_map = {
        'additional_images': 'additionalImages',
        'category_ancestor_ids': 'categoryAncestorIds',
        'category_id': 'categoryId',
        'energy_efficiency_class': 'energyEfficiencyClass',
        'event_id': 'eventId',
        'image': 'image',
        'item_affiliate_web_url': 'itemAffiliateWebUrl',
        'item_group_id': 'itemGroupId',
        'item_group_type': 'itemGroupType',
        'item_id': 'itemId',
        'item_web_url': 'itemWebUrl',
        'legacy_item_id': 'legacyItemId',
        'marketing_price': 'marketingPrice',
        'price': 'price',
        'qualified_programs': 'qualifiedPrograms',
        'shipping_options': 'shippingOptions',
        'title': 'title',
        'unit_price': 'unitPrice',
        'unit_pricing_measure': 'unitPricingMeasure'
    }

    def __init__(self, additional_images=None, category_ancestor_ids=None, category_id=None, energy_efficiency_class=None, event_id=None, image=None, item_affiliate_web_url=None, item_group_id=None, item_group_type=None, item_id=None, item_web_url=None, legacy_item_id=None, marketing_price=None, price=None, qualified_programs=None, shipping_options=None, title=None, unit_price=None, unit_pricing_measure=None):  # noqa: E501
        """EventItem - a model defined in Swagger"""  # noqa: E501
        self._additional_images = None
        self._category_ancestor_ids = None
        self._category_id = None
        self._energy_efficiency_class = None
        self._event_id = None
        self._image = None
        self._item_affiliate_web_url = None
        self._item_group_id = None
        self._item_group_type = None
        self._item_id = None
        self._item_web_url = None
        self._legacy_item_id = None
        self._marketing_price = None
        self._price = None
        self._qualified_programs = None
        self._shipping_options = None
        self._title = None
        self._unit_price = None
        self._unit_pricing_measure = None
        self.discriminator = None
        if additional_images is not None:
            self.additional_images = additional_images
        if category_ancestor_ids is not None:
            self.category_ancestor_ids = category_ancestor_ids
        if category_id is not None:
            self.category_id = category_id
        if energy_efficiency_class is not None:
            self.energy_efficiency_class = energy_efficiency_class
        if event_id is not None:
            self.event_id = event_id
        if image is not None:
            self.image = image
        if item_affiliate_web_url is not None:
            self.item_affiliate_web_url = item_affiliate_web_url
        if item_group_id is not None:
            self.item_group_id = item_group_id
        if item_group_type is not None:
            self.item_group_type = item_group_type
        if item_id is not None:
            self.item_id = item_id
        if item_web_url is not None:
            self.item_web_url = item_web_url
        if legacy_item_id is not None:
            self.legacy_item_id = legacy_item_id
        if marketing_price is not None:
            self.marketing_price = marketing_price
        if price is not None:
            self.price = price
        if qualified_programs is not None:
            self.qualified_programs = qualified_programs
        if shipping_options is not None:
            self.shipping_options = shipping_options
        if title is not None:
            self.title = title
        if unit_price is not None:
            self.unit_price = unit_price
        if unit_pricing_measure is not None:
            self.unit_pricing_measure = unit_pricing_measure

    @property
    def additional_images(self):
        """Gets the additional_images of this EventItem.  # noqa: E501

        The additional images for the event item.  # noqa: E501

        :return: The additional_images of this EventItem.  # noqa: E501
        :rtype: list[Image]
        """
        return self._additional_images

    @additional_images.setter
    def additional_images(self, additional_images):
        """Sets the additional_images of this EventItem.

        The additional images for the event item.  # noqa: E501

        :param additional_images: The additional_images of this EventItem.  # noqa: E501
        :type: list[Image]
        """

        self._additional_images = additional_images

    @property
    def category_ancestor_ids(self):
        """Gets the category_ancestor_ids of this EventItem.  # noqa: E501

        The IDs of the ancestors for the primary category.  # noqa: E501

        :return: The category_ancestor_ids of this EventItem.  # noqa: E501
        :rtype: list[str]
        """
        return self._category_ancestor_ids

    @category_ancestor_ids.setter
    def category_ancestor_ids(self, category_ancestor_ids):
        """Sets the category_ancestor_ids of this EventItem.

        The IDs of the ancestors for the primary category.  # noqa: E501

        :param category_ancestor_ids: The category_ancestor_ids of this EventItem.  # noqa: E501
        :type: list[str]
        """

        self._category_ancestor_ids = category_ancestor_ids

    @property
    def category_id(self):
        """Gets the category_id of this EventItem.  # noqa: E501

        The ID of the leaf category for the event item. A leaf category is the lowest level in a category and has no children.  # noqa: E501

        :return: The category_id of this EventItem.  # noqa: E501
        :rtype: str
        """
        return self._category_id

    @category_id.setter
    def category_id(self, category_id):
        """Sets the category_id of this EventItem.

        The ID of the leaf category for the event item. A leaf category is the lowest level in a category and has no children.  # noqa: E501

        :param category_id: The category_id of this EventItem.  # noqa: E501
        :type: str
        """

        self._category_id = category_id

    @property
    def energy_efficiency_class(self):
        """Gets the energy_efficiency_class of this EventItem.  # noqa: E501

        A string value specifying the Energy Efficiency class.  # noqa: E501

        :return: The energy_efficiency_class of this EventItem.  # noqa: E501
        :rtype: str
        """
        return self._energy_efficiency_class

    @energy_efficiency_class.setter
    def energy_efficiency_class(self, energy_efficiency_class):
        """Sets the energy_efficiency_class of this EventItem.

        A string value specifying the Energy Efficiency class.  # noqa: E501

        :param energy_efficiency_class: The energy_efficiency_class of this EventItem.  # noqa: E501
        :type: str
        """

        self._energy_efficiency_class = energy_efficiency_class

    @property
    def event_id(self):
        """Gets the event_id of this EventItem.  # noqa: E501

        The unique event identifier associated with the item.  # noqa: E501

        :return: The event_id of this EventItem.  # noqa: E501
        :rtype: str
        """
        return self._event_id

    @event_id.setter
    def event_id(self, event_id):
        """Sets the event_id of this EventItem.

        The unique event identifier associated with the item.  # noqa: E501

        :param event_id: The event_id of this EventItem.  # noqa: E501
        :type: str
        """

        self._event_id = event_id

    @property
    def image(self):
        """Gets the image of this EventItem.  # noqa: E501


        :return: The image of this EventItem.  # noqa: E501
        :rtype: Image
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this EventItem.


        :param image: The image of this EventItem.  # noqa: E501
        :type: Image
        """

        self._image = image

    @property
    def item_affiliate_web_url(self):
        """Gets the item_affiliate_web_url of this EventItem.  # noqa: E501

        The item web URL with affiliate attribution.  # noqa: E501

        :return: The item_affiliate_web_url of this EventItem.  # noqa: E501
        :rtype: str
        """
        return self._item_affiliate_web_url

    @item_affiliate_web_url.setter
    def item_affiliate_web_url(self, item_affiliate_web_url):
        """Sets the item_affiliate_web_url of this EventItem.

        The item web URL with affiliate attribution.  # noqa: E501

        :param item_affiliate_web_url: The item_affiliate_web_url of this EventItem.  # noqa: E501
        :type: str
        """

        self._item_affiliate_web_url = item_affiliate_web_url

    @property
    def item_group_id(self):
        """Gets the item_group_id of this EventItem.  # noqa: E501

        The unique identifier for the event item group. This is the parent item ID for the seller-defined variations.<br /><br /><span class=\"tablenote\"><b>Note: </b>This field is returned for multiple-SKU items.</span>  # noqa: E501

        :return: The item_group_id of this EventItem.  # noqa: E501
        :rtype: str
        """
        return self._item_group_id

    @item_group_id.setter
    def item_group_id(self, item_group_id):
        """Sets the item_group_id of this EventItem.

        The unique identifier for the event item group. This is the parent item ID for the seller-defined variations.<br /><br /><span class=\"tablenote\"><b>Note: </b>This field is returned for multiple-SKU items.</span>  # noqa: E501

        :param item_group_id: The item_group_id of this EventItem.  # noqa: E501
        :type: str
        """

        self._item_group_id = item_group_id

    @property
    def item_group_type(self):
        """Gets the item_group_type of this EventItem.  # noqa: E501

        An enumeration value that indicates the type of item group. An item group contains items that have various aspect differences, such as color, size, or storage capacity. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/buy/deal/types/api:ItemGroupTypeEnum'>eBay API documentation</a>  # noqa: E501

        :return: The item_group_type of this EventItem.  # noqa: E501
        :rtype: str
        """
        return self._item_group_type

    @item_group_type.setter
    def item_group_type(self, item_group_type):
        """Sets the item_group_type of this EventItem.

        An enumeration value that indicates the type of item group. An item group contains items that have various aspect differences, such as color, size, or storage capacity. For implementation help, refer to <a href='https://developer.ebay.com/api-docs/buy/deal/types/api:ItemGroupTypeEnum'>eBay API documentation</a>  # noqa: E501

        :param item_group_type: The item_group_type of this EventItem.  # noqa: E501
        :type: str
        """

        self._item_group_type = item_group_type

    @property
    def item_id(self):
        """Gets the item_id of this EventItem.  # noqa: E501

        The unique identifier for the event item.<br /><br /><span class=\"tablenote\"><b>Note: </b>This field is only returned for single-SKU items.</span>  # noqa: E501

        :return: The item_id of this EventItem.  # noqa: E501
        :rtype: str
        """
        return self._item_id

    @item_id.setter
    def item_id(self, item_id):
        """Sets the item_id of this EventItem.

        The unique identifier for the event item.<br /><br /><span class=\"tablenote\"><b>Note: </b>This field is only returned for single-SKU items.</span>  # noqa: E501

        :param item_id: The item_id of this EventItem.  # noqa: E501
        :type: str
        """

        self._item_id = item_id

    @property
    def item_web_url(self):
        """Gets the item_web_url of this EventItem.  # noqa: E501

        The web URL for the event item.  # noqa: E501

        :return: The item_web_url of this EventItem.  # noqa: E501
        :rtype: str
        """
        return self._item_web_url

    @item_web_url.setter
    def item_web_url(self, item_web_url):
        """Sets the item_web_url of this EventItem.

        The web URL for the event item.  # noqa: E501

        :param item_web_url: The item_web_url of this EventItem.  # noqa: E501
        :type: str
        """

        self._item_web_url = item_web_url

    @property
    def legacy_item_id(self):
        """Gets the legacy_item_id of this EventItem.  # noqa: E501

        The legacy item ID associated with the event item.  # noqa: E501

        :return: The legacy_item_id of this EventItem.  # noqa: E501
        :rtype: str
        """
        return self._legacy_item_id

    @legacy_item_id.setter
    def legacy_item_id(self, legacy_item_id):
        """Sets the legacy_item_id of this EventItem.

        The legacy item ID associated with the event item.  # noqa: E501

        :param legacy_item_id: The legacy_item_id of this EventItem.  # noqa: E501
        :type: str
        """

        self._legacy_item_id = legacy_item_id

    @property
    def marketing_price(self):
        """Gets the marketing_price of this EventItem.  # noqa: E501


        :return: The marketing_price of this EventItem.  # noqa: E501
        :rtype: MarketingPrice
        """
        return self._marketing_price

    @marketing_price.setter
    def marketing_price(self, marketing_price):
        """Sets the marketing_price of this EventItem.


        :param marketing_price: The marketing_price of this EventItem.  # noqa: E501
        :type: MarketingPrice
        """

        self._marketing_price = marketing_price

    @property
    def price(self):
        """Gets the price of this EventItem.  # noqa: E501


        :return: The price of this EventItem.  # noqa: E501
        :rtype: Amount
        """
        return self._price

    @price.setter
    def price(self, price):
        """Sets the price of this EventItem.


        :param price: The price of this EventItem.  # noqa: E501
        :type: Amount
        """

        self._price = price

    @property
    def qualified_programs(self):
        """Gets the qualified_programs of this EventItem.  # noqa: E501

        A list of programs applicable to the event item.  # noqa: E501

        :return: The qualified_programs of this EventItem.  # noqa: E501
        :rtype: list[str]
        """
        return self._qualified_programs

    @qualified_programs.setter
    def qualified_programs(self, qualified_programs):
        """Sets the qualified_programs of this EventItem.

        A list of programs applicable to the event item.  # noqa: E501

        :param qualified_programs: The qualified_programs of this EventItem.  # noqa: E501
        :type: list[str]
        """

        self._qualified_programs = qualified_programs

    @property
    def shipping_options(self):
        """Gets the shipping_options of this EventItem.  # noqa: E501

        The cost required to ship the event item.  # noqa: E501

        :return: The shipping_options of this EventItem.  # noqa: E501
        :rtype: list[ShippingOption]
        """
        return self._shipping_options

    @shipping_options.setter
    def shipping_options(self, shipping_options):
        """Sets the shipping_options of this EventItem.

        The cost required to ship the event item.  # noqa: E501

        :param shipping_options: The shipping_options of this EventItem.  # noqa: E501
        :type: list[ShippingOption]
        """

        self._shipping_options = shipping_options

    @property
    def title(self):
        """Gets the title of this EventItem.  # noqa: E501

        The title of the event item.  # noqa: E501

        :return: The title of this EventItem.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this EventItem.

        The title of the event item.  # noqa: E501

        :param title: The title of this EventItem.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def unit_price(self):
        """Gets the unit_price of this EventItem.  # noqa: E501


        :return: The unit_price of this EventItem.  # noqa: E501
        :rtype: Amount
        """
        return self._unit_price

    @unit_price.setter
    def unit_price(self, unit_price):
        """Sets the unit_price of this EventItem.


        :param unit_price: The unit_price of this EventItem.  # noqa: E501
        :type: Amount
        """

        self._unit_price = unit_price

    @property
    def unit_pricing_measure(self):
        """Gets the unit_pricing_measure of this EventItem.  # noqa: E501

        The designation used to specify the quantity of the event item, such as size, weight, volume, and count. This helps buyers compare prices. <br /><br />For example, the following tells the buyer that the item is 7.99 per 100 grams. <br /><br /><code>\"unitPricingMeasure\": \"100g\",<br /> \"unitPrice\": {<br />&nbsp;&nbsp;\"value\": \"7.99\",<br />&nbsp;&nbsp;\"currency\": \"GBP\"</code>  # noqa: E501

        :return: The unit_pricing_measure of this EventItem.  # noqa: E501
        :rtype: str
        """
        return self._unit_pricing_measure

    @unit_pricing_measure.setter
    def unit_pricing_measure(self, unit_pricing_measure):
        """Sets the unit_pricing_measure of this EventItem.

        The designation used to specify the quantity of the event item, such as size, weight, volume, and count. This helps buyers compare prices. <br /><br />For example, the following tells the buyer that the item is 7.99 per 100 grams. <br /><br /><code>\"unitPricingMeasure\": \"100g\",<br /> \"unitPrice\": {<br />&nbsp;&nbsp;\"value\": \"7.99\",<br />&nbsp;&nbsp;\"currency\": \"GBP\"</code>  # noqa: E501

        :param unit_pricing_measure: The unit_pricing_measure of this EventItem.  # noqa: E501
        :type: str
        """

        self._unit_pricing_measure = unit_pricing_measure

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
        if issubclass(EventItem, dict):
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
        if not isinstance(other, EventItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
