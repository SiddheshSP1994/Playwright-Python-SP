import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-4581", "title": "Orders scenario 4581", "data": {"sku": "SKU4581", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user4581@example.com", "threshold": 810}},
    {"id": "ORDERS-4582", "title": "Orders scenario 4582", "data": {"sku": "SKU4582", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user4582@example.com", "threshold": 820}},
    {"id": "ORDERS-4583", "title": "Orders scenario 4583", "data": {"sku": "SKU4583", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user4583@example.com", "threshold": 830}},
    {"id": "ORDERS-4584", "title": "Orders scenario 4584", "data": {"sku": "SKU4584", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user4584@example.com", "threshold": 840}},
    {"id": "ORDERS-4585", "title": "Orders scenario 4585", "data": {"sku": "SKU4585", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user4585@example.com", "threshold": 850}},
    {"id": "ORDERS-4586", "title": "Orders scenario 4586", "data": {"sku": "SKU4586", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user4586@example.com", "threshold": 860}},
    {"id": "ORDERS-4587", "title": "Orders scenario 4587", "data": {"sku": "SKU4587", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user4587@example.com", "threshold": 870}},
    {"id": "ORDERS-4588", "title": "Orders scenario 4588", "data": {"sku": "SKU4588", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user4588@example.com", "threshold": 880}},
    {"id": "ORDERS-4589", "title": "Orders scenario 4589", "data": {"sku": "SKU4589", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user4589@example.com", "threshold": 890}},
    {"id": "ORDERS-4590", "title": "Orders scenario 4590", "data": {"sku": "SKU4590", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user4590@example.com", "threshold": 900}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
