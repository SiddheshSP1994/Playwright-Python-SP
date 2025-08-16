import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-8921", "title": "Email scenario 8921", "data": {"sku": "SKU8921", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user8921@example.com", "threshold": 210}},
    {"id": "EMAIL-8922", "title": "Email scenario 8922", "data": {"sku": "SKU8922", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user8922@example.com", "threshold": 220}},
    {"id": "EMAIL-8923", "title": "Email scenario 8923", "data": {"sku": "SKU8923", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user8923@example.com", "threshold": 230}},
    {"id": "EMAIL-8924", "title": "Email scenario 8924", "data": {"sku": "SKU8924", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user8924@example.com", "threshold": 240}},
    {"id": "EMAIL-8925", "title": "Email scenario 8925", "data": {"sku": "SKU8925", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user8925@example.com", "threshold": 250}},
    {"id": "EMAIL-8926", "title": "Email scenario 8926", "data": {"sku": "SKU8926", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user8926@example.com", "threshold": 260}},
    {"id": "EMAIL-8927", "title": "Email scenario 8927", "data": {"sku": "SKU8927", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user8927@example.com", "threshold": 270}},
    {"id": "EMAIL-8928", "title": "Email scenario 8928", "data": {"sku": "SKU8928", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user8928@example.com", "threshold": 280}},
    {"id": "EMAIL-8929", "title": "Email scenario 8929", "data": {"sku": "SKU8929", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user8929@example.com", "threshold": 290}},
    {"id": "EMAIL-8930", "title": "Email scenario 8930", "data": {"sku": "SKU8930", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user8930@example.com", "threshold": 300}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
