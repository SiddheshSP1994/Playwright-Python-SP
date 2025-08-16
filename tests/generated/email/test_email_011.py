import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "EMAIL-0641", "title": "Email scenario 641", "data": {"sku": "SKU641", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user641@example.com", "threshold": 410}},
    {"id": "EMAIL-0642", "title": "Email scenario 642", "data": {"sku": "SKU642", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user642@example.com", "threshold": 420}},
    {"id": "EMAIL-0643", "title": "Email scenario 643", "data": {"sku": "SKU643", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user643@example.com", "threshold": 430}},
    {"id": "EMAIL-0644", "title": "Email scenario 644", "data": {"sku": "SKU644", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user644@example.com", "threshold": 440}},
    {"id": "EMAIL-0645", "title": "Email scenario 645", "data": {"sku": "SKU645", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user645@example.com", "threshold": 450}},
    {"id": "EMAIL-0646", "title": "Email scenario 646", "data": {"sku": "SKU646", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user646@example.com", "threshold": 460}},
    {"id": "EMAIL-0647", "title": "Email scenario 647", "data": {"sku": "SKU647", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user647@example.com", "threshold": 470}},
    {"id": "EMAIL-0648", "title": "Email scenario 648", "data": {"sku": "SKU648", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user648@example.com", "threshold": 480}},
    {"id": "EMAIL-0649", "title": "Email scenario 649", "data": {"sku": "SKU649", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user649@example.com", "threshold": 490}},
    {"id": "EMAIL-0650", "title": "Email scenario 650", "data": {"sku": "SKU650", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user650@example.com", "threshold": 500}},
])
def test_email(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
