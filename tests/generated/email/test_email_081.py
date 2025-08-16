import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-4841", "title": "Email scenario 4841", "data": {"sku": "SKU4841", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user4841@example.com", "threshold": 410}},
    {"id": "EMAIL-4842", "title": "Email scenario 4842", "data": {"sku": "SKU4842", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user4842@example.com", "threshold": 420}},
    {"id": "EMAIL-4843", "title": "Email scenario 4843", "data": {"sku": "SKU4843", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user4843@example.com", "threshold": 430}},
    {"id": "EMAIL-4844", "title": "Email scenario 4844", "data": {"sku": "SKU4844", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user4844@example.com", "threshold": 440}},
    {"id": "EMAIL-4845", "title": "Email scenario 4845", "data": {"sku": "SKU4845", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user4845@example.com", "threshold": 450}},
    {"id": "EMAIL-4846", "title": "Email scenario 4846", "data": {"sku": "SKU4846", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user4846@example.com", "threshold": 460}},
    {"id": "EMAIL-4847", "title": "Email scenario 4847", "data": {"sku": "SKU4847", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user4847@example.com", "threshold": 470}},
    {"id": "EMAIL-4848", "title": "Email scenario 4848", "data": {"sku": "SKU4848", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user4848@example.com", "threshold": 480}},
    {"id": "EMAIL-4849", "title": "Email scenario 4849", "data": {"sku": "SKU4849", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user4849@example.com", "threshold": 490}},
    {"id": "EMAIL-4850", "title": "Email scenario 4850", "data": {"sku": "SKU4850", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user4850@example.com", "threshold": 500}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
