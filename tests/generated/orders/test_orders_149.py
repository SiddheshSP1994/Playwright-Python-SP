import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-8901", "title": "Orders scenario 8901", "data": {"sku": "SKU8901", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user8901@example.com", "threshold": 10}},
    {"id": "ORDERS-8902", "title": "Orders scenario 8902", "data": {"sku": "SKU8902", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user8902@example.com", "threshold": 20}},
    {"id": "ORDERS-8903", "title": "Orders scenario 8903", "data": {"sku": "SKU8903", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user8903@example.com", "threshold": 30}},
    {"id": "ORDERS-8904", "title": "Orders scenario 8904", "data": {"sku": "SKU8904", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user8904@example.com", "threshold": 40}},
    {"id": "ORDERS-8905", "title": "Orders scenario 8905", "data": {"sku": "SKU8905", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user8905@example.com", "threshold": 50}},
    {"id": "ORDERS-8906", "title": "Orders scenario 8906", "data": {"sku": "SKU8906", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user8906@example.com", "threshold": 60}},
    {"id": "ORDERS-8907", "title": "Orders scenario 8907", "data": {"sku": "SKU8907", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user8907@example.com", "threshold": 70}},
    {"id": "ORDERS-8908", "title": "Orders scenario 8908", "data": {"sku": "SKU8908", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user8908@example.com", "threshold": 80}},
    {"id": "ORDERS-8909", "title": "Orders scenario 8909", "data": {"sku": "SKU8909", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user8909@example.com", "threshold": 90}},
    {"id": "ORDERS-8910", "title": "Orders scenario 8910", "data": {"sku": "SKU8910", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user8910@example.com", "threshold": 100}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
