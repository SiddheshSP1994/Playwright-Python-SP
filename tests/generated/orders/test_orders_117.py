import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-6981", "title": "Orders scenario 6981", "data": {"sku": "SKU6981", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user6981@example.com", "threshold": 810}},
    {"id": "ORDERS-6982", "title": "Orders scenario 6982", "data": {"sku": "SKU6982", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user6982@example.com", "threshold": 820}},
    {"id": "ORDERS-6983", "title": "Orders scenario 6983", "data": {"sku": "SKU6983", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user6983@example.com", "threshold": 830}},
    {"id": "ORDERS-6984", "title": "Orders scenario 6984", "data": {"sku": "SKU6984", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user6984@example.com", "threshold": 840}},
    {"id": "ORDERS-6985", "title": "Orders scenario 6985", "data": {"sku": "SKU6985", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user6985@example.com", "threshold": 850}},
    {"id": "ORDERS-6986", "title": "Orders scenario 6986", "data": {"sku": "SKU6986", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user6986@example.com", "threshold": 860}},
    {"id": "ORDERS-6987", "title": "Orders scenario 6987", "data": {"sku": "SKU6987", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user6987@example.com", "threshold": 870}},
    {"id": "ORDERS-6988", "title": "Orders scenario 6988", "data": {"sku": "SKU6988", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user6988@example.com", "threshold": 880}},
    {"id": "ORDERS-6989", "title": "Orders scenario 6989", "data": {"sku": "SKU6989", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user6989@example.com", "threshold": 890}},
    {"id": "ORDERS-6990", "title": "Orders scenario 6990", "data": {"sku": "SKU6990", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user6990@example.com", "threshold": 900}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
