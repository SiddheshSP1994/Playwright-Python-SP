import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-0221", "title": "Email scenario 221", "data": {"sku": "SKU221", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user221@example.com", "threshold": 210}},
    {"id": "EMAIL-0222", "title": "Email scenario 222", "data": {"sku": "SKU222", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user222@example.com", "threshold": 220}},
    {"id": "EMAIL-0223", "title": "Email scenario 223", "data": {"sku": "SKU223", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user223@example.com", "threshold": 230}},
    {"id": "EMAIL-0224", "title": "Email scenario 224", "data": {"sku": "SKU224", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user224@example.com", "threshold": 240}},
    {"id": "EMAIL-0225", "title": "Email scenario 225", "data": {"sku": "SKU225", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user225@example.com", "threshold": 250}},
    {"id": "EMAIL-0226", "title": "Email scenario 226", "data": {"sku": "SKU226", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user226@example.com", "threshold": 260}},
    {"id": "EMAIL-0227", "title": "Email scenario 227", "data": {"sku": "SKU227", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user227@example.com", "threshold": 270}},
    {"id": "EMAIL-0228", "title": "Email scenario 228", "data": {"sku": "SKU228", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user228@example.com", "threshold": 280}},
    {"id": "EMAIL-0229", "title": "Email scenario 229", "data": {"sku": "SKU229", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user229@example.com", "threshold": 290}},
    {"id": "EMAIL-0230", "title": "Email scenario 230", "data": {"sku": "SKU230", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user230@example.com", "threshold": 300}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
