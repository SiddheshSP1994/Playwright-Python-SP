import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-4521", "title": "Orders scenario 4521", "data": {"sku": "SKU4521", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user4521@example.com", "threshold": 210}},
    {"id": "ORDERS-4522", "title": "Orders scenario 4522", "data": {"sku": "SKU4522", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user4522@example.com", "threshold": 220}},
    {"id": "ORDERS-4523", "title": "Orders scenario 4523", "data": {"sku": "SKU4523", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user4523@example.com", "threshold": 230}},
    {"id": "ORDERS-4524", "title": "Orders scenario 4524", "data": {"sku": "SKU4524", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user4524@example.com", "threshold": 240}},
    {"id": "ORDERS-4525", "title": "Orders scenario 4525", "data": {"sku": "SKU4525", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user4525@example.com", "threshold": 250}},
    {"id": "ORDERS-4526", "title": "Orders scenario 4526", "data": {"sku": "SKU4526", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user4526@example.com", "threshold": 260}},
    {"id": "ORDERS-4527", "title": "Orders scenario 4527", "data": {"sku": "SKU4527", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user4527@example.com", "threshold": 270}},
    {"id": "ORDERS-4528", "title": "Orders scenario 4528", "data": {"sku": "SKU4528", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user4528@example.com", "threshold": 280}},
    {"id": "ORDERS-4529", "title": "Orders scenario 4529", "data": {"sku": "SKU4529", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user4529@example.com", "threshold": 290}},
    {"id": "ORDERS-4530", "title": "Orders scenario 4530", "data": {"sku": "SKU4530", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user4530@example.com", "threshold": 300}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
