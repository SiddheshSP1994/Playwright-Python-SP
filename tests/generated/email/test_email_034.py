import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-2021", "title": "Email scenario 2021", "data": {"sku": "SKU2021", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user2021@example.com", "threshold": 210}},
    {"id": "EMAIL-2022", "title": "Email scenario 2022", "data": {"sku": "SKU2022", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user2022@example.com", "threshold": 220}},
    {"id": "EMAIL-2023", "title": "Email scenario 2023", "data": {"sku": "SKU2023", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user2023@example.com", "threshold": 230}},
    {"id": "EMAIL-2024", "title": "Email scenario 2024", "data": {"sku": "SKU2024", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user2024@example.com", "threshold": 240}},
    {"id": "EMAIL-2025", "title": "Email scenario 2025", "data": {"sku": "SKU2025", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user2025@example.com", "threshold": 250}},
    {"id": "EMAIL-2026", "title": "Email scenario 2026", "data": {"sku": "SKU2026", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user2026@example.com", "threshold": 260}},
    {"id": "EMAIL-2027", "title": "Email scenario 2027", "data": {"sku": "SKU2027", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user2027@example.com", "threshold": 270}},
    {"id": "EMAIL-2028", "title": "Email scenario 2028", "data": {"sku": "SKU2028", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user2028@example.com", "threshold": 280}},
    {"id": "EMAIL-2029", "title": "Email scenario 2029", "data": {"sku": "SKU2029", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user2029@example.com", "threshold": 290}},
    {"id": "EMAIL-2030", "title": "Email scenario 2030", "data": {"sku": "SKU2030", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user2030@example.com", "threshold": 300}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
