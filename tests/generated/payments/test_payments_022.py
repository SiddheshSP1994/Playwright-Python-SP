import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-1291", "title": "Payments scenario 1291", "data": {"sku": "SKU1291", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user1291@example.com", "threshold": 910}},
    {"id": "PAYMENTS-1292", "title": "Payments scenario 1292", "data": {"sku": "SKU1292", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user1292@example.com", "threshold": 920}},
    {"id": "PAYMENTS-1293", "title": "Payments scenario 1293", "data": {"sku": "SKU1293", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user1293@example.com", "threshold": 930}},
    {"id": "PAYMENTS-1294", "title": "Payments scenario 1294", "data": {"sku": "SKU1294", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user1294@example.com", "threshold": 940}},
    {"id": "PAYMENTS-1295", "title": "Payments scenario 1295", "data": {"sku": "SKU1295", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user1295@example.com", "threshold": 950}},
    {"id": "PAYMENTS-1296", "title": "Payments scenario 1296", "data": {"sku": "SKU1296", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user1296@example.com", "threshold": 960}},
    {"id": "PAYMENTS-1297", "title": "Payments scenario 1297", "data": {"sku": "SKU1297", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user1297@example.com", "threshold": 970}},
    {"id": "PAYMENTS-1298", "title": "Payments scenario 1298", "data": {"sku": "SKU1298", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user1298@example.com", "threshold": 980}},
    {"id": "PAYMENTS-1299", "title": "Payments scenario 1299", "data": {"sku": "SKU1299", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user1299@example.com", "threshold": 990}},
    {"id": "PAYMENTS-1300", "title": "Payments scenario 1300", "data": {"sku": "SKU1300", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user1300@example.com", "threshold": 0}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
