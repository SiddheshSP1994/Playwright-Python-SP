import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-4481", "title": "Email scenario 4481", "data": {"sku": "SKU4481", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user4481@example.com", "threshold": 810}},
    {"id": "EMAIL-4482", "title": "Email scenario 4482", "data": {"sku": "SKU4482", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user4482@example.com", "threshold": 820}},
    {"id": "EMAIL-4483", "title": "Email scenario 4483", "data": {"sku": "SKU4483", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user4483@example.com", "threshold": 830}},
    {"id": "EMAIL-4484", "title": "Email scenario 4484", "data": {"sku": "SKU4484", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user4484@example.com", "threshold": 840}},
    {"id": "EMAIL-4485", "title": "Email scenario 4485", "data": {"sku": "SKU4485", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user4485@example.com", "threshold": 850}},
    {"id": "EMAIL-4486", "title": "Email scenario 4486", "data": {"sku": "SKU4486", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user4486@example.com", "threshold": 860}},
    {"id": "EMAIL-4487", "title": "Email scenario 4487", "data": {"sku": "SKU4487", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user4487@example.com", "threshold": 870}},
    {"id": "EMAIL-4488", "title": "Email scenario 4488", "data": {"sku": "SKU4488", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user4488@example.com", "threshold": 880}},
    {"id": "EMAIL-4489", "title": "Email scenario 4489", "data": {"sku": "SKU4489", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user4489@example.com", "threshold": 890}},
    {"id": "EMAIL-4490", "title": "Email scenario 4490", "data": {"sku": "SKU4490", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user4490@example.com", "threshold": 900}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
