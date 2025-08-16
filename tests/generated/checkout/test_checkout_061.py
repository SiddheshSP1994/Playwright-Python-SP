import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-3601", "title": "Checkout scenario 3601", "data": {"sku": "SKU3601", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user3601@example.com", "threshold": 10}},
    {"id": "CHECKOUT-3602", "title": "Checkout scenario 3602", "data": {"sku": "SKU3602", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user3602@example.com", "threshold": 20}},
    {"id": "CHECKOUT-3603", "title": "Checkout scenario 3603", "data": {"sku": "SKU3603", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user3603@example.com", "threshold": 30}},
    {"id": "CHECKOUT-3604", "title": "Checkout scenario 3604", "data": {"sku": "SKU3604", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user3604@example.com", "threshold": 40}},
    {"id": "CHECKOUT-3605", "title": "Checkout scenario 3605", "data": {"sku": "SKU3605", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user3605@example.com", "threshold": 50}},
    {"id": "CHECKOUT-3606", "title": "Checkout scenario 3606", "data": {"sku": "SKU3606", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user3606@example.com", "threshold": 60}},
    {"id": "CHECKOUT-3607", "title": "Checkout scenario 3607", "data": {"sku": "SKU3607", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user3607@example.com", "threshold": 70}},
    {"id": "CHECKOUT-3608", "title": "Checkout scenario 3608", "data": {"sku": "SKU3608", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user3608@example.com", "threshold": 80}},
    {"id": "CHECKOUT-3609", "title": "Checkout scenario 3609", "data": {"sku": "SKU3609", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user3609@example.com", "threshold": 90}},
    {"id": "CHECKOUT-3610", "title": "Checkout scenario 3610", "data": {"sku": "SKU3610", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user3610@example.com", "threshold": 100}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
