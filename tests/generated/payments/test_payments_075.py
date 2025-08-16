import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-4471", "title": "Payments scenario 4471", "data": {"sku": "SKU4471", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user4471@example.com", "threshold": 710}},
    {"id": "PAYMENTS-4472", "title": "Payments scenario 4472", "data": {"sku": "SKU4472", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user4472@example.com", "threshold": 720}},
    {"id": "PAYMENTS-4473", "title": "Payments scenario 4473", "data": {"sku": "SKU4473", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user4473@example.com", "threshold": 730}},
    {"id": "PAYMENTS-4474", "title": "Payments scenario 4474", "data": {"sku": "SKU4474", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user4474@example.com", "threshold": 740}},
    {"id": "PAYMENTS-4475", "title": "Payments scenario 4475", "data": {"sku": "SKU4475", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user4475@example.com", "threshold": 750}},
    {"id": "PAYMENTS-4476", "title": "Payments scenario 4476", "data": {"sku": "SKU4476", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user4476@example.com", "threshold": 760}},
    {"id": "PAYMENTS-4477", "title": "Payments scenario 4477", "data": {"sku": "SKU4477", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user4477@example.com", "threshold": 770}},
    {"id": "PAYMENTS-4478", "title": "Payments scenario 4478", "data": {"sku": "SKU4478", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user4478@example.com", "threshold": 780}},
    {"id": "PAYMENTS-4479", "title": "Payments scenario 4479", "data": {"sku": "SKU4479", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user4479@example.com", "threshold": 790}},
    {"id": "PAYMENTS-4480", "title": "Payments scenario 4480", "data": {"sku": "SKU4480", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user4480@example.com", "threshold": 800}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
