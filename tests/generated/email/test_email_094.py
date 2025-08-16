import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-5621", "title": "Email scenario 5621", "data": {"sku": "SKU5621", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user5621@example.com", "threshold": 210}},
    {"id": "EMAIL-5622", "title": "Email scenario 5622", "data": {"sku": "SKU5622", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user5622@example.com", "threshold": 220}},
    {"id": "EMAIL-5623", "title": "Email scenario 5623", "data": {"sku": "SKU5623", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user5623@example.com", "threshold": 230}},
    {"id": "EMAIL-5624", "title": "Email scenario 5624", "data": {"sku": "SKU5624", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user5624@example.com", "threshold": 240}},
    {"id": "EMAIL-5625", "title": "Email scenario 5625", "data": {"sku": "SKU5625", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user5625@example.com", "threshold": 250}},
    {"id": "EMAIL-5626", "title": "Email scenario 5626", "data": {"sku": "SKU5626", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user5626@example.com", "threshold": 260}},
    {"id": "EMAIL-5627", "title": "Email scenario 5627", "data": {"sku": "SKU5627", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user5627@example.com", "threshold": 270}},
    {"id": "EMAIL-5628", "title": "Email scenario 5628", "data": {"sku": "SKU5628", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user5628@example.com", "threshold": 280}},
    {"id": "EMAIL-5629", "title": "Email scenario 5629", "data": {"sku": "SKU5629", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user5629@example.com", "threshold": 290}},
    {"id": "EMAIL-5630", "title": "Email scenario 5630", "data": {"sku": "SKU5630", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user5630@example.com", "threshold": 300}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
