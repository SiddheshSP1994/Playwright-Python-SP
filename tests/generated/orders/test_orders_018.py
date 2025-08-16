import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-1041", "title": "Orders scenario 1041", "data": {"sku": "SKU1041", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user1041@example.com", "threshold": 410}},
    {"id": "ORDERS-1042", "title": "Orders scenario 1042", "data": {"sku": "SKU1042", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user1042@example.com", "threshold": 420}},
    {"id": "ORDERS-1043", "title": "Orders scenario 1043", "data": {"sku": "SKU1043", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user1043@example.com", "threshold": 430}},
    {"id": "ORDERS-1044", "title": "Orders scenario 1044", "data": {"sku": "SKU1044", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user1044@example.com", "threshold": 440}},
    {"id": "ORDERS-1045", "title": "Orders scenario 1045", "data": {"sku": "SKU1045", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user1045@example.com", "threshold": 450}},
    {"id": "ORDERS-1046", "title": "Orders scenario 1046", "data": {"sku": "SKU1046", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user1046@example.com", "threshold": 460}},
    {"id": "ORDERS-1047", "title": "Orders scenario 1047", "data": {"sku": "SKU1047", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user1047@example.com", "threshold": 470}},
    {"id": "ORDERS-1048", "title": "Orders scenario 1048", "data": {"sku": "SKU1048", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user1048@example.com", "threshold": 480}},
    {"id": "ORDERS-1049", "title": "Orders scenario 1049", "data": {"sku": "SKU1049", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user1049@example.com", "threshold": 490}},
    {"id": "ORDERS-1050", "title": "Orders scenario 1050", "data": {"sku": "SKU1050", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user1050@example.com", "threshold": 500}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
