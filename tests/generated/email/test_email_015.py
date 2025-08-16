import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-0881", "title": "Email scenario 881", "data": {"sku": "SKU881", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user881@example.com", "threshold": 810}},
    {"id": "EMAIL-0882", "title": "Email scenario 882", "data": {"sku": "SKU882", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user882@example.com", "threshold": 820}},
    {"id": "EMAIL-0883", "title": "Email scenario 883", "data": {"sku": "SKU883", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user883@example.com", "threshold": 830}},
    {"id": "EMAIL-0884", "title": "Email scenario 884", "data": {"sku": "SKU884", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user884@example.com", "threshold": 840}},
    {"id": "EMAIL-0885", "title": "Email scenario 885", "data": {"sku": "SKU885", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user885@example.com", "threshold": 850}},
    {"id": "EMAIL-0886", "title": "Email scenario 886", "data": {"sku": "SKU886", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user886@example.com", "threshold": 860}},
    {"id": "EMAIL-0887", "title": "Email scenario 887", "data": {"sku": "SKU887", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user887@example.com", "threshold": 870}},
    {"id": "EMAIL-0888", "title": "Email scenario 888", "data": {"sku": "SKU888", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user888@example.com", "threshold": 880}},
    {"id": "EMAIL-0889", "title": "Email scenario 889", "data": {"sku": "SKU889", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user889@example.com", "threshold": 890}},
    {"id": "EMAIL-0890", "title": "Email scenario 890", "data": {"sku": "SKU890", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user890@example.com", "threshold": 900}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
