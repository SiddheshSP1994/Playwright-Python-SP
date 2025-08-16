import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-1541", "title": "Email scenario 1541", "data": {"sku": "SKU1541", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user1541@example.com", "threshold": 410}},
    {"id": "EMAIL-1542", "title": "Email scenario 1542", "data": {"sku": "SKU1542", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user1542@example.com", "threshold": 420}},
    {"id": "EMAIL-1543", "title": "Email scenario 1543", "data": {"sku": "SKU1543", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user1543@example.com", "threshold": 430}},
    {"id": "EMAIL-1544", "title": "Email scenario 1544", "data": {"sku": "SKU1544", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user1544@example.com", "threshold": 440}},
    {"id": "EMAIL-1545", "title": "Email scenario 1545", "data": {"sku": "SKU1545", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user1545@example.com", "threshold": 450}},
    {"id": "EMAIL-1546", "title": "Email scenario 1546", "data": {"sku": "SKU1546", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user1546@example.com", "threshold": 460}},
    {"id": "EMAIL-1547", "title": "Email scenario 1547", "data": {"sku": "SKU1547", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user1547@example.com", "threshold": 470}},
    {"id": "EMAIL-1548", "title": "Email scenario 1548", "data": {"sku": "SKU1548", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user1548@example.com", "threshold": 480}},
    {"id": "EMAIL-1549", "title": "Email scenario 1549", "data": {"sku": "SKU1549", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user1549@example.com", "threshold": 490}},
    {"id": "EMAIL-1550", "title": "Email scenario 1550", "data": {"sku": "SKU1550", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user1550@example.com", "threshold": 500}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
