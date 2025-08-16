import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "PAYMENTS-1951", "title": "Payments scenario 1951", "data": {"sku": "SKU1951", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON12", "payment": "card", "email": "user1951@example.com", "threshold": 510}},
    {"id": "PAYMENTS-1952", "title": "Payments scenario 1952", "data": {"sku": "SKU1952", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON13", "payment": "card", "email": "user1952@example.com", "threshold": 520}},
    {"id": "PAYMENTS-1953", "title": "Payments scenario 1953", "data": {"sku": "SKU1953", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON14", "payment": "card", "email": "user1953@example.com", "threshold": 530}},
    {"id": "PAYMENTS-1954", "title": "Payments scenario 1954", "data": {"sku": "SKU1954", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON15", "payment": "card", "email": "user1954@example.com", "threshold": 540}},
    {"id": "PAYMENTS-1955", "title": "Payments scenario 1955", "data": {"sku": "SKU1955", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON16", "payment": "card", "email": "user1955@example.com", "threshold": 550}},
    {"id": "PAYMENTS-1956", "title": "Payments scenario 1956", "data": {"sku": "SKU1956", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON17", "payment": "card", "email": "user1956@example.com", "threshold": 560}},
    {"id": "PAYMENTS-1957", "title": "Payments scenario 1957", "data": {"sku": "SKU1957", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON18", "payment": "card", "email": "user1957@example.com", "threshold": 570}},
    {"id": "PAYMENTS-1958", "title": "Payments scenario 1958", "data": {"sku": "SKU1958", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON19", "payment": "card", "email": "user1958@example.com", "threshold": 580}},
    {"id": "PAYMENTS-1959", "title": "Payments scenario 1959", "data": {"sku": "SKU1959", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON20", "payment": "card", "email": "user1959@example.com", "threshold": 590}},
    {"id": "PAYMENTS-1960", "title": "Payments scenario 1960", "data": {"sku": "SKU1960", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON1", "payment": "card", "email": "user1960@example.com", "threshold": 600}},
])
def test_payments(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
