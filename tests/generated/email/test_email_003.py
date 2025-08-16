import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-0161", "title": "Email scenario 161", "data": {"sku": "SKU161", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user161@example.com", "threshold": 610}},
    {"id": "EMAIL-0162", "title": "Email scenario 162", "data": {"sku": "SKU162", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user162@example.com", "threshold": 620}},
    {"id": "EMAIL-0163", "title": "Email scenario 163", "data": {"sku": "SKU163", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user163@example.com", "threshold": 630}},
    {"id": "EMAIL-0164", "title": "Email scenario 164", "data": {"sku": "SKU164", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user164@example.com", "threshold": 640}},
    {"id": "EMAIL-0165", "title": "Email scenario 165", "data": {"sku": "SKU165", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user165@example.com", "threshold": 650}},
    {"id": "EMAIL-0166", "title": "Email scenario 166", "data": {"sku": "SKU166", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user166@example.com", "threshold": 660}},
    {"id": "EMAIL-0167", "title": "Email scenario 167", "data": {"sku": "SKU167", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user167@example.com", "threshold": 670}},
    {"id": "EMAIL-0168", "title": "Email scenario 168", "data": {"sku": "SKU168", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user168@example.com", "threshold": 680}},
    {"id": "EMAIL-0169", "title": "Email scenario 169", "data": {"sku": "SKU169", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user169@example.com", "threshold": 690}},
    {"id": "EMAIL-0170", "title": "Email scenario 170", "data": {"sku": "SKU170", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user170@example.com", "threshold": 700}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
