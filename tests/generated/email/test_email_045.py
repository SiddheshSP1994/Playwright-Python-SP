import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-2681", "title": "Email scenario 2681", "data": {"sku": "SKU2681", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user2681@example.com", "threshold": 810}},
    {"id": "EMAIL-2682", "title": "Email scenario 2682", "data": {"sku": "SKU2682", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user2682@example.com", "threshold": 820}},
    {"id": "EMAIL-2683", "title": "Email scenario 2683", "data": {"sku": "SKU2683", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user2683@example.com", "threshold": 830}},
    {"id": "EMAIL-2684", "title": "Email scenario 2684", "data": {"sku": "SKU2684", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user2684@example.com", "threshold": 840}},
    {"id": "EMAIL-2685", "title": "Email scenario 2685", "data": {"sku": "SKU2685", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user2685@example.com", "threshold": 850}},
    {"id": "EMAIL-2686", "title": "Email scenario 2686", "data": {"sku": "SKU2686", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user2686@example.com", "threshold": 860}},
    {"id": "EMAIL-2687", "title": "Email scenario 2687", "data": {"sku": "SKU2687", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user2687@example.com", "threshold": 870}},
    {"id": "EMAIL-2688", "title": "Email scenario 2688", "data": {"sku": "SKU2688", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user2688@example.com", "threshold": 880}},
    {"id": "EMAIL-2689", "title": "Email scenario 2689", "data": {"sku": "SKU2689", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user2689@example.com", "threshold": 890}},
    {"id": "EMAIL-2690", "title": "Email scenario 2690", "data": {"sku": "SKU2690", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user2690@example.com", "threshold": 900}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
