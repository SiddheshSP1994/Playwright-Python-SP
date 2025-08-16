import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-7041", "title": "Orders scenario 7041", "data": {"sku": "SKU7041", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user7041@example.com", "threshold": 410}},
    {"id": "ORDERS-7042", "title": "Orders scenario 7042", "data": {"sku": "SKU7042", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user7042@example.com", "threshold": 420}},
    {"id": "ORDERS-7043", "title": "Orders scenario 7043", "data": {"sku": "SKU7043", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user7043@example.com", "threshold": 430}},
    {"id": "ORDERS-7044", "title": "Orders scenario 7044", "data": {"sku": "SKU7044", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user7044@example.com", "threshold": 440}},
    {"id": "ORDERS-7045", "title": "Orders scenario 7045", "data": {"sku": "SKU7045", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user7045@example.com", "threshold": 450}},
    {"id": "ORDERS-7046", "title": "Orders scenario 7046", "data": {"sku": "SKU7046", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user7046@example.com", "threshold": 460}},
    {"id": "ORDERS-7047", "title": "Orders scenario 7047", "data": {"sku": "SKU7047", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user7047@example.com", "threshold": 470}},
    {"id": "ORDERS-7048", "title": "Orders scenario 7048", "data": {"sku": "SKU7048", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user7048@example.com", "threshold": 480}},
    {"id": "ORDERS-7049", "title": "Orders scenario 7049", "data": {"sku": "SKU7049", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user7049@example.com", "threshold": 490}},
    {"id": "ORDERS-7050", "title": "Orders scenario 7050", "data": {"sku": "SKU7050", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user7050@example.com", "threshold": 500}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
