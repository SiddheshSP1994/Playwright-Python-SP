import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-5681", "title": "Email scenario 5681", "data": {"sku": "SKU5681", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user5681@example.com", "threshold": 810}},
    {"id": "EMAIL-5682", "title": "Email scenario 5682", "data": {"sku": "SKU5682", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user5682@example.com", "threshold": 820}},
    {"id": "EMAIL-5683", "title": "Email scenario 5683", "data": {"sku": "SKU5683", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user5683@example.com", "threshold": 830}},
    {"id": "EMAIL-5684", "title": "Email scenario 5684", "data": {"sku": "SKU5684", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user5684@example.com", "threshold": 840}},
    {"id": "EMAIL-5685", "title": "Email scenario 5685", "data": {"sku": "SKU5685", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user5685@example.com", "threshold": 850}},
    {"id": "EMAIL-5686", "title": "Email scenario 5686", "data": {"sku": "SKU5686", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user5686@example.com", "threshold": 860}},
    {"id": "EMAIL-5687", "title": "Email scenario 5687", "data": {"sku": "SKU5687", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user5687@example.com", "threshold": 870}},
    {"id": "EMAIL-5688", "title": "Email scenario 5688", "data": {"sku": "SKU5688", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user5688@example.com", "threshold": 880}},
    {"id": "EMAIL-5689", "title": "Email scenario 5689", "data": {"sku": "SKU5689", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user5689@example.com", "threshold": 890}},
    {"id": "EMAIL-5690", "title": "Email scenario 5690", "data": {"sku": "SKU5690", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user5690@example.com", "threshold": 900}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
