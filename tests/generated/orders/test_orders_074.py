import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "ORDERS-4401", "title": "Orders scenario 4401", "data": {"sku": "SKU4401", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user4401@example.com", "threshold": 10}},
    {"id": "ORDERS-4402", "title": "Orders scenario 4402", "data": {"sku": "SKU4402", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user4402@example.com", "threshold": 20}},
    {"id": "ORDERS-4403", "title": "Orders scenario 4403", "data": {"sku": "SKU4403", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user4403@example.com", "threshold": 30}},
    {"id": "ORDERS-4404", "title": "Orders scenario 4404", "data": {"sku": "SKU4404", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user4404@example.com", "threshold": 40}},
    {"id": "ORDERS-4405", "title": "Orders scenario 4405", "data": {"sku": "SKU4405", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user4405@example.com", "threshold": 50}},
    {"id": "ORDERS-4406", "title": "Orders scenario 4406", "data": {"sku": "SKU4406", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user4406@example.com", "threshold": 60}},
    {"id": "ORDERS-4407", "title": "Orders scenario 4407", "data": {"sku": "SKU4407", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user4407@example.com", "threshold": 70}},
    {"id": "ORDERS-4408", "title": "Orders scenario 4408", "data": {"sku": "SKU4408", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user4408@example.com", "threshold": 80}},
    {"id": "ORDERS-4409", "title": "Orders scenario 4409", "data": {"sku": "SKU4409", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user4409@example.com", "threshold": 90}},
    {"id": "ORDERS-4410", "title": "Orders scenario 4410", "data": {"sku": "SKU4410", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user4410@example.com", "threshold": 100}},
])
def test_orders(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
