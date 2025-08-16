import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-4041", "title": "Orders scenario 4041", "data": {"sku": "SKU4041", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user4041@example.com", "threshold": 410}},
    {"id": "ORDERS-4042", "title": "Orders scenario 4042", "data": {"sku": "SKU4042", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user4042@example.com", "threshold": 420}},
    {"id": "ORDERS-4043", "title": "Orders scenario 4043", "data": {"sku": "SKU4043", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user4043@example.com", "threshold": 430}},
    {"id": "ORDERS-4044", "title": "Orders scenario 4044", "data": {"sku": "SKU4044", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user4044@example.com", "threshold": 440}},
    {"id": "ORDERS-4045", "title": "Orders scenario 4045", "data": {"sku": "SKU4045", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user4045@example.com", "threshold": 450}},
    {"id": "ORDERS-4046", "title": "Orders scenario 4046", "data": {"sku": "SKU4046", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user4046@example.com", "threshold": 460}},
    {"id": "ORDERS-4047", "title": "Orders scenario 4047", "data": {"sku": "SKU4047", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user4047@example.com", "threshold": 470}},
    {"id": "ORDERS-4048", "title": "Orders scenario 4048", "data": {"sku": "SKU4048", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user4048@example.com", "threshold": 480}},
    {"id": "ORDERS-4049", "title": "Orders scenario 4049", "data": {"sku": "SKU4049", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user4049@example.com", "threshold": 490}},
    {"id": "ORDERS-4050", "title": "Orders scenario 4050", "data": {"sku": "SKU4050", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user4050@example.com", "threshold": 500}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
