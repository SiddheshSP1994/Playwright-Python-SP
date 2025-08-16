import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-0581", "title": "Email scenario 581", "data": {"sku": "SKU581", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user581@example.com", "threshold": 810}},
    {"id": "EMAIL-0582", "title": "Email scenario 582", "data": {"sku": "SKU582", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user582@example.com", "threshold": 820}},
    {"id": "EMAIL-0583", "title": "Email scenario 583", "data": {"sku": "SKU583", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user583@example.com", "threshold": 830}},
    {"id": "EMAIL-0584", "title": "Email scenario 584", "data": {"sku": "SKU584", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user584@example.com", "threshold": 840}},
    {"id": "EMAIL-0585", "title": "Email scenario 585", "data": {"sku": "SKU585", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user585@example.com", "threshold": 850}},
    {"id": "EMAIL-0586", "title": "Email scenario 586", "data": {"sku": "SKU586", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user586@example.com", "threshold": 860}},
    {"id": "EMAIL-0587", "title": "Email scenario 587", "data": {"sku": "SKU587", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user587@example.com", "threshold": 870}},
    {"id": "EMAIL-0588", "title": "Email scenario 588", "data": {"sku": "SKU588", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user588@example.com", "threshold": 880}},
    {"id": "EMAIL-0589", "title": "Email scenario 589", "data": {"sku": "SKU589", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user589@example.com", "threshold": 890}},
    {"id": "EMAIL-0590", "title": "Email scenario 590", "data": {"sku": "SKU590", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user590@example.com", "threshold": 900}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
