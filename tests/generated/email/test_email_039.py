import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-2321", "title": "Email scenario 2321", "data": {"sku": "SKU2321", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user2321@example.com", "threshold": 210}},
    {"id": "EMAIL-2322", "title": "Email scenario 2322", "data": {"sku": "SKU2322", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user2322@example.com", "threshold": 220}},
    {"id": "EMAIL-2323", "title": "Email scenario 2323", "data": {"sku": "SKU2323", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user2323@example.com", "threshold": 230}},
    {"id": "EMAIL-2324", "title": "Email scenario 2324", "data": {"sku": "SKU2324", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user2324@example.com", "threshold": 240}},
    {"id": "EMAIL-2325", "title": "Email scenario 2325", "data": {"sku": "SKU2325", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user2325@example.com", "threshold": 250}},
    {"id": "EMAIL-2326", "title": "Email scenario 2326", "data": {"sku": "SKU2326", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user2326@example.com", "threshold": 260}},
    {"id": "EMAIL-2327", "title": "Email scenario 2327", "data": {"sku": "SKU2327", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user2327@example.com", "threshold": 270}},
    {"id": "EMAIL-2328", "title": "Email scenario 2328", "data": {"sku": "SKU2328", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user2328@example.com", "threshold": 280}},
    {"id": "EMAIL-2329", "title": "Email scenario 2329", "data": {"sku": "SKU2329", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user2329@example.com", "threshold": 290}},
    {"id": "EMAIL-2330", "title": "Email scenario 2330", "data": {"sku": "SKU2330", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user2330@example.com", "threshold": 300}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
