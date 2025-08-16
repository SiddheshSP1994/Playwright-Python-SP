import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-5121", "title": "Orders scenario 5121", "data": {"sku": "SKU5121", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user5121@example.com", "threshold": 210}},
    {"id": "ORDERS-5122", "title": "Orders scenario 5122", "data": {"sku": "SKU5122", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user5122@example.com", "threshold": 220}},
    {"id": "ORDERS-5123", "title": "Orders scenario 5123", "data": {"sku": "SKU5123", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user5123@example.com", "threshold": 230}},
    {"id": "ORDERS-5124", "title": "Orders scenario 5124", "data": {"sku": "SKU5124", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user5124@example.com", "threshold": 240}},
    {"id": "ORDERS-5125", "title": "Orders scenario 5125", "data": {"sku": "SKU5125", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user5125@example.com", "threshold": 250}},
    {"id": "ORDERS-5126", "title": "Orders scenario 5126", "data": {"sku": "SKU5126", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user5126@example.com", "threshold": 260}},
    {"id": "ORDERS-5127", "title": "Orders scenario 5127", "data": {"sku": "SKU5127", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user5127@example.com", "threshold": 270}},
    {"id": "ORDERS-5128", "title": "Orders scenario 5128", "data": {"sku": "SKU5128", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user5128@example.com", "threshold": 280}},
    {"id": "ORDERS-5129", "title": "Orders scenario 5129", "data": {"sku": "SKU5129", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user5129@example.com", "threshold": 290}},
    {"id": "ORDERS-5130", "title": "Orders scenario 5130", "data": {"sku": "SKU5130", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user5130@example.com", "threshold": 300}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
