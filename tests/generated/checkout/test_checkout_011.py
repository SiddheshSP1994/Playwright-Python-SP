import pytest

@pytest.mark.regression
@pytest.mark.parametrize("case", [
    {"id": "CHECKOUT-0601", "title": "Checkout scenario 601", "data": {"sku": "SKU601", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON2", "payment": "card", "email": "user601@example.com", "threshold": 10}},
    {"id": "CHECKOUT-0602", "title": "Checkout scenario 602", "data": {"sku": "SKU602", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON3", "payment": "card", "email": "user602@example.com", "threshold": 20}},
    {"id": "CHECKOUT-0603", "title": "Checkout scenario 603", "data": {"sku": "SKU603", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON4", "payment": "card", "email": "user603@example.com", "threshold": 30}},
    {"id": "CHECKOUT-0604", "title": "Checkout scenario 604", "data": {"sku": "SKU604", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON5", "payment": "card", "email": "user604@example.com", "threshold": 40}},
    {"id": "CHECKOUT-0605", "title": "Checkout scenario 605", "data": {"sku": "SKU605", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON6", "payment": "card", "email": "user605@example.com", "threshold": 50}},
    {"id": "CHECKOUT-0606", "title": "Checkout scenario 606", "data": {"sku": "SKU606", "qty": 2, "country": "IN", "sort": "asc", "coupon": "COUPON7", "payment": "card", "email": "user606@example.com", "threshold": 60}},
    {"id": "CHECKOUT-0607", "title": "Checkout scenario 607", "data": {"sku": "SKU607", "qty": 3, "country": "IN", "sort": "asc", "coupon": "COUPON8", "payment": "card", "email": "user607@example.com", "threshold": 70}},
    {"id": "CHECKOUT-0608", "title": "Checkout scenario 608", "data": {"sku": "SKU608", "qty": 4, "country": "IN", "sort": "asc", "coupon": "COUPON9", "payment": "card", "email": "user608@example.com", "threshold": 80}},
    {"id": "CHECKOUT-0609", "title": "Checkout scenario 609", "data": {"sku": "SKU609", "qty": 5, "country": "IN", "sort": "asc", "coupon": "COUPON10", "payment": "card", "email": "user609@example.com", "threshold": 90}},
    {"id": "CHECKOUT-0610", "title": "Checkout scenario 610", "data": {"sku": "SKU610", "qty": 1, "country": "IN", "sort": "asc", "coupon": "COUPON11", "payment": "card", "email": "user610@example.com", "threshold": 100}},
])
def test_checkout(case):
    # TODO: implement test logic using case data
    assert isinstance(case["id"], str)
