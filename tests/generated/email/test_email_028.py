import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-1661", "title": "Email scenario 1661", "data": {"sku": "SKU1661", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user1661@example.com", "threshold": 610}},
    {"id": "EMAIL-1662", "title": "Email scenario 1662", "data": {"sku": "SKU1662", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user1662@example.com", "threshold": 620}},
    {"id": "EMAIL-1663", "title": "Email scenario 1663", "data": {"sku": "SKU1663", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user1663@example.com", "threshold": 630}},
    {"id": "EMAIL-1664", "title": "Email scenario 1664", "data": {"sku": "SKU1664", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user1664@example.com", "threshold": 640}},
    {"id": "EMAIL-1665", "title": "Email scenario 1665", "data": {"sku": "SKU1665", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user1665@example.com", "threshold": 650}},
    {"id": "EMAIL-1666", "title": "Email scenario 1666", "data": {"sku": "SKU1666", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user1666@example.com", "threshold": 660}},
    {"id": "EMAIL-1667", "title": "Email scenario 1667", "data": {"sku": "SKU1667", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user1667@example.com", "threshold": 670}},
    {"id": "EMAIL-1668", "title": "Email scenario 1668", "data": {"sku": "SKU1668", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user1668@example.com", "threshold": 680}},
    {"id": "EMAIL-1669", "title": "Email scenario 1669", "data": {"sku": "SKU1669", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user1669@example.com", "threshold": 690}},
    {"id": "EMAIL-1670", "title": "Email scenario 1670", "data": {"sku": "SKU1670", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user1670@example.com", "threshold": 700}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
