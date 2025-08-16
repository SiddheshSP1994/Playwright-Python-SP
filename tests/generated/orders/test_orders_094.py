import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-5601", "title": "Orders scenario 5601", "data": {"sku": "SKU5601", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user5601@example.com", "threshold": 10}},
    {"id": "ORDERS-5602", "title": "Orders scenario 5602", "data": {"sku": "SKU5602", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user5602@example.com", "threshold": 20}},
    {"id": "ORDERS-5603", "title": "Orders scenario 5603", "data": {"sku": "SKU5603", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user5603@example.com", "threshold": 30}},
    {"id": "ORDERS-5604", "title": "Orders scenario 5604", "data": {"sku": "SKU5604", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user5604@example.com", "threshold": 40}},
    {"id": "ORDERS-5605", "title": "Orders scenario 5605", "data": {"sku": "SKU5605", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user5605@example.com", "threshold": 50}},
    {"id": "ORDERS-5606", "title": "Orders scenario 5606", "data": {"sku": "SKU5606", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user5606@example.com", "threshold": 60}},
    {"id": "ORDERS-5607", "title": "Orders scenario 5607", "data": {"sku": "SKU5607", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user5607@example.com", "threshold": 70}},
    {"id": "ORDERS-5608", "title": "Orders scenario 5608", "data": {"sku": "SKU5608", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user5608@example.com", "threshold": 80}},
    {"id": "ORDERS-5609", "title": "Orders scenario 5609", "data": {"sku": "SKU5609", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user5609@example.com", "threshold": 90}},
    {"id": "ORDERS-5610", "title": "Orders scenario 5610", "data": {"sku": "SKU5610", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user5610@example.com", "threshold": 100}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
