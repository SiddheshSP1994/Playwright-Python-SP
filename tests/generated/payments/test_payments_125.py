import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-7471", "title": "Payments scenario 7471", "data": {"sku": "SKU7471", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user7471@example.com", "threshold": 710}},
    {"id": "PAYMENTS-7472", "title": "Payments scenario 7472", "data": {"sku": "SKU7472", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user7472@example.com", "threshold": 720}},
    {"id": "PAYMENTS-7473", "title": "Payments scenario 7473", "data": {"sku": "SKU7473", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user7473@example.com", "threshold": 730}},
    {"id": "PAYMENTS-7474", "title": "Payments scenario 7474", "data": {"sku": "SKU7474", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user7474@example.com", "threshold": 740}},
    {"id": "PAYMENTS-7475", "title": "Payments scenario 7475", "data": {"sku": "SKU7475", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user7475@example.com", "threshold": 750}},
    {"id": "PAYMENTS-7476", "title": "Payments scenario 7476", "data": {"sku": "SKU7476", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user7476@example.com", "threshold": 760}},
    {"id": "PAYMENTS-7477", "title": "Payments scenario 7477", "data": {"sku": "SKU7477", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user7477@example.com", "threshold": 770}},
    {"id": "PAYMENTS-7478", "title": "Payments scenario 7478", "data": {"sku": "SKU7478", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user7478@example.com", "threshold": 780}},
    {"id": "PAYMENTS-7479", "title": "Payments scenario 7479", "data": {"sku": "SKU7479", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user7479@example.com", "threshold": 790}},
    {"id": "PAYMENTS-7480", "title": "Payments scenario 7480", "data": {"sku": "SKU7480", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user7480@example.com", "threshold": 800}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
