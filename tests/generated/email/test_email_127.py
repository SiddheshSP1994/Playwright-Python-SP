import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-7601", "title": "Email scenario 7601", "data": {"sku": "SKU7601", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user7601@example.com", "threshold": 10}},
    {"id": "EMAIL-7602", "title": "Email scenario 7602", "data": {"sku": "SKU7602", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user7602@example.com", "threshold": 20}},
    {"id": "EMAIL-7603", "title": "Email scenario 7603", "data": {"sku": "SKU7603", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user7603@example.com", "threshold": 30}},
    {"id": "EMAIL-7604", "title": "Email scenario 7604", "data": {"sku": "SKU7604", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user7604@example.com", "threshold": 40}},
    {"id": "EMAIL-7605", "title": "Email scenario 7605", "data": {"sku": "SKU7605", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user7605@example.com", "threshold": 50}},
    {"id": "EMAIL-7606", "title": "Email scenario 7606", "data": {"sku": "SKU7606", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user7606@example.com", "threshold": 60}},
    {"id": "EMAIL-7607", "title": "Email scenario 7607", "data": {"sku": "SKU7607", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user7607@example.com", "threshold": 70}},
    {"id": "EMAIL-7608", "title": "Email scenario 7608", "data": {"sku": "SKU7608", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user7608@example.com", "threshold": 80}},
    {"id": "EMAIL-7609", "title": "Email scenario 7609", "data": {"sku": "SKU7609", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user7609@example.com", "threshold": 90}},
    {"id": "EMAIL-7610", "title": "Email scenario 7610", "data": {"sku": "SKU7610", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user7610@example.com", "threshold": 100}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
