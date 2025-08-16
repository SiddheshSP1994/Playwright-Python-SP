import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-1481", "title": "Email scenario 1481", "data": {"sku": "SKU1481", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user1481@example.com", "threshold": 810}},
    {"id": "EMAIL-1482", "title": "Email scenario 1482", "data": {"sku": "SKU1482", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user1482@example.com", "threshold": 820}},
    {"id": "EMAIL-1483", "title": "Email scenario 1483", "data": {"sku": "SKU1483", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user1483@example.com", "threshold": 830}},
    {"id": "EMAIL-1484", "title": "Email scenario 1484", "data": {"sku": "SKU1484", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user1484@example.com", "threshold": 840}},
    {"id": "EMAIL-1485", "title": "Email scenario 1485", "data": {"sku": "SKU1485", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user1485@example.com", "threshold": 850}},
    {"id": "EMAIL-1486", "title": "Email scenario 1486", "data": {"sku": "SKU1486", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user1486@example.com", "threshold": 860}},
    {"id": "EMAIL-1487", "title": "Email scenario 1487", "data": {"sku": "SKU1487", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user1487@example.com", "threshold": 870}},
    {"id": "EMAIL-1488", "title": "Email scenario 1488", "data": {"sku": "SKU1488", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user1488@example.com", "threshold": 880}},
    {"id": "EMAIL-1489", "title": "Email scenario 1489", "data": {"sku": "SKU1489", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user1489@example.com", "threshold": 890}},
    {"id": "EMAIL-1490", "title": "Email scenario 1490", "data": {"sku": "SKU1490", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user1490@example.com", "threshold": 900}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
