import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-2921", "title": "Email scenario 2921", "data": {"sku": "SKU2921", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user2921@example.com", "threshold": 210}},
    {"id": "EMAIL-2922", "title": "Email scenario 2922", "data": {"sku": "SKU2922", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user2922@example.com", "threshold": 220}},
    {"id": "EMAIL-2923", "title": "Email scenario 2923", "data": {"sku": "SKU2923", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user2923@example.com", "threshold": 230}},
    {"id": "EMAIL-2924", "title": "Email scenario 2924", "data": {"sku": "SKU2924", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user2924@example.com", "threshold": 240}},
    {"id": "EMAIL-2925", "title": "Email scenario 2925", "data": {"sku": "SKU2925", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user2925@example.com", "threshold": 250}},
    {"id": "EMAIL-2926", "title": "Email scenario 2926", "data": {"sku": "SKU2926", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user2926@example.com", "threshold": 260}},
    {"id": "EMAIL-2927", "title": "Email scenario 2927", "data": {"sku": "SKU2927", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user2927@example.com", "threshold": 270}},
    {"id": "EMAIL-2928", "title": "Email scenario 2928", "data": {"sku": "SKU2928", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user2928@example.com", "threshold": 280}},
    {"id": "EMAIL-2929", "title": "Email scenario 2929", "data": {"sku": "SKU2929", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user2929@example.com", "threshold": 290}},
    {"id": "EMAIL-2930", "title": "Email scenario 2930", "data": {"sku": "SKU2930", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user2930@example.com", "threshold": 300}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
