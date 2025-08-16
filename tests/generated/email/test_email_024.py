import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-1421", "title": "Email scenario 1421", "data": {"sku": "SKU1421", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user1421@example.com", "threshold": 210}},
    {"id": "EMAIL-1422", "title": "Email scenario 1422", "data": {"sku": "SKU1422", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user1422@example.com", "threshold": 220}},
    {"id": "EMAIL-1423", "title": "Email scenario 1423", "data": {"sku": "SKU1423", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user1423@example.com", "threshold": 230}},
    {"id": "EMAIL-1424", "title": "Email scenario 1424", "data": {"sku": "SKU1424", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user1424@example.com", "threshold": 240}},
    {"id": "EMAIL-1425", "title": "Email scenario 1425", "data": {"sku": "SKU1425", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user1425@example.com", "threshold": 250}},
    {"id": "EMAIL-1426", "title": "Email scenario 1426", "data": {"sku": "SKU1426", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user1426@example.com", "threshold": 260}},
    {"id": "EMAIL-1427", "title": "Email scenario 1427", "data": {"sku": "SKU1427", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user1427@example.com", "threshold": 270}},
    {"id": "EMAIL-1428", "title": "Email scenario 1428", "data": {"sku": "SKU1428", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user1428@example.com", "threshold": 280}},
    {"id": "EMAIL-1429", "title": "Email scenario 1429", "data": {"sku": "SKU1429", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user1429@example.com", "threshold": 290}},
    {"id": "EMAIL-1430", "title": "Email scenario 1430", "data": {"sku": "SKU1430", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user1430@example.com", "threshold": 300}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
