import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-5921", "title": "Email scenario 5921", "data": {"sku": "SKU5921", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user5921@example.com", "threshold": 210}},
    {"id": "EMAIL-5922", "title": "Email scenario 5922", "data": {"sku": "SKU5922", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user5922@example.com", "threshold": 220}},
    {"id": "EMAIL-5923", "title": "Email scenario 5923", "data": {"sku": "SKU5923", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user5923@example.com", "threshold": 230}},
    {"id": "EMAIL-5924", "title": "Email scenario 5924", "data": {"sku": "SKU5924", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user5924@example.com", "threshold": 240}},
    {"id": "EMAIL-5925", "title": "Email scenario 5925", "data": {"sku": "SKU5925", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user5925@example.com", "threshold": 250}},
    {"id": "EMAIL-5926", "title": "Email scenario 5926", "data": {"sku": "SKU5926", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user5926@example.com", "threshold": 260}},
    {"id": "EMAIL-5927", "title": "Email scenario 5927", "data": {"sku": "SKU5927", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user5927@example.com", "threshold": 270}},
    {"id": "EMAIL-5928", "title": "Email scenario 5928", "data": {"sku": "SKU5928", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user5928@example.com", "threshold": 280}},
    {"id": "EMAIL-5929", "title": "Email scenario 5929", "data": {"sku": "SKU5929", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user5929@example.com", "threshold": 290}},
    {"id": "EMAIL-5930", "title": "Email scenario 5930", "data": {"sku": "SKU5930", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user5930@example.com", "threshold": 300}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
