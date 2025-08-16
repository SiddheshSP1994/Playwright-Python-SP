import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-5901", "title": "Orders scenario 5901", "data": {"sku": "SKU5901", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user5901@example.com", "threshold": 10}},
    {"id": "ORDERS-5902", "title": "Orders scenario 5902", "data": {"sku": "SKU5902", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user5902@example.com", "threshold": 20}},
    {"id": "ORDERS-5903", "title": "Orders scenario 5903", "data": {"sku": "SKU5903", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user5903@example.com", "threshold": 30}},
    {"id": "ORDERS-5904", "title": "Orders scenario 5904", "data": {"sku": "SKU5904", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user5904@example.com", "threshold": 40}},
    {"id": "ORDERS-5905", "title": "Orders scenario 5905", "data": {"sku": "SKU5905", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user5905@example.com", "threshold": 50}},
    {"id": "ORDERS-5906", "title": "Orders scenario 5906", "data": {"sku": "SKU5906", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user5906@example.com", "threshold": 60}},
    {"id": "ORDERS-5907", "title": "Orders scenario 5907", "data": {"sku": "SKU5907", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user5907@example.com", "threshold": 70}},
    {"id": "ORDERS-5908", "title": "Orders scenario 5908", "data": {"sku": "SKU5908", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user5908@example.com", "threshold": 80}},
    {"id": "ORDERS-5909", "title": "Orders scenario 5909", "data": {"sku": "SKU5909", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user5909@example.com", "threshold": 90}},
    {"id": "ORDERS-5910", "title": "Orders scenario 5910", "data": {"sku": "SKU5910", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user5910@example.com", "threshold": 100}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
