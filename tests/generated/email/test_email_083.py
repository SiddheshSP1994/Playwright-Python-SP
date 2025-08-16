import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-4961", "title": "Email scenario 4961", "data": {"sku": "SKU4961", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user4961@example.com", "threshold": 610}},
    {"id": "EMAIL-4962", "title": "Email scenario 4962", "data": {"sku": "SKU4962", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user4962@example.com", "threshold": 620}},
    {"id": "EMAIL-4963", "title": "Email scenario 4963", "data": {"sku": "SKU4963", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user4963@example.com", "threshold": 630}},
    {"id": "EMAIL-4964", "title": "Email scenario 4964", "data": {"sku": "SKU4964", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user4964@example.com", "threshold": 640}},
    {"id": "EMAIL-4965", "title": "Email scenario 4965", "data": {"sku": "SKU4965", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user4965@example.com", "threshold": 650}},
    {"id": "EMAIL-4966", "title": "Email scenario 4966", "data": {"sku": "SKU4966", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user4966@example.com", "threshold": 660}},
    {"id": "EMAIL-4967", "title": "Email scenario 4967", "data": {"sku": "SKU4967", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user4967@example.com", "threshold": 670}},
    {"id": "EMAIL-4968", "title": "Email scenario 4968", "data": {"sku": "SKU4968", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user4968@example.com", "threshold": 680}},
    {"id": "EMAIL-4969", "title": "Email scenario 4969", "data": {"sku": "SKU4969", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user4969@example.com", "threshold": 690}},
    {"id": "EMAIL-4970", "title": "Email scenario 4970", "data": {"sku": "SKU4970", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user4970@example.com", "threshold": 700}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
