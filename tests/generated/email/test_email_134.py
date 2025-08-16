import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-8021", "title": "Email scenario 8021", "data": {"sku": "SKU8021", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user8021@example.com", "threshold": 210}},
    {"id": "EMAIL-8022", "title": "Email scenario 8022", "data": {"sku": "SKU8022", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user8022@example.com", "threshold": 220}},
    {"id": "EMAIL-8023", "title": "Email scenario 8023", "data": {"sku": "SKU8023", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user8023@example.com", "threshold": 230}},
    {"id": "EMAIL-8024", "title": "Email scenario 8024", "data": {"sku": "SKU8024", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user8024@example.com", "threshold": 240}},
    {"id": "EMAIL-8025", "title": "Email scenario 8025", "data": {"sku": "SKU8025", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user8025@example.com", "threshold": 250}},
    {"id": "EMAIL-8026", "title": "Email scenario 8026", "data": {"sku": "SKU8026", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user8026@example.com", "threshold": 260}},
    {"id": "EMAIL-8027", "title": "Email scenario 8027", "data": {"sku": "SKU8027", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user8027@example.com", "threshold": 270}},
    {"id": "EMAIL-8028", "title": "Email scenario 8028", "data": {"sku": "SKU8028", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user8028@example.com", "threshold": 280}},
    {"id": "EMAIL-8029", "title": "Email scenario 8029", "data": {"sku": "SKU8029", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user8029@example.com", "threshold": 290}},
    {"id": "EMAIL-8030", "title": "Email scenario 8030", "data": {"sku": "SKU8030", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user8030@example.com", "threshold": 300}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
