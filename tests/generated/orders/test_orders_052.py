import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-3081", "title": "Orders scenario 3081", "data": {"sku": "SKU3081", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user3081@example.com", "threshold": 810}},
    {"id": "ORDERS-3082", "title": "Orders scenario 3082", "data": {"sku": "SKU3082", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user3082@example.com", "threshold": 820}},
    {"id": "ORDERS-3083", "title": "Orders scenario 3083", "data": {"sku": "SKU3083", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user3083@example.com", "threshold": 830}},
    {"id": "ORDERS-3084", "title": "Orders scenario 3084", "data": {"sku": "SKU3084", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user3084@example.com", "threshold": 840}},
    {"id": "ORDERS-3085", "title": "Orders scenario 3085", "data": {"sku": "SKU3085", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user3085@example.com", "threshold": 850}},
    {"id": "ORDERS-3086", "title": "Orders scenario 3086", "data": {"sku": "SKU3086", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user3086@example.com", "threshold": 860}},
    {"id": "ORDERS-3087", "title": "Orders scenario 3087", "data": {"sku": "SKU3087", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user3087@example.com", "threshold": 870}},
    {"id": "ORDERS-3088", "title": "Orders scenario 3088", "data": {"sku": "SKU3088", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user3088@example.com", "threshold": 880}},
    {"id": "ORDERS-3089", "title": "Orders scenario 3089", "data": {"sku": "SKU3089", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user3089@example.com", "threshold": 890}},
    {"id": "ORDERS-3090", "title": "Orders scenario 3090", "data": {"sku": "SKU3090", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user3090@example.com", "threshold": 900}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
