import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-1891", "title": "Payments scenario 1891", "data": {"sku": "SKU1891", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user1891@example.com", "threshold": 910}},
    {"id": "PAYMENTS-1892", "title": "Payments scenario 1892", "data": {"sku": "SKU1892", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user1892@example.com", "threshold": 920}},
    {"id": "PAYMENTS-1893", "title": "Payments scenario 1893", "data": {"sku": "SKU1893", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user1893@example.com", "threshold": 930}},
    {"id": "PAYMENTS-1894", "title": "Payments scenario 1894", "data": {"sku": "SKU1894", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user1894@example.com", "threshold": 940}},
    {"id": "PAYMENTS-1895", "title": "Payments scenario 1895", "data": {"sku": "SKU1895", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user1895@example.com", "threshold": 950}},
    {"id": "PAYMENTS-1896", "title": "Payments scenario 1896", "data": {"sku": "SKU1896", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user1896@example.com", "threshold": 960}},
    {"id": "PAYMENTS-1897", "title": "Payments scenario 1897", "data": {"sku": "SKU1897", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user1897@example.com", "threshold": 970}},
    {"id": "PAYMENTS-1898", "title": "Payments scenario 1898", "data": {"sku": "SKU1898", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user1898@example.com", "threshold": 980}},
    {"id": "PAYMENTS-1899", "title": "Payments scenario 1899", "data": {"sku": "SKU1899", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user1899@example.com", "threshold": 990}},
    {"id": "PAYMENTS-1900", "title": "Payments scenario 1900", "data": {"sku": "SKU1900", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user1900@example.com", "threshold": 0}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
