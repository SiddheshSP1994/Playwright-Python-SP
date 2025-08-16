import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-3741", "title": "Orders scenario 3741", "data": {"sku": "SKU3741", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user3741@example.com", "threshold": 410}},
    {"id": "ORDERS-3742", "title": "Orders scenario 3742", "data": {"sku": "SKU3742", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user3742@example.com", "threshold": 420}},
    {"id": "ORDERS-3743", "title": "Orders scenario 3743", "data": {"sku": "SKU3743", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user3743@example.com", "threshold": 430}},
    {"id": "ORDERS-3744", "title": "Orders scenario 3744", "data": {"sku": "SKU3744", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user3744@example.com", "threshold": 440}},
    {"id": "ORDERS-3745", "title": "Orders scenario 3745", "data": {"sku": "SKU3745", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user3745@example.com", "threshold": 450}},
    {"id": "ORDERS-3746", "title": "Orders scenario 3746", "data": {"sku": "SKU3746", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user3746@example.com", "threshold": 460}},
    {"id": "ORDERS-3747", "title": "Orders scenario 3747", "data": {"sku": "SKU3747", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user3747@example.com", "threshold": 470}},
    {"id": "ORDERS-3748", "title": "Orders scenario 3748", "data": {"sku": "SKU3748", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user3748@example.com", "threshold": 480}},
    {"id": "ORDERS-3749", "title": "Orders scenario 3749", "data": {"sku": "SKU3749", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user3749@example.com", "threshold": 490}},
    {"id": "ORDERS-3750", "title": "Orders scenario 3750", "data": {"sku": "SKU3750", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user3750@example.com", "threshold": 500}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
