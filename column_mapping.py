COLUMN_MAPPING = {
    "sales": {
        # order
        "ordernumber": "order_id",
        "order_number": "order_id",

        "orderdate": "order_date",
        "order_date": "order_date",

        # customer
        "customer name index": "customer_id",
        "customer_name_index": "customer_id",
        "customer_id": "customer_id",

        # product
        "product description index": "product_id",
        "product_description_index": "product_id",

        # region
        "delivery region index": "region_id",
        "delivery_region_index": "region_id",

        # channel
        "channel": "channel",

        # metrics
        "order quantity": "quantity",
        "order_quantity": "quantity",

        "unit price": "unit_price",
        "unit_price": "unit_price",

        "line total": "revenue",
        "line_total": "revenue",

        "total unit cost": "cost",
        "total_unit_cost": "cost"
    },

    "customers": {
        "customer index": "customer_id",
        "customer_index": "customer_id",

        "customer names": "customer_name",
        "customer_name": "customer_name"
    },

    "products": {
        "index": "product_id",
        "product name": "product_name"
    },

    "regions": {
        "id": "region_id",
        "state": "state",
        "county": "county",
        "median_income": "median_income",
        "population": "population"
    },

    "campaigns": {
        "campaign name": "campaign_name",
        "campaign_start": "start_date",
        "campaign start": "start_date",

        "campaign_end": "end_date",
        "campaign end": "end_date",

        "region": "region",
        "strategy": "strategy",
        "cost": "cost"
    }
}