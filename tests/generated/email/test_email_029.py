import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-1721", "title": "Email scenario 1721", "data": {"sku": "SKU1721", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user1721@example.com", "threshold": 210}},
    {"id": "EMAIL-1722", "title": "Email scenario 1722", "data": {"sku": "SKU1722", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user1722@example.com", "threshold": 220}},
    {"id": "EMAIL-1723", "title": "Email scenario 1723", "data": {"sku": "SKU1723", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user1723@example.com", "threshold": 230}},
    {"id": "EMAIL-1724", "title": "Email scenario 1724", "data": {"sku": "SKU1724", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user1724@example.com", "threshold": 240}},
    {"id": "EMAIL-1725", "title": "Email scenario 1725", "data": {"sku": "SKU1725", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user1725@example.com", "threshold": 250}},
    {"id": "EMAIL-1726", "title": "Email scenario 1726", "data": {"sku": "SKU1726", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user1726@example.com", "threshold": 260}},
    {"id": "EMAIL-1727", "title": "Email scenario 1727", "data": {"sku": "SKU1727", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user1727@example.com", "threshold": 270}},
    {"id": "EMAIL-1728", "title": "Email scenario 1728", "data": {"sku": "SKU1728", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user1728@example.com", "threshold": 280}},
    {"id": "EMAIL-1729", "title": "Email scenario 1729", "data": {"sku": "SKU1729", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user1729@example.com", "threshold": 290}},
    {"id": "EMAIL-1730", "title": "Email scenario 1730", "data": {"sku": "SKU1730", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user1730@example.com", "threshold": 300}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
