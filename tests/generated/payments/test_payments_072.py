import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-4291", "title": "Payments scenario 4291", "data": {"sku": "SKU4291", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user4291@example.com", "threshold": 910}},
    {"id": "PAYMENTS-4292", "title": "Payments scenario 4292", "data": {"sku": "SKU4292", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user4292@example.com", "threshold": 920}},
    {"id": "PAYMENTS-4293", "title": "Payments scenario 4293", "data": {"sku": "SKU4293", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user4293@example.com", "threshold": 930}},
    {"id": "PAYMENTS-4294", "title": "Payments scenario 4294", "data": {"sku": "SKU4294", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user4294@example.com", "threshold": 940}},
    {"id": "PAYMENTS-4295", "title": "Payments scenario 4295", "data": {"sku": "SKU4295", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user4295@example.com", "threshold": 950}},
    {"id": "PAYMENTS-4296", "title": "Payments scenario 4296", "data": {"sku": "SKU4296", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user4296@example.com", "threshold": 960}},
    {"id": "PAYMENTS-4297", "title": "Payments scenario 4297", "data": {"sku": "SKU4297", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user4297@example.com", "threshold": 970}},
    {"id": "PAYMENTS-4298", "title": "Payments scenario 4298", "data": {"sku": "SKU4298", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user4298@example.com", "threshold": 980}},
    {"id": "PAYMENTS-4299", "title": "Payments scenario 4299", "data": {"sku": "SKU4299", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user4299@example.com", "threshold": 990}},
    {"id": "PAYMENTS-4300", "title": "Payments scenario 4300", "data": {"sku": "SKU4300", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user4300@example.com", "threshold": 0}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
